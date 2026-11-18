"""Specs de montage (compose.py) du reel et de la story השכנים 18.11 (format A : action dès l'image 0 + texte en haut, centre libre).
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {'pour': {'dir': f'{R}/c_pour30', 'fps': 30}, 'face': {'dir': f'{R}/c_face', 'fps': 10}}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:4px;width:38%;vertical-align:top;background:{bg};color:#fff;font:900 28px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'נכנסת 🚪', '#2fbf71'), btn('2️⃣', 'קוראת לשכנים 📣', '#E5484D')
D = 7.3
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .35, 'novg': 2.7, 'vgmax': .35,
 'hits': [0.05, 1.4, 2.67, 3.37, 4.49, 5.82],
 'seg': [{'t0': 0, 't1': 1.4, 'clip': 'pour', 'off': 0, 'zoom': .06},
         {'t0': 1.4, 't1': 2.67, 'clip': 'pour', 'off': 1.4, 'zoom': .1},
         {'t0': 2.67, 't1': 5.82, 'clip': 'face', 'off': 0, 'zoom': .07},
         {'t0': 5.82, 't1': D, 'clip': 'pour', 'off': 2.1, 'zoom': .06}],
 'ov': [dict(O(0, 1.4, 'T', bx('הדלת נפתחה! 😱', 58)), np=1),
        dict(O(0, 2.67, 'B', pill('אתם מחליטים: 1 או 2?', 26, '#C792EA', '#1a0f2a')), np=1),
        O(1.4, 2.67, 'T', bx(f'{Y("ארנבים")} בכל מקום! 🐰', 46)),
        O(2.67, 5.82, 'T', bx('מה אני עושה? 😨', 54)),
        O(3.37, 4.49, 'B', B1), O(4.49, 5.82, 'B', B1 + B2), dict(O(5.82, D, 'B', B1 + B2), np=1),
        O(5.82, 6.55, 'T', pill('כתבו "שכן" ותיכנסו 🏢', 44)), dict(O(6.55, D, 'T', pill('📩 שלחו לשכן שלכם', 46)), np=1)]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 7.5
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 2.3, 4.12, 5.28], 'novg': 1.0, 'vgmax': .45,
 'seg': [{'t0': 0, 't1': 2.3, 'clip': 'face', 'off': .85, 'zoom': .05}, {'t0': 2.3, 't1': 4.12, 'clip': 'pour', 'off': .2, 'zoom': .08},
         {'t0': 4.12, 't1': 5.28, 'clip': 'pour', 'off': 2.0, 'zoom': .1}, {'t0': 5.28, 't1': SD, 'clip': 'face', 'off': 0, 'zoom': .05}],
 'ov': [dict(O(0, SD, 'T', pill('🏢 השכנים · פרק חדש!', 28, '#C792EA', '#1a0f2a')), np=1),
        dict(O(0, 2.3, 'B', bx(f'{Y("הילי")}! דלת 10<br>נפתחה… 🚪', 52)), np=1),
        O(2.3, 4.12, 'M', bx(f'וארנבים<br>בכל מקום! 🐰', 54)),
        O(4.12, 5.28, 'M', pill('בריל החדש ←', 52, '#fff')),
        O(5.28, SD, 'B', bx(f'כתבו {Y("שכן")} 🏢<br>והשם שלכם בפרק הבא!', 46))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
