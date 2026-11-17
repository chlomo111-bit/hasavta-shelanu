"""Story image-question השכנים 17.11. Usage : python3 story_vote.py <fond.jpg> <sortie.jpg> <node_modules>"""
import sys, base64
from playwright.sync_api import sync_playwright
bg, out, NM = sys.argv[1:4]
b64 = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
F = NM + '/@fontsource/heebo/files/heebo-hebrew-900-normal.woff2'
H = f"""<html><head><meta charset=utf-8><style>@font-face{{font-family:H;src:url(data:font/woff2;base64,{b64(F)})}}
body{{margin:0;width:540px;height:960px;overflow:hidden;font-family:H;direction:rtl;position:relative;background:#2a2550}}
img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.w{{position:absolute;left:30px;right:30px;top:50%;transform:translateY(-50%);text-align:center;color:#fff}}
.c{{background:rgba(14,10,34,.84);border-radius:28px;padding:22px 18px;margin:14px 0}}
.p{{display:inline-block;border-radius:22px;padding:8px 20px;font-size:26px}}
.b{{display:block;border-radius:22px;padding:14px;margin:12px 0;font-size:40px}}</style></head><body><img src="data:image/jpeg;base64,{b64(bg)}">
<div class=w><div class=p style="background:#C792EA;color:#1a0f2a">🏢 השכנים · ההצבעה פתוחה</div>
<div class=c><div style="font-size:42px;line-height:1.2">הארנב נכנס<br>לדלת <span style="color:#FFC24B">10</span>… 🐰🚪</div>
<div style="font-size:30px;margin-top:10px">יש שם אור ורוד. מה דנה עושה?</div></div>
<div class=b style="background:#2fbf71">1️⃣ דופקת בדלת 🚪</div><div class=b style="background:#E5484D">2️⃣ מחכה בחוץ ⏳</div>
<div class=c style="font-size:30px">תענו 1 או 2 בריל 👇<br><span style="color:#FFC24B">כתבו שכן – ותיכנסו לסיפור</span></div></div></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
    pg.set_content(H); pg.wait_for_timeout(400); pg.screenshot(path=out, type='jpeg', quality=92); b.close()
