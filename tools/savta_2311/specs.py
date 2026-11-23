"""Specs « הסבתא עם הכי הרבה נכדים בעולם? » חלק 2 (23.11 matin) : « תרגום מסבתאית » — 5 vraies phrases de joueurs.
Usage : python3 specs.py <dossier_clips> """
import json, sys, re, glob, math
R = sys.argv[1]
SH = {'s1': (0, 1.17), 's2': (1.17, 1.96), 's3': (1.96, 3.33), 's4': (3.33, 3.99), 's5': (3.99, 5.67), 's6': (5.67, 6.57), 's7': (6.57, 8.25), 's8': (8.25, 8.79), 's9': (8.79, 10.75), 's10': (10.75, 11.49), 's11': (11.49, 12.96), 's12': (12.96, 13.92), 's13': (13.92, 15.62), 's14': (15.62, 17.72), 's15': (17.72, 19.85)}
C = {k: {'dir': f'{R}/{k}', 'fps': 30} for k in SH}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
START, END = 12, 130
def title(v):
    return (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR(f"{v:,} / 10,000")} נכדים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 2</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
SHARE = '<br><div class=pill style="margin-top:8px;background:#FF8FB8;color:#2a0a18;font:900 24px H">💌 שלחו לסבתא שלכם</div>'
TOP5 = '<br><div class=pill style="margin-top:8px;background:#FFC24B;color:#140c04;font:900 20px/1.25 H">🏆 5 התגובות הכי טובות<br>נכנסות לפרק הבא</div>'
def who(u): return f'<div class=pill style="background:#FFC24B;color:#140c04;font:900 24px H;margin-bottom:10px">🏆 {LTR("@"+u)}</div>'
def quote(u, w, sz=84): return '<div class=box>' + who(u) + big(w, sz) + '</div>'
D = 19.85
ov = [O(0, 13.0, 'T', title(START), 1)]
ts = [13.0 + i / 15 for i in range(0, 38)]
for a, b in zip(ts, ts[1:] + [15.5]):
    k = min(1, max(0, (a - 13.0) / 2.4)); k = k * k * (3 - 2 * k)
    ov.append(O(a, b, 'T', title(round(START + (END - START) * k)), 1))
ov.append(O(15.5, D, 'T', title(END), 1))
ov += [O(0, 13.92, 'B', BAR, 1), O(13.92, 17.72, 'B', BAR, 1), O(17.72, D, 'B', BAR + TOP5, 1),
  O(0, .55, 'M', big('סבתא', 84), 1), O(.55, 1.17, 'M', big(f'{Y("מתרגמת!")} 👵', 80)),
  O(1.17, 1.96, 'M', quote('kaplan_mei', 'בריאותתתתת!', 70)),
  O(1.96, 2.51, 'M', big('זה אומר:', 64)),
  O(2.51, 3.33, 'M', '<div class=box>' + big(f'{Y("אני אוהבת")}<br>{Y("אותך")} 💛', 68) + '</div>'),
  O(3.33, 3.99, 'M', quote('ohad613', 'הוא יחכה!', 76)),
  O(3.99, 4.5, 'M', big('זה אומר:', 64)),
  O(4.5, 5.05, 'M', '<div class=box>' + big(Y('אתה לא יוצא'), 66) + '</div>'),
  O(5.05, 5.67, 'M', '<div class=box>' + big(f'{Y("מפה רעב")} 🍲', 70) + '</div>'),
  O(5.67, 6.57, 'M', quote('eliav_marciano123', 'חבל יזרק!', 76)),
  O(6.57, 7.06, 'M', big('זה אומר:', 64)),
  O(7.06, 7.6, 'M', '<div class=box>' + big(Y('תגמור הכול'), 68) + '</div>'),
  O(7.6, 8.25, 'M', '<div class=box>' + big(f'{Y("בצלחת")} 🍽️', 72) + '</div>'),
  O(8.25, 8.79, 'M', quote('mebyyali', 'חמסה! 🪬', 80)),
  O(8.79, 9.45, 'M', big('זה אומר:', 64)),
  O(9.45, 10.0, 'M', '<div class=box>' + big(Y('שאף אחד'), 70) + '</div>'),
  O(10.0, 10.75, 'M', '<div class=box>' + big(f'{Y("לא יקנא בך")} 😎', 62) + '</div>'),
  O(10.75, 11.49, 'M', quote('mayaspam1208', 'באוי תואכלי!', 62)),
  O(11.49, 11.99, 'M', big('זה אומר:', 64)),
  O(11.99, 12.96, 'M', '<div class=box>' + big(f'{Y("אל תקום")}<br>מהשולחן 🪑', 66) + '</div>'),
  O(12.96, 13.92, 'M', '<div class=box>' + big(f'{Y("ובזכותכם…")}', 76) + '</div>'),
  O(13.92, 14.8, 'M', '<div class=box>' + big(Y(LTR('130')), 130) + '</div>'),
  O(14.8, 15.62, 'M', '<div class=box>' + big(f'{Y("נכדים!")} 🎉', 84) + '</div>'),
  O(15.62, 16.4, 'M', big('כתבו משפט', 70)),
  O(16.4, 17.1, 'M', big(Y('שסבתא שלכם'), 66)),
  O(17.1, 17.72, 'M', big(f'תמיד אומרת 👇', 66)),
  O(17.72, 18.5, 'M', '<div class=box>' + big(f'{Y("ואני אתרגם!")}', 66) + '</div>'),
  O(18.5, D, 'M', '<div class=box>' + big(f'שלחו {Y("לסבתא")}<br>שלכם 💌', 60) + '</div>')]
def sp(k, a, b): 
    n = len(glob.glob(f'{R}/{k}/f*.jpg'))
    return min(1, (n - 1) / 30 / (b - a + 1 / 30))
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .4, 'novg': 1.2, 'vgmax': .35,
 'hits': [0.02, 1.17, 1.96, 3.33, 3.99, 5.67, 6.57, 8.25, 8.79, 10.75, 11.49, 12.96, 13.92, 15.62, 17.72],
 'seg': [{'t0': a, 't1': b, 'clip': k, 'off': 0, 'zoom': .04, 'speed': sp(k, a, b)} for k, (a, b) in SH.items()], 'ov': ov}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False)
print('ok', len(ov))
