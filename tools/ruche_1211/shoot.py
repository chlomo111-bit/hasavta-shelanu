import sys,time,os,json
from playwright.sync_api import sync_playwright
SP="/root"; T=SP+"/three3/node_modules/three/"; F=SP+"/three3/node_modules/@fontsource/heebo/files/"
src=open("/home/claude/hakaveret/index.html").read()
html=src.split("<body>",1)[1].rsplit("</body>",1)[0]
fonts="<style>@font-face{font-family:Heebo;font-weight:900;src:url(http://test/h900.woff2);unicode-range:U+0590-05FF,U+20AA}@font-face{font-family:Heebo;font-weight:900;src:url(http://test/l900.woff2);unicode-range:U+0000-00FF}@font-face{font-family:Heebo;font-weight:700;src:url(http://test/h700.woff2)}</style>"
page_html="<!doctype html><html><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"+fonts+"</head><body>"+html+"</body></html>"
SHOTS=json.load(open(sys.argv[1])); OUT=sys.argv[2]; os.makedirs(OUT,exist_ok=True)
W,H=(540,675) if os.environ.get("FMT","post")=="post" else (540,960)
with sync_playwright() as p:
    b=p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"])
    pg=b.new_page(viewport={"width":W,"height":H},device_scale_factor=2)
    pg.add_init_script("window.CAP=true")
    errs=[]; pg.on("pageerror",lambda e: errs.append(str(e)))
    def route(r):
        u=r.request.url
        if "three.min.js" in u: r.fulfill(path=T+"build/three.min.js",content_type="text/javascript")
        elif "OrbitControls" in u: r.fulfill(path=T+"examples/js/controls/OrbitControls.js",content_type="text/javascript")
        elif u.endswith("h900.woff2"): r.fulfill(path=F+"heebo-hebrew-900-normal.woff2",content_type="font/woff2")
        elif u.endswith("l900.woff2"): r.fulfill(path=F+"heebo-latin-900-normal.woff2",content_type="font/woff2")
        elif u.endswith("h700.woff2"): r.fulfill(path=F+"heebo-hebrew-700-normal.woff2",content_type="font/woff2")
        elif "/rest/v1/bees" in u: r.fulfill(status=200,body=open("bees.json").read(),content_type="application/json")
        elif "supabase.co" in u: r.fulfill(status=200,body="[]",content_type="application/json")
        elif u.startswith("http://test/"): r.fulfill(body=page_html,content_type="text/html")
        else: r.abort()
    pg.route("**/*",route); pg.goto("http://test/"); time.sleep(3)
    pg.evaluate(open("hook.js").read())
    pg.evaluate("document.head.insertAdjacentHTML('beforeend',`<style>"+open("ov.css").read().replace("`","")+"</style>`);document.body.insertAdjacentHTML('beforeend','<div id=my></div>')")
    for i in range(60): pg.evaluate("loop()")
    for n,s in enumerate(SHOTS):
        pg.evaluate("s=>{window.SHOT=s;document.getElementById('my').innerHTML=s.html||''}",s)
        for i in range(s.get("n",25)): pg.evaluate("loop()")
        if s.get("video"):
            vd=f"{OUT}/{s['video']}";os.makedirs(vd,exist_ok=True)
            for i in range(s["video_n"]):
                tl=[h for (t0,h) in s.get("tl",[]) if i/30>=t0]
                if tl: pg.evaluate("h=>{const m=document.getElementById('my');if(m.dataset.h!==h){m.dataset.h=h;m.innerHTML=h}}",tl[-1])
                pg.evaluate("loop()"); pg.screenshot(path=f"{vd}/f{i:04d}.jpg",type="jpeg",quality=90)
        else:
            pg.screenshot(path=f"{OUT}/{s.get('name','s%d'%n)}.jpg",type="jpeg",quality=92)
    print("errs",errs[:5]); b.close()
