"""Specs compose.py « ידעתם? עם דבורה » #2 (24.11 matin) : תמנון, 3 לבבות. Usage : python3 specs.py <dossier_images_10fps> > spec.json"""
import json, sys
R = sys.argv[1]; D = 17.2
Y = lambda s: f'<span class=y>{s}</span>'
big = lambda s, sz=84: f'<div style="font:900 {sz}px/1.1 H">{s}</div>'
sub = lambda s: f'<div class=box style="font:900 34px/1.2 H">{s}</div>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
title = '<div class=pill style="background:#FFC24B;color:#140c04;font:900 30px/1.15 H">ידעתם? עם דבורה 🐝 · 2</div>'
ov = [O(0, D, 'T', title, 1)]
M = [(0, 1.15, f'{Y("ידעתם")}?'), (1.15, 2.5, f'{Y("תמנון")} 🐙'), (2.5, 3.4, f'{Y("שני")} ❤️❤️'), (3.4, 4.62, f'{Y("זימים")}'),
     (4.62, 5.4, f'{Y("השלישי")} ❤️'), (5.4, 7.4, f'כל {Y("הגוף")}'), (7.4, 8.5, f'שלחו 📩'), (8.5, 9.8, f'{Y("לב ענק")} 💖'),
     (9.8, 10.8, f'{Y("מחר")}'), (10.8, 12.0, f'{Y("דבש")} 🍯'), (12.0, 13.5, f'דבורה {Y("אחת")}?'), (13.5, 14.6, f'{Y("עקבו")} 🐝'),
     (14.3, 15.45, f'{Y("כתבו")} שם ✍️'), (15.45, D, f'{Y("אקרא")} לכם!')]
for a, b, h in M: ov.append(O(a, b, 'M', big(h), 1 if a == 0 else 0))
B = [(0.05, 2.45, f'ידעתם שלתמנון יש {Y("שלושה לבבות")}?'), (2.7, 4.62, f'שני לבבות שולחים דם {Y("לזימים")}'),
     (4.65, 7.0, f'והשלישי שולח אותו {Y("לכל שאר הגוף")}'), (7.5, 9.4, f'שלחו את זה לחבר {Y("עם לב ענק")}'),
     (9.7, 13.5, f'מחר: כמה {Y("דבש")} עושה דבורה אחת בכל חייה?'), (13.7, D, f'עקבו, וכתבו {Y("שם")} בתגובות — ואני אקרא לכם!')]
for a, b, h in B: ov.append(O(a, b, 'B', sub(h)))
spec = {'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .3, 'novg': 0, 'vgmax': .3,
        'hits': [0.02, 2.55, 4.65, 7.45, 9.8, 13.7],
        'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': 0}], 'ov': ov}
print(json.dumps(spec, ensure_ascii=False))
