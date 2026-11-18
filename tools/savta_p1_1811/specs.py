"""Specs du reel « פרק 1 – רק עוד ביס אחד! » (18.11) + story vidéo. Usage : python3 specs.py <frames_reel> <outdir>"""
import json, sys
F, OUT = sys.argv[1], sys.argv[2]
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=False: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, **({'np': True} if np else {})}
EP = '<div style="font:900 20px H;color:#fff;opacity:.85;margin-bottom:8px;text-shadow:0 2px 8px #000">פרק 1 · דברים שכל סבתא אומרת</div>'
T = lambda s, sz=58, np=False: (lambda h: h)(EP + bx(s, sz))
# voix (coupée + atempo 1.12) : ביס 0 | עור ועצמות 1.44 | קציצה 4.02 | ועוד 5.02 | ועוד! 5.85 | שבעתם 6.67 | רגע 7.8 | לא הולכים 8.61 | סבתא הכינה 10.0 | עוד משהו 10.78 | אתם מחליטים 11.31 | אחת 12.13 | או שתיים 12.53 | שלחו 13.12 | fin 14.43
ov = [O(-1, 1.44, 'T', T(f'{Y("רק עוד ביס אחד!")} 🥄', 62), True),
      O(1.44, 4.02, 'T', T(f'תראו אותך…<br>{Y("עור ועצמות!")} 😂', 56)),
      O(4.02, 5.02, 'T', T('עוד קציצה…', 58)), O(5.02, 5.85, 'T', T('…ועוד אחת…', 58), True),
      O(5.85, 6.67, 'T', T(f'{Y("ועוד אחת!!")} 😱', 64)),
      O(6.67, 7.8, 'T', T(f'מה, {Y("שבעתם?!")} 🤨', 62)),
      O(7.8, 8.61, 'T', T('רגע…', 60)), O(8.61, 10.0, 'T', T(f'לא הולכים<br>{Y("לשום מקום!")} ✋', 56), True),
      O(10.0, 10.78, 'T', T('סבתא הכינה…', 58)), O(10.78, 11.45, 'T', T(f'…{Y("עוד משהו")} 👀', 60), True),
      ]
V = '<div style="height:10px"></div>' + pill('מה יש בסיר? 🍲', 34, '#ffffff') + '<div style="height:10px"></div>' + \
    '<div style="display:flex;gap:10px;justify-content:center;white-space:nowrap">' + pill('1 🍲 עוד אוכל', 30) + pill('2 🎂 עוגה ענקית', 30, '#FF8FB8', '#2a0a18') + '</div>'
ov += [O(11.45, 20, 'T', EP + pill('אתם מחליטים: 1 או 2?<br>בתגובות 👇', 38) + V), O(13.12, 20, 'B', pill('💌 שלחו לסבתא שלכם', 42, '#FF8FB8', '#2a0a18'))]
reel = {'dur': 14.8, 'clips': {'a': {'dir': F, 'fps': 10}}, 'flash': .35, 'hits': [4.15, 5.15, 6.0, 7.04, 11.45], 'novg': 2.0, 'vgmax': .5,
        'seg': [{'t0': 0, 't1': 14.8, 'clip': 'a', 'off': 0, 'zoom': 0}], 'ov': ov}
json.dump(reel, open(f'{OUT}/reel.json', 'w'), ensure_ascii=False)
print('ok')
