"""Specs « הבניין הכי גבוה בעולם? » חלק 2 (22.11 soir) + story compteur. Usage : python3 specs.py <dossier_clips> <avant> <points>"""
import json, sys, re
ISO = lambda d: [o.update(html=re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', o['html'])) for o in d['ov']]
R = sys.argv[1]; A = int(sys.argv[2]); PTS = int(sys.argv[3])
C = {k: {'dir': f'{R}/{k}', 'fps': 10} for k in ('rise', 'build', 'demo', 'top', 'end')}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
def TITLE(n):
    return (f'<div class=box style="font:900 42px/1.15 H">הבניין הכי {Y("גבוה")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🏢 <span dir=ltr style=\"unicode-bidi:isolate\">{n:,} / 10,000</span> דיירים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 2</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
SHARE = '<br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 24px H">📩 שלחו לשכן שלכם</div>'
def ramp(t0, t1, pos, mk, steps=18):
    out = []
    for i in range(steps):
        a, b = t0 + (t1 - t0) * i / steps, t0 + (t1 - t0) * (i + 1) / steps
        k = (i + 1) / steps; k = 1 - (1 - k) ** 2
        out.append(O(a, b, pos, mk(int(round(A + (PTS - A) * k))), 1))
    return out
D = 19.8
BUB = lambda s, c: f'<div class=pill style="background:#fff;color:#140c04;font:900 34px/1.2 H;box-shadow:0 6px 20px rgba(0,0,0,.5);margin:6px">{s}</div>'
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .45, 'novg': 2.0, 'vgmax': .35,
 'hits': [0.02, 4.54, 6.34, 8.79, 10.07, 11.1, 11.7, 12.95, 15.37, 17.26],
 'seg': [{'t0': 0, 't1': 4.54, 'clip': 'rise', 'off': 0, 'zoom': .04},
         {'t0': 4.54, 't1': 8.79, 'clip': 'build', 'off': 0, 'zoom': .05},
         {'t0': 8.79, 't1': 12.95, 'clip': 'demo', 'off': 0, 'zoom': .05},
         {'t0': 12.95, 't1': 15.37, 'clip': 'top', 'off': 0, 'zoom': .05},
         {'t0': 15.37, 't1': D, 'clip': 'end', 'off': 0, 'zoom': .03}],
 'ov': [O(0, 4.54, 'T', TITLE(A), 1)] + ramp(4.54, 6.34, 'T', TITLE) + [O(6.34, D, 'T', TITLE(PTS), 1),
        O(0, 15.37, 'B', BAR, 1), O(15.37, D, 'B', BAR + SHARE, 1),
        O(0, 1.3, 'M', big(f'{Y("חלק 2")} 🏗️', 76), 1),
        O(1.3, 2.55, 'M', big(f'הכי {Y("גבוה")}<br>בעולם!')),
        O(2.55, 3.92, 'M', big(f'הבוקר: {Y(f"{A:,}")}', 76)),
        O(3.92, 4.54, 'M', big('ועכשיו?', 76))] + ramp(4.54, 6.34, 'M', lambda n: big(f'{Y(f"{n:,}")}<br>דיירים!', 96)) + [
        O(6.34, 7.5, 'M', '<div class=box>' + big(f'עברנו את {Y("100")}!', 70) + '</div>'),
        O(7.5, 8.79, 'M', big(f'קומה {Y("חדשה")}! 🏢', 70)),
        O(8.79, 10.07, 'M', big(f'לייק ❤️<br>{Y("+1")} דייר', 72)),
        O(10.07, 11.1, 'M', big(f'תגובה 💬<br>{Y("+3")} דיירים', 72)),
        O(11.1, 11.7, 'M', big('שיתוף 🚀', 76)),
        O(11.7, 12.95, 'M', '<div class=box>' + big(f'{Y("+10")}<br>בבת אחת!', 80) + '</div>'),
        O(12.95, 13.93, 'M', big(f'מה השכנים<br>{Y("שומעים")}? 👂', 68)),
        O(13.93, 15.37, 'M', '<div style="font:900 22px H;margin-bottom:8px">🏆 מהתגובות שלכם · חלק 1</div>'
          + BUB('🔊 "דפיקות… שקופצים!"', 0) + '<br>' + BUB('🔥🔥🔥', 0)),
        O(15.37, 17.26, 'M', big(f'כתבו מה {Y("השכנים")}<br>שומעים מהדירה<br>שלכם 👇', 52)),
        O(17.26, D, 'M', big(f'{Y("5")} התגובות הכי טובות<br>נכנסות לפרק הבא 🏆', 50))]}
ISO(reel); json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
SD = 6.6
story = {'dur': SD, 'fps': 30, 'clips': C, 'flash': .35, 'novg': 1.5, 'vgmax': .4, 'hits': [0.02, 3.03, 4.2],
 'seg': [{'t0': 0, 't1': 2.6, 'clip': 'rise', 'off': 1.5, 'zoom': .04}, {'t0': 2.6, 't1': SD, 'clip': 'build', 'off': .2, 'zoom': .05}],
 'ov': [O(0, SD, 'T', TITLE(PTS), 1), O(0, SD, 'B', BAR, 1),
        O(0, 1.5, 'M', big(f'🏢 {Y(f"{PTS:,}")}<br>דיירים!', 80), 1),
        O(1.5, 3.03, 'M', big(f'קומה {Y("חדשה")}<br>נבנתה! 🏗️', 66)),
        O(3.03, 4.2, 'M', big('שתפו את הריל 🚀', 64)),
        O(4.2, SD, 'M', '<div class=box>' + big(f'שיתוף = {Y("+10")}<br>בבת אחת!', 66) + '</div>')]}
ISO(story); json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
