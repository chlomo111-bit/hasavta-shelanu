import json,base64,os
from playwright.sync_api import sync_playwright
F='/root/three3/node_modules/@fontsource/heebo/files/'
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
html=f"""<html><head><meta charset=utf-8><style>@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-hebrew-900-normal.woff2')})}}
@font-face{{font-family:H;font-weight:900;src:url(data:font/woff2;base64,{b(F+'heebo-latin-900-normal.woff2')});unicode-range:U+0000-00FF}}
html{{overflow:hidden}}body{{margin:0;background:#000;width:1080px;height:1920px;position:relative;overflow:hidden;font-family:H;direction:rtl;color:#fff}}
img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:blur(10px) brightness(.55) saturate(1.2);transform:scale(1.1)}}
.c{{position:absolute;left:70px;right:70px;top:230px;text-align:center}}
.h{{font:900 100px/1.1 H}}.y{{color:#FFC24B}}
.row{{background:rgba(10,8,24,.85);border-radius:34px;padding:22px 30px;margin-top:26px;font:900 46px/1.3 H}}
.free{{background:rgba(255,194,75,.18);border:4px dashed #FFC24B;color:#FFC24B}}
.pill{{display:inline-block;background:#FFC24B;color:#140c04;border-radius:40px;padding:12px 44px;font:900 60px H;margin-top:26px}}
.bar{{position:absolute;left:70px;right:70px;bottom:330px;text-align:center;background:rgba(10,8,24,.88);border-radius:34px;padding:22px;font:900 44px/1.4 H}}
</style></head><body><img src="data:image/jpeg;base64,{b('/root/w2/wide/f0030.jpg')}"><div class=c>
<div class=h>🏆 הטופ 5 <span class=y>בפרק הבא</span></div>
<div class=pill>🏢 <span dir=ltr style="unicode-bidi:isolate">1,182 / 10,000</span> דיירים</div>
<div class=row>1️⃣ <span class=y dir=ltr>@hillimoshe7</span><br>״משהוא שר במקלחת״</div>
<div class=row>2️⃣ <span class=y dir=ltr>@hayley645726</span><br>״מה לא ריבים״</div>
<div class="row free">3 מקומות פנויים<br>כתבו מה השכנים שומעים אצלכם 👇</div>
<div class=row>🎉 <span class=y>מאור</span> כבר בפנים</div></div>
<div class=bar>❤️ לייק <span dir=ltr style="unicode-bidi:isolate">+1</span> · 💬 תגובה <span dir=ltr style="unicode-bidi:isolate">+3</span><br>🔖 שמירה <span dir=ltr style="unicode-bidi:isolate">+5</span> · 🚀 שיתוף <span dir=ltr style="unicode-bidi:isolate">+10</span></div></body></html>"""
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':1080,'height':1920});pg.set_content(html);pg.wait_for_timeout(500);pg.screenshot(path='/root/w2/story_b.jpg',type='jpeg',quality=92);br.close()
# story a : spec compose
C={'wide':{'dir':'/root/w2/wide','fps':10},'top':{'dir':'/root/w2/top','fps':10}}
exec(open('specs.py').read().split("D=19.6")[0].split("A=int")[0].replace("R=sys.argv[1]; ",""),{}) if False else None
Y=lambda s:f'<span class=y>{s}</span>'
ISO=lambda s: s.replace('+10','<span dir=ltr style="unicode-bidi:isolate">+10</span>')
O=lambda t0,t1,pos,h,np=0:{'t0':t0,'t1':t1,'pos':pos,'html':ISO(h),'np':np}
big=lambda s,sz=66:f'<div class=box style="font:900 {sz}px/1.12 H;padding:6px 22px">{s}</div>'
TT=('<div class=box style="font:900 40px/1.15 H">הבניין הכי <span class=y>גבוה</span> בעולם?</div><br><div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🏢 <span dir=ltr style="unicode-bidi:isolate">1,182 / 10,000</span> דיירים</div>')
D=6.9
sp={'dur':D,'fps':30,'clips':C,'flash':.4,'novg':1.0,'vgmax':.35,'hits':[0.02,3.4],
 'seg':[{'t0':0,'t1':3.4,'clip':'wide','off':0,'zoom':.03},{'t0':3.4,'t1':D,'clip':'top','off':3.0,'zoom':.02}],
 'ov':[O(0,D,'T',TT,1),O(0,3.4,'M',big(f'{Y("1,182")}<br>דיירים!',92),1),O(3.4,D,'M',big(f'שתפו את הריל<br>{Y("= +10")} דיירים 🚀',56)),
       O(0,D,'B','<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'.replace('+10','<span dir=ltr style="unicode-bidi:isolate">+10</span>'),1)]}
json.dump(sp,open('/root/w2/story_a.json','w'),ensure_ascii=False)
