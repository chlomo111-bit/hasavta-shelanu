"""Specs du reel « הכוורת הכי גדולה בעולם? » חלק 2 (23.11 matin) : les 5 types d'amies du groupe WhatsApp de la ruche.
Usage : python3 specs.py <dossier_clips> <points_avant> <points_reels> ; temps lus dans tm.json (voix montée)."""
import json, sys, re
R = sys.argv[1]; P0 = int(sys.argv[2]); P1 = int(sys.argv[3])
TM = json.load(open('tm.json')); END = TM['END']; tl = {a if a=='sil' else round(a,2): (o0, o1) for a, o0, o1 in TM['tl']}
SEG = [(o0, o1) for a, o0, o1 in TM['tl']]  # wide, cool, romantic, smart, party, queen, G, sil, end
W0, W1 = 0, SEG[0][1]; CO = (SEG[1][0], SEG[1][1]); RO = (SEG[2][0], SEG[2][1]); SM = (SEG[3][0], SEG[3][1]); PA = (SEG[4][0], SEG[4][1]); QU = (SEG[5][0], SEG[5][1])
DM0 = SEG[5][1]; DM1 = SEG[7][1]; EN0 = DM1; D = END
C = {k: {'dir': f'{R}/{k}', 'fps': 10} for k in ['wide', 'cool', 'romantic', 'smart', 'party', 'queen', 'demo2', 'end']}
Y = lambda s: f'<span class=y>{s}</span>'
O = lambda t0, t1, pos, h, np=0: {'t0': round(t0, 2), 't1': round(t1, 2), 'pos': pos, 'html': h, 'np': np}
big = lambda s, sz=64: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
box = lambda s: '<div class=box>' + s + '</div>'
def title(n): return (f'<div class=box style="font:900 40px/1.15 H">הכוורת הכי {Y("גדולה")} בעולם?</div><br>'
        f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H"><span dir=ltr style="unicode-bidi:isolate">🐝 {n} / 10,000</span> דבורים</div>'
        f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 2</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
SHARE = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div><br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 24px H">📩 שלחו לחברה שלכם</div>'
SHARE = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', SHARE)
ov = []
# titre + compteur : 13 (reel précédent) puis monte jusqu'à la vraie valeur P1 pendant le barème
ov.append(O(0, DM0 + 0.2, 'T', title(P0), 1))
steps = 9; ta, tb = DM0 + 0.2, DM0 + 2.4
for i in range(steps):
    v = P0 + round((P1 - P0) * (i + 1) / steps)
    t0 = ta + (tb - ta) * i / steps; t1 = ta + (tb - ta) * (i + 1) / steps if i < steps - 1 else EN0
    ov.append(O(t0, t1, 'T', title(v), 1))
ov.append(O(EN0, D, 'T', title(P1), 1))
ov.append(O(0, EN0, 'B', BAR, 1)); ov.append(O(EN0, D, 'B', SHARE, 1))
# 1 gros mot à la fois, calé sur la voix
ov += [O(0, W1, 'M', big(f'איזו חברה<br>{Y("את")}? 💬', 76), 1)]
t = TM
ov += [O(t['kolit'], t['achat'], 'M', big(f'🎤 {Y("הקולית")}', 76)),
       O(t['achat'], CO[1], 'M', box(big(f'{Y("11")} הודעות<br>קוליות!', 62))),
       O(t['romantit'], t['ani'], 'M', big(f'🌸 {Y("הרומנטית")}', 76)),
       O(t['ani'], t['adayin'], 'M', box(big('"אני כבר<br>בדרך"', 62))),
       O(t['adayin'], RO[1], 'M', box(big(f'עדיין {Y("במיטה")}! 🛏️', 56))),
       O(t['chakhama'], t["ra'ata"], 'M', big(f'🤓 {Y("החכמה")}', 76)),
       O(t["ra'ata"], SM[1], 'M', box(big(f'ראתה… ולא<br>{Y("ענתה")}! ✔✔', 58))),
       O(t['balyanit'], t['mi'], 'M', big(f'🎩 {Y("הבליינית")}', 76)),
       O(t['mi'], t['nealma'], 'M', box(big('"מי בא<br>הלילה?"', 62))),
       O(t['nealma'], PA[1], 'M', box(big(f'ונעלמה! 💨', 62))),
       O(t['malka'], t['megenet'], 'M', big(f'👑 {Y("המלכה")}', 76)),
       O(t['megenet'], QU[1], 'M', box(big(f'מארגנת<br>את {Y("כולן")}!', 62))),
       O(DM0, DM0 + 0.95, 'M', big(f'אנחנו על<br>{Y(P1)} 🐝', 70)),
       O(DM0 + 0.95, DM0 + 1.62, 'M', big(f'לייק ❤️ {Y("+1")}', 62)),
       O(DM0 + 1.62, DM0 + 2.3, 'M', big(f'תגובה 💬 {Y("+3")}', 62)),
       O(DM0 + 2.3, EN0, 'M', box(big(f'שיתוף 🚀 {Y("+10")}', 66))),
       O(EN0, t['tagu'], 'M', box(big(f'כתבו איזה<br>{Y("תפקיד")} אתן 👇', 56) + '<div style="margin-top:8px;font:900 28px H">🎤 🌸 🤓 🎩 👑</div>')),
       O(t['tagu'], D, 'M', box(big(f'{Y("תייגו")} את<br>החברה! 🏷️', 58) + '<div style="margin-top:10px;font:900 22px/1.3 H;color:#fff">🏆 5 התגובות הכי טובות נכנסות לפרק הבא<br>המקומות פנויים – תהיו הראשונות!</div>'))]
ov = [o for o in ov if o['t1'] > o['t0']]
ISO = lambda d: [o.update(html=re.sub(r'\+(\d+)', lambda m: m.group(0) if 'isolate' in o['html'] else f'<span dir=ltr style="unicode-bidi:isolate">+{m.group(1)}</span>', o['html'])) for o in d]
ISO(ov)
names = ['wide', 'cool', 'romantic', 'smart', 'party', 'queen', 'demo2', 'end']
edges = [W0, W1, CO[1], RO[1], SM[1], PA[1], QU[1], EN0, D]
seg = [{'t0': edges[i], 't1': edges[i + 1], 'clip': names[i], 'off': 0, 'zoom': .04} for i in range(8)]
seg[6]['t1'] = EN0
reel = {'dur': D, 'fps': 30, 'clips': C, 'flash': .35, 'novg': 1.2, 'vgmax': .35,
        'hits': [0.02, W1, CO[1], RO[1], SM[1], PA[1], QU[1], DM0 + 2.3, EN0], 'seg': seg, 'ov': ov}
json.dump(reel, open(f'{R}/reel.json', 'w'), ensure_ascii=False); print('ok', D, edges)
