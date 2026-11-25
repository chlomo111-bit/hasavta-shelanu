"""Specs compose.py « ידעתם? עם דבורה » #4 (25.11 matin) : וומבט קוביות. Usage : python3 specs.py <dossier_images_10fps> > spec.json"""
import json, sys
R = sys.argv[1]; D = 18.15
Y = lambda s: f'<span class=y>{s}</span>'
big = lambda s, sz=84: f'<div style="font:900 {sz}px/1.1 H">{s}</div>'
sub = lambda s: f'<div class=box style="font:900 32px/1.2 H">{s}</div>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
title = '<div class=pill style="background:#FFC24B;color:#140c04;font:900 30px/1.15 H">ידעתם? עם דבורה 🐝 · 4</div>'
ov = [O(0, D, 'T', title, 1)]
M = [(0, .8, f'{Y("ידעתם")}?'), (.8, 1.6, f'{Y("וומבט")} 🟫'), (1.6, 2.7, f'{Y("קובייה")}?!'),
     (2.8, 3.6, f'{Y("בסוף")}'), (3.6, 4.65, f'{Y("המעי")}'),
     (4.75, 5.8, f'{Y("דפנות")}'), (5.8, 6.8, f'{Y("נמתחות")}'), (6.8, 8.0, f'לא {Y("שווה")}'),
     (8.1, 9.55, big(f'לא {Y("מתגלגלות")}', 68)), (9.6, 10.6, f'{Y("כנראה")}'), (10.6, 11.4, f'{Y("לסמן")}'), (11.4, 12.5, f'{Y("טריטוריה")}'),
     (12.7, 13.7, f'{Y("שלחו")} 📩'), (13.7, 15.1, f'{Y("קופסאות")} 📦'),
     (15.2, 16.2, f'{Y("כתבו")} שם ✍️'), (16.2, 17.2, f'{Y("אקרא")}'), (17.2, D, f'{Y("לכם")}!')]
for a, b, h in M: ov.append(O(a, b, 'M', big(h), 1 if a == 0 else 0))
B = [(0.05, 2.7, f'ידעתם שהקקי של {Y("וומבט")} בצורת {Y("קובייה")}?'), (2.8, 4.7, f'הוא מקבל את הצורה {Y("בסוף המעי")}'),
     (4.75, 8.0, f'כנראה כי דפנות המעי {Y("נמתחות לא באותה מידה")}'), (8.1, 12.5, f'קוביות לא מתגלגלות — כנראה {Y("מסמן טריטוריה")}'),
     (12.7, 15.1, f'שלחו למי שמסדר הכול {Y("בקופסאות")}'), (15.2, D, f'כתבו {Y("שם")} בתגובות — ואני אקרא לכם!')]
for a, b, h in B: ov.append(O(a, b, 'B', sub(h)))
spec = {'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .3, 'novg': 0, 'vgmax': .3,
        'hits': [0.02, 2.8, 4.75, 8.1, 12.7, 15.2],
        'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': 0}], 'ov': ov}
print(json.dumps(spec, ensure_ascii=False))
