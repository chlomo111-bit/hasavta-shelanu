"""Specs « הסבתא עם הכי הרבה נכדים בעולם? » חלק 1 (22.11) + story compteur. Usage : python3 specs.py <dossier_clips> <points>"""
import json, sys, re
ISO = lambda d: [o.update(html=re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', o['html'])) for o in d['ov']]
R = sys.argv[1]; PTS = int(sys.argv[2])
SH = {'s1': (0, 2.13), 's2': (2.13, 4.33), 's3': (4.33, 6.05), 's4': (6.05, 8.14), 's5': (8.14, 9.42), 's6': (9.42, 11.9), 's7': (11.9, 13.86), 's8': (13.86, 17.3), 's9': (17.3, 19.3)}
C = {k: {'dir': f'{R}/{k}', 'fps': 10} for k in SH}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
TITLE = (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
         f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR(f"{PTS:,} / 10,000")} נכדים</div>'
         f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 1</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
SHARE = '<br><div class=pill style="margin-top:8px;background:#FF8FB8;color:#2a0a18;font:900 24px H">💌 שלחו לסבתא שלכם</div>'
D = 19.3
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 2.2, 'vgmax': .35,
 'hits': [0.02, 2.13, 4.33, 5.73, 6.05, 7.12, 8.14, 8.78, 9.42, 10.02, 11.9, 13.86, 17.3],
 'seg': [{'t0': a, 't1': b, 'clip': k, 'off': 0, 'zoom': .04, 'speed': min(1, (len(__import__('glob').glob(f'{R}/{k}_i30/f*.jpg')) - 1) / 30 / (b - a + 1/30))} for k, (a, b) in SH.items()],
 'ov': [O(0, D, 'T', TITLE, 1), O(0, 13.86, 'B', BAR, 1), O(13.86, D, 'B', BAR + SHARE, 1),
        O(0, .54, 'M', big('אני צריכה…', 62), 1),
        O(.54, 1.36, 'M', '<div class=box>' + big(Y(LTR('10,000')), 96) + '</div>', 1),
        O(1.36, 2.13, 'M', big(f'{Y("נכדים!")} 👵', 84)),
        O(2.13, 2.9, 'M', big('הסבתא', 80)),
        O(2.9, 3.79, 'M', big(f'הכי {Y("הרבה")}<br>נכדים', 76)),
        O(3.79, 4.33, 'M', big(f'{Y("בעולם!")} 🌍', 80)),
        O(4.33, 5.73, 'M', big('ועכשיו<br>יש לי…', 70)),
        O(5.73, 6.05, 'M', '<div class=box>' + big(Y(LTR(f'{PTS}')), 130) + '</div>'),
        O(6.05, 6.63, 'M', big('אז ככה:', 72)),
        O(6.63, 8.14, 'M', big(f'לייק ❤️<br>{Y("+1")} נכד', 74)),
        O(8.14, 8.78, 'M', big('תגובה 💬', 76)),
        O(8.78, 9.42, 'M', big(f'{Y("+3")} נכדים!', 80)),
        O(9.42, 10.02, 'M', big('שיתוף 🚀', 80)),
        O(10.02, 10.89, 'M', '<div class=box>' + big(f'{Y("+10")}<br>נכדים!', 88) + '</div>'),
        O(10.89, 11.9, 'M', big(f'רצים {Y("לשולחן!")} 🏃', 66)),
        O(11.9, 12.92, 'M', '<div class=box><div style="font:900 26px H;margin-bottom:8px">🏆 טופ 5 מהתגובות</div>' + big(f'המקומות<br>{Y("פנויים")}', 72) + '</div>'),
        O(12.92, 13.86, 'M', '<div class=box>' + big(f'תהיו {Y("הראשונים!")}', 64) + '</div>'),
        O(13.86, 15.3, 'M', big(f'כתבו משפט<br>ש{Y("סבתא שלכם")}', 64)),
        O(15.3, 16.04, 'M', big(f'{Y("תמיד")} אומרת 👇', 68)),
        O(16.04, 17.3, 'M', '<div class=box>' + big(f'{Y("5")} התגובות הכי טובות<br>נכנסות לפרק הבא 🏆', 44) + '</div>'),
        O(17.3, D, 'M', '<div class=box>' + big(f'כתבו משפט<br>ש{Y("סבתא שלכם")}<br>תמיד אומרת 👇', 44) + '</div>' + '<div style="height:10px"></div>'
          + '<div class=pill style="background:#FFC24B;color:#140c04;font:900 22px/1.25 H">🏆 5 התגובות הכי טובות<br>נכנסות לפרק הבא</div>')]}
ISO(reel); json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
# story (a) : voix anachnu 0 | efes .95 | shatfu 1.81 | asara 3.0 | END 5.24
SD = 6.2
story = {'dur': SD, 'fps': 30, 'clips': C, 'flash': .35, 'novg': 1.5, 'vgmax': .4, 'hits': [0.02, 1.81, 3.0],
 'seg': [{'t0': 0, 't1': 1.81, 'clip': 's1', 'off': 0, 'zoom': .04}, {'t0': 1.81, 't1': SD, 'clip': 's6', 'off': .3, 'zoom': .05}],
 'ov': [O(0, SD, 'T', TITLE, 1), O(0, SD, 'B', BAR, 1),
        O(0, 1.81, 'M', big(f'אנחנו על<br>{Y(LTR(str(PTS)))} נכדים…', 70), 1),
        O(1.81, 3.0, 'M', big('שתפו את הריל 🚀', 64)),
        O(3.0, SD, 'M', '<div class=box>' + big(f'שיתוף = {Y("+10")}<br>נכדים בבת אחת!', 60) + '</div>')]}
ISO(story); json.dump(story, open(f'{R}/story.json', 'w'), ensure_ascii=False)
print('ok')
