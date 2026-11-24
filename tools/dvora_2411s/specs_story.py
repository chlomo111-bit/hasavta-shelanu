"""Story teaser 24.11 soir. Usage : python3 specs_story.py <dossier_images_10fps> > spec.json"""
import json, sys
R = sys.argv[1]; D = 6.6
Y = lambda s: f'<span class=y>{s}</span>'
big = lambda s, sz=88: f'<div style="font:900 {sz}px/1.1 H;margin-top:70px">{s}</div>'
sub = lambda s: f'<div class=box style="font:900 36px/1.2 H;margin-bottom:110px">{s}</div>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
ov = []
M = [(0, 1.0, f'{Y("מחר")}'), (1.0, 2.0, f'{Y("וומבט")}'), (2.0, 2.96, f'{Y("קוביות")} 🟫'), (2.96, 4.3, f'{Y("עקבו")} 🐝'), (4.3, D, f'{Y("ידעתם")}? 🐝')]
for a, b, h in M: ov.append(O(a, b, 'M', big(h), 1 if a == 0 else 0))
B = [(0.05, 2.7, f'מחר: למה {Y("הוומבט")} עושה {Y("קוביות")}?'), (2.9, D, f'עקבו כדי {Y("לדעת")} — ידעתם? עם דבורה')]
for a, b, h in B: ov.append(O(a, b, 'B', sub(h)))
print(json.dumps({'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .3, 'novg': 0, 'vgmax': .3, 'hits': [0.02, 1.0, 2.0, 2.96],
  'seg': [{'t0': 0, 't1': D, 'clip': 'st', 'off': 0, 'zoom': 0}] and [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': 0}], 'ov': ov}, ensure_ascii=False))
