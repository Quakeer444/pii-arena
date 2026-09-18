import argparse
import collections
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = {
    'secrets': ('Credentials', 'Passwords, keys & tokens', 'Source-labeled credentials; validity is not tested'),
    'logins': ('Credentials', 'Logins & usernames', 'Account names; not necessarily confidential alone'),
    'financial': ('Personal & contextual data', 'Bank accounts & cards', 'Account numbers, payment cards and bank codes'),
    'identity': ('Personal & contextual data', 'Documents & identifiers', 'Passports, tax IDs, insurance and device identifiers'),
    'names': ('Personal & contextual data', 'People\'s names', 'Names and name parts retained by each source'),
    'contacts': ('Personal & contextual data', 'Phone numbers & email', 'Contact details, including source-labeled handles'),
    'addresses': ('Personal & contextual data', 'Addresses & locations', 'Postal addresses, places and coordinates'),
    'dates': ('Personal & contextual data', 'Dates & times', 'Birth dates and retained date/time annotations'),
    'organizations': ('Personal & contextual data', 'Organizations', 'Company and organization mentions'),
    'network': ('Personal & contextual data', 'Network identifiers', 'IP addresses, URLs, domains and host names'),
    'accounts': ('Personal & contextual data', 'Customer & employee IDs', 'Account references, badges and social identifiers'),
    'other': ('Personal & contextual data', 'Other sensitive attributes', 'Health, demographics and other retained labels'),
}
GROUP_CATEGORY = dict(zip(
    ('PERSON', 'ADDRESS', 'CONTACT', 'ID', 'NET', 'ACCOUNT', 'SECRET', 'ORG', 'DATE', 'OTHER'),
    ('names', 'addresses', 'contacts', 'identity', 'network', 'accounts', 'secrets', 'organizations', 'dates', 'other')))
FINANCIAL = set(('ACCOUNTNUM ACCOUNT_NUMBER BANK_CARD_NUMBER CARD_NUMBER CREDITCARDNUMBER '
                 'CREDIT_CARD CREDIT_DEBIT_CARD CVC CVV Credit_Card_Numbers IBAN IBAN_CODE '
                 'ROUTING_NUMBER SWIFT_BIC US_BANK_NUMBER account_number bank_routing_number '
                 'bban credit_card_number credit_card_security_code credit_debit_card cvv '
                 'iban swift_bic swift_bic_code').split())


def category(label, group):
    if label in FINANCIAL:
        return 'financial'
    if label in {'USERNAME', 'username', 'user_name', 'login'}:
        return 'logins'
    if label in {'DATE', 'TIME', 'date'}:
        return 'dates'
    return GROUP_CATEGORY[group]


def tally_row(gold, original, predicted, raw):
    counts = collections.defaultdict(collections.Counter)
    for a, b, label in gold:
        span = set(range(a, b))
        overlap = len(span & predicted)
        counts[label].update(hit=int(bool(overlap)), hidden=int(overlap == len(span)),
                             raw_hidden=int(span <= raw), covered_characters=overlap)
    for e in original:
        counts[e['type']]['original_hidden'] += int(set(range(e['start'], e['end'])) <= raw)
    return counts


def measure(S, SR, dataset, members, votes, cooked, raw):
    types = collections.defaultdict(collections.Counter)
    totals = collections.Counter()
    for rid, (text, entities) in S.gold(dataset)[0].items():
        gold = S.gold_norm(dataset)[rid]
        pc = SR.covered(cooked, members, rid, votes)
        rc = SR.covered(raw, members, rid, votes)
        gc = S.chars(gold)
        for label, row in tally_row(gold, entities, pc, rc).items():
            types[label].update(row)
        totals.update(char_tp=len(gc & pc), char_fp=len(pc - gc), char_fn=len(gc - pc),
                      positive_rows=int(bool(entities)),
                      residual_rows=int(bool(gc - pc)), raw_residual_rows=int(bool(gc - rc)),
                      raw_original_residual_rows=int(any(
                          any(p not in rc for p in range(e['start'], e['end'])) for e in entities)))
        if not entities:
            totals.update(negative_rows=1, negative_rows_touched=int(bool(pc)),
                          negative_characters=len(text), negative_characters_masked=len(pc))
    for key in ('negative_rows', 'negative_rows_touched', 'negative_characters', 'negative_characters_masked'):
        totals.setdefault(key, 0)
    return dict(totals) | {'types': [dict(label=label, **dict(values)) for label, values in sorted(types.items())]}


def build(data, snapshot):
    os.environ['BENCHMARK_DATA'] = str(data)
    sys.path.insert(0, str(ROOT / 'benchmark'))
    import score as S
    import secrets_recall as SR
    S.THRESH = snapshot['threshold']
    systems = {f"model:{r['model']}": {'id': f"model:{r['model']}", 'kind': 'model',
               'members': [r['model']], 'votes': 1} for r in snapshot['measurements']}
    selected = {r['composition'] for r in snapshot['composition_counts']}
    for r in snapshot['ensembles']:
        if r['composition'] in selected:
            key = f"composition:{r['composition']}"
            systems[key] = {'id': key, 'kind': 'composition', 'members': r['members'], 'votes': r['votes']}
    result, taxonomy = [], []
    expected_combos = {(r['composition'], r['dataset']): r for r in snapshot['composition_counts']}
    for index, d in enumerate(snapshot['datasets'], 1):
        dataset = d['id']
        path = data / 'BENCH' / dataset / 'bench.csv'
        if S.bench_sha256(path) != d['bench_sha256']:
            raise ValueError(f'Frozen corpus changed: {dataset}')
        gold, normalized, groups = S.gold(dataset)[0], S.gold_norm(dataset), S.meta_of(dataset)['groups']
        original_n, normalized_n, characters = (collections.Counter() for _ in range(3))
        for _, ents in gold.values():
            original_n.update(e['type'] for e in ents)
        for ents in normalized.values():
            for a, b, label in ents:
                normalized_n[label] += 1
                characters[label] += b - a
        if (sum(original_n.values()), sum(normalized_n.values())) != (d['original_annotations'], d['gold_spans']):
            raise ValueError(f'Frozen gold totals changed: {dataset}')
        for label in sorted(original_n):
            taxonomy.append({'dataset': dataset, 'label': label, 'group': groups[label],
                             'category': category(label, groups[label]), 'gold': normalized_n[label],
                             'original_gold': original_n[label], 'characters': characters[label]})
        model_rows = [r for r in snapshot['measurements'] if r['dataset'] == dataset]
        combo_rows = [r for r in snapshot['composition_counts'] if r['dataset'] == dataset]
        retained = {m for r in combo_rows for m in systems[f"composition:{r['composition']}"]['members']}
        cooked, raw = {}, {}
        for i, row in enumerate(model_rows, 1):
            model = row['model']
            f = data / 'RESULTS' / dataset / f'pred.{model}.jsonl'
            # T03: this path recomputes diagnostics from the current local
            # predictions, so the inputs must be the published ones - the
            # digest recorded for this dataset/config in the snapshot sources.
            # A changed prediction stops the run before anything is written;
            # a deliberate new build goes through export.py, which rewrites
            # sources, inventory and breakdowns together.
            recorded = (snapshot.get('sources') or {}).get(f'RESULTS/{dataset}/pred.{model}.jsonl')
            actual = hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None
            if recorded != actual:
                raise ValueError(f'Frozen prediction changed: {dataset}/{model} '
                                 f'(recorded {recorded}, local {actual}); '
                                 f'use scripts/export.py --recompute-compositions for a new result revision')
            meta, pred = S.read_pred(f)
            if bad := S.check_predictions(f, meta, pred, complete=True, expected=dataset, expected_model=model):
                raise ValueError(bad)
            if bool(dataset in S.dirty(model)) != row['train']:
                raise ValueError(f'Training-source status changed: {dataset}/{model}')
            cooked[model], raw[model] = {}, {}
            for rid, (text, _) in gold.items():
                spans = S.keep(pred[rid]['spans'])
                cooked[model][rid] = S.norm(text, spans, 'label')
                raw[model][rid] = [(e['start'], e['end'], e['label']) for e in spans
                                   if 0 <= e['start'] < e['end'] <= len(text)]
            counts = measure(S, SR, dataset, [model], 1, cooked, raw)
            hit = sum(r['hit'] for r in counts['types'])
            hidden = sum(r['hidden'] for r in counts['types'])
            if d['gold_spans'] - hit != row['missed'] or abs(100 * hidden / d['gold_spans'] - row['hidden_pct_reported']) > .051:
                raise ValueError(f'Frozen model result differs: {dataset}/{model}')
            precision, recall, f1 = S.prf(counts['char_tp'], counts['char_fp'], counts['char_fn'])
            for actual, field in ((precision, 'char_precision_reported'), (recall, 'char_recall_reported'), (f1, 'char_f1_reported')):
                if abs(actual - row[field]) > .00051:
                    raise ValueError(f'Frozen character metric differs: {dataset}/{model}/{field}')
            result.append({'system': f'model:{model}', 'dataset': dataset, 'train': row['train'], **counts})
            if model not in retained:
                del cooked[model], raw[model]
            if i % 10 == 0:
                print(f'{index}/41 {dataset}: {i}/{len(model_rows)} configurations', flush=True)
        for r in combo_rows:
            key = f"composition:{r['composition']}"
            system = systems[key]
            if any(dataset in S.dirty(m) for m in system['members']):
                raise ValueError(f'Training-source overlap: {dataset}/{key}')
            counts = measure(S, SR, dataset, system['members'], system['votes'], cooked, raw)
            expected = expected_combos[(r['composition'], dataset)]
            got = (sum(x['hit'] for x in counts['types']), sum(x['hidden'] for x in counts['types']),
                   counts['char_tp'], counts['char_fp'], counts['char_fn'], counts['negative_rows_touched'],
                   counts['negative_characters_masked'])
            if got != tuple(expected[k] for k in ('hit', 'hid', 'tp', 'fp', 'fn', 'fire', 'extra')):
                raise ValueError(f'Frozen composition differs: {dataset}/{key}')
            result.append({'system': key, 'dataset': dataset, 'train': False, **counts})
        print(f'{index}/41 {dataset}: matched all models and compositions', flush=True)
        for fn in (S.gold, S.gold_norm, S.chars_of, S._canon):
            fn.cache_clear()
    return {'taxonomy_version': 1, 'categories': [dict(id=k, family=v[0], title=v[1], description=v[2])
            for k, v in CATEGORIES.items()], 'taxonomy': taxonomy,
            'systems': list(systems.values()), 'results': result}


def main():
    parser = argparse.ArgumentParser(description='Recompute type-level diagnostics from frozen local predictions.')
    parser.add_argument('--data', type=Path, default=ROOT / '.local/research')
    args = parser.parse_args()
    path = ROOT / 'results/snapshot.json'
    snapshot = json.loads(path.read_text())
    breakdowns = build(args.data.resolve(), snapshot)
    snapshot['schema_version'] = 3
    snapshot['breakdowns'] = breakdowns
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(snapshot, ensure_ascii=True, indent=2) + '\n')
    temporary.replace(path)
    print(f"Saved {len(breakdowns['results'])} exact configuration/dataset results and complete type diagnostics.")


if __name__ == '__main__':
    main()
