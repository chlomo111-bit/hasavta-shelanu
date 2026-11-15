"""Specs du reel « נו… מתי חתונה? » (15.11, format B) + story « אסף כתב לי ». Usage : python3 specs.py <frames_reel> <frames_story> <outdir>"""
import json, sys
F, FS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=False: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, **({'np': True} if np else {})}
def words(ws, end, pos, sz):
    return [O(t, ws[i + 1][0] if i + 1 < len(ws) else end, pos, bx(' '.join(w for _, w in ws[:i + 1]), sz), i > 0) for i, (t, _) in enumerate(ws)]
# voix coupée + atempo 1.1 : נו .15 מתי .76 חתונה 1.16 | rire 1.85 | סבתא 2.43 כבר 2.75 הזמינה 3.01 עוגה 3.34 | כתבו 3.86 נכד 4.30 או 4.66 נכדה 4.74 | ושלחו 5.39 לסבתא 5.83 שלכם 6.34 | fin 7.0
Q = pill('😅 גם סבתא שלכם שואלת?', 30, '#FFC24B')
ov = [O(-1, 3.86, 'T', Q), O(6.3, 9, 'T', Q)]
ov += [O(-1, 2.43, 'M', bx(f'נו… מתי {Y("חתונה?")} 💍', 60))]
ov += words([(2.43, 'סבתא'), (2.75, 'כבר'), (3.01, 'הזמינה'), (3.34, Y('עוגה!') + ' 🎂')], 3.86, 'M', 52)
ov += [O(3.86, 4.30, 'M', pill('כתבו', 50)), O(4.30, 4.95, 'M', pill('כתבו<br>נכד / נכדה', 50), True), O(4.95, 9, 'M', pill('כתבו<br>נכד / נכדה<br>ותיכנסו 👇', 50), True)]
ov += [O(5.39, 9, 'B', pill('💌 שלחו לסבתא שלכם', 40, '#FF8FB8', '#2a0a18'))]
reel = {'dur': 7.5, 'clips': {'a': {'dir': F, 'fps': 10}}, 'flash': .35, 'hits': [2.0, 3.34, 3.86], 'novg': 2.0, 'vgmax': .55,
        'seg': [{'t0': 0, 't1': 7.5, 'clip': 'a', 'off': 0, 'zoom': 0}], 'ov': ov}
json.dump(reel, open(f'{OUT}/reel.json', 'w'), ensure_ascii=False)
# story : אסף .07 כתב .63 לי .89 | ד"ש 1.33 חם 1.70 ממני 1.96 סבתא 2.37 מזל 2.67 | גם 3.49 לך 3.68 מותק 3.86 | ומתי 4.75 החתונה 5.12 | תראו 6.08 בריל 6.42 החדש 6.75 | fin 7.5
st = [O(-1, 9, 'T', pill('💌 התגובה של היום', 32, '#FF8FB8', '#2a0a18')),
      O(-1, 1.33, 'M', bx(f'{Y("אסף")} כתב לי…', 50)),
      O(1.33, 3.49, 'M', bx('“ד״ש חם ממני<br>סבתא מזל” 💛<div style="font-size:26px;margin-top:6px"><span dir=ltr>@asaf.2509</span></div>', 46)),
      O(3.49, 4.75, 'M', bx(f'גם לך, {Y("מותק")}! 😘', 50)),
      O(4.75, 6.08, 'M', bx(f'ומתי ה{Y("חתונה")}? 💍', 50)),
      O(6.08, 9, 'M', pill('בריל החדש 👇<br>כתבו נכד / נכדה', 44))]
story = {'dur': 7.6, 'clips': {'a': {'dir': FS, 'fps': 7}}, 'flash': .2, 'hits': [0.05, 4.75], 'novg': 0, 'vgmax': .5,
         'seg': [{'t0': 0, 't1': 7.6, 'clip': 'a', 'off': 0, 'zoom': .04}], 'ov': st}
json.dump(story, open(f'{OUT}/story.json', 'w'), ensure_ascii=False)
print('ok')
