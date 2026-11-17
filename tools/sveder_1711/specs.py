"""Specs du reel « תלבש סוודר! » (17.11, format B) + story vidéo. Usage : python3 specs.py <frames_reel> <outdir>"""
import json, sys
F, OUT = sys.argv[1], sys.argv[2]
bx = lambda s, sz=30: f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill = lambda s, sz=30, bg='#FFC24B', fg='#140c04': f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=False: {'t0': t0, 't1': t1, 'pos': pos, 'html': h, **({'np': True} if np else {})}
# voix coupée + atempo 1.12 : תלבש סוודר 0 | קר בחוץ 1.05 | הנה עוד אחד 1.71 | ועוד אחד 2.58 | rire 3.3 | כתבו 3.8 נכד 4.0 או נכדה 4.6 ותיכנסו 5.33 | ושלחו 5.94 | fin 7.33
Q = pill('🧶 גם סבתא שלכם אומרת?', 30, '#FFC24B')
ov = [O(-1, 3.8, 'T', Q), O(6.6, 9, 'T', Q)]
ov += [O(-1, 1.05, 'M', bx(f'{Y("תלבש סוודר!")} 🧶', 64)), O(1.05, 1.71, 'M', bx(f'{Y("תלבש סוודר!")} 🧶<br>קר בחוץ! 🥶', 64), True)]
ov += [O(1.71, 2.58, 'M', bx('הנה עוד אחד…', 56)), O(2.58, 3.8, 'M', bx(f'…ו{Y("עוד אחד!")} 😂', 60))]
ov += [O(3.8, 4.0, 'M', pill('כתבו', 46)), O(4.0, 5.33, 'M', pill('כתבו נכד / נכדה', 46), True), O(5.33, 9, 'M', pill('כתבו נכד / נכדה<br>ותיכנסו 👇', 46), True)]
ov += [O(5.94, 9, 'B', pill('💌 שלחו לסבתא שלכם', 40, '#FF8FB8', '#2a0a18'))]
reel = {'dur': 7.5, 'clips': {'a': {'dir': F, 'fps': 10}}, 'flash': .35, 'hits': [1.9, 2.58, 3.8], 'novg': 2.0, 'vgmax': .55,
        'seg': [{'t0': 0, 't1': 7.5, 'clip': 'a', 'off': 0, 'zoom': 0}], 'ov': ov}
json.dump(reel, open(f'{OUT}/reel.json', 'w'), ensure_ascii=False)
# story (voix coupée + atempo 1.15) : קר בחוץ 0 | אז סבתא סרגה סוודרים לכולם .65 | ראיתם בריל החדש 2.83 | כתבו נכד או נכדה 3.98 | והשם שלכם בסטורי הבא 5.42 | fin 7.08
st = [O(-1, 9, 'T', pill('👵 סבתא סורגת', 32, '#FF8FB8', '#2a0a18')),
      O(-1, .65, 'M', bx(f'קר {Y("בחוץ")}… 🥶', 54)),
      O(.65, 2.83, 'M', bx(f'סבתא סרגה<br>{Y("סוודרים לכולם!")} 🧶', 52)),
      O(2.83, 3.98, 'M', pill('ראיתם בריל החדש? 👀', 44)),
      O(3.98, 5.42, 'M', pill('כתבו<br>נכד / נכדה', 50)),
      O(5.42, 9, 'M', pill('כתבו נכד / נכדה<br>ותהיו בסטורי הבא ✨', 44))]
story = {'dur': 7.2, 'clips': {'a': {'dir': F, 'fps': 10}}, 'flash': .25, 'hits': [2.83], 'novg': 0, 'vgmax': .5,
         'seg': [{'t0': 0, 't1': 3.4, 'clip': 'a', 'off': 1.9, 'zoom': .03}, {'t0': 3.4, 't1': 7.2, 'clip': 'a', 'off': 3.8, 'zoom': .03}], 'ov': st}
json.dump(story, open(f'{OUT}/story.json', 'w'), ensure_ascii=False)
print('ok')
