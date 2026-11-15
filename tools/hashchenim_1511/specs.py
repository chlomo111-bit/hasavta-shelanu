"""Specs de montage (compose.py) du reel et de la story השכנים 15.11 (format B : gros plan visage + texte au centre).
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['face', 'door', 'react']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:40%;background:{bg};color:#fff;font:900 40px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'נכנסת 🚪', '#2fbf71'), btn('2️⃣', 'טורקת 💥', '#E5484D')
D = 7.6
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .45, 'novg': 2.0, 'vgmax': .55,
 'hits': [0.05, 2.0, 2.66, 3.6, 6.4],
 'seg': [{'t0': 0, 't1': 2.0, 'clip': 'face', 'off': 0, 'zoom': .06},
         {'t0': 2.0, 't1': 3.6, 'clip': 'door', 'off': .3, 'zoom': .1},
         {'t0': 3.6, 't1': 6.4, 'clip': 'react', 'off': 0, 'zoom': .08},
         {'t0': 6.4, 't1': D, 'clip': 'face', 'off': 1.5, 'zoom': .05}],
 'ov': [dict(O(0, 2.0, 'T', pill('1 או 2? 👇', 30, 'rgba(10,8,24,.82)', '#fff')), np=1),
        dict(O(0, 1.56, 'M', bx(f'המפתח {Y("פתח")}… 🗝️', 60)), np=1),
        O(1.56, 2.0, 'M', bx(f'את דלת {Y("8")} 🚪', 60)),
        O(2.0, 2.66, 'M', bx('ו…', 64)),
        O(2.66, 3.6, 'B', pill('משהו יצא משם! 😱', 58, '#fff')),
        O(3.6, 5.59, 'T', bx('מה אני עושה? 😨', 46)),
        O(3.38, 3.6, 'M', B1), O(3.6, 4.54, 'B', B1), O(4.54, 5.59, 'B', B1 + B2), dict(O(5.59, D, 'B', B1 + B2), np=1),
        O(5.59, 6.4, 'T', pill('כתבו "שכן" ותיכנסו 🏢', 44)), O(6.4, D, 'T', pill('📩 שלחו לשכן שלכם', 46))]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 6.9
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 1.29, 2.54, 4.22], 'novg': 1.0, 'vgmax': .5,
 'seg': [{'t0': 0, 't1': 1.29, 'clip': 'face', 'off': .3, 'zoom': .05}, {'t0': 1.29, 't1': 2.54, 'clip': 'door', 'off': .2, 'zoom': .08},
         {'t0': 2.54, 't1': 4.22, 'clip': 'react', 'off': .5, 'zoom': .07}, {'t0': 4.22, 't1': SD, 'clip': 'face', 'off': 1.0, 'zoom': .05}],
 'ov': [dict(O(0, SD, 'T', pill('🏢 השכנים · שכנה חדשה!', 28, '#C792EA', '#1a0f2a')), np=1),
        dict(O(0, 1.29, 'M', bx(f'{Y("הילי")} נכנסה לבניין! 🙌', 52)), np=1),
        O(1.29, 2.54, 'M', bx(f'ודלת {Y("8")} נפתחה… 🚪', 52)),
        O(2.54, 3.4, 'M', bx('מה יצא משם? 👀', 52)), O(3.4, 4.22, 'M', pill('בריל החדש ←', 52, '#fff')),
        O(4.22, SD, 'M', bx(f'כתבו {Y("שכן")} 🏢<br>והשם שלכם בפרק הבא!', 46))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
