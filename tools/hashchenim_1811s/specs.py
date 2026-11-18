"""Specs de montage du reel « השכנים · פרק 1 » (série « les voisins qu'on a tous ») + story, 18.11 soir.
Usage : python3 specs.py <dossier_clips>"""
import json, sys
R = sys.argv[1]
C = {k: {'dir': f'{R}/c_{k}', 'fps': 10} for k in ['wake', 'glow', 'nerv', 'face', 'eyes']}
C['pour'] = {'dir': f'{R}/c_pour30', 'fps': 30}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, **k: dict({'t0': t0, 't1': t1, 'pos': pos, 'html': h}, **k)
btn = lambda n, w, bg: f'<div class=pill style="display:inline-block;margin:4px;width:38%;vertical-align:top;background:{bg};color:#fff;font:900 28px/1.15 H">{n}<br>{w}</div>'
B1, B2 = btn('1️⃣', 'נכנסת 🚪', '#2fbf71'), btn('2️⃣', 'קוראת לשכנים 📣', '#E5484D')
TAG = '<div style="margin-top:8px">' + pill('📣 תייגו את השכן הכי רועש', 30, '#fff') + '</div>'
BADGE = '<div style="position:absolute;top:2.6%;right:4%;background:rgba(12,10,30,.6);border:2px solid #C792EA;border-radius:999px;padding:3px 12px;font:900 15px H;color:#fff">🏢 פרק 1</div>'
D = 14.9
reel = {'dur': D, 'fps': 10, 'clips': C, 'flash': .35, 'novg': 2.8, 'vgmax': .35, 'badge': BADGE,
 'hits': [0.05, 1.38, 2.79, 4.0, 4.62, 5.67, 7.0, 8.02, 11.09],
 'seg': [{'t0': 0, 't1': 1.38, 'clip': 'wake', 'off': 0, 'zoom': .05},
         {'t0': 1.38, 't1': 2.79, 'clip': 'wake', 'off': 1.4, 'zoom': .12},
         {'t0': 2.79, 't1': 4.0, 'clip': 'glow', 'off': 0, 'zoom': .06},
         {'t0': 4.0, 't1': 4.62, 'clip': 'nerv', 'off': 0, 'zoom': .05},
         {'t0': 4.62, 't1': 5.67, 'clip': 'glow', 'off': 1.3, 'zoom': .14},
         {'t0': 5.67, 't1': 7.0, 'clip': 'pour', 'off': .4, 'zoom': .06},
         {'t0': 7.0, 't1': 8.02, 'clip': 'face', 'off': 0, 'zoom': .08},
         {'t0': 8.02, 't1': 9.6, 'clip': 'pour', 'off': .4, 'zoom': .15, 'speed': .6},
         {'t0': 9.6, 't1': D, 'clip': 'eyes', 'off': 0, 'zoom': .1}],
 'ov': [O(0, 2.79, 'T', bx(f'🕑 2 בלילה… והשכן<br>{Y("שוב")} עושה רעש 😤', 44), np=1),
        O(0, 2.79, 'B', pill('מכירים את השכן הזה? 🙄', 28, '#C792EA', '#1a0f2a'), np=1),
        O(2.79, 4.0, 'T', bx(f'זה בא מ{Y("דלת 10")}… 🚪', 52)),
        O(4.0, 5.67, 'T', bx(f'רגע… הדלת {Y("זזה")} 😳', 52)),
        O(5.67, 8.02, 'T', bx(f'{Y("ארנבים")}!!! 🐰🐰🐰', 64)),
        O(8.02, 9.78, 'T', bx(f'ומשהו {Y("ענק")}…', 56)),
        O(9.78, 11.09, 'T', bx('מסתכל עליי מבפנים 👁️👁️', 50)),
        O(11.09, D, 'T', pill('אתם מחליטים: 1 או 2?<br>בתגובות 👇', 44)),
        O(11.96, 13.23, 'B', B1), O(13.23, 13.84, 'B', B1 + B2), O(13.84, D, 'B', B1 + B2 + TAG)]}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 6.6
story = {'dur': SD, 'fps': 10, 'clips': C, 'flash': .3, 'hits': [0.05, 1.75, 3.35, 4.3], 'novg': SD, 'vgmax': 0, 'Ttop': '17%', 'Bbot': '19%',
 'badge': '',
 'seg': [{'t0': 0, 't1': 1.75, 'clip': 'eyes', 'off': 1.0, 'zoom': .06}, {'t0': 1.75, 't1': 3.35, 'clip': 'pour', 'off': .3, 'zoom': .08},
         {'t0': 3.35, 't1': SD, 'clip': 'eyes', 'off': 1.95, 'zoom': .08}],
 'ov': [O(0, 1.75, 'T', bx(f'מה יש מאחורי {Y("הדלת")}? 👀', 50), np=1),
        O(1.75, 3.35, 'T', bx(f'הפרק החדש {Y("בריל")}! 🎬', 52)),
        O(3.35, SD, 'T', bx('1 או 2?<br>אתם מחליטים 👇', 52)),
        O(1.75, SD, 'B', pill('🏢 השכנים · פרק 1', 34, '#C792EA', '#1a0f2a'))]}
json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
