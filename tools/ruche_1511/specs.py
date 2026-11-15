"""Specs de montage (compose.py) du reel et de la story Ruche 15.11 (format B : gros plan + texte au centre).
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['pink', 'cool', 'pinksad']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:35%;background:{bg};color:#fff;font:900 34px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'הוורודה 🌸', '#E0609A'), btn('2️⃣', 'המשקפיים 😎', '#3A7BD5')
D = 7.0
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .45, 'novg': 2.6, 'vgmax': .5,
 'hits': [0.05, 1.94, 2.9, 3.4, 4.5],
 'seg': [{'t0': 0, 't1': 2.6, 'clip': 'pink', 'off': 0, 'zoom': .05},
         {'t0': 2.6, 't1': 4.5, 'clip': 'cool', 'off': .2, 'zoom': .07},
         {'t0': 4.5, 't1': D, 'clip': 'pinksad', 'off': 0, 'zoom': .05}],
 'ov': [dict(O(0, 1.94, 'M', bx(f'רק אחת תקבל<br>את {Y("הכתר")} 👑', 60)), np=1),
        O(1.94, 2.92, 'M', bx(f'רגע… {Y("מה")}?! 😳', 64)),
        O(2.9, 3.4, 'B', bx(f'{Y("היא")}?! 😎', 72)),
        O(3.4, 4.5, 'M', bx(f'{Y("1")} או {Y("2")}? 👇', 60)),
        O(3.4, 3.92, 'B', B1), O(3.92, 4.5, 'B', B1 + B2),
        O(4.5, 5.9, 'M', pill('כתבו "דבורה"<br>ותיכנסו 🐝', 54)),
        O(5.9, D, 'M', pill('📩 שלחו<br>לחברה שלכם', 56, '#fff'))]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 6.9
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 2.04, 3.14, 4.22], 'novg': 1.0, 'vgmax': .5,
 'seg': [{'t0': 0, 't1': 2.04, 'clip': 'pink', 'off': .4, 'zoom': .05}, {'t0': 2.04, 't1': 3.14, 'clip': 'pink', 'off': 1.6, 'zoom': .06},
         {'t0': 3.14, 't1': 4.9, 'clip': 'cool', 'off': .05, 'zoom': .07}, {'t0': 4.9, 't1': SD, 'clip': 'cool', 'off': 2.0, 'zoom': .05}],
 'ov': [dict(O(0, SD, 'T', pill('🐝 הכוורת שלנו · מלכת השבוע', 28)), np=1),
        dict(O(0, 2.04, 'M', bx(f'<span dir=ltr>@shellydor20</span><br>{Y("שוב")} מלכת השבוע! 👑', 46)), np=1),
        O(2.04, 3.14, 'M', bx('אבל בריל החדש… 👀', 50)),
        O(3.14, 4.22, 'M', pill('הכתר עף! 😱', 62, '#fff')),
        O(4.22, 4.9, 'M', bx(f'מי מגיע לה? {Y("1")} או {Y("2")}', 48)),
        O(4.9, SD, 'M', bx(f'כתבו {Y("דבורה")} 🐝<br>והשם שלכן בכוורת!', 46)),
        O(4.9, SD, 'B', pill('👈 בריל החדש', 44, '#fff'))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
