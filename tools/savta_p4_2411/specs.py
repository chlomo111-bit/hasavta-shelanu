"""Specs « הסבתא עם הכי הרבה נכדים בעולם? » חלק 4 (24.11 matin) : compteur 286 -> 333 (palier 300), « שב תאכל, הוא יחכה », Top 5 réel.
Usage : python3 specs.py <dossier_clip 'all'>"""
import json, sys, re
R = sys.argv[1]
C = {'all': {'dir': R, 'fps': 10}}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
START, END = 286, 333
def title(v):
    return (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR(f"{v:,} / 10,000")} נכדים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 4</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
END_B = ('<br><div class=pill style="margin-top:8px;background:#FFC24B;color:#140c04;font:900 20px/1.25 H">🏆 5 התגובות הכי טובות<br>נכנסות לפרק הבא</div>'
         '<br><div class=pill style="margin-top:6px;background:#FF8FB8;color:#2a0a18;font:900 22px H">💌 שלחו לסבתא שלכם</div>')
HAN = '<div class=pill style="background:#3fa7ff;color:#07203d;font:900 24px/1.2 H">🕎 עוד 10 ימים לחנוכה</div>'
def who(u): return f'<div class=pill style="background:#FFC24B;color:#140c04;font:900 24px H;margin-bottom:10px">🏆 {LTR("@"+u)}</div>'
def quote(u, w, sz=60): return '<div style="position:relative;top:165px"><div class=box>' + who(u) + big(w, sz) + '</div></div>'
D = 19.5
ov = [O(0, 0.3, 'T', title(START), 1)]
ts = [0.3 + i / 15 for i in range(0, 18)]
for a, b in zip(ts, ts[1:] + [1.5]):
    k = min(1, max(0, (a - 0.3) / 1.0)); k = k * k * (3 - 2 * k)
    ov.append(O(a, b, 'T', title(round(START + (END - START) * k)), 1))
ov.append(O(1.5, D, 'T', title(END), 1))
ov += [O(0, 8.4, 'B', BAR, 1), O(8.4, 10.6, 'B', BAR + '<br><div style="height:8px"></div>' + HAN, 1), O(10.6, 16.13, 'B', BAR, 1), O(16.13, D, 'B', BAR + END_B, 1),
  O(0.0, .5, 'M', big('עברנו', 84), 1), O(.5, 1.0, 'M', big(Y(LTR('300')), 100)), O(1.0, 1.68, 'M', big(f'{Y("נכדים!")} 🎉', 84)),
  O(1.68, 3.14, 'M', quote('ohad613', 'אני חייב<br>לזוז…', 66)),
  O(3.14, 4.21, 'M', big(f'יש לי {Y("טיסה")} ✈️', 74)),
  O(4.21, 4.65, 'M', big(Y('שב!'), 100)), O(4.65, 5.2, 'M', big(f'{Y("תאכל!")} 🍲', 90)), O(5.2, 5.88, 'M', big(f'הוא {Y("יחכה")} ⏰', 76)),
  O(5.88, 7.58, 'M', quote('kaplan_mei', 'בריאותתתת 🤧', 62)),
  O(7.58, 8.4, 'M', big(Y('בריאות!'), 84)), O(8.4, 9.14, 'M', big(f'מתוקים {Y("שלי")} 💛', 68)),
  O(9.14, 10.65, 'M', quote('mayaspam1208', 'בואי תאכלי 🍲', 60)),
  O(10.65, 11.4, 'M', big(Y('בואו!'), 100)), O(11.4, 12.04, 'M', big(f'{Y("לאכול")} 🍽️', 84)),
  O(12.04, 13.63, 'M', quote('mebyyali', 'חמסה 🪬', 78)),
  O(13.63, 15.43, 'M', quote('lifeofhyro', 'אם אני לא<br>נכדדדד', 62)),
  O(15.43, 16.13, 'M', big(f'אתה {Y("נכד!")} 💛', 84)),
  O(16.13, 17.5, 'M', '<div class=box>' + big(f'כתבו משפט שסבתא<br>שלכם {Y("תמיד אומרת")} 👇', 52) + '</div>'),
  O(17.5, D, 'M', '<div class=box>' + big(f'ושלחו {Y("לסבתא")} 💌', 70) + '</div>')]
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 1.2, 'vgmax': .35,
 'hits': [0.02, 1.68, 4.21, 5.88, 9.14, 12.04, 13.63, 16.13],
 'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': .04, 'speed': 0.98}], 'ov': ov}
json.dump(reel, open(f'{R}/../reel.json', 'w'), ensure_ascii=False)
print('ok', len(ov))
