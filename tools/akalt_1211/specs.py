"""Specs du reel « אכלת משהו? » (12.11) + story « התגובה של השבוע ». Usage : python3 specs.py <frames3d> <outdir>"""
import json, sys
F, OUT = sys.argv[1], sys.argv[2]
C = {'a': {'dir': F, 'fps': 15}}
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
P = lambda s: f'<span class=p>{s}</span>'
O = lambda t0, t1, pos, h: {'t0': t0, 't1': t1, 'pos': pos, 'html': h}
# mots (scribe) : אכלת .12 משהו .62 | אתה 1.38 נראה 1.64 לי 1.94 רזה 2.08 | מה 3.08 זה 3.32 רק 3.7 שלוש 3.94 מנות 4.32 | קח 5.82 עוד 6.04 אחת 6.24 לדרך 6.52 | כתבו 7.5 נכד 7.94 או 8.28 נכדה 8.4 ותיכנסו 8.88 | ושלחו 9.94 לסבתא 10.38 שלכם 10.88
def words(ws, end, pos, sz, wrap=lambda s: s):
    out = []
    for i, (t, _) in enumerate(ws):
        t1 = ws[i + 1][0] if i + 1 < len(ws) else end
        o = O(t, t1, pos, bx(wrap(' '.join(w for _, w in ws[:i + 1])), sz))
        if i: o['np'] = True
        out.append(o)
    return out
Q = pill('🤔 גם סבתא שלכם<br>אומרת את זה?', 34, '#FFC24B')
ov = [O(-1, 7.45, 'T', Q), O(9.9, 12.0, 'T', Q)]
ov += [O(-1, 1.38, 'B', bx('אכלת משהו? 🍲', 62))]
ov += words([(1.38, 'אתה'), (1.64, 'נראה'), (1.94, 'לי'), (2.08, Y('רזה!'))], 3.05, 'B', 56)
ov += words([(3.05, 'מה'), (3.32, 'זה,'), (3.7, 'רק'), (3.94, Y('שלוש')), (4.32, Y('מנות?!') + ' 😱')], 5.8, 'B', 56)
ov += words([(5.8, 'קח'), (6.04, 'עוד'), (6.24, 'אחת'), (6.52, P('לדרך') + ' 😂')], 7.45, 'B', 56)
ov += [O(7.45, 7.94, 'M', pill('כתבו', 52)), {**O(7.94, 8.88, 'M', pill('כתבו<br>נכד / נכדה', 52)), 'np': True}, {**O(8.88, 12.0, 'M', pill('כתבו<br>נכד / נכדה<br>ותיכנסו 👇', 52)), 'np': True}]
ov += [O(9.94, 12.0, 'B', pill('💌 שלחו לסבתא שלכם', 42, '#FF8FB8', '#2a0a18'))]
reel = {'dur': 12.0, 'clips': C, 'flash': .35, 'hits': [3.08, 3.94, 5.25, 7.5, 9.94], 'novg': 2.0, 'vgmax': .6,
        'seg': [{'t0': 0, 't1': 12.0, 'clip': 'a', 'off': 0, 'zoom': 0}], 'ov': ov}
json.dump(reel, open(f'{OUT}/reel.json', 'w'), ensure_ascii=False)
# story : fond = plan final (Savta qui rit), ralenti
st = [O(-1, 8.0, 'T', pill('💌 התגובה של השבוע', 32, '#FF8FB8', '#2a0a18')),
      O(-1, 1.7, 'B', bx('שחר כתבה לי…', 48)),
      O(1.7, 3.45, 'B', bx('“אני אחת<br>השכנות שם” 😃<div style="font-size:26px;margin-top:6px">@shahar_b.y</div>', 46)),
      O(3.45, 6.1, 'B', bx(f'ברוכה הבאה, {Y("נשמה")}! 💛', 44)),
      O(6.1, 8.0, 'B', bx(f'מחר אני מביאה לך {Y("עוגיות")} 🍪', 40))]
story = {'dur': 8.0, 'clips': C, 'flash': .2, 'hits': [0.05, 1.73], 'novg': 0, 'vgmax': .6,
         'seg': [{'t0': 0, 't1': 8.0, 'clip': 'a', 'off': 15.2, 'speed': .5, 'zoom': .06}], 'ov': st}
json.dump(story, open(f'{OUT}/story.json', 'w'), ensure_ascii=False)
print('ok')
