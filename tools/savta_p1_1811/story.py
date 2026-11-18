"""Story vidéo 18.11 (teste le cliffhanger du פרק 1). Usage : python3 story.py <frames_reel> <outdir>"""
import json, sys
F, OUT = sys.argv[1], sys.argv[2]
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=False: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, **({'np': True} if np else {})}
# voix : הסיר רועד 0 | מה סבתא תעשה 1.17 | הפרק החדש בריל 2.33 | תבחרו 4.03 | אחת 4.85 | או שתיים 5.53 | fin 6.3
st = [O(-1, 9, 'T', pill('👵 פרק 1 · דברים שכל סבתא אומרת', 26, '#FF8FB8', '#2a0a18')),
      O(-1, 1.17, 'M', bx(f'הסיר {Y("רועד…")} 👀', 56)),
      O(1.17, 2.33, 'M', bx(f'מה סבתא<br>{Y("תעשה?")} 🤔', 58)),
      O(2.33, 4.03, 'M', pill('הפרק החדש בריל 👀', 46)),
      O(4.03, 9, 'M', bx('תבחרו בתגובות 👇', 44) + '<div style="height:14px"></div><div style="display:flex;gap:12px;justify-content:center;white-space:nowrap">' + pill('1 🍲 עוד אוכל', 32) + pill('2 🎂 עוגה ענקית', 32, '#FF8FB8', '#2a0a18') + '</div>', False)]
story = {'dur': 7.0, 'clips': {'a': {'dir': F, 'fps': 10}}, 'flash': .25, 'hits': [2.33, 4.03], 'novg': 0, 'vgmax': .45,
         'seg': [{'t0': 0, 't1': 2.33, 'clip': 'a', 'off': 10.0, 'zoom': .04}, {'t0': 2.33, 't1': 7.0, 'clip': 'a', 'off': 8.4, 'zoom': .03}], 'ov': st}
json.dump(story, open(f'{OUT}/story.json', 'w'), ensure_ascii=False)
print('ok')
