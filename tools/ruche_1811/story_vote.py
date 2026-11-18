"""Story image-question Ruche 18.11 : classement de la couronne + « תענו 1 או 2 ». Usage : python3 story_vote.py bg.jpg out.jpg"""
import sys, base64
from playwright.sync_api import sync_playwright
F='/root/three3/node_modules/@fontsource/heebo/files/'
b=lambda p: base64.b64encode(open(p,'rb').read()).decode()
H=f"""<html><head><meta charset=utf-8><style>@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-hebrew-900-normal.woff2')})}}
@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-latin-900-normal.woff2')});unicode-range:U+0000-00FF}}
body{{margin:0;width:540px;height:960px;overflow:hidden;font-family:H;direction:rtl;color:#fff;text-align:center;position:relative;background:#2A1606}}
#bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.c{{position:absolute;left:0;right:0;padding:0 34px}}
.box{{display:inline-block;background:rgba(26,14,6,.82);border-radius:26px;padding:14px 26px}}
.y{{color:#FFC24B}} .pill{{display:inline-block;border-radius:22px;padding:10px 22px}}
.row{{display:flex;justify-content:space-between;font:900 30px H;padding:6px 4px}}
.b{{display:inline-block;width:38%;margin:0 6px;border-radius:24px;padding:14px 0;font:900 36px/1.2 H}}
</style></head><body><img id=bg src="data:image/jpeg;base64,{b(sys.argv[1])}">
<div class=c style="top:12%"><div class=pill style="background:#FFC24B;color:#140c04;font:900 26px H">🐝 הכוורת שלנו · מרוץ הכתר</div></div>
<div class=c style="top:20%"><div class=box style="width:80%"><div style="font:900 34px H;margin-bottom:8px">👑 מלכת השבוע</div>
<div class=row><span dir=ltr>@shellydor20</span><span class=y>7 קולות</span></div>
<div class=row><span dir=ltr>@shahar_b.y</span><span class=y>1</span></div>
<div style="font:900 24px H;margin-top:8px">🐝 דבורה חדשה: <span dir=ltr class=y>@hyll.khbsvb</span></div></div></div>
<div class=c style="top:50%"><div class=box style="font:900 44px/1.15 H">מי <span class=y>צודקת</span>?<br>תענו <span class=y>1</span> או <span class=y>2</span> 👇</div></div>
<div class=c style="top:64%"><span class=b style="background:#2E9E5B">1️⃣<br>הירוקה 🤓</span><span class=b style="background:#E0609A">2️⃣<br>הגנבת 😈</span></div>
<div class=c style="bottom:9%"><div class=pill style="background:#fff;color:#140c04;font:900 24px H">כתבו דבורה – והשם שלכן בכוורת 🐝</div></div>
</body></html>"""
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':540,'height':960},device_scale_factor=2);pg.set_content(H);pg.wait_for_timeout(400)
    pg.screenshot(path=sys.argv[2],type='jpeg',quality=92);br.close()
