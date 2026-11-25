import asyncio, sys, os
from playwright.async_api import async_playwright
OUT=sys.argv[1]; FR=os.path.join(OUT,'fr'); os.makedirs(FR,exist_ok=True)
DUR=7.9; FPS=30; A=352; B=369
CSS="""
*{box-sizing:border-box;margin:0}
body{width:1080px;height:1920px;overflow:hidden;font-family:'Heebo','Arial Hebrew',Arial,sans-serif;font-weight:900;direction:rtl;
background:linear-gradient(#5a2a1c,#8a4a2c 55%,#f0a64b);color:#fff;position:relative}
.tbl{position:absolute;left:0;right:0;bottom:0;height:620px;background:#6b3a1f;border-top:14px solid #c98a4b}
.p{position:absolute;width:90px;height:90px;border-radius:50%;background:#FFC24B;box-shadow:0 6px 14px #0006;font-size:56px;text-align:center;line-height:90px}
.title{position:absolute;top:230px;width:100%;text-align:center;font-size:76px;text-shadow:0 4px 18px #0008}
.num{position:absolute;top:560px;width:100%;text-align:center;font-size:260px;direction:ltr;color:#FFC24B;text-shadow:0 6px 24px #000a}
.of{position:absolute;top:860px;width:100%;text-align:center;font-size:60px;direction:ltr;opacity:.9}
.sub{position:absolute;top:1000px;width:100%;text-align:center;font-size:96px;text-shadow:0 4px 18px #000a}
.sub b{color:#FFC24B}
.gma{position:absolute;left:0;width:100%;top:1330px;text-align:center;font-size:200px}
.bar{position:absolute;bottom:260px;width:100%;text-align:center;font-size:44px;background:#000a;padding:22px 0}
"""
HTML=f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<div class=tbl id=t></div>
<div class=title>הסבתא עם הכי הרבה נכדים בעולם? 👵</div>
<div class=num id=n>{A}</div><div class=of>/ 10,000</div>
<div class=sub id=s></div><div class=gma id=g>👵🍲</div>
<div class=bar>לייק <bdi dir=ltr>+1</bdi> · תגובה <bdi dir=ltr>+3</bdi> · שמירה <bdi dir=ltr>+5</bdi> · שיתוף <bdi dir=ltr>+10</bdi></div>
<script>
const t=document.getElementById('t');const E=['👦','👧','🧒','👶','🧑'];
for(let i=0;i<{B}-{A}+10;i++){{const d=document.createElement('div');d.className='p';d.textContent=E[i%5];d.style.left=(40+(i%9)*110)+'px';d.style.top=(40+Math.floor(i/9)*110)+'px';d.style.opacity=0;t.appendChild(d)}}
const P=[...t.children];
function setT(x){{
 const v=Math.round({A}+Math.min(1,Math.max(0,(x-0.3)/3.2))*({B}-{A}));
 document.getElementById('n').textContent=v.toLocaleString('en-US');
 P.forEach((p,i)=>{{const on=i<(v-{A})+(x>5?10:0);p.style.opacity=on?1:0;p.style.transform='translateY('+(on?0:-30)+'px)'}});
 document.getElementById('s').innerHTML = x<2.6? '<b>נכדים</b> לשולחן!' : x<5.0? 'סבתא רוצה <b>עוד</b>' : '<b>שתפו</b> את הריל<br>= <b><bdi dir=ltr>+10</bdi></b> נכדים 🚀';
 document.getElementById('n').style.transform='scale('+(1+0.05*Math.sin(x*9))+')';
 document.getElementById('g').style.transform='translateY('+(Math.sin(x*6)*10)+'px)';
}}
</script></body></html>"""
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(); pg=await br.new_page(viewport={'width':1080,'height':1920})
        await pg.set_content(HTML); await pg.wait_for_timeout(500)
        for i in range(int(DUR*FPS)):
            await pg.evaluate(f'setT({i/FPS})'); await pg.screenshot(path=f'{FR}/f{i:04d}.jpg',type='jpeg',quality=90)
        pg2=await br.new_page(viewport={'width':1080,'height':1920})
        css2=CSS+".c{position:absolute;left:70px;right:70px;background:#000a;border-radius:28px;padding:22px 34px;font-size:42px;line-height:1.3}.c small{display:block;font-size:32px;color:#FFC24B}"
        rows=[('kaplan_mei','בריאותתתתת'),('ohad613','שב תאכל, הוא יחכה'),('mayaspam1208','באוי תואכלי'),('mebyyali','חמסה 🪬'),('lifeofhyro','אם אני לא נכדדדד')]
        h='';top=640
        for k,(u,tx) in enumerate(rows):
            h+=f'<div class=c style="top:{top}px"><small>#{k+1} · <bdi dir=ltr>@{u}</bdi></small>{tx}</div>'; top+=150
        html2=f"""<html><head><meta charset=utf-8><style>{css2}</style></head><body>
<div class=title style="top:250px;font-size:56px;white-space:nowrap">הסבתא עם הכי הרבה נכדים בעולם? 👵</div>
<div class=sub style="top:370px;font-size:78px"><b>{B}</b> נכדים מתוך 10,000</div>
<div class=sub style="top:510px;font-size:58px">🏆 הטופ 5 של משפטי סבתא</div>{h}
<div class=bar style="bottom:300px;font-size:44px">כתבו משפט שסבתא שלכם תמיד אומרת 👇</div>
<div class=bar style="bottom:200px;font-size:38px;background:#0000">לייק <bdi dir=ltr>+1</bdi> · תגובה <bdi dir=ltr>+3</bdi> · שמירה <bdi dir=ltr>+5</bdi> · שיתוף <bdi dir=ltr>+10</bdi></div>
</body></html>"""
        await pg2.set_content(html2); await pg2.wait_for_timeout(500)
        await pg2.screenshot(path=f'{OUT}/story_b.jpg',type='jpeg',quality=92)
        await br.close()
asyncio.run(main())
