"""Specs « הסבתא עם הכי הרבה נכדים בעולם? » חלק 6 (25.11 matin) : compteur 335 -> 352, « לא יוצאים מסבתא בידיים ריקות » (tour de קופסאות), Top réel.
Usage : python3 specs.py <dossier_clip 'all'>"""
import json, sys, re
from cut import m as MM
R = sys.argv[1]
C = {'all': {'dir': R, 'fps': 10}}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
START, END = 335, 352
def title(v):
    return (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR(f"{v:,} / 10,000")} נכדים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 6</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
END_B = ('<br><div class=pill style="margin-top:8px;background:#FFC24B;color:#140c04;font:900 20px/1.25 H">🏆 5 התגובות הכי טובות<br>נכנסות לפרק הבא</div>'
         '<br><div class=pill style="margin-top:6px;background:#FF8FB8;color:#2a0a18;font:900 22px H">💌 שלחו לסבתא שלכם</div>')
HAN = '<div class=pill style="background:#3fa7ff;color:#07203d;font:900 24px/1.2 H">🕎 עוד 9 ימים לחנוכה</div>'
def who(u): return f'<div class=pill style="background:#FFC24B;color:#140c04;font:900 24px H;margin-bottom:10px">🏆 {LTR("@"+u)}</div>'
def quote(u, w, sz=60): return '<div style="position:relative;top:165px"><div class=box>' + who(u) + big(w, sz) + '</div></div>'

m = lambda t: round(MM(t), 2)
D = 19.9
ov = [O(0, 0.2, 'T', title(START), 1)]
t0c, t1c = 0.2, m(1.84)
ts = [t0c + i * (t1c - t0c) / 14 for i in range(0, 15)]
for a, b in zip(ts, ts[1:] + [t1c + .1]):
    k = min(1, max(0, (a - t0c) / (t1c - t0c))); k = k * k * (3 - 2 * k)
    ov.append(O(a, b, 'T', title(round(START + (END - START) * k)), 1))
ov.append(O(t1c + .1, D, 'T', title(END), 1))
for a, b in zip(ts, ts[1:] + [m(1.84)]):
    k = min(1, max(0, (a - t0c) / (t1c - t0c))); k = k * k * (3 - 2 * k)
    ov.append(O(a, b, 'M', big(Y(LTR(str(round(START + (END - START) * k)))), 112), 1))
ov.append(O(0, t0c, 'M', big(Y(LTR(str(START))), 112), 1))
def Q(t0, t1, u, w, sz=60): return O(t0, t1, 'M', quote(u, w, sz))
mQ1, mQ2, mQ3, mHan, mHanE, mKt = m(14.09), m(16.32), m(18.08), m(20.45), m(22.08), m(22.24)
ov += [O(0, mHan, 'B', BAR, 1), O(mHan, mHanE, 'B', BAR + '<br><div style="height:8px"></div>' + HAN, 1), O(mHanE, mKt, 'B', BAR, 1), O(mKt, D, 'B', BAR + END_B, 1),
  O(m(1.84), m(3.64), 'M', big(f'{Y("נכדים!")} 👵', 90)),
  O(m(3.64), m(4.4), 'M', big(Y('אף אחד'), 100)), O(m(4.4), m(5.28), 'M', big(f'לא {Y("יוצא")}', 96)), O(m(5.28), m(6.77), 'M', big(f'בידיים<br>{Y("ריקות!")} 🙌', 80)),
  O(m(6.77), m(7.68), 'M', big(f'קח {Y("קופסה!")} 🥡', 76)), O(m(7.68), m(8.64), 'M', big(f'עוד {Y("קופסה!")}', 84)), O(m(8.64), m(10.0), 'M', big(f'ועוד {Y("אחת!!")}', 90)),
  O(m(10.0), m(10.32), 'M', big(f'❤️ {Y("לייק")}', 92)), O(m(10.32), m(10.88), 'M', big(f'💬 {Y("תגובה")}', 90)), O(m(10.88), m(11.6), 'M', big(f'🚀 {Y("שיתוף")}', 92)),
  Q(mQ1, mQ2, 'eliav_marciano123', 'חבל יזרק!', 70), Q(mQ2, mQ3, 'agamhudydyr', 'עלייך פשוט<br>חולה חולה 💛', 54), Q(mQ3, mHan, 'linoygruzman', 'משעמם לי', 72),
  O(mHan, mHanE, 'M', big(f'עוד {Y(LTR("9"))} ימים<br>{Y("לחנוכה")} 🕎', 78)),
  O(mHanE, m(25.1), 'M', '<div class=box>' + big(f'כתבו משפט שסבתא<br>שלכם {Y("תמיד אומרת")} 👇', 52) + '</div>'),
  O(m(25.1), D, 'M', '<div class=box>' + big(f'וסבתא {Y("קוראת")} לכם<br>לשולחן 🍽️', 54) + '</div>')]
hits = [0.02, m(3.64), m(6.77), m(10.05), m(10.88), m(14.09), mHan, mKt]
reel = {'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .4, 'novg': 1.2, 'vgmax': .35,
 'hits': hits, 'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': .04, 'speed': 0.99}], 'ov': ov}
json.dump(reel, open(f'{R}/../reel.json', 'w'), ensure_ascii=False)
print('ok', len(ov), hits)
