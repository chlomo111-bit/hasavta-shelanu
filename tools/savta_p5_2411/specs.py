"""Specs « הסבתא עם הכי הרבה נכדים בעולם? » חלק 5 (24.11 matin) : compteur 286 -> 333 (palier 300), « שב תאכל, הוא יחכה », Top 5 réel.
Usage : python3 specs.py <dossier_clip 'all'>"""
import json, sys, re
R = sys.argv[1]
C = {'all': {'dir': R, 'fps': 10}}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
START, END = 333, 335
def title(v):
    return (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR(f"{v:,} / 10,000")} נכדים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 5</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
END_B = ('<br><div class=pill style="margin-top:8px;background:#FFC24B;color:#140c04;font:900 20px/1.25 H">🏆 5 התגובות הכי טובות<br>נכנסות לפרק הבא</div>'
         '<br><div class=pill style="margin-top:6px;background:#FF8FB8;color:#2a0a18;font:900 22px H">💌 שלחו לסבתא שלכם</div>')
HAN = '<div class=pill style="background:#3fa7ff;color:#07203d;font:900 24px/1.2 H">🕎 עוד 10 ימים לחנוכה</div>'
def who(u): return f'<div class=pill style="background:#FFC24B;color:#140c04;font:900 24px H;margin-bottom:10px">🏆 {LTR("@"+u)}</div>'
def quote(u, w, sz=60): return '<div style="position:relative;top:165px"><div class=box>' + who(u) + big(w, sz) + '</div></div>'
D = 18.6
ov = [O(0, 0.3, 'T', title(START), 1)]
ts = [0.3 + i / 15 for i in range(0, 18)]
for a, b in zip(ts, ts[1:] + [1.5]):
    k = min(1, max(0, (a - 0.3) / 1.0)); k = k * k * (3 - 2 * k)
    ov.append(O(a, b, 'T', title(round(START + (END - START) * k)), 1))
ov.append(O(1.5, D, 'T', title(END), 1))
TOP = ['ohad613', 'kaplan_mei', 'mayaspam1208', 'mebyyali', 'lifeofhyro']
wall = '<div class=box>' + big(f'אתם {Y("כתבתם!")} 💛', 58) + '<div style="height:8px"></div>' + ''.join(f'<div class=pill style="background:#FFC24B;color:#140c04;font:900 21px H;margin:3px 0;display:block">🏆 {LTR("@"+u)}</div>' for u in TOP) + '</div>'
ov += [O(0, 12.11, 'B', BAR, 1), O(12.11, 14.1, 'B', BAR + '<br><div style="height:8px"></div>' + HAN, 1), O(14.1, 15.0, 'B', BAR, 1), O(15.0, D, 'B', BAR + END_B, 1),
  O(0.0, .66, 'M', big('אני צריכה', 84), 1), O(.66, 1.51, 'M', big(Y(LTR('10,000')), 100)), O(1.51, 2.31, 'M', big(f'{Y("נכדים!")} 👵', 90)),
  O(2.31, 3.18, 'M', big(Y('אכלת?'), 110)), O(3.18, 3.97, 'M', big(f'לא {Y("אכלת!")}', 90)),
  O(3.97, 4.3, 'M', big(Y('שב!'), 110)), O(4.3, 5.16, 'M', big(f'תאכל {Y("עוד!")} 🍲', 66)),
  O(5.16, 5.71, 'M', big(f'❤️ {Y("לייק")}', 92)), O(5.71, 6.5, 'M', big(f'{Y(LTR("+1"))} נכד', 96)),
  O(6.5, 7.18, 'M', big(f'💬 {Y("תגובה")}', 90)), O(7.18, 7.74, 'M', big(f'{Y(LTR("+3"))} נכדים', 90)),
  O(7.74, 8.37, 'M', big(f'🚀 {Y("שיתוף")}', 92)), O(8.37, 9.07, 'M', big(f'{Y(LTR("+10"))} נכדים!', 90)),
  O(9.07, 10.16, 'M', quote('kaplan_mei', 'בריאותתת 🤧', 66)),
  O(10.16, 11.5, 'M', quote('ohad613', 'שב, תאכל,<br>הוא יחכה ✈️', 58)),
  O(11.5, 12.11, 'M', quote('mebyyali', 'חמסה 🪬', 78)),
  O(12.11, 14.1, 'M', wall),
  O(14.1, 15.0, 'M', big(f'עכשיו {Y("תורכם")} 👇', 80)),
  O(15.0, 17.63, 'M', '<div class=box>' + big(f'כתבו משפט שסבתא<br>שלכם {Y("תמיד אומרת")} 👇', 52) + '</div>'),
  O(17.63, D, 'M', '<div class=box>' + big(f'ובואו {Y("לאכול")} 🍽️', 76) + '</div>')]
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 1.2, 'vgmax': .35,
 'hits': [0.02, 2.31, 3.97, 5.16, 7.74, 9.07, 12.11, 15.0],
 'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': .04, 'speed': 0.98}], 'ov': ov}
json.dump(reel, open(f'{R}/../reel.json', 'w'), ensure_ascii=False)
print('ok', len(ov))
