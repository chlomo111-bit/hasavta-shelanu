"""Specs du reel « פרק 2 – רגע! יש גם קינוח! » (19.11). Usage : python3 specs.py <frames_reel> <outdir>"""
import json, sys
F, OUT = sys.argv[1], sys.argv[2]
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=False: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, **({'np': True} if np else {})}
EP = '<div style="font:900 20px H;color:#fff;opacity:.85;margin-bottom:8px;text-shadow:0 2px 8px #000">פרק 2 · דברים שכל סבתא אומרת</div>'
T = lambda s, sz=58: EP + bx(s, sz)
PREV = '<div style="font:900 24px H;color:#FF8FB8;margin-bottom:6px;text-shadow:0 2px 8px #000">⏪ בפרק הקודם…</div>'
# voix (coupée + atempo 1.24) : רגע 0 | הסיר רעד 1.6 | ומה יצא 2.65 | עוגה 3.35 | ועוד קומה 3.9 / 4.66 | והנרות 5.56 | לא יום הולדת 6.34 | בשביל מי שלא מתקשר 7.29 | דינג דונג 9.05 | מי בדלת 9.77 | אתם מחליטים 10.72 | אחת הנכד 11.59 | שתיים השכנה 12.65 | שלחו 13.65 | fin 14.93
ov = [O(-1, 1.6, 'T', T(f'רגע! {Y("יש גם קינוח!")} 🎂', 60), True),
      O(1.6, 2.65, 'T', EP + PREV + bx(f'הסיר {Y("רעד…")} 🍲', 58)),
      O(2.65, 3.35, 'T', EP + PREV + bx(f'…ומה {Y("יצא?")} 👀', 58), True),
      O(3.35, 3.9, 'T', T(f'{Y("עוגה!!")} 🎂', 70)),
      O(3.9, 4.66, 'T', T('ועוד קומה…', 60)), O(4.66, 5.56, 'T', T(f'{Y("ועוד קומה!")} 😱', 62), True),
      O(5.56, 6.34, 'T', T('והנרות… 🕯️', 60)),
      O(6.34, 7.29, 'T', T(f'זה לא {Y("יום הולדת…")}', 56)),
      O(7.29, 9.05, 'T', T(f'זה בשביל מי<br>{Y("שלא מתקשר")} לסבתא 📵', 52), True),
      O(9.05, 9.77, 'T', T(f'🔔 {Y("דינג דונג!")}', 64)),
      O(9.77, 10.62, 'T', T(f'מי {Y("בדלת?!")} 👀', 66), True)]
V = '<div style="height:10px"></div>' + pill('מי בדלת? 🚪', 34, '#ffffff') + '<div style="height:10px"></div>' + \
    '<div style="display:flex;flex-direction:column;gap:10px;align-items:center;white-space:nowrap">' + pill('1 👦 הנכד שלא מתקשר', 32) + pill('2 👵 השכנה החטטנית', 32, '#FF8FB8', '#2a0a18') + '</div>'
ov += [O(10.62, 20, 'T', EP + pill('אתם מחליטים: 1 או 2?<br>בתגובות 👇', 38) + V), O(13.65, 20, 'B', pill('💌 שלחו לסבתא שלכם', 42, '#FF8FB8', '#2a0a18'))]
reel = {'dur': 15.1, 'clips': {'a': {'dir': F, 'fps': 10}}, 'flash': .35, 'hits': [3.4, 3.95, 4.7, 9.05, 10.62], 'novg': 2.0, 'vgmax': .5,
        'seg': [{'t0': 0, 't1': 15.1, 'clip': 'a', 'off': 0, 'zoom': 0}], 'ov': ov}
json.dump(reel, open(f'{OUT}/reel.json', 'w'), ensure_ascii=False)
print('ok')
