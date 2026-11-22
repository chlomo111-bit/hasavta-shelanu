"""Specs du reel « הבניין הכי גבוה בעולם? » חלק 1 (22.11) + story compteur. Usage : python3 specs.py <dossier_clips> <points> """
import json, sys, re
ISO = lambda d: [o.update(html=re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', o['html'])) for o in d['ov']]
R = sys.argv[1]; PTS = int(sys.argv[2]) if len(sys.argv) > 2 else 0
C = {k: {'dir': f'{R}/{k}', 'fps': 30} for k in ('rise', 'demo', 'empty', 'end')}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
cnt = f'{PTS:,}'
TITLE = (f'<div class=box style="font:900 42px/1.15 H">הבניין הכי {Y("גבוה")} בעולם?</div><br>'
         f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🏢 {cnt} / 10,000 דיירים</div>'
         f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 1</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
D = 17.6
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 2.0, 'vgmax': .35,
 'hits': [0.02, 2.32, 4.9, 6.35, 7.45, 8.0, 9.48, 11.85, 13.99],
 'seg': [{'t0': 0, 't1': 4.9, 'clip': 'rise', 'off': 0, 'zoom': .04},
         {'t0': 4.9, 't1': 9.48, 'clip': 'demo', 'off': 0, 'zoom': .05},
         {'t0': 9.48, 't1': 11.85, 'clip': 'empty', 'off': 0, 'zoom': .05},
         {'t0': 11.85, 't1': D, 'clip': 'end', 'off': 0, 'zoom': .03}],
 'ov': [O(0, D, 'T', TITLE, 1),
        O(0, 9.48, 'B', BAR, 1), O(9.48, 11.85, 'B', '<div class=pill style="background:#2fbf71;color:#fff;font:900 26px/1.3 H">🏆 המקומות פנויים –<br>תהיו הראשונים!</div>'),
        O(11.85, 13.99, 'B', BAR, 1),
        O(13.99, D, 'B', BAR + '<br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 24px H">📩 שלחו לשכן שלכם</div>', 1),
        O(0, 1.05, 'M', big(f'אנחנו {Y("בונים")} 🏗️'), 1),
        O(1.05, 2.32, 'M', big(f'הכי {Y("גבוה")}<br>בעולם!')),
        O(2.32, 3.7, 'M', big(f'{Y("10,000")}<br>דיירים', 80)),
        O(3.7, 4.9, 'M', big(f'כל 100 =<br>עוד {Y("קומה")}')),
        O(4.9, 5.6, 'M', big('לייק ❤️', 76)),
        O(5.6, 6.35, 'M', big(f'{Y("+1")} דייר!', 76)),
        O(6.35, 6.89, 'M', big('תגובה 💬', 76)),
        O(6.89, 7.45, 'M', big(f'{Y("+3")} דיירים!', 76)),
        O(7.45, 8.0, 'M', big('שיתוף 🚀', 76)),
        O(8.0, 9.48, 'M', '<div class=box>' + big(f'{Y("+10")}<br>קומה שלמה!', 80) + '</div>'),
        O(9.48, 10.65, 'M', big(f'אנחנו על {Y(cnt)}')),
        O(10.65, 11.85, 'M', big(f'עזרו לעבור<br>את {Y("100")}!')),
        O(11.85, 13.99, 'M', big(f'כתבו מה {Y("השכנים")}<br>שומעים מהדירה<br>שלכם 👇', 52)),
        O(13.99, D, 'M', big(f'{Y("5")} התגובות הכי טובות<br>נכנסות לפרק הבא 🏆', 50))]}
ISO(reel); json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
# story (a) 6.6 s : compteur du jour + partage = +10
SD = 6.6
story = {'dur': SD, 'fps': 30, 'clips': C, 'flash': .35, 'novg': 1.5, 'vgmax': .4, 'hits': [0.02, 1.77, 3.04, 3.74],
 'seg': [{'t0': 0, 't1': 2.4, 'clip': 'rise', 'off': 1.0, 'zoom': .04}, {'t0': 2.4, 't1': SD, 'clip': 'demo', 'off': .4, 'zoom': .05}],
 'ov': [O(0, SD, 'T', TITLE, 1), O(0, SD, 'B', BAR, 1),
        O(0, 1.77, 'M', big(f'🏢 {Y(cnt)}<br>מתוך 10,000', 70), 1),
        O(1.77, 3.04, 'M', big(f'אנחנו על<br>{Y(cnt)} דיירים', 70)),
        O(3.04, 3.74, 'M', big('שתפו את הריל 🚀', 64)),
        O(3.74, SD, 'M', '<div class=box>' + big(f'שיתוף = {Y("+10")}<br>בבת אחת!', 66) + '</div>')]}
ISO(story); json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
