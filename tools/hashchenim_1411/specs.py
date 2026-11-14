"""Specs de montage (compose.py) du reel et de la story השכנים 14.11. Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 15} for k in ['face', 'rabbits', 'key', 'vote', 'enter']}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:6px;width:40%;background:{bg};color:#fff;font:900 40px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'לוקחת 🗝️', '#2fbf71'), btn('2️⃣', 'בורחת 🏃‍♀️', '#E5484D')
D = 11.9
reel = {'dur': D, 'clips': C, 'flash': .4, 'novg': 2.0, 'vgmax': .6,
 'hits': [0.05, 2.1, 2.72, 3.5, 4.55, 6.12, 7.49, 8.77, 10.19],
 'seg': [{'t0': 0, 't1': 2.1, 'clip': 'face', 'off': 0, 'zoom': .05},
         {'t0': 2.1, 't1': 3.5, 'clip': 'rabbits', 'off': 0, 'zoom': .08},
         {'t0': 3.5, 't1': 5.45, 'clip': 'key', 'off': 0, 'zoom': .1},
         {'t0': 5.45, 't1': 8.77, 'clip': 'vote', 'off': 0, 'zoom': .05},
         {'t0': 8.77, 't1': D, 'clip': 'rabbits', 'off': 1.6, 'zoom': .06}],
 'ov': [dict(O(0, 5.45, 'T', pill(f'1 או 2? 👇', 34, 'rgba(10,8,24,.82)', '#fff')), np=1),
        dict(O(0, 1.13, 'B', bx(f'נכנסתי לדירה…', 54)), np=1), O(1.13, 2.1, 'B', bx(f'נכנסתי לדירה<br>של {Y("השכן")} 🚪', 54)),
        O(2.1, 2.72, 'B', bx('והיא מלאה…', 54)), O(2.72, 3.5, 'M', pill('בארנבים! 🐰🐰🐰', 58, '#fff')),
        O(2.1, 3.5, 'B', pill('✅ הצבעתם: נכנסת', 36, '#2fbf71', '#fff')),
        O(3.5, 4.55, 'B', bx(f'ואחד מהם מחזיק…', 52)), O(4.55, 5.45, 'B', bx(f'את {Y("המפתח שלי")}! 🗝️', 56)),
        O(5.45, D, 'T', bx(f'מה אני עושה? 😱', 50)),
        O(6.12, 7.49, 'B', B1), O(7.49, 8.77, 'B', B1 + B2), dict(O(8.77, D, 'M', B1 + B2), np=1),
        O(8.77, 10.19, 'B', pill(f'כתבו "שכן" ותיכנסו 🏢', 44)), O(10.19, D, 'B', pill('📩 שלחו לשכן שלכם', 46))]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 7.6
story = {'dur': SD, 'clips': C, 'flash': .25, 'hits': [0.05, 1.6, 4.63], 'novg': 1.0, 'vgmax': .6,
 'seg': [{'t0': 0, 't1': 4.3, 'clip': 'enter', 'off': 0.4, 'zoom': .06}, {'t0': 4.3, 't1': SD, 'clip': 'rabbits', 'off': .3, 'zoom': .07}],
 'ov': [dict(O(0, SD, 'T', pill('🏢 השכנים · תוצאות ההצבעה', 28, '#C792EA', '#1a0f2a')), np=1),
        dict(O(0, 1.12, 'B', bx(f'{Y("הילי")} הצביעה… 🗳️', 52)), np=1), O(1.12, 2.34, 'M', pill('✅ ודנה נכנסה!', 56, '#2fbf71', '#fff')),
        O(2.34, 3.24, 'B', bx('מה היא מצאה שם? 👀', 50)), O(3.24, 4.31, 'B', bx(f'בריל {Y("החדש")} ←', 52)),
        O(4.31, SD, 'B', bx(f'כתבו {Y("שכן")} 🏢<br>והשם שלכם בפרק הבא!', 46))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
