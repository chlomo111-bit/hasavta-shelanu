"""Specs du reel « הכוורת הכי גדולה בעולם? » חלק 1 (22.11) + story compteur. Usage : python3 specs.py <dossier_clips> <points>"""
import json, sys, re
ISO = lambda d: [o.update(html=re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', o['html'])) for o in d['ov']]
R = sys.argv[1]; PTS = int(sys.argv[2]) if len(sys.argv) > 2 else 0
C = {'wide': {'dir': f'{R}/wide', 'fps': 10}, 'demo': {'dir': f'{R}/demo', 'fps': 10}, 'end': {'dir': f'{R}/end', 'fps': 10}}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
cnt = f'{PTS:,}'
TITLE = (f'<div class=box style="font:900 42px/1.15 H">הכוורת הכי {Y("גדולה")} בעולם?</div><br>'
         f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🐝 {cnt} / 10,000 דבורים</div>'
         f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 1</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
D = 17.4
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 2.0, 'vgmax': .35,
 'hits': [0.02, 2.57, 4.47, 6.17, 7.56, 8.65, 11.05, 13.06],
 'seg': [{'t0': 0, 't1': 4.03, 'clip': 'wide', 'off': 0, 'zoom': .04},
         {'t0': 4.03, 't1': 8.65, 'clip': 'demo', 'off': 0, 'zoom': .05},
         {'t0': 8.65, 't1': D, 'clip': 'end', 'off': 0, 'zoom': .03}],
 'ov': [O(0, D, 'T', TITLE, 1),
        O(0, 9.51, 'B', BAR, 1), O(9.51, 11.05, 'B', '<div class=pill style="background:#2fbf71;color:#fff;font:900 26px/1.3 H">🏆 המקומות פנויים –<br>תהיו הראשונים!</div>'),
        O(11.05, 13.06, 'B', BAR, 1),
        O(13.06, D, 'B', BAR + '<br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 24px H">📩 שלחו לחברה שלכם</div>', 1),
        O(0, .79, 'M', big(f'אנחנו {Y("בונים")} 🏗️'), 1),
        O(.79, 1.39, 'M', big(f'את {Y("הכוורת")} 🐝')),
        O(1.39, 2.57, 'M', big(f'הכי {Y("גדולה")}<br>בעולם!')),
        O(2.57, 4.03, 'M', big(f'{Y("10,000")}<br>דבורים', 80)),
        O(4.03, 4.47, 'M', big('לייק ❤️', 76)),
        O(4.47, 5.68, 'M', big(f'{Y("+1")} דבורה!', 76)),
        O(5.68, 6.17, 'M', big('תגובה 💬', 76)),
        O(6.17, 6.97, 'M', big(f'{Y("+3")} דבורים!', 76)),
        O(6.97, 7.56, 'M', big('שיתוף 🚀', 76)),
        O(7.56, 8.65, 'M', '<div class=box>' + big(f'{Y("+10")}<br>בבת אחת!', 80) + '</div>'),
        O(8.65, 9.51, 'M', big(f'אנחנו על {Y(cnt)}')),
        O(9.51, 11.05, 'M', '<div class=box>' + big(f'עזרו לעבור<br>את {Y("100")}!') + '</div>'),
        O(11.05, 13.06, 'M', '<div class=box>' + big(f'כתבו איזה {Y("תפקיד")}<br>אתם רוצים<br>בכוורת 👇', 54) + '<div style="margin-top:10px;font:900 25px/1.4 H">👑 מלכה · 🛡️ שומרת<br>🍯 מכינה דבש · 😴 עצלנית</div></div>'),
        O(13.06, D, 'M', '<div class=box>' + big(f'{Y("5")} התגובות הכי טובות<br>נכנסות לפרק הבא 🏆', 48) + '</div>')]}
ISO(reel); json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 6.6
story = {'dur': SD, 'fps': 30, 'clips': C, 'flash': .35, 'novg': 1.5, 'vgmax': .4, 'hits': [0.02, 2.04, 3.16],
 'seg': [{'t0': 0, 't1': 2.04, 'clip': 'wide', 'off': 1.0, 'zoom': .04}, {'t0': 2.04, 't1': SD, 'clip': 'demo', 'off': 2.23, 'zoom': .05}],
 'ov': [O(0, SD, 'T', TITLE, 1), O(0, SD, 'B', BAR, 1),
        O(0, 2.04, 'M', big(f'🐝 {Y(cnt)}<br>מתוך 10,000', 70), 1),
        O(2.04, 3.16, 'M', big('שתפו את הריל 🚀', 64)),
        O(3.16, SD, 'M', '<div class=box>' + big(f'שיתוף = {Y("+10")}<br>דבורים בבת אחת!', 62) + '</div>')]}
ISO(story); json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
