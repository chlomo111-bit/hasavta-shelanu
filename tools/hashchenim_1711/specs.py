"""Specs de montage (compose.py) du reel et de la story השכנים 17.11 (format B : gros plan visage + texte au centre).
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['face', 'door10', 'glow']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
P = lambda s: f'<span class=p>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:40%;background:{bg};color:#fff;font:900 36px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'דופקת 🚪', '#2fbf71'), btn('2️⃣', 'מחכה ⏳', '#E5484D')
D = 7.7
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .35, 'novg': 2.0, 'vgmax': .45,
 'hits': [0.05, 0.8, 2.5, 3.79, 6.04],
 'seg': [{'t0': 0, 't1': 0.8, 'clip': 'face', 'off': 0, 'zoom': .06},
         {'t0': 0.8, 't1': 2.5, 'clip': 'door10', 'off': .3, 'zoom': .08},
         {'t0': 2.5, 't1': 3.79, 'clip': 'glow', 'off': 0, 'zoom': .08},
         {'t0': 3.79, 't1': 6.04, 'clip': 'face', 'off': .6, 'zoom': .07},
         {'t0': 6.04, 't1': D, 'clip': 'glow', 'off': .8, 'zoom': .06}],
 'ov': [dict(O(0, D, 'T', pill('🏢 השכנים · אתם מחליטים: 1 או 2?', 24, '#C792EA', '#1a0f2a')), np=1),
        dict(O(0, 1.83, 'M', bx(f'ארנב ענק נכנס<br>לדלת {Y("10")}! 😨', 50)), np=1),
        O(1.83, 3.79, 'M', bx(f'ויש שם אור {P("ורוד")}… 👀', 48)),
        O(3.79, 6.04, 'M', bx('מה אני עושה? 😨', 48)),
        O(3.79, 4.93, 'B', B1), O(4.93, 6.04, 'B', B1 + B2), dict(O(6.04, D, 'B', B1 + B2), np=1),
        O(6.04, 6.9, 'M', pill('כתבו "שכן" ותיכנסו 🏢', 42)), O(6.9, D, 'M', pill('📩 שלחו לשכן שלכם', 44))]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 7.0
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 1.59, 3.13, 4.45], 'novg': 1.0, 'vgmax': .5,
 'seg': [{'t0': 0, 't1': 1.59, 'clip': 'face', 'off': 0, 'zoom': .05}, {'t0': 1.59, 't1': 3.13, 'clip': 'door10', 'off': .4, 'zoom': .08},
         {'t0': 3.13, 't1': 4.45, 'clip': 'glow', 'off': .3, 'zoom': .07}, {'t0': 4.45, 't1': SD, 'clip': 'face', 'off': .5, 'zoom': .05}],
 'ov': [dict(O(0, SD, 'T', pill('🏢 השכנים · פרק חדש!', 28, '#C792EA', '#1a0f2a')), np=1),
        dict(O(0, 1.59, 'M', bx(f'דנה רדפה<br>אחרי {Y("הארנב")}… 🏃‍♀️', 50)), np=1),
        O(1.59, 3.13, 'M', bx(f'והוא נכנס<br>לדלת {Y("10")}! 🐰', 50)),
        O(3.13, 4.45, 'M', pill('בריל החדש ←', 52, '#fff')),
        O(4.45, SD, 'M', bx(f'כתבו {Y("שכן")} 🏢<br>והשם שלכם בפרק הבא!', 46))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
