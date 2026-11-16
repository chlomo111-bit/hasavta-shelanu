"""Specs de montage (compose.py) du reel et de la story השכנים 16.11 (format A : action dès l'image 0, petit texte en haut, centre libre).
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['run', 'key', 'face']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:40%;background:{bg};color:#fff;font:900 36px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'רודפת 🏃‍♀️', '#2fbf71'), btn('2️⃣', 'נועלת 🔒', '#E5484D')
D = 7.0
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .4, 'novg': 2.0, 'vgmax': .45,
 'hits': [0.05, 1.31, 2.64, 5.16],
 'seg': [{'t0': 0, 't1': 1.31, 'clip': 'run', 'off': .6, 'zoom': .1},
         {'t0': 1.31, 't1': 2.64, 'clip': 'key', 'off': .2, 'zoom': .1},
         {'t0': 2.64, 't1': 5.16, 'clip': 'face', 'off': 0, 'zoom': .07},
         {'t0': 5.16, 't1': D, 'clip': 'run', 'off': 0, 'zoom': .08}],
 'ov': [dict(O(0, 1.31, 'T', bx('הוא ברח! 🐰', 44)), np=1),
        O(1.31, 2.64, 'T', bx(f'עם {Y("המפתח")} שלי! 🗝️', 44)),
        O(2.64, 5.16, 'T', bx('מה אני עושה? 😨', 42)),
        O(2.64, 4.03, 'B', B1), O(4.03, 5.16, 'B', B1 + B2), dict(O(5.16, D, 'B', B1 + B2), np=1),
        O(5.16, 6.1, 'T', pill('כתבו "שכן" ותיכנסו 🏢', 40)), O(6.1, D, 'T', pill('📩 שלחו לשכן שלכם', 42))]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 7.2
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 1.57, 3.36, 4.51], 'novg': 1.0, 'vgmax': .5,
 'seg': [{'t0': 0, 't1': 1.57, 'clip': 'face', 'off': .3, 'zoom': .05}, {'t0': 1.57, 't1': 3.36, 'clip': 'run', 'off': .4, 'zoom': .08},
         {'t0': 3.36, 't1': 4.51, 'clip': 'key', 'off': .5, 'zoom': .07}, {'t0': 4.51, 't1': SD, 'clip': 'face', 'off': 1.0, 'zoom': .05}],
 'ov': [dict(O(0, SD, 'T', pill('🏢 השכנים · שכנה חדשה!', 28, '#C792EA', '#1a0f2a')), np=1),
        dict(O(0, 1.57, 'M', bx(f'{Y("הילי")} בבניין! 🙌', 52)), np=1),
        O(1.57, 3.36, 'M', bx(f'והארנב ברח<br>עם {Y("המפתח")}! 🗝️', 50)),
        O(3.36, 4.51, 'M', pill('בריל החדש ←', 52, '#fff')),
        O(4.51, SD, 'M', bx(f'כתבו {Y("שכן")} 🏢<br>והשם שלכם בפרק הבא!', 46))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
