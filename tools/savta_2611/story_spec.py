"""Story vidéo (a) 26.11 soir : compteur 374 + « שתפו את הריל = +10 נכדים ». Voix = segments de la prise unique du reel (aucun crédit en plus).
Usage : CUT=1 python3 story_spec.py <dossier_clip>"""
import json, sys, re, subprocess, os
R = sys.argv[1]
SEGS = [(0.06, 2.22), (2.46, 5.16), (11.74, 13.94)]
TEMPO = 1.2
f = ''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={b-a-0.03:.3f}:d=0.03[s{i}];' for i, (a, b) in enumerate(SEGS))
f += ''.join(f'[s{i}]' for i in range(len(SEGS))) + f'concat=n={len(SEGS)}:v=0:a=1,atempo={TEMPO}[o]'
if os.environ.get('CUT'): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', '/root/sv/p7/raw.mp3', '-filter_complex', f, '-map', '[o]', '-ar', '44100', '/root/sv/p7/story_voice.mp3'], check=True)
d = [(b - a) / TEMPO for a, b in SEGS]; S = [0, d[0], d[0] + d[1]]; V = sum(d)
D = round(V + 1.0, 2)
Y = lambda s: f'<span class=y>{s}</span>'
LTR = lambda s: f'<span dir=ltr style="unicode-bidi:isolate">{s}</span>'
big = lambda s, sz=66: f'<div style="font:900 {sz}px/1.12 H">{s}</div>'
O = lambda t0, t1, pos, h, np=0: {'t0': round(t0, 2), 't1': round(t1, 2), 'pos': pos, 'html': h, 'np': np}
title = (f'<div class=box style="font:900 34px/1.18 H">הסבתא עם הכי הרבה<br>{Y("נכדים")} בעולם?</div><br>'
         f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">👵 {LTR("374 / 10,000")} נכדים</div>')
BAR = '<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
BAR = re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', BAR)
SH = f'<div class=pill style="margin-bottom:8px;background:#FF8FB8;color:#2a0a18;font:900 26px/1.2 H">🚀 שתפו את הריל = {LTR("+10")} נכדים</div><br>'
ov = [O(0, D, 'T', title, 1), O(0, D, 'B', SH + BAR, 1),
      O(0, S[1], 'M', big(f'{Y("נכדים!")} 👵<br>בואו לשולחן', 76)),
      O(S[1], S[2], 'M', '<div>' + big(Y(LTR('374')), 112) + f'<div class=pill style="margin-top:6px;background:#FFC24B;color:#140c04;font:900 30px H">עוד {LTR("26")} ל־{LTR("400")}!</div></div>', 1),
      O(S[2], D, 'M', big(f'🚀 {Y("שיתוף")} {Y(LTR("+10"))}<br>נכדים!', 76))]
hits = [0.02, S[1], S[2]]
json.dump({'dur': D, 'fps': 30, 'clips': {'all': {'dir': R, 'fps': 10}}, 'flash': .4, 'novg': 1.2, 'vgmax': .35, 'hits': hits,
           'seg': [{'t0': 0, 't1': D, 'clip': 'all', 'off': 0, 'zoom': .04, 'speed': 1.0}], 'ov': ov}, open('/root/sv/p7/story.json', 'w'), ensure_ascii=False)
print('story dur', D, 'voice', round(V, 2), S)
