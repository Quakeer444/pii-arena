"""Deterministic SVG figures in one skin that follows the reader's light or dark theme.

Hand-built SVG instead of a plotting library: the published bytes stay stable
across platforms, and one CSS variable block covers both GitHub themes.
"""
from pathlib import Path
from math import floor, log10

WIDTH = 960
MARGIN = 40
SANS = "ui-sans-serif,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

BG, INK, MUTED, SOFT = 'var(--bg)', 'var(--ink)', 'var(--muted)', 'var(--soft)'
GRID, RULE, ZEBRA = 'var(--grid)', 'var(--rule)', 'var(--zebra)'
BAR, BARLINE = 'var(--bar)', 'var(--barline)'
ACCENT, ACCENT_BAR = 'var(--accent)', 'var(--accent-bar)'
SECOND, SECOND_BAR = 'var(--second)', 'var(--second-bar)'
HEAT = [f'var(--heat{i})' for i in range(5)]
HEAT_INK = [f'var(--heat-ink{i})' for i in range(5)]

CSS = (
    ':root{--bg:#ffffff;--ink:#111827;--muted:#5b6472;--soft:#8b93a1;'
    '--grid:rgba(17,24,39,.09);--rule:rgba(17,24,39,.20);--zebra:rgba(17,24,39,.032);'
    '--bar:rgba(91,100,114,.16);--barline:#98a0ad;--accent:#0d7d74;'
    '--accent-bar:rgba(13,125,116,.22);--second:#7c5cbf;--second-bar:rgba(124,92,191,.20);'
    '--heat0:rgba(13,125,116,.06);--heat1:rgba(13,125,116,.20);--heat2:rgba(13,125,116,.40);'
    '--heat3:rgba(13,125,116,.65);--heat4:#0d7d74;'
    '--heat-ink0:#111827;--heat-ink1:#111827;--heat-ink2:#111827;--heat-ink3:#0a2f2b;--heat-ink4:#ffffff}'
    '@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--ink:#e6edf3;--muted:#9198a1;--soft:#6e7681;'
    '--grid:rgba(230,237,243,.08);--rule:rgba(230,237,243,.20);--zebra:rgba(230,237,243,.035);'
    '--bar:rgba(145,152,161,.20);--barline:#6e7681;--accent:#2dd4bf;'
    '--accent-bar:rgba(45,212,191,.24);--second:#c4a7f5;--second-bar:rgba(196,167,245,.22);'
    '--heat0:rgba(45,212,191,.08);--heat1:rgba(45,212,191,.22);--heat2:rgba(45,212,191,.42);'
    '--heat3:rgba(45,212,191,.66);--heat4:#2dd4bf;'
    '--heat-ink0:#e6edf3;--heat-ink1:#e6edf3;--heat-ink2:#e6edf3;--heat-ink3:#04211d;--heat-ink4:#04211d}}'
)


def esc(value):
    return (str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;'))


def text(x, y, value, fill=INK, size=11, anchor='start', font=None, weight='400', spacing=None):
    extra = f' font-family="{font}"' if font else ''
    extra += f' letter-spacing="{spacing}"' if spacing else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}"{extra}>{esc(value)}</text>')


def line(x1, y1, x2, y2, stroke=GRID, width=1, opacity=None):
    extra = f' stroke-opacity="{opacity}"' if opacity is not None else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
            f'stroke-width="{width}"{extra}/>')


def bar(x, y, w, h, fill=BAR, stroke=BARLINE, width=.8, radius=1.5):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w, .8):.1f}" height="{h}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')


def log_ticks(low, high):
    ticks, step = [], 10.0 ** floor(log10(low))
    while step <= high:
        for factor in (1, 2, 5):
            value = step * factor
            if low <= value <= high:
                ticks.append(value)
        step *= 10
    return ticks


def short(value):
    """Two significant-looking digits without trailing noise, for axis and value labels."""
    return f'{value:.2f}' if value < 1 else (f'{value:.1f}' if value < 10 else f'{value:.0f}')


class Figure:
    """A figure is a header, a stack of blocks and a footnote band."""

    def __init__(self, title, subtitle, eyebrow, width=WIDTH):
        self.width = width
        self.title = title
        self.parts = []
        if eyebrow:
            self.parts.append(text(MARGIN, 34, eyebrow.upper(), ACCENT, 9, font=MONO,
                                   weight='600', spacing='1.6'))
        self.parts.append(text(MARGIN, 64, title, INK, 21, weight='650'))
        self.parts.append(text(MARGIN, 89, subtitle, MUTED, 11.5))
        self.parts.append(line(MARGIN, 109, width - MARGIN, 109, RULE))
        self.y = 109

    def add(self, *parts):
        self.parts.extend(parts)

    def zebra(self, index, y, pitch=21):
        return (bar(MARGIN, y - pitch / 2, self.width - 2 * MARGIN, pitch, ZEBRA, 'none', 0, 0)
                if index % 2 else '')

    def save(self, root, slug, description, notes):
        height = self.y + 30 + 13 * len(notes) + 18
        foot = [line(MARGIN, height - 26 - 13 * len(notes), self.width - MARGIN,
                     height - 26 - 13 * len(notes), GRID)]
        for i, note in enumerate(notes):
            foot.append(text(MARGIN, height - 13 * len(notes) - 6 + 13 * i, note, SOFT, 9.5))
        foot.append(text(self.width - MARGIN, height - 13 * len(notes) - 6,
                         'PII & Secrets Benchmark  |  snapshot 2026-09-09', SOFT, 9, 'end', MONO))
        body = '\n'.join(part for part in self.parts + foot if part)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
               f'viewBox="0 0 {self.width} {height}" width="{self.width}" height="{height}" '
               f'font-family="{SANS}" role="img" aria-label="{esc(description)}">\n'
               f'<title>{esc(self.title)}</title>\n<desc>{esc(description)}</desc>\n'
               '<metadata>\n<rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" '
               'xmlns:cc="http://creativecommons.org/ns#" '
               'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n<cc:Work>\n'
               '<dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>\n'
               f'<dc:title>{esc(self.title)}</dc:title>\n<dc:description>{esc(description)}</dc:description>\n'
               '<dc:format>image/svg+xml</dc:format>\n</cc:Work>\n</rdf:RDF>\n</metadata>\n'
               f'<style>{CSS}text{{dominant-baseline:middle}}</style>\n'
               f'<rect width="{self.width}" height="{height}" fill="{BG}"/>\n{body}\n</svg>\n')
        (root / 'assets').mkdir(exist_ok=True)
        (root / f'assets/{slug}.svg').write_text(svg)
        return svg


def bartable(fig, rows, columns, label_width=250, pitch=21, value_width=78):
    """Ranked rows with one small bar per metric column.

    rows: dicts with `label`, optional `sub`, `focal`, `note`, and one value per column key.
    columns: (heading, key, hint, domain, formatter).
    """
    x0 = MARGIN + label_width
    span = (fig.width - MARGIN - x0) / len(columns)
    top = fig.y + 62
    for index, (heading, key, hint, domain, _) in enumerate(columns):
        x = x0 + span * index
        fig.add(text(x, top - 44, heading.upper(), MUTED, 9, font=MONO, weight='600', spacing='1.1'),
                text(x, top - 30, hint, SOFT, 8.5),
                line(x - 12, top - 18, x - 12, top + pitch * (len(rows) - 1) + 11, GRID))
    for index, row in enumerate(rows):
        y = top + pitch * index
        ink = ACCENT if row.get('focal') else INK
        fig.add(fig.zebra(index, y, pitch),
                text(MARGIN, y, row['label'], ink, 11, font=MONO,
                     weight='600' if row.get('focal') else '400'))
        if row.get('sub'):
            fig.add(text(x0 - 16, y, row['sub'], SOFT, 9, 'end', MONO))
        for column, (heading, key, hint, domain, formatter) in enumerate(columns):
            x = x0 + span * column
            track = span - value_width
            width = track * min(row[key] / domain, 1) if domain else 0
            fig.add(line(x, y + 6, x + track, y + 6, GRID),
                    bar(x, y - 4.5, width, 9, ACCENT_BAR if row.get('focal') else BAR,
                        ACCENT if row.get('focal') else BARLINE, 1 if row.get('focal') else .7),
                    text(x + track + 10, y, row.get(f'{key}_text') or formatter(row[key]),
                         ink if row.get('focal') else MUTED, 9.5, font=MONO,
                         weight='600' if row.get('focal') else '400'))
    fig.y = top + pitch * (len(rows) - 1) + 16


def lollipop(fig, rows, axis_label, right_label, label_width=260, pitch=21, right_width=196):
    """One dot per row on a log axis: bar length from an arbitrary origin would lie."""
    x0 = MARGIN + label_width
    x1 = fig.width - right_width
    low = min(row['value'] for row in rows) * .8
    high = max(row['value'] for row in rows) * 1.2
    place = lambda v: x0 + (x1 - x0) * (log10(v) - log10(low)) / (log10(high) - log10(low))
    top = fig.y + 56
    bottom = top + pitch * (len(rows) - 1) + 12
    for value in log_ticks(low, high):
        x = place(value)
        fig.add(line(x, top - 14, x, bottom, GRID), text(x, top - 26, short(value), SOFT, 9, 'middle', MONO))
    fig.add(text(MARGIN, top - 26, axis_label, SOFT, 9, font=MONO),
            text(fig.width - MARGIN, top - 26, right_label, SOFT, 9, 'end', MONO))
    for index, row in enumerate(rows):
        y = top + pitch * index
        focal = row.get('focal')
        ink = ACCENT if focal else INK
        x = place(row['value'])
        fig.add(fig.zebra(index, y, pitch),
                text(x0 - 16, y, row['label'], ink, 11, 'end', MONO, '600' if focal else '400'),
                line(x0, y, x, y, ACCENT if focal else BARLINE, 1.4 if focal else 1, 1 if focal else .55),
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5.2 if focal else 4.2}" '
                f'fill="{ACCENT_BAR if focal else BAR}" stroke="{ACCENT if focal else BARLINE}" '
                f'stroke-width="{1.4 if focal else 1}"/>',
                text(x + 11, y, row['text'], ink, 10, font=MONO, weight='600' if focal else '400'),
                text(fig.width - MARGIN, y, row['right'], SOFT, 9, 'end', MONO))
    fig.y = bottom + 4


def heatmap(fig, rows, columns, label_width=250, cell_height=26, gap=2, header_lines=1):
    """rows: (label, sub, cells) with cells as (bucket 0-4, text). columns: header lines."""
    x0 = MARGIN + label_width
    span = (fig.width - MARGIN - x0) / len(columns)
    top = fig.y + 26 + 14 * header_lines
    for index, header in enumerate(columns):
        x = x0 + span * index + span / 2
        for depth, part in enumerate(header):
            fig.add(text(x, top - 14 * (len(header) - depth) - 6, part, MUTED if not depth else SOFT,
                         9.5 if not depth else 9, 'middle', MONO, '600' if not depth else '400'))
    for index, (label, sub, cells) in enumerate(rows):
        y = top + (cell_height + gap) * index
        fig.add(text(x0 - 14, y + cell_height / 2, label, INK, 10.5, 'end', MONO))
        if sub:
            fig.add(text(MARGIN, y + cell_height / 2, sub, SOFT, 9, font=MONO))
        for column, (bucket, value) in enumerate(cells):
            x = x0 + span * column
            fig.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{span - gap:.1f}" height="{cell_height}" '
                    f'rx="2" fill="{HEAT[bucket]}"/>',
                    text(x + (span - gap) / 2, y + cell_height / 2, value, HEAT_INK[bucket], 10,
                         'middle', MONO, '500'))
    fig.y = top + (cell_height + gap) * len(rows) + 6


def scatter(fig, points, x_label, y_label, y_max, height=430, label_min=None, corner=None, title=None):
    """points: dicts with x (log axis), y, label, focal."""
    x0, x1 = MARGIN + 72, fig.width - MARGIN
    if title:
        fig.add(text(MARGIN, fig.y + 22, title, INK, 12, weight='600'))
    y0 = fig.y + (78 if title else 44)
    y1 = y0 + height
    low = min(p['x'] for p in points) * .8
    high = max(p['x'] for p in points) * 1.3
    place_x = lambda v: x0 + (x1 - x0) * (log10(v) - log10(low)) / (log10(high) - log10(low))
    place_y = lambda v: y1 - (y1 - y0) * v / y_max
    for value in log_ticks(low, high):
        x = place_x(value)
        fig.add(line(x, y0, x, y1, GRID), text(x, y1 + 18, short(value), SOFT, 9, 'middle', MONO))
    for value in range(0, y_max + 1, y_max // 5):
        y = place_y(value)
        fig.add(line(x0, y, x1, y, GRID), text(x0 - 12, y, f'{value}%', SOFT, 9, 'end', MONO))
    fig.add(line(x0, y0, x0, y1, RULE), line(x0, y1, x1, y1, RULE),
            text(x0, y0 - 20, y_label, MUTED, 10), text(x0, y1 + 40, x_label, MUTED, 10))
    if corner:
        fig.add(text(x1, y0 - 20, corner, SOFT, 9.5, 'end'))
    placed, marks, labels = [], [], []
    for point in sorted(points, key=lambda p: (not p.get('focal'), p['y'])):
        focal = point.get('focal')
        x, y = place_x(point['x']), place_y(point['y'])
        marks.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{6 if focal else 4.3}" '
                     f'fill="{ACCENT_BAR if focal else BAR}" stroke="{ACCENT if focal else BARLINE}" '
                     f'stroke-width="{1.5 if focal else .9}"/>')
        if not (focal or label_min is None or point['y'] <= label_min):
            continue
        width = len(point['label']) * 6.1 + 12
        for shift in (0, -11, 11, -22, 22, -33, 33):
            left = x + 10 if x + 10 + width < x1 else x - 10 - width
            box = (left, y + shift - 6, left + width, y + shift + 6)
            if any(box[0] < other[2] and other[0] < box[2] and box[1] < other[3] and other[1] < box[3]
                   for other in placed):
                continue
            placed.append(box)
            labels.append(text(x + (11 if left > x else -11), y + shift, point['label'],
                               ACCENT if focal else MUTED, 9.5, 'start' if left > x else 'end',
                               MONO, '600' if focal else '400'))
            if shift:
                labels.append(line(x + (7 if left > x else -7), y, x + (10 if left > x else -10),
                                   y + shift, GRID))
            break
    fig.add(*marks, *labels)
    fig.y = y1 + 52
