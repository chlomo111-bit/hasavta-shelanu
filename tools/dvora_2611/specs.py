"""Specs compose.py « ידעתם? עם דבורה » #6 (26.11 soir) : בננה = ברי. Usage : python3 specs.py <dossier_images_10fps> > spec.json"""
import json, sys
R = sys.argv[1]; D = 17.9
Y = lambda s: f'<span class=y>{s}</span>'
big = lambda s, sz=84: f'<div style="font:900 {sz}px/1.1 H">{s}</div>'
sub = lambda s: f'<div class=box style="font:900 32px/1.2 H">{s}</div>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
title = '<div class=pill style="background:#FFC24B;color:#140c04;font:900 30px/1.15 H">ידעתם? עם דבורה 🐝 · 6</div>'
ov = [O(0, D, 'T', title, 1)]
M = [(0, .9, f'{Y("ידעתם")}?'), (.9, 1.7, f'{Y("בננה")} 🍌'), (1.7, 2.4, f'{Y("ברי")}!'), (2.4, 3.3, f'{Y("תות שדה")}? 🍓'),
     (3.3, 4.4, f'{Y("פרח")} אחד 🌸'), (4.4, 5.9, f'{Y("שחלה")} אחת'), (5.9, 7.5, f'{Y("בננה")} ✅'),
     (7.5, 8.7, f'{Y("הרבה")}'), (8.7, 9.7, f'{Y("שחלות")}'), (9.7, 11.0, f'לא {Y("ברי")} ❌'),
     (11.0, 12.8, f'{Y("שלחו")} 📩'), (12.8, 14.0, f'{Y("מבין")} בפירות?'),
     (14.0, 14.9, f'{Y("מחר")}:'), (14.9, 15.9, f'{Y("כריש")} 🦈'), (15.9, 16.7, f'או {Y("עץ")}? 🌳'), (16.7, D, f'{Y("עקבו")} 🐝')]
for a, b, h in M: ov.append(O(a, b, 'M', big(h), 1 if a == 0 else 0))
B = [(0.07, 3.3, f'ידעתם ש{Y("בננה")} היא בעצם {Y("ברי")} — ותות שדה {Y("לא")}?'),
     (3.3, 7.5, f'ברי נוצר מ{Y("פרח אחד")} עם {Y("שחלה אחת")} — וזה בדיוק הבננה'),
     (7.5, 11.0, f'בתות שדה יש {Y("הרבה שחלות")} — אז הוא לא נחשב ברי'),
     (11.0, 14.0, f'שלחו למי ש{Y("חושב שהוא מבין בפירות")} 😛'),
     (14.0, 16.7, f'מחר: מה עתיק יותר — {Y("כריש")} או {Y("עץ")}?'), (16.7, D, f'{Y("עקבו")} כדי לדעת 🐝')]
for a, b, h in B: ov.append(O(a, b, 'B', sub(h)))
spec = {'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .3, 'novg': 0, 'vgmax': .3,
        'hits': [0.02, 3.3, 7.5, 11.0, 14.0],
        'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': 0}], 'ov': ov}
print(json.dumps(spec, ensure_ascii=False))
