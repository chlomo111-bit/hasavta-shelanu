import base64, io
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright
F='/root/three3/node_modules/@fontsource/heebo/files/heebo-hebrew-{w}-normal.woff2'
FL='/root/three3/node_modules/@fontsource/heebo/files/heebo-latin-{w}-normal.woff2'
S={
 'ruche':('ruche_3.jpg',(.30,.86),'#FFC24B','הכוורת הכי גדולה בעולם?','דבורים','כל לייק = עוד דבורה 🐝','חלק 1 הערב ב־18:30'),
 'bateau':('bateau_3.jpg',(.36,.92),'#5EC8FF','הספינה הכי גדולה בעולם?','נוסעים','כל לייק = עוד נוסע 🚢','חלק 1 הערב ב־19:30'),
 'noise':('noise_9.jpg',(.28,.78),'#FF5A6E','המקהלה הכי מזייפת בעולם?','זמרים','כל לייק = עוד זמר 🎤','חלק 1 מחר ב־20:00'),
 'savta':('savta_9.jpg',(.50,.99),'#FFB3C7','הסבתא עם הכי הרבה נכדים בעולם?','נכדים','כל לייק = עוד נכד 👵','חלק 1 הערב ב־19:00'),
}
def b64(im):
    b=io.BytesIO(); im.save(b,'JPEG',quality=92); return base64.b64encode(b.getvalue()).decode()
def font(w):
    a=base64.b64encode(open(F.format(w=w),'rb').read()).decode(); l=base64.b64encode(open(FL.format(w=w),'rb').read()).decode()
    return f"@font-face{{font-family:H;font-weight:{w};src:url(data:font/woff2;base64,{a})}}@font-face{{font-family:H;font-weight:{w};src:url(data:font/woff2;base64,{l});unicode-range:U+0000-00FF}}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for k,(src,win,acc,title,unit,sub,when) in S.items():
        im=Image.open(src).convert('RGB').resize((1080,1920))
        bg=b64(im.filter(ImageFilter.GaussianBlur(30)))
        w=im.crop((0,int(1920*win[0]),1080,int(1920*win[1])))
        html=f'''<html><head><style>{font(800)}{font(900)}{font(700)}
body{{margin:0;width:1080px;height:1920px;font-family:H;direction:rtl;color:#fff;overflow:hidden;
background:url(data:image/jpeg;base64,{bg}) center/cover}}
.dim{{position:absolute;inset:0;background:rgba(0,0,0,.35)}}
.wrap{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;padding:0 70px;text-align:center}}
h1{{font-weight:900;font-size:84px;line-height:1.08;margin:0;text-shadow:0 6px 24px rgba(0,0,0,.6)}}
.win{{width:820px;height:640px;border-radius:44px;background:url(data:image/jpeg;base64,{b64(w)}) center/cover;border:8px solid {acc};box-shadow:0 20px 60px rgba(0,0,0,.5)}}
.cnt{{background:rgba(0,0,0,.62);border-radius:36px;padding:22px 46px;font-weight:900;font-size:92px}}
.cnt small{{font-size:52px;color:{acc}}}
.sub{{font-weight:800;font-size:48px;white-space:nowrap}}
.bar{{font-weight:800;font-size:40px;background:{acc};color:#111;border-radius:28px;padding:16px 30px}}
.when{{font-weight:900;font-size:58px;color:{acc};text-shadow:0 4px 16px rgba(0,0,0,.7)}}
</style></head><body><div class=dim></div><div class=wrap>
<h1>{title}</h1><div class=win></div>
<div class=cnt><span dir=ltr>0 / 10,000</span> <small>{unit}</small></div>
<div class=sub>מתחילים מאפס – {sub}</div>
<div class=bar>לייק <bdi dir=ltr>+1</bdi> · תגובה <bdi dir=ltr>+3</bdi> · שמירה <bdi dir=ltr>+5</bdi> · שיתוף <bdi dir=ltr>+10</bdi></div>
<div class=when><bdi>{when}</bdi> 🔥</div></div></body></html>'''
        pg.set_content(html); pg.wait_for_timeout(400)
        pg.screenshot(path=f'story_{k}.jpg',type='jpeg',quality=92)
    b.close()
