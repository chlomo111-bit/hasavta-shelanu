"""Specs de montage (compose.py) du reel et de la story Ruche 16.11 (format A : action dès l'image 0, petit texte en haut, centre libre).
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['drop', 'tug', 'win', 'end']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:35%;background:{bg};color:#fff;font:900 34px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'מגיע לה 👑', '#2E9E5B'), btn('2️⃣', 'לא מגיע 😤', '#E0609A')
D = 7.2
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .4, 'novg': 3.0, 'vgmax': .45,
 'hits': [0.2, 1.8, 3.0, 3.5, 4.6],
 'seg': [{'t0': 0, 't1': 1.8, 'clip': 'drop', 'off': .7, 'zoom': .05},
         {'t0': 1.8, 't1': 3.0, 'clip': 'tug', 'off': 0, 'zoom': .06},
         {'t0': 3.0, 't1': 4.6, 'clip': 'win', 'off': 0, 'zoom': .07},
         {'t0': 4.6, 't1': D, 'clip': 'end', 'off': 0, 'zoom': .05}],
 'ov': [dict(O(0, 1.8, 'T', bx(f'2 בנות. {Y("כתר")} אחד 👑', 46)), np=1),
        O(1.8, 3.0, 'T', bx(f'מי {Y("תתפוס")}?! 😳', 50)),
        O(3.0, 4.2, 'T', bx(f'{Y("הירוקה")} לקחה! 🤓', 50)),
        O(4.2, 5.7, 'T', bx(f'מגיע לה? {Y("1")} או {Y("2")} 👇', 46)),
        O(4.2, 4.75, 'B', B1), O(4.75, 5.7, 'B', B1 + B2),
        O(5.7, 6.45, 'M', pill('כתבו "דבורה"<br>ותיכנסו 🐝', 54)),
        O(6.45, D, 'M', pill('📩 שלחו<br>לחברה שלכם', 56, '#fff'))]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 7.9
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 2.16, 3.31, 5.14], 'novg': 1.0, 'vgmax': .5,
 'seg': [{'t0': 0, 't1': 2.16, 'clip': 'end', 'off': .2, 'zoom': .05}, {'t0': 2.16, 't1': 3.31, 'clip': 'drop', 'off': .55, 'zoom': .06},
         {'t0': 3.31, 't1': 5.14, 'clip': 'tug', 'off': 0, 'zoom': .06}, {'t0': 5.14, 't1': SD, 'clip': 'win', 'off': .1, 'zoom': .05}],
 'ov': [dict(O(0, SD, 'T', pill('🐝 הכוורת שלנו · מרוץ הכתר', 28)), np=1),
        dict(O(0, 2.16, 'M', bx(f'<span dir=ltr>@shellydor20</span><br>{Y("עדיין")} מלכת השבוע 👑', 46)), np=1),
        O(2.16, 3.31, 'M', bx('אבל בריל החדש… 👀', 50)),
        O(3.31, 5.14, 'M', pill('2 בנות. כתר אחד! 😱', 52, '#fff')),
        O(5.14, 5.84, 'M', bx(f'מי {Y("תנצח")}?', 56)),
        O(5.84, SD, 'M', bx(f'כתבו {Y("דבורה")} 🐝<br>והשם שלכן בכוורת!', 46)),
        O(5.84, SD, 'B', pill('👈 בריל החדש', 44, '#fff'))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
