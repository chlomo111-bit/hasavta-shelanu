"""Specs de montage (compose.py local, avec badge « פרק 1 ») du reel Ruche 18.11 soir — série « drames d'amies dans la ruche », פרק 1 « אותה שמלה ».
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['meet', 'dress', 'lookA', 'lookG', 'crowd', 'close', 'end']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:40%;background:{bg};color:#fff;font:900 30px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'הולכת להחליף 👗', '#E0609A'), btn('2️⃣', 'מצטלמות תאומות 📸', '#2E9E5B')
D = 14.2
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .45, 'novg': 2.0, 'vgmax': .4,
 'ep': '<span style="display:inline-block;background:rgba(26,14,6,.6);border-radius:14px;padding:3px 14px;font:900 20px H;color:#fff">פרק 1</span>',
 'hits': [0.08, 3.4, 5.5, 9.05, 9.45],
 'seg': [{'t0': 0, 't1': 1.5, 'clip': 'meet', 'off': .4, 'zoom': .05},
         {'t0': 1.5, 't1': 3.4, 'clip': 'dress', 'off': 0, 'zoom': .05},
         {'t0': 3.4, 't1': 4.0, 'clip': 'lookA', 'off': .2, 'zoom': .08},
         {'t0': 4.0, 't1': 5.5, 'clip': 'crowd', 'off': 0, 'zoom': .03},
         {'t0': 5.5, 't1': 6.3, 'clip': 'lookG', 'off': 0, 'zoom': .08},
         {'t0': 6.3, 't1': 9.45, 'clip': 'close', 'off': 0, 'zoom': .1},
         {'t0': 9.45, 't1': D, 'clip': 'end', 'off': 0, 'zoom': .04, 'speed': .65}],
 'ov': [dict(O(0, 1.5, 'T', bx(f'כשהחברה שלך באה<br>עם {Y("אותה שמלה")} בדיוק… 😳', 44)), np=1),
        O(1.5, 3.4, 'T', bx(f'אותה. שמלה. {Y("בדיוק.")} 👗', 50)),
        O(3.4, 4.0, 'T', bx('רגע… מה?! 😳', 54)),
        O(4.0, 5.5, 'T', bx(f'כל הכוורת {Y("מסתכלת")}… 👀', 50)),
        O(5.5, 6.3, 'T', bx('היא לא מוותרת 😤', 50)),
        O(6.3, 7.45, 'T', bx(f'והיא {Y("מתקרבת")}…', 54)),
        O(7.45, 8.6, 'T', bx('עוד צעד… 😬', 56)),
        O(8.6, 9.45, 'T', bx('ו…', 80)),
        O(9.45, 11.8, 'T', bx(f'{Y("אתם מחליטים")}:<br>1 או 2? בתגובות 👇', 46)),
        O(11.8, D, 'T', bx(f'אתם מחליטים: {Y("1")} או {Y("2")}? 👇<br>👯‍♀️ {Y("תייגו")} את החברה שלכם', 40)),
        O(10.62, 11.1, 'B', B1), O(11.1, D, 'B', B1 + B2),
        ]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 7.4
story = {'dur': SD, 'fps': 30, 'clips': C, 'flash': .35, 'hits': [0.05, 1.37, 3.64], 'novg': 1.0, 'vgmax': .45,
 'ep': '<span style="display:inline-block;background:#FFC24B;border-radius:14px;padding:4px 16px;font:900 24px H;color:#140c04">🐝 פרק 1 · אותה שמלה</span>',
 'seg': [{'t0': 0, 't1': 1.37, 'clip': 'close', 'off': 1.6, 'zoom': .06}, {'t0': 1.37, 't1': 3.64, 'clip': 'end', 'off': 0, 'zoom': .05, 'speed': .9},
         {'t0': 3.64, 't1': SD, 'clip': 'dress', 'off': 0, 'zoom': .05, 'speed': .45}],
 'ov': [dict(O(0, 1.37, 'M', bx(f'אז מה היא {Y("עושה")}? 😬', 52)), np=1),
        O(1.37, 3.64, 'M', bx(f'{Y("1")} הולכת להחליף 👗', 50)),
        O(3.64, SD, 'M', bx(f'{Y("2")} מצטלמות תאומות 📸', 50)),
        O(6.07, SD, 'B', pill('כתבו 1 או 2 בתגובות לרילס 👇', 34, '#fff'))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
