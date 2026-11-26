"""Story image (b) 26.11 : Top 5 réel en cours. Usage : python3 story_img.py bg.jpg out.jpg"""
import sys, base64, os
from playwright.sync_api import sync_playwright
bg, out = sys.argv[1:3]
F = os.environ.get('THREE3', '/root/three3') + '/node_modules/@fontsource/heebo/files/'
b = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
rows = [('kaplan_mei', 'בריאותתתתת'), ('ohad613', 'שב תאכל, הוא יחכה'), ('mayaspam1208', 'באוי תואכלי'), ('mebyyali', 'חמסה 🪬'), ('lifeofhyro', 'אם אני לא נכדדדד')]
R = ''.join(f'<div class=r><span class=u dir=ltr>@{u}</span><span class=q>״{q}״</span></div>' for u, q in rows)
html = f"""<html><head><meta charset=utf-8><style>@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-hebrew-900-normal.woff2')})}}
@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-latin-900-normal.woff2')});unicode-range:U+0000-00FF}}
html{{overflow:hidden}}body{{margin:0;background:#000;width:1080px;height:1920px;position:relative;overflow:hidden;font-family:H;direction:rtl}}
img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:blur(10px) brightness(.55) saturate(1.2);transform:scale(1.08)}}
.c{{position:absolute;left:70px;right:70px;top:300px;text-align:center;color:#fff}}
.t{{font:900 70px/1.15 H;text-shadow:0 6px 30px rgba(0,0,0,.9)}}.t span{{color:#FFC24B}}
.h{{display:inline-block;margin:26px 0 30px;background:#FFC24B;color:#140c04;border-radius:36px;padding:12px 44px;font:900 56px H}}
.r{{background:rgba(10,8,24,.8);border-radius:28px;padding:16px 28px;margin:14px 0;display:flex;flex-direction:column;align-items:center}}
.u{{font:900 38px H;color:#FFC24B}}.q{{font:900 54px/1.15 H}}
.k{{margin-top:34px;font:900 56px/1.2 H;background:rgba(10,8,24,.8);border-radius:28px;padding:18px 30px}}.k span{{color:#FFC24B}}
.b{{margin-top:22px;display:inline-block;background:#FF8FB8;color:#2a0a18;border-radius:30px;padding:12px 36px;font:900 40px/1.3 H}}</style></head>
<body><img src="data:image/jpeg;base64,{b(bg)}"><div class=c><div class=t>הסבתא עם הכי הרבה <span>נכדים</span> בעולם?</div>
<div class=h>🏆 הטופ 5 בפרק הבא</div>{R}
<div class=k>כתבו משפט שסבתא שלכם <span>תמיד אומרת</span> 👇</div><div class=b>❤️ לייק <span style="display:inline-block;direction:ltr">+1</span> · 💬 תגובה <span style="display:inline-block;direction:ltr">+3</span><br>🔖 שמירה <span style="display:inline-block;direction:ltr">+5</span> · 🚀 שיתוף <span style="display:inline-block;direction:ltr">+10</span></div></div></body></html>"""
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920}); pg.set_content(html); pg.wait_for_timeout(500)
    pg.screenshot(path=out, type='jpeg', quality=92); br.close()
