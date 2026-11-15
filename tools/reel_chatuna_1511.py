"""סבתא מזל – reel 15.11 « נו… מתי חתונה? » : gros plan, gâteau de mariage géant + bague + confettis.
Usage : NOTEXT=1 DSF=1.5 NOSH=1 python3 tools/reel_chatuna_1511.py <node_modules> <dossier> 2"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
R = '/home/claude/hasavta-shelanu'; FPS = 30; TOTAL = 7.5
os.makedirs(OUT, exist_ok=True)
FONTS = ''.join(f"@font-face{{font-family:Heebo;src:url(http://local/__f/heebo-{s}-{w}-normal.woff2);font-weight:{w}}}" for s in ('hebrew', 'latin') for w in (400, 800, 900))

EXTRA = r'''
{const {scene,camera,controls,SPOT,skyGroup,renderer}=window.__S;const SP=SPOT.clone();
 const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.55,emissive:e||0,emissiveIntensity:ei||0});
 // gâteau de mariage 3 étages + bague
 const CK=new THREE.Group();CK.position.set(SP.x+1.25,SP.y,SP.z+1.6);scene.add(CK);
 const tiers=[[.62,.42],[.46,.38],[.31,.34]];let y=0;
 tiers.forEach(([r,h],i)=>{const t=new THREE.Mesh(new THREE.CylinderGeometry(r,r,h,40),M(0xfff8f0,0xfff0e0,.25));t.position.y=y+h/2;CK.add(t);
   const band=new THREE.Mesh(new THREE.TorusGeometry(r+.005,.03,8,48),M(0xffc24b,0x8a5a00,.4));band.rotation.x=Math.PI/2;band.position.y=y+.06;CK.add(band);
   for(let k=0;k<10;k++){const p=new THREE.Mesh(new THREE.SphereGeometry(.045,10,8),M(0xff8fb8,0x701030,.25));const a=k/10*Math.PI*2+i;p.position.set(Math.cos(a)*(r+.01),y+h-.04,Math.sin(a)*(r+.01));CK.add(p)}
   y+=h});
 const RG=new THREE.Group();const ring=new THREE.Mesh(new THREE.TorusGeometry(.14,.035,12,40),M(0xffd36b,0xb07a00,.6));RG.add(ring);
 const gem=new THREE.Mesh(new THREE.OctahedronGeometry(.08),new THREE.MeshStandardMaterial({color:0xe8f6ff,emissive:0x9fdcff,emissiveIntensity:.9,roughness:.1,metalness:.3}));gem.position.y=.19;RG.add(gem);
 RG.position.y=y+.2;CK.add(RG);
 // confettis coeurs
 const CF=[];const cols=[0xff5c8a,0xffc24b,0xffffff,0xff8fb8,0x7fd4ff];
 for(let i=0;i<70;i++){const m=new THREE.Mesh(new THREE.PlaneGeometry(.07,.11),new THREE.MeshBasicMaterial({color:cols[i%5],side:THREE.DoubleSide}));m.userData={x:(Math.random()-.5)*3.2,z:(Math.random()-.5)*2.2,s:.6+Math.random()*.8,p:Math.random()*6};scene.add(m);m.visible=false;CF.push(m)}
 window.BD={CK,RG,CF,SP};
 const ov=document.createElement('div');ov.id='ov';ov.style.cssText='position:fixed;inset:0;z-index:9999;pointer-events:none';document.body.appendChild(ov);
 const css=document.createElement('style');css.textContent=`body.cap *:not(canvas):not(#ov):not(#ov *){visibility:hidden}`;document.head.appendChild(css);
 ov.innerHTML='<div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div>';
}
'''

STEP = r'''o=>{const B=window.BD,S=B.SP,{camera,controls,skyGroup,renderer,scene}=window.__S;
 capHook(o.t+0.4);
 const W=window.__S;W.rc.visible=false;W.sgn.visible=false;W.tears.forEach(x=>x.visible=false);const C=W.getCit();(C.meshes||[]).forEach(m=>m.visible=false);(C.list||[]).forEach(p=>{if(p.sprite)p.sprite.visible=false;if(p.glow)p.glow.visible=false});
 B.CK.visible=o.cake>0.001;B.CK.scale.setScalar(Math.max(.001,o.cake));B.CK.rotation.y=o.t*.5;
 B.RG.rotation.y=o.t*2.2;B.RG.position.y=1.34+.06*Math.sin(o.t*4);
 B.CF.forEach(m=>{m.visible=o.conf>=0;if(o.conf>=0){const u=m.userData;const fy=3.6-((o.conf*u.s+u.p*.4)%3.6);m.position.set(S.x+0.6+u.x+Math.sin(o.t*2+u.p)*.15,S.y+fy,S.z+1.7+u.z);m.rotation.set(o.t*3+u.p,o.t*2+u.p,0)}});
 if(o.happy!=null)window.__S.setHappy(o.happy+0.4);
 camera.position.set(...o.cam);controls.target.set(...o.look);camera.lookAt(controls.target);skyGroup.position.copy(camera.position);
 document.getElementById('oF').style.opacity=o.flash;
 renderer.render(scene,camera)}'''

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)

HITS = [0.0, 2.0, 2.6, 5.0]
BIG = {2.0}
def plan(t):
    o = dict(t=t, cake=0, conf=-1, happy=None)
    if t < 2.0:  # gros plan visage
        k = ease(t / 2.0); o.update(cam=lerp([0.5, 2.85, 14.1], [0.35, 2.78, 13.4], k), look=[0.1, 2.5, 10.7])
        return o
    if t < 4.6:  # SURPRISE : gâteau de mariage géant + confettis
        lt = t - 2.0; g = min(1, lt / .5); over = 1 + .18 * math.sin(min(1, lt / .9) * math.pi) * (1 - min(1, lt / .9))
        o.update(cake=1.3 * ease(g) * over, conf=lt, happy=2.0, cam=lerp([1.2, 2.9, 15.6], [1.0, 3.3, 16.8], ease(lt / 2.6)), look=lerp([0.7, 2.2, 11.6], [0.5, 2.1, 11.5], ease(lt / 2.6)))
        return o
    lt = t - 4.6; k = ease(lt / 2.9)
    o.update(cake=1.3, conf=2.6 + lt, happy=2.0 + 2.5 * int((t - 2.0) / 2.5), cam=lerp([1.0, 3.3, 16.8], [0.5, 2.85, 14.1], k), look=lerp([0.5, 2.1, 11.5], [0.1, 2.5, 10.7], k))
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
