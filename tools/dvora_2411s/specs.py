"""Specs compose.py « ידעתם? עם דבורה » #3 (24.11 soir) : דבש 1/12 כפית. Usage : python3 specs.py <dossier_images_10fps> > spec.json"""
import json, sys
R = sys.argv[1]; D = 18.76
Y = lambda s: f'<span class=y>{s}</span>'
FR = '<span style="direction:ltr;unicode-bidi:isolate;display:inline-block">1/12</span>'
big = lambda s, sz=84: f'<div style="font:900 {sz}px/1.1 H">{s}</div>'
sub = lambda s: f'<div class=box style="font:900 34px/1.2 H">{s}</div>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
title = '<div class=pill style="background:#FFC24B;color:#140c04;font:900 30px/1.15 H">ידעתם? עם דבורה 🐝 · 3</div>'
ov = [O(0, D, 'T', title, 1)]
M = [(0, 1.0, f'{Y("ידעתם")}?'), (1.0, 2.0, f'{Y("דבורה")} 🐝'), (2.0, 3.0, f'{Y("אחת")}'), (3.0, 4.3, f'{Y(FR)} כפית'), (4.3, 5.5, f'{Y("דבש")} 🍯'),
     (5.6, 6.8, f'כפית {Y("אחת")}'), (6.8, 8.2, f'{Y("12")}'), (8.2, 9.9, f'{Y("דבורים")} 🐝'),
     (10.2, 11.3, f'{Y("שלחו")} 📩'), (11.3, 12.5, f'בלי {Y("רחמים")}'),
     (12.7, 13.7, f'{Y("מחר")}'), (13.7, 14.9, f'{Y("וומבט")}'), (14.9, 16.5, f'{Y("קוביות")} 🟫'),
     (16.7, 17.7, f'{Y("כתבו")} שם ✍️'), (17.7, D, f'{Y("אקרא")} לכם!')]
for a, b, h in M: ov.append(O(a, b, 'M', big(h), 1 if a == 0 else 0))
B = [(0.05, 5.4, f'ידעתם שדבורה אחת מייצרת רק {Y(FR+" כפית דבש")} בכל חייה?'), (5.6, 9.9, f'כדי למלא כפית אחת — צריך את העבודה של {Y("12 דבורים")}'),
     (10.2, 12.5, f'שלחו למי שמורח {Y("דבש בלי רחמים")}'), (12.7, 16.6, f'מחר: למה {Y("הוומבט")} עושה {Y("קוביות")}? עקבו!'), (16.7, D, f'כתבו {Y("שם")} בתגובות — ואני אקרא לכם!')]
for a, b, h in B: ov.append(O(a, b, 'B', sub(h)))
spec = {'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .3, 'novg': 0, 'vgmax': .3,
        'hits': [0.02, 3.0, 5.6, 8.2, 10.2, 12.7, 14.9, 16.7],
        'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': 0}], 'ov': ov}
print(json.dumps(spec, ensure_ascii=False))
