"""Story image-question 17.11 : « סבתא שלכם סרגה לכם סוודר? תענו 1 או 2 ». Usage : python3 story_vote.py <fond.jpg> <out.jpg>"""
import sys, base64
from playwright.sync_api import sync_playwright
bg, out = sys.argv[1], sys.argv[2]
F = '/root/three3/node_modules/@fontsource/heebo/files/'
b = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
H = f"""<html><head><meta charset=utf-8><style>
@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-hebrew-900-normal.woff2')})}}
@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-latin-900-normal.woff2')});unicode-range:U+0000-00FF}}
body{{margin:0;width:540px;height:960px;overflow:hidden;font-family:H;direction:rtl;position:relative;background:#000}}
img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.c{{position:absolute;left:30px;right:30px;text-align:center;color:#fff;font-weight:900}}
.q{{top:120px;background:rgba(10,8,24,.8);border-radius:26px;padding:18px 16px;font-size:40px;line-height:1.2}}
.y{{color:#FFC24B}}
.o{{display:block;margin:16px auto;border-radius:24px;padding:16px;font-size:38px;color:#140c04}}
.ans{{top:560px}}
.t{{top:40px;font-size:24px}} .t span{{background:#FF8FB8;color:#2a0a18;border-radius:18px;padding:8px 18px}}
.f{{top:860px;font-size:28px}} .f span{{background:rgba(10,8,24,.8);border-radius:18px;padding:8px 18px}}
</style></head><body><img src="data:image/jpeg;base64,{b(bg)}">
<div class="c t"><span>👵 שאלה של סבתא</span></div>
<div class="c q">סבתא שלכם<br>סרגה לכם <span class=y>סוודר?</span> 🧶</div>
<div class="c ans"><span class=o style="background:#FFC24B">1 · 🧶 כן! יש לי ערימה</span><span class=o style="background:#FF8FB8">2 · 🥶 עדיין מחכה…</span></div>
<div class="c f"><span>תענו 1 או 2 בהודעה 👇</span></div>
</body></html>"""
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
    pg.set_content(H); pg.wait_for_timeout(500); pg.screenshot(path=out, type='jpeg', quality=90); br.close()
print('ok')
