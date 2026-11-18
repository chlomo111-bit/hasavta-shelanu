"""Specs de montage (compose.py) du reel et de la story Ruche 18.11 (format A : action dès l'image 0, petit texte en haut, centre libre).
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['steal', 'chase', 'drop', 'end']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:35%;background:{bg};color:#fff;font:900 34px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'הירוקה 🤓', '#2E9E5B'), btn('2️⃣', 'הגנבת 😈', '#E0609A')
D = 7.8
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .4, 'novg': 3.0, 'vgmax': .45,
 'hits': [0.25, 1.5, 2.7, 3.07, 4.4],
 'seg': [{'t0': 0, 't1': 1.5, 'clip': 'steal', 'off': .2, 'zoom': .05},
         {'t0': 1.5, 't1': 2.7, 'clip': 'chase', 'off': 0, 'zoom': .06},
         {'t0': 2.7, 't1': 4.4, 'clip': 'drop', 'off': 0, 'zoom': .07},
         {'t0': 4.4, 't1': D, 'clip': 'end', 'off': 0, 'zoom': .05}],
 'ov': [dict(O(0, 1.18, 'T', bx(f'היא {Y("גנבה")} את הכתר! 😱', 42)), np=1),
        O(1.18, 2.7, 'T', bx(f'{Y("רדיפה")} בכוורת! 🐝💨', 50)),
        O(2.7, 3.83, 'T', bx(f'אוי! הכתר {Y("נפל")}! 👑', 50)),
        O(3.83, 4.75, 'T', bx(f'בחזרה {Y("לירוקה")}! 🤓', 50)),
        O(4.75, 6.31, 'T', bx(f'מי צודקת? {Y("1")} או {Y("2")} 👇', 46)),
        O(4.75, 5.39, 'B', B1), O(5.39, 6.31, 'B', B1 + B2),
        O(6.31, 7.05, 'M', pill('כתבו "דבורה"<br>ותיכנסו 🐝', 54)),
        O(7.05, D, 'M', pill('📩 שלחו<br>לחברה שלכם', 56, '#fff'))]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 7.0
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 1.15, 3.38, 4.09], 'novg': 1.0, 'vgmax': .5,
 'seg': [{'t0': 0, 't1': 1.15, 'clip': 'end', 'off': .3, 'zoom': .05}, {'t0': 1.15, 't1': 3.38, 'clip': 'steal', 'off': 0, 'zoom': .06},
         {'t0': 3.38, 't1': 4.09, 'clip': 'drop', 'off': .2, 'zoom': .06}, {'t0': 4.09, 't1': SD, 'clip': 'chase', 'off': 0, 'zoom': .05}],
 'ov': [dict(O(0, SD, 'T', pill('🐝 הכוורת שלנו · מרוץ הכתר', 28)), np=1),
        dict(O(0, 1.15, 'M', bx(f'<span dir=ltr>@hyll.khbsvb</span><br>{Y("נכנסה")} לכוורת! 🐝', 46)), np=1),
        O(1.15, 2.3, 'M', bx('אבל בריל החדש… 👀', 50)),
        O(2.3, 3.38, 'M', pill('מישהי גנבה את הכתר! 😱', 48, '#fff')),
        O(3.38, 4.09, 'M', bx(f'מי {Y("צודקת")}?', 56)),
        O(4.09, SD, 'M', bx(f'כתבו {Y("דבורה")} 🐝<br>והשם שלכן בסטורי!', 46)),
        O(4.09, SD, 'B', pill('👈 בריל החדש', 44, '#fff'))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
