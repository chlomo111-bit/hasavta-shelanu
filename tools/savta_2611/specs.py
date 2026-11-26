"""Specs « הסבתא עם הכי הרבה נכדים בעולם? » חלק 7 (26.11 soir) : compteur 374 (inchangé), « סבתא משלימה את המשפט » : le Top 5 réel, סבתא termine chaque phrase.
Usage : python3 specs.py <dossier_clip>"""
import json, sys, re
from cut import m as MM
R = sys.argv[1]
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
V = 374
D = 19.9
m = lambda t: round(MM(t), 2)
title = (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
         f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR(f"{V:,} / 10,000")} נכדים</div>'
         f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 7</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
END_B = ('<br><div class=pill style="margin-top:8px;background:#FFC24B;color:#140c04;font:900 20px/1.25 H">🏆 5 התגובות הכי טובות<br>נכנסות לפרק הבא</div>'
         '<br><div class=pill style="margin-top:6px;background:#FF8FB8;color:#2a0a18;font:900 22px H">💌 שלחו לסבתא שלכם</div>')
HAN = '<div class=pill style="background:#3fa7ff;color:#07203d;font:900 24px/1.2 H">🕎 עוד 8 ימים לחנוכה</div>'
def who(u): return f'<div class=pill style="background:#FFC24B;color:#140c04;font:900 24px H;margin-bottom:10px">🏆 {LTR("@"+u)}</div>'
def quote(u, phrase, comp, sz=44):
    return ('<div style="position:relative;top:15px"><div class=box>' + who(u) +
            f'<div style="font:900 {sz}px/1.15 H">״{phrase}״</div>' +
            f'<div style="font:900 {sz+2}px/1.15 H;margin-top:6px">👵 {Y(comp)}</div></div></div>')
ov = [O(0, D, 'T', title, 1)]
T = {}
import cut
S = lambda i: round(cut.seg_start(i), 2)
E = lambda i: round(cut.seg_start(i) + (cut.SEGS[i][1] - cut.SEGS[i][0]) / cut.TEMPO, 2)
sH, eH = S(10), E(10)
gs = [(5, 'kaplan_mei', 'בריאותתתתת', 'ותאכל, אתה עור ועצמות!'),
      (6, 'ohad613', 'שב תאכל, הוא יחכה', 'המטוס כבר התרגל לחכות!'),
      (7, 'mayaspam1208', 'באוי תואכלי', 'ותקחי גם לדרך!'),
      (8, 'mebyyali', 'חמסה 🪬', 'שלא תהיה עין רעה על הצלחת!'),
      (9, 'lifeofhyro', 'אם אני לא נכדדדד', 'אז מי? שב, יש לך מקום!')]
hanS, hanE = S(8) - .1, S(8) + 2.5
ov += [O(0, hanS, 'B', BAR, 1), O(hanS, hanE, 'B', BAR + '<br><div style="height:8px"></div>' + HAN, 1), O(hanE, sH, 'B', BAR, 1), O(sH, D, 'B', BAR + END_B, 1)]
ov += [O(0, round(MM(1.2),2), 'M', big(f'{Y("נכדים!")} 👵', 90)), O(round(MM(1.2),2), S(1) - .05, 'M', big(f'בואו {Y("לשולחן!")}', 70)),
       O(S(1) - .05, S(1) + .05, 'M', big(Y(LTR('374')), 112), 1),
       O(S(1) + .05, S(2) - .1, 'M', '<div style="position:relative">' + big(Y(LTR('374')), 112) + f'<div class=pill style="margin-top:6px;background:#FFC24B;color:#140c04;font:900 30px H">עוד {LTR("26")} ל־{LTR("400")}!</div></div>', 1),
       O(S(2) - .1, S(3), 'M', big(f'❤️ {Y("לייק")}<br>{Y(LTR("+1"))}', 84)),
       O(S(3), S(4), 'M', big(f'💬 {Y("תגובה")}<br>{Y(LTR("+3"))}', 80)),
       O(S(4), S(5) - .2, 'M', big(f'🚀 {Y("שיתוף")}<br>{Y(LTR("+10"))}', 84)),
       O(S(5) - .2, S(5) - .01, 'M', big(f'{Y("תכתבו")} —<br>סבתא משלימה', 60))]
for k, (i, u, ph, comp) in enumerate(gs):
    t0 = S(i) - .2
    t1 = S(i + 1) - .2 if i < 9 else S(10) - .1
    ov.append(O(max(t0, 0), t1, 'M', quote(u, ph, comp, 40 if len(ph) < 14 else 36)))
ov.append(O(sH - .1, D, 'M', '<div class=box>' + big(f'כתבו משפט שסבתא<br>שלכם {Y("תמיד אומרת")} 👇', 50) + '</div>'))
hits = [0.02, S(1), S(2) + .5, S(3) + .25, S(4) + .3, S(5), S(6), S(7), S(8), S(9), sH]
reel = {'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .4, 'novg': 1.2, 'vgmax': .35,
        'hits': hits, 'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': .04, 'speed': 0.99}], 'ov': ov}
json.dump(reel, open(f'{R}/../reel.json', 'w'), ensure_ascii=False)
print('ok', len(ov), hits)
