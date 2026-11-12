"""סבתא מזל – reel 12.11 « אכלת משהו? » : gros plan, bol fumant, tour de 30 assiettes qui jaillit, boîte géante pour la route.
Usage : NOTEXT=1 DSF=1.5 NOSH=1 python3 tools/reel_akalt_1211.py <node_modules> <dossier> 2"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
R = '/home/claude/hasavta-shelanu'; FPS = 30; TOTAL = 12.0
os.makedirs(OUT, exist_ok=True)
FONTS = ''.join(f"@font-face{{font-family:Heebo;src:url(http://local/__f/heebo-{s}-{w}-normal.woff2);font-weight:{w}}}" for s in ('hebrew', 'latin') for w in (400, 800, 900))

EXTRA = r'''
{const {scene,camera,controls,SPOT,skyGroup,renderer}=window.__S;const SP=SPOT.clone();
 const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.7,emissive:e||0,emissiveIntensity:ei||0});
 // tour d'assiettes pleines
 const T=new THREE.Group();T.position.set(SP.x+.95,SP.y,SP.z+1.7);scene.add(T);
 const foods=[0xffb347,0xe8553f,0x7ccf5a,0xf5d76e,0xc8743a,0xff8fb8];const P=[];
 for(let i=0;i<30;i++){const g=new THREE.Group();const pl=new THREE.Mesh(new THREE.CylinderGeometry(.38,.3,.05,28),M(0xffffff));g.add(pl);
   const f=new THREE.Mesh(new THREE.SphereGeometry(.24,16,10),M(foods[i%6],foods[i%6],.08));f.scale.set(1,.28,1);f.position.y=.05;g.add(f);
   g.position.y=.09*i+.05;g.rotation.y=i*.7;g.position.x=Math.sin(i*1.7)*.03;g.visible=false;T.add(g);P.push(g)}
 // bol de soupe fumant (au début)
 const BW=new THREE.Group();const bw=new THREE.Mesh(new THREE.SphereGeometry(.42,24,12,0,Math.PI*2,Math.PI/2,Math.PI/2),new THREE.MeshStandardMaterial({color:0xff6b4a,emissive:0x501000,emissiveIntensity:.15,side:THREE.DoubleSide}));BW.add(bw);
 const soup=new THREE.Mesh(new THREE.CircleGeometry(.39,24),M(0xf2c14e,0x6a4000,.25));soup.rotation.x=-Math.PI/2;soup.position.y=-.03;BW.add(soup);
 const steam=[];for(let i=0;i<5;i++){const s=new THREE.Mesh(new THREE.SphereGeometry(.09,10,8),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.55}));BW.add(s);steam.push(s)}
 scene.add(BW);BW.visible=false;
 // énorme boîte « pour la route »
 const BX=new THREE.Group();const tb=new THREE.Mesh(new THREE.BoxGeometry(1.2,.7,.9),new THREE.MeshStandardMaterial({color:0xffffff,transparent:true,opacity:.55,roughness:.2}));BX.add(tb);
 const lid=new THREE.Mesh(new THREE.BoxGeometry(1.26,.12,.96),M(0x2f8cff,0x0a2a60,.2));lid.position.y=.41;BX.add(lid);
 for(let i=0;i<9;i++){const f=new THREE.Mesh(new THREE.SphereGeometry(.17,12,8),M(foods[i%6]));f.position.set(-.4+(i%3)*.4,-.18+Math.floor(i/3)*.16,-.2+((i*7)%3)*.2);BX.add(f)}
 scene.add(BX);BX.visible=false;
 window.BD={T,P,BW,steam,BX,SP};
 const ov=document.createElement('div');ov.id='ov';ov.style.cssText='position:fixed;inset:0;z-index:9999;pointer-events:none';document.body.appendChild(ov);
 const css=document.createElement('style');css.textContent=`body.cap *:not(canvas):not(#ov):not(#ov *){visibility:hidden}`;document.head.appendChild(css);
 ov.innerHTML='<div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div>';
}
'''

STEP = r'''o=>{const B=window.BD,S=B.SP,{camera,controls,skyGroup,renderer,scene}=window.__S;
 capHook(o.t+0.4);
 const W=window.__S;W.rc.visible=false;W.sgn.visible=false;W.tears.forEach(x=>x.visible=false);const C=W.getCit();(C.meshes||[]).forEach(m=>m.visible=false);(C.list||[]).forEach(p=>{if(p.sprite)p.sprite.visible=false;if(p.glow)p.glow.visible=false});
 B.P.forEach((p,i)=>{p.visible=i<o.np;if(i===o.np-1&&o.drop>0){p.position.y=.09*i+.05+o.drop}else p.position.y=.09*i+.05});
 B.T.rotation.z=Math.sin(o.t*5)*o.wob;
 B.BW.visible=o.bowl>0;if(o.bowl>0){B.BW.position.set(S.x+.75,S.y+1.7+o.bowl*.3,S.z+1.9);B.steam.forEach((s,i)=>{const u=((o.t*.6+i/5)%1);s.position.set(Math.sin(i*2+o.t*2)*.12,.1+u*.9,0);s.scale.setScalar(.6+u*1.4);s.material.opacity=.55*(1-u)})}
 B.BX.visible=o.box>=0;if(o.box>=0){B.BX.position.set(S.x-1.0,S.y+.35+o.box,S.z+1.4);B.BX.rotation.y=.4+o.box*.3}
 if(o.happy!=null)window.__S.setHappy(o.happy+0.4);
 camera.position.set(...o.cam);controls.target.set(...o.look);camera.lookAt(controls.target);skyGroup.position.copy(camera.position);
 document.getElementById('oF').style.opacity=o.flash;
 renderer.render(scene,camera)}'''

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)

HITS = [0.0, 1.39, 3.01, 5.19, 7.49, 9.93]
BIG = {3.01, 5.19}
def plan(t):
    o = dict(t=t, np=0, drop=0, wob=0, bowl=0, box=-1, happy=None)
    if t < 3.0:  # gros plan visage + bol fumant
        k = ease(t / 3.0); o.update(cam=lerp([0.5, 2.85, 14.3], [0.3, 2.75, 13.2], k), look=[0.1, 2.5, 10.7], bowl=.3 + .7 * ease(min(1, t / .6)))
        return o
    if t < 5.2:  # SURPRISE : la tour d'assiettes jaillit
        lt = t - 3.0; n = min(30, 1 + int(lt * 22)); k = ease(lt / 2.0)
        o.update(np=n, drop=.35 * max(0, 1 - ((lt * 22) % 1) * 2), wob=.02 * min(1, lt), cam=lerp([1.0, 2.5, 15.0], [1.6, 3.6, 17.6], k), look=lerp([0.7, 2.0, 11.6], [0.6, 2.2, 11.6], k))
        return o
    if t < 7.45:  # « une de plus pour la route » : la boîte géante tombe, Savta rit
        lt = t - 5.2; o.update(np=30, wob=.02, happy=5.2, box=max(0, 1.8 * (1 - ease(lt / .45))))
        o.update(cam=lerp([1.0, 3.2, 17.0], [0.2, 3.0, 16.2], ease(lt / 2.25)), look=[-0.1, 1.9, 11.4])
        return o
    lt = t - 7.45; o.update(np=30, wob=.015, box=0, happy=7.45 + 2.5 * int(lt / 2.5))
    a = lt * .07; o.update(cam=[0.2 + 4 * math.sin(a), 3.2 + lt * .15, 11.4 + 4.8 * math.cos(a) + lt * .2], look=[0, 1.9, 11.2])
    return o

def routes(pg):
    pg.route('https://**', lambda r: r.abort())
    pg.route('https://cdnjs.cloudflare.com/**', lambda r: r.fulfill(path=f'{NM}/three/build/three.min.js', content_type='text/javascript'))
    pg.route('https://cdn.jsdelivr.net/npm/three@0.128.0/**', lambda r: r.fulfill(path=f'{NM}/three/examples/js/controls/OrbitControls.js', content_type='text/javascript'))
    pg.route('https://fonts.googleapis.com/**', lambda r: r.fulfill(body=FONTS, content_type='text/css'))
    pg.route('https://*.supabase.co/**', lambda r: r.fulfill(status=200, body='[]', content_type='application/json'))
    def loc(r):
        p = r.request.url.split('http://local/')[1].split('?')[0].split('#')[0]
        if p.startswith('__f/'): return r.fulfill(path=f'{NM}/@fontsource/heebo/files/{p[4:]}')
        if p in ('', 'index.html'):
            h = open(f'{R}/index.html').read()
            h = h.replace('window.capHook = function(t){', 'window.__S={scene,camera,controls,SPOT,skyGroup,renderer,applyTime,setHappy:v=>{happyStart=v},rc:rainCloud,sgn:signMesh,tears,getCit:()=>cit};\nwindow.capHook = function(t){', 1)
            return r.fulfill(body=h, content_type='text/html')
        f = f'{R}/{p}'
        return r.fulfill(path=f) if os.path.isfile(f) else r.fulfill(status=404, body='')
    pg.route('http://local/**', loc)

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=float(os.environ.get('DSF','2'))); routes(pg)
        pg.add_init_script(("window.SHADOWS_OFF=true;" if os.environ.get("NOSH") else "")+"window.CAP=true;Math.random=(()=>{let s=4242;return()=>{s=(s*16807)%2147483647;return(s-1)/2147483646}})();")
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('http://local/index.html?cap=1'); pg.wait_for_timeout(5000)
        pg.evaluate("try{window.__S.applyTime(12.5)}catch(e){};if(window.SHADOWS_OFF)window.__S.renderer.shadowMap.enabled=false;0")
        pg.evaluate(EXTRA + ";0")
        pg.evaluate("window.requestAnimationFrame=()=>0;0"); pg.wait_for_timeout(500)
        if os.environ.get('NOTEXT'): pg.add_style_tag(content='#ov>div:not(#oF):not(#oD):not(#oV){display:none!important}')
        n = int(os.environ.get('MAXF') or round(TOTAL * FPS))
        idxs = [int(float(x)*FPS) for x in os.environ['TEST'].split(',')] if os.environ.get('TEST') else range(n)
        for i in idxs:
            if os.environ.get('TEST'): pass
            elif i % SAMPLE: continue
            if os.environ.get('RANGE'):
                _a,_b=map(float,os.environ['RANGE'].split(','))
                if not (_a <= i / FPS < _b): continue
            t = i / FPS
            o = plan(t)
            h = max([z for z in HITS if z <= t], default=-9); dt = t - h
            kick = math.exp(-dt * (5 if h in BIG else 9)) if dt < .4 else 0
            o.update(flash=kick * (.3 if h in BIG else 0))
            import time as _t; _a=_t.time(); pg.evaluate(STEP, o); _b=_t.time()
            pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
            if os.environ.get('MAXF'): print('eval %.1f shot %.1f'%(_b-_a,_t.time()-_b), flush=True)
        print('images', n, 'erreurs', errs[:5]); b.close()

main()
