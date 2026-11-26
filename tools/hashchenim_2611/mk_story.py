import base64
from playwright.sync_api import sync_playwright
F='/root/three3/node_modules/@fontsource/heebo/files/'
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
html=f"""<html><head><meta charset=utf-8><style>
@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-hebrew-900-normal.woff2')})}}
@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-latin-900-normal.woff2')});unicode-range:U+0000-00FF}}
html{{overflow:hidden}}body{{margin:0;width:540px;height:960px;overflow:hidden;font-family:H;direction:rtl;position:relative;color:#fff;text-align:center}}
#bg{{position:absolute;left:0;top:0;width:540px;height:960px;background:url(data:image/jpeg;base64,{b('sbg.jpg')}) center/cover;filter:blur(10px) brightness(.55);transform:scale(1.1)}}
.c{{position:absolute;left:0;right:0}}
.y{{color:#FFC24B}}.card{{display:block;margin:7px 40px;background:rgba(10,8,24,.82);border-radius:18px;padding:8px 14px;font-size:21px;line-height:1.25}}
.card small{{display:block;font-size:17px;color:#FFC24B}}
.pill{{display:inline-block;border-radius:22px;padding:8px 20px}}
</style></head><body><div id=bg></div>
<div class=c style="top:150px"><div class=pill style="background:rgba(10,8,24,.85);font-size:32px">הבניין הכי <span class=y>גבוה</span> בעולם?</div><br>
<div class=pill style="margin-top:8px;background:#FFC24B;color:#140c04;font-size:24px">🏢 <span dir=ltr style="unicode-bidi:isolate">1,707 / 10,000</span> דיירים</div></div>
<div class=c style="top:285px"><div style="font-size:26px;margin-bottom:6px">🏆 הטופ 5 בפרק הבא</div>
<div class=card><small dir=ltr>@hillimoshe7</small>משהוא שר במקלחת</div>
<div class=card><small dir=ltr>@hayley645726</small>מה לא ריבים</div>
<div class=card><small dir=ltr>@____alonii____</small>השכן עם הסיפורים המוזרים</div>
<div class=card style="opacity:.8">2 מקומות פנויים – תהיו הראשונים!</div></div>
<div class=c style="top:690px"><div class=pill style="background:#C792EA;color:#1a0f2a;font-size:23px;line-height:1.3">כתבו מה השכנים שומעים<br>מהדירה שלכם 👇</div></div>
<div class=c style="top:780px"><div class=pill style="background:rgba(10,8,24,.85);font-size:18px;line-height:1.4">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div></div>
</body></html>"""
import re
html=re.sub(r"\+(\d+)",r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>',html)
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':540,'height':960},device_scale_factor=2);pg.set_content(html);pg.wait_for_timeout(400);pg.screenshot(path='story_top5.jpg',type='jpeg',quality=92);br.close()
