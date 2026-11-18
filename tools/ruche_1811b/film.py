"""Ruche 18.11 soir « פרק 1 : אותה שמלה » : filme un plan (meet | dress | look | crowd | close | end) du plateau 3D de la ruche, sans texte, à 10 i/s.
Usage : DSF=1.5 python3 film.py <dossier_sortie> <plan> <durée_s>"""
import sys, os, time
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
SP="/root"; T=SP+"/three3/node_modules/three/"; F=SP+"/three3/node_modules/@fontsource/heebo/files/"
src=open("/home/claude/hakaveret/index.html").read()
html=src.split("<body>",1)[1].rsplit("</body>",1)[0]
page_html="<!doctype html><html><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'></head><body>"+html+"</body></html>"
OUT,SHOT,DUR=sys.argv[1],sys.argv[2],float(sys.argv[3]); os.makedirs(OUT,exist_ok=True); FPS=10
with sync_playwright() as p:
    b=p.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"])
    pg=b.new_page(viewport={"width":540,"height":960},device_scale_factor=float(os.environ.get("DSF",1.5)))
    pg.add_init_script("window.CAP=true;Math.random=(()=>{let s=4242;return()=>{s=(s*16807)%2147483647;return(s-1)/2147483646}})();")
    errs=[]; pg.on("pageerror",lambda e: errs.append(str(e)))
    def route(r):
        u=r.request.url
        if "three.min.js" in u: r.fulfill(path=T+"build/three.min.js",content_type="text/javascript")
        elif "OrbitControls" in u: r.fulfill(path=T+"examples/js/controls/OrbitControls.js",content_type="text/javascript")
        elif "/rest/v1/bees" in u: r.fulfill(status=200,body=open(HERE+"/bees.json").read(),content_type="application/json")
        elif "supabase.co" in u: r.fulfill(status=200,body="[]",content_type="application/json")
        elif u.startswith("http://test/"): r.fulfill(body=page_html,content_type="text/html")
        else: r.abort()
    pg.route("**/*",route); pg.goto("http://test/"); time.sleep(3)
    pg.evaluate(open(HERE+"/hook.js").read())
    pg.evaluate("window.SH={shot:%r,t:0}"%SHOT)
    for i in range(int(os.environ.get("WARM",90))): pg.evaluate("loop()")
    for i in range(int(round(DUR*FPS))):
        pg.evaluate("t=>{window.SH.t=t;loop();loop();loop()}",i/FPS+float(os.environ.get("T0",0)))
        pg.screenshot(path=f"{OUT}/f{i:04d}.jpg",type="jpeg",quality=90)
    print(SHOT,"errs",errs[:5]); b.close()
