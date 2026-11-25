import asyncio, sys, os
from playwright.async_api import async_playwright
OUT=sys.argv[1]; FR=os.path.join(OUT,'fr'); os.makedirs(FR,exist_ok=True)
DUR=7.4; FPS=30
CSS="""
*{box-sizing:border-box;margin:0}
body{width:1080px;height:1920px;overflow:hidden;font-family:'Heebo','Arial Hebrew',Arial,sans-serif;font-weight:900;direction:rtl;
background:linear-gradient(#1c2b5a,#3b2f6b 55%,#f08a4b);color:#fff;position:relative}
.bld{position:absolute;left:210px;width:660px;bottom:0;height:1500px;background:#2a2f4a;border-radius:18px 18px 0 0;
display:grid;grid-template-columns:repeat(6,1fr);gap:22px;padding:40px 36px}
.w{background:#161a2e;border-radius:6px;height:56px}
.w.on{background:#FFC24B;box-shadow:0 0 22px #FFC24B}
.title{position:absolute;top:250px;width:100%;text-align:center;font-size:76px;text-shadow:0 4px 18px #0008}
.num{position:absolute;top:620px;width:100%;text-align:center;font-size:230px;direction:ltr;color:#FFC24B;text-shadow:0 6px 24px #000a}
.sub{position:absolute;top:900px;width:100%;text-align:center;font-size:96px;text-shadow:0 4px 18px #000a}
.sub b{color:#FFC24B}
.bar{position:absolute;bottom:260px;width:100%;text-align:center;font-size:44px;background:#000a;padding:22px 0}
"""
HTML=f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<div class=bld id=b></div>
<div class=title>הבניין הכי גבוה בעולם? 🏢</div>
<div class=num id=n>1,691</div>
<div class=sub id=s></div>
<div class=bar>לייק <bdi dir=ltr>+1</bdi> · תגובה <bdi dir=ltr>+3</bdi> · שמירה <bdi dir=ltr>+5</bdi> · שיתוף <bdi dir=ltr>+10</bdi></div>
<script>
const b=document.getElementById('b');for(let i=0;i<96;i++){{const d=document.createElement('div');d.className='w';b.appendChild(d)}}
const W=[...b.children];
function setT(t){{
 const v=Math.round(1691+Math.min(1,Math.max(0,(t-0.3)/2.2))*5);
 document.getElementById('n').textContent=v.toLocaleString('en-US');
 const lit=Math.floor(36+ (v-1691)*2 + Math.max(0,t-4)*4 + (t>5.2?10:0));
 W.forEach((w,i)=>w.className='w'+(((i*37)%96)<lit?' on':''));
 const s=document.getElementById('s');
 s.innerHTML = t<2.8? 'דיירים!' : t<5.0? 'הבניין <b>גדל</b> 🏗️' : '<b>שתפו</b> את הריל<br>= <b><bdi dir=ltr>+10</bdi></b> דיירים 🚀';
 document.getElementById('n').style.transform='scale('+(1+0.06*Math.sin(t*9))+')';
}}
</script></body></html>"""
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(); pg=await br.new_page(viewport={'width':1080,'height':1920})
        await pg.set_content(HTML); await pg.wait_for_timeout(500)
        n=int(DUR*FPS)
        for i in range(n):
            await pg.evaluate(f'setT({i/FPS})'); await pg.screenshot(path=f'{FR}/f{i:04d}.jpg',type='jpeg',quality=90)
        # image story
        pg2=await br.new_page(viewport={'width':1080,'height':1920})
        css2=CSS+".c{position:absolute;left:70px;right:70px;background:#000a;border-radius:28px;padding:26px 34px;font-size:44px;line-height:1.3}.c small{display:block;font-size:34px;color:#FFC24B}.free{color:#ccc;font-weight:700}"
        card=lambda u,t:f'<div class=c style="top:{{top}}px"><small><bdi dir=ltr>@{u}</bdi></small>{t}</div>'
        rows=[('hillimoshe7','משהוא שר במקלחת'),('hayley645726','מה לא ריבים'),('____alonii____','השכן עם הסיפורים המוזרים')]
        h=''
        top=640
        for k,(u,t) in enumerate(rows):
            h+=f'<div class=c style="top:{top}px"><small>#{k+1} · <bdi dir=ltr>@{u}</bdi></small>{t}</div>'; top+=170
        for k in (4,5):
            h+=f'<div class=c style="top:{top}px"><small>#{k}</small><span class=free>המקום פנוי – תהיו הראשונים</span></div>'; top+=170
        html2=f"""<html><head><meta charset=utf-8><style>{css2}</style></head><body>
<div class=title style="top:240px;font-size:80px">הבניין הכי גבוה בעולם? 🏢</div>
<div class=sub style="top:380px;font-size:70px"><b>1,696</b> דיירים מתוך 10,000</div>
<div class=sub style="top:520px;font-size:60px">🏆 הטופ 5 לפרק הבא</div>{h}
<div class=bar style="bottom:300px;font-size:46px">כתבו מה השכנים שומעים מהדירה שלכם 👇</div>
<div class=bar style="bottom:200px;font-size:38px;background:#0000">לייק <bdi dir=ltr>+1</bdi> · תגובה <bdi dir=ltr>+3</bdi> · שמירה <bdi dir=ltr>+5</bdi> · שיתוף <bdi dir=ltr>+10</bdi></div>
</body></html>"""
        await pg2.set_content(html2); await pg2.wait_for_timeout(500)
        await pg2.screenshot(path=f'{OUT}/story_b.jpg',type='jpeg',quality=92)
        await br.close()
asyncio.run(main())
