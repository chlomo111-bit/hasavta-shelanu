"""Specs « הבניין הכי גבוה בעולם? » חלק 3 (23.11 matin) : מה שומעים בבניין. Usage : python3 specs.py <dossier_clips> <avant> <points>"""
import json, sys, re
ISO = lambda d: [o.update(html=re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', o['html'])) for o in d['ov']]
R = sys.argv[1]; A = int(sys.argv[2]); PTS = int(sys.argv[3])
C = {k: {'dir': f'{R}/{k}', 'fps': 10} for k in ('wide', 'ride', 'reveal', 'top', 'end')}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
def TITLE(n):
    return (f'<div class=box style="font:900 40px/1.15 H">הבניין הכי {Y("גבוה")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🏢 <span dir=ltr style="unicode-bidi:isolate">{n:,} / 10,000</span> דיירים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 3</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
SHARE = '<br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 24px H">📩 שלחו לשכן שלכם</div>'
def ramp(t0, t1, pos, mk, steps=14):
    out = []
    for i in range(steps):
        a, b = t0 + (t1 - t0) * i / steps, t0 + (t1 - t0) * (i + 1) / steps
        k = (i + 1) / steps; k = 1 - (1 - k) ** 2
        out.append(O(a, b, pos, mk(int(round(A + (PTS - A) * k))), 1))
    return out
BUB = lambda s: f'<div class=pill style="background:#fff;color:#140c04;font:900 38px/1.2 H;box-shadow:0 6px 20px rgba(0,0,0,.5)">{s}</div>'
WHO = lambda u, txt: f'<div class=pill style="margin-top:10px;background:rgba(10,8,24,.85);color:#fff;font:900 22px/1.3 H">🏆 <span dir=ltr style="unicode-bidi:isolate" class=y>@{u}</span><br>כתב: ״{txt}״</div>'
D = 17.7
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 1.0, 'vgmax': .35,
 'hits': [0.02, 1.95, 3.92, 5.27, 7.55, 8.85, 9.71, 11.79, 12.73, 13.93, 15.23],
 'seg': [{'t0': 0, 't1': 1.95, 'clip': 'wide', 'off': 0, 'zoom': .03},
         {'t0': 1.95, 't1': 7.55, 'clip': 'ride', 'off': 0, 'zoom': .02},
         {'t0': 7.55, 't1': 9.71, 'clip': 'reveal', 'off': 0, 'zoom': .03},
         {'t0': 9.71, 't1': 15.23, 'clip': 'top', 'off': 0, 'zoom': .03},
         {'t0': 15.23, 't1': D, 'clip': 'end', 'off': 0, 'zoom': .02}],
 'ov': [O(0, 9.71, 'T', TITLE(A), 1)] + ramp(9.71, 11.4, 'T', TITLE) + [O(11.4, D, 'T', TITLE(PTS), 1),
        O(0, 15.23, 'B', BAR, 1), O(15.23, D, 'B', BAR + SHARE, 1),
        O(0, 1.95, 'M', big(f'בבניין שלנו<br>{Y("שומעים")} הכול! 👂', 62), 1),
        O(1.95, 3.92, 'M', BUB('🔊 דפיקות… שקופצים!') + '<br>' + WHO('hillimoshe7', 'הם שומעים דפיקות שקופצים')),
        O(3.92, 5.27, 'M', BUB('🔊 ריבים! 😅') + '<br>' + WHO('hayley645726', 'מה לא ריבים')),
        O(5.27, 7.55, 'M', BUB('🔊 מקדחה… 🛠️') + '<br><div class=pill style="margin-top:10px;background:rgba(10,8,24,.85);color:#fff;font:900 26px H">בשבת בבוקר 😩</div>'),
        O(7.55, 8.85, 'M', big(f'ומי הכי {Y("רועש")}<br>בבניין? 🤔', 62)),
        O(8.85, 9.71, 'M', '<div class=box>' + big(f'{Y("השכן")} שלכם! 👀', 70) + '</div>'),
        O(9.71, 11.79, 'M', big(f'{Y("809")}<br>דיירים!', 100), 1),
        O(11.79, 12.73, 'M', big(f'לייק ❤️<br>{Y("+1")} דייר', 72)),
        O(12.73, 13.93, 'M', big(f'תגובה 💬<br>{Y("+3")} דיירים', 72)),
        O(13.93, 15.23, 'M', '<div class=box>' + big(f'שיתוף 🚀<br>{Y("+10")} בבת אחת!', 66) + '</div>'),
        O(15.23, 17.0, 'M', big(f'כתבו מה {Y("שומעים")}<br>אצלכם 👇', 56)),
        O(17.0, D, 'M', big(f'{Y("3")} מקומות פנויים<br>בטופ 5 🏆', 46))]}
ISO(reel); json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
print('ok')
