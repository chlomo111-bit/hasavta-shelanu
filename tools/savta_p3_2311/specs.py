"""Specs « הסבתא עם הכי הרבה נכדים בעולם? » חלק 3 (23.11 soir) : compteur 130 -> 286 (palier 200), Top réel, rappel חנוכה.
Usage : python3 specs.py <dossier_clips_fusionnes 'all'>"""
import json, sys, re
R = sys.argv[1]
C = {'all': {'dir': R, 'fps': 10}}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
START, END = 130, 286
def title(v):
    return (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR(f"{v:,} / 10,000")} נכדים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 3</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
END_B = ('<br><div class=pill style="margin-top:8px;background:#FFC24B;color:#140c04;font:900 20px/1.25 H">🏆 התגובות הכי טובות<br>נכנסות לפרק הבא</div>'
         '<br><div class=pill style="margin-top:6px;background:#FF8FB8;color:#2a0a18;font:900 22px H">💌 שלחו לסבתא שלכם</div>')
HAN = '<div class=pill style="background:#3fa7ff;color:#07203d;font:900 24px/1.2 H">🕎 חנוכה · 04.12 · עוד 11 ימים</div>'
def who(u): return f'<div class=pill style="background:#FFC24B;color:#140c04;font:900 24px H;margin-bottom:10px">🏆 {LTR("@"+u)}</div>'
def quote(u, w, sz=60): return '<div style="position:relative;top:165px"><div class=box>' + who(u) + big(w, sz) + '</div></div>'
D = 19.6
ov = [O(0, 0.3, 'T', title(START), 1)]
ts = [0.3 + i / 15 for i in range(0, 18)]
for a, b in zip(ts, ts[1:] + [1.5]):
    k = min(1, max(0, (a - 0.3) / 1.0)); k = k * k * (3 - 2 * k)
    ov.append(O(a, b, 'T', title(round(START + (END - START) * k)), 1))
ov.append(O(1.5, D, 'T', title(END), 1))
ov += [O(0, 11.87, 'B', BAR, 1), O(11.87, 14.17, 'B', BAR + '<br><div style="height:8px"></div>' + HAN, 1), O(14.17, 17.22, 'B', BAR, 1), O(17.22, D, 'B', BAR + END_B, 1),
  O(0, .41, 'M', big('עברנו', 84), 1), O(.41, .81, 'M', big(Y('מאתיים'), 90)), O(.81, 1.38, 'M', big(f'{Y("נכדים!")} 🎉', 84)),
  O(1.38, 3.18, 'M', quote('____alonii____', 'תיקח איתך<br>את הזבל', 64)),
  O(3.18, 4.2, 'M', big(Y('תיקח, תיקח!'), 76)), O(4.2, 5.25, 'M', '<div class=box>' + big(f'וגם {Y("אוכל")}<br>לדרך 🥡', 70) + '</div>'),
  O(5.25, 7.04, 'M', quote('maayan8304', 'סבתא, אני רעב 🤤', 62)),
  O(7.04, 7.7, 'M', big(f'{Y("יש מרק?")} 🍲', 78)), O(7.7, 8.66, 'M', big(f'תמיד {Y("יש מרק!")} 🍲', 66)),
  O(8.66, 10.39, 'M', quote('myt44015', 'אתה לא ישן<br>פה היום?', 62)),
  O(10.39, 11.87, 'M', quote('ohad613', 'אוהד: ואני גם יכול<br>לבוא לאכול?', 52)),
  O(11.87, 12.83, 'M', big(f'{Y("חנוכה")}? 🕎', 86)), O(12.83, 13.41, 'M', big(f'{Y("כן!")} 🎉', 96)), O(13.41, 14.17, 'M', big(f'נחגוג {Y("ביחד")} 🕎', 70)),
  O(14.17, 14.55, 'M', big(f'{Y("נרות")} 🕯️', 80)), O(14.55, 15.05, 'M', big(f'{Y("סופגניות")} 🍩', 72)), O(15.05, 15.61, 'M', big(Y('סביבונים'), 76)),
  O(15.61, 16.6, 'M', '<div class=box>' + big(f'בעוד {Y(LTR("11"))} ימים', 74) + '</div>'), O(16.6, 17.22, 'M', big(f'סימנו ביומן 🗓️', 62)),
  O(17.22, 18.3, 'M', '<div class=box>' + big(f'כתבו את {Y("השם")}<br>שלכם 👇', 68) + '</div>'),
  O(18.3, D, 'M', '<div class=box>' + big(f'וסבתא קוראת<br>לכם {Y("לשולחן")} 🍽️', 62) + '</div>')]
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 1.2, 'vgmax': .35,
 'hits': [0.02, 0.41, 1.37, 3.18, 5.25, 7.04, 8.66, 10.39, 11.87, 14.17, 15.61, 17.22],
 'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': .04, 'speed': 1}], 'ov': ov}
json.dump(reel, open(f'{R}/../reel.json', 'w'), ensure_ascii=False)
print('ok', len(ov))
