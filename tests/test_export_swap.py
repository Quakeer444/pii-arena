"""R03: repeat export must keep the companion file, and a failed second
directory switch must leave the old or the new projection as a whole."""
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import export as E


def marker(path):
    value = json.loads(Path(path).read_text())
    return value[0].get('marker') if isinstance(value, list) else value.get('marker')


def fake_export_tree(base, m):
    (base / 'results').mkdir(parents=True)
    (base / 'datasets').mkdir()
    (base / 'results/snapshot.json').write_text(json.dumps({'marker': m}))
    (base / 'results/composition-counts.json').write_text(json.dumps([{'marker': m}]))
    (base / 'datasets/catalog.json').write_text(json.dumps({'marker': m}))


with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    fake_export_tree(root, 'old')
    # render.py-only output present in the previous tree
    (root / 'results/summary.csv').write_text('rendered')
    (root / 'results/types').mkdir()
    (root / 'results/types/alexen2.md').write_text('page')

    # 1. A reuse-only export must carry composition-counts.json into the new
    # tree: after the swap the companion file belongs to the new projection.
    staging = Path(tempfile.mkdtemp(prefix='export-staging-', dir=str(root)))
    staged_results, staged_catalog = staging / 'results', staging / 'datasets'
    staged_results.mkdir(parents=True)
    staged_catalog.mkdir()
    (staged_results / 'snapshot.json').write_text(json.dumps({'marker': 'new'}))
    (staged_results / 'composition-counts.json').write_text(json.dumps([{'marker': 'new'}]))
    (staged_catalog / 'catalog.json').write_text(json.dumps({'marker': 'new'}))
    E.replace_projection(staged_results, staged_catalog, root)
    assert marker(root / 'results/snapshot.json') == 'new'
    assert marker(root / 'results/composition-counts.json') == 'new', 'companion file lost in swap'
    assert marker(root / 'datasets/catalog.json') == 'new'
    assert (root / 'results/summary.csv').read_text() == 'rendered', 'render output lost in swap'
    assert (root / 'results/types/alexen2.md').read_text() == 'page', 'render pages lost in swap'

    # 2. Failure of the second switch rolls the first one back: the projection
    # stays entirely the previous export.
    staging2 = Path(tempfile.mkdtemp(prefix='export-staging-', dir=str(root)))
    sres, scat = staging2 / 'results', staging2 / 'datasets'
    sres.mkdir(parents=True)
    scat.mkdir()
    (sres / 'composition-counts.json').write_text(json.dumps([{'marker': 'newer'}]))
    (scat / 'catalog.json').write_text(json.dumps({'marker': 'newer'}))
    real_swap = E._swap
    calls = []

    def failing_swap(staging_dir, destination, keep_backup=False, preserve=()):
        calls.append(destination.name)
        if destination.name == 'datasets':
            raise OSError('simulated second-switch failure')
        return real_swap(staging_dir, destination, keep_backup=keep_backup, preserve=preserve)


    E._swap = failing_swap
    try:
        try:
            E.replace_projection(sres, scat, root)
        except OSError:
            pass
        else:
            raise AssertionError('Second-switch failure was swallowed')
    finally:
        E._swap = real_swap
    assert calls == ['results', 'datasets'], calls
    assert marker(root / 'results/snapshot.json') == 'new', 'results not rolled back'
    assert marker(root / 'results/composition-counts.json') == 'new'
    assert marker(root / 'datasets/catalog.json') == 'new', 'datasets changed unexpectedly'
    assert (root / 'results').is_dir() and (root / 'datasets').is_dir()

    # 3. The staged-projection completeness list names every required file,
    # including the companion file that a reuse-only export previously lost.
    staging3 = Path(tempfile.mkdtemp(prefix='export-staging-', dir=str(root)))
    sres3 = staging3 / 'results'
    sres3.mkdir(parents=True)
    (sres3 / 'snapshot.json').write_text('{}')
    try:
        missing = [n for n in E.REQUIRED_ARTIFACTS if not (sres3 / n).exists()]
        assert 'composition-counts.json' in missing and 'snapshot.json' not in missing, missing
    finally:
        shutil.rmtree(staging3, ignore_errors=True)
    # 4. A failure while carrying the renderer output into staging happens
    # before any rename, so the live projection stays exactly as it was.
    staging4 = Path(tempfile.mkdtemp(prefix='export-staging-', dir=str(root)))
    sres4, scat4 = staging4 / 'results', staging4 / 'datasets'
    sres4.mkdir(parents=True)
    scat4.mkdir()
    (sres4 / 'snapshot.json').write_text(json.dumps({'marker': 'newest'}))
    (sres4 / 'composition-counts.json').write_text(json.dumps([{'marker': 'newest'}]))
    (scat4 / 'catalog.json').write_text(json.dumps({'marker': 'newest'}))
    real_copy2 = shutil.copy2

    def failing_copy2(*a, **kw):
        raise OSError('simulated renderer-file copy failure')


    shutil.copy2 = failing_copy2
    try:
        try:
            E.replace_projection(sres4, scat4, root)
        except OSError:
            pass
        else:
            raise AssertionError('Renderer-copy failure was swallowed')
    finally:
        shutil.copy2 = real_copy2
    assert marker(root / 'results/snapshot.json') == 'new', 'results changed on a failed preserve'
    assert marker(root / 'results/composition-counts.json') == 'new'
    assert (root / 'results/summary.csv').read_text() == 'rendered', 'render output lost'
    assert (root / 'results/types/alexen2.md').read_text() == 'page', 'render pages lost'
    assert marker(root / 'datasets/catalog.json') == 'new', 'datasets changed unexpectedly'
    print("export swap checks passed")
