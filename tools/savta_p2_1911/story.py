"""Story vidéo 19.11 (teaser du cliffhanger du פרק 2). Usage : python3 story.py <frames_reel> <outdir>"""
import json, sys
F, OUT = sys.argv[1], sys.argv[2]
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=False: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, **({'np': True} if np else {})}
# voix : מישהו בדלת 0 | הנכד שלא מתקשר 1.63 | או השכנה 3.23 | תכתבו 1 או 2 4.63 | fin 6.43
st = [O(-1, 9, 'T', pill('👵 פרק 2 · דברים שכל סבתא אומרת', 26, '#FF8FB8', '#2a0a18')),
      O(-1, 1.63, 'M', bx(f'מישהו {Y("בדלת")}<br>של סבתא… 🚪', 54)),
      O(1.63, 3.23, 'B', pill('1 👦 הנכד שלא מתקשר?', 40)),
      O(3.23, 4.63, 'B', pill('2 👵 השכנה החטטנית?', 40, '#FF8FB8', '#2a0a18')),
      O(4.63, 9, 'B', bx('תכתבו בתגובות לריל 👇', 40) + '<div style="height:14px"></div><div style="display:flex;gap:12px;justify-content:center;white-space:nowrap">' + pill('1 👦 הנכד', 34) + pill('2 👵 השכנה', 34, '#FF8FB8', '#2a0a18') + '</div>')]
story = {'dur': 6.8, 'clips': {'a': {'dir': F, 'fps': 10}}, 'flash': .25, 'hits': [1.63, 4.63], 'novg': 0, 'vgmax': .45,
         'seg': [{'t0': 0, 't1': 1.63, 'clip': 'a', 'off': 9.55, 'zoom': .04}, {'t0': 1.63, 't1': 4.63, 'clip': 'a', 'off': 11.0, 'zoom': .03},
                 {'t0': 4.63, 't1': 6.8, 'clip': 'a', 'off': 9.9, 'zoom': .05}], 'ov': st}
json.dump(story, open(f'{OUT}/story.json', 'w'), ensure_ascii=False)
print('ok')
