"""סבתא מזל – reel 17.11 « תלבש סוודר! » : gros plan, un pull qui vole vers elle, puis tour de pulls géante.
Usage : NOTEXT=1 DSF=1.5 NOSH=1 python3 tools/reel_sveder_1711.py <node_modules> <dossier> 2"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
R = '/home/claude/hasavta-shelanu'; FPS = 30; TOTAL = 7.6
os.makedirs(OUT, exist_ok=True)
FONTS = ''.join(f"@font-face{{font-family:Heebo;src:url(http://local/__f/heebo-{s}-{w}-normal.woff2);font-weight:{w}}}" for s in ('hebrew', 'latin') for w in (400, 800, 900))

EXTRA = r"""
{const {scene,camera,controls,SPOT,skyGroup,renderer}=window.__S;const SP=SPOT.clone();
 const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.8,emissive:e||0,emissiveIntensity:ei||.06});
 const COLS=[[0xff5c8a,0xffd1e0],[0x3fa7ff,0xffffff],[0xffc24b,0xff6b3d],[0x52c96b,0xfff3c4],[0xa77bff,0xffc24b],[0xff7a3d,0xffffff],[0x2fd1c5,0xff5c8a]];
 function sweater(i){const [c1,c2]=COLS[i%COLS.length];const g=new THREE.Group();
   const body=new THREE.Mesh(new THREE.BoxGeometry(.62,.62,.13),M(c1,c1));g.add(body);
   for(const yy of[-.12,.12]){const st=new THREE.Mesh(new THREE.BoxGeometry(.635,.07,.14),M(c2,c2));st.position.y=yy;g.add(st)}
   for(const sx of[-1,1]){const sl=new THREE.Mesh(new THREE.BoxGeometry(.5,.17,.13),M(c1,c1));sl.position.set(sx*.5,.12,0);sl.rotation.z=sx*-.75;g.add(sl);
     const cf=new THREE.Mesh(new THREE.BoxGeometry(.08,.19,.14),M(c2,c2));cf.position.set(sx*.69,-.09,0);cf.rotation.z=sx*-.75;g.add(cf)}
   const col=new THREE.Mesh(new THREE.TorusGeometry(.12,.045,8,20),M(c2,c2));col.position.y=.3;col.rotation.x=Math.PI/2;g.add(col);
   const hrt=new THREE.Mesh(new THREE.BoxGeometry(.12,.12,.14),M(0xffffff,0xffffff,.3));hrt.rotation.z=Math.PI/4;g.add(hrt);
   return g}
 function folded(i){const [c1,c2]=COLS[i%COLS.length];const g=new THREE.Group();
   const b=new THREE.Mesh(new THREE.BoxGeometry(.95,.17,.62),M(c1,c1));g.add(b);
   const st=new THREE.Mesh(new THREE.BoxGeometry(.97,.05,.64),M(c2,c2));st.position.y=.02;g.add(st);
   const sl=new THREE.Mesh(new THREE.BoxGeometry(.2,.175,.63),M(c2,c2));sl.position.x=.3;g.add(sl);return g}
 const FL=sweater(0);scene.add(FL);
 const TW=new THREE.Group();TW.position.set(SP.x+1.2,SP.y,SP.z+1.35);scene.add(TW);const ST=[];
 for(let i=0;i<16;i++){const f=folded(i+1);f.position.y=.09+i*.175;f.rotation.y=(Math.random()-.5)*.35;f.userData.r=f.rotation.y;TW.add(f);ST.push(f)}
 const TOP=sweater(3);TW.add(TOP);
 window.BD={FL,TW,ST,TOP,SP};
 const ov=document.createElement('div');ov.id='ov';ov.style.cssText='position:fixed;inset:0;z-index:9999;pointer-events:none';document.body.appendChild(ov);
 const css=document.createElement('style');css.textContent=`body.cap *:not(canvas):not(#ov):not(#ov *){visibility:hidden}`;document.head.appendChild(css);
 ov.innerHTML='<div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div>';
}
"""

STEP = r"""o=>{const B=window.BD,S=B.SP,{camera,controls,skyGroup,renderer,scene}=window.__S;
 capHook(o.t+0.4);
 const W=window.__S;W.rc.visible=false;W.sgn.visible=false;W.tears.forEach(x=>x.visible=false);const C=W.getCit();(C.meshes||[]).forEach(m=>m.visible=false);(C.list||[]).forEach(p=>{if(p.sprite)p.sprite.visible=false;if(p.glow)p.glow.visible=false});
 B.FL.position.set(...o.fl);B.FL.rotation.set(o.flr[0],o.flr[1],o.flr[2]);B.FL.scale.setScalar(o.fls);
 const n=o.n;B.ST.forEach((f,i)=>{const k=Math.max(0,Math.min(1,n-i));f.visible=k>0;const d=(1-k);f.position.y=.09+i*.175+d*1.6;f.scale.setScalar(.001+k*(1+.25*Math.sin(k*Math.PI)));f.rotation.y=f.userData.r+Math.sin(o.t*3+i)*.04*(i/16)});
 const top=Math.max(0,Math.min(16,Math.floor(n)));B.TOP.visible=n>=16.5;B.TOP.position.set(0,.2+16*.175+.35,0);B.TOP.rotation.y=o.t*1.5;B.TOP.scale.setScalar(Math.min(1.4,Math.max(.001,(n-16.5)*2)));
 B.TW.rotation.z=.05*Math.sin(o.t*2.3)*Math.min(1,n/16);
 if(o.happy!=null)window.__S.setHappy(o.happy+0.4);
 camera.position.set(...o.cam);controls.target.set(...o.look);camera.lookAt(controls.target);skyGroup.position.copy(camera.position);
 document.getElementById('oF').style.opacity=o.flash;
 renderer.render(scene,camera)}"""

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)

HITS = [0.0, 0.7, 1.9, 4.2]
BIG = {1.9}
HIDE = [0, -30, 0]
def plan(t):
    o = dict(t=t, n=0, happy=None, fl=HIDE, flr=[0, 0, 0], fls=1)
    if t < 1.9:  # gros plan visage + un pull qui vole vers elle (visible dès l'image 0)
        k = ease(t / 1.9); kf = ease(min(1, (t + .25) / .95))
        o.update(cam=lerp([0.45, 2.6, 15.0], [0.32, 2.55, 14.3], k), look=[0.1, 2.5, 10.7],
                 fl=lerp([0.75, 2.2, 13.2], [0.08, 1.42, 11.45], kf), flr=[0.15, -0.4 * (1 - kf), 0.9 * (1 - kf) + .05 * math.sin(t * 6)], fls=1.25)
        return o
    if t < 4.6:  # SURPRISE : la tour de pulls monte à côté d'elle
        lt = t - 1.9
        o.update(n=min(17.2, lt * 8.5), happy=1.9, fl=[0.08, 1.42, 11.45], flr=[0.15, 0, .05 * math.sin(t * 6)],
                 cam=lerp([-0.5, 2.5, 15.6], [-0.9, 3.5, 17.6], ease(lt / 2.7)), look=lerp([0.55, 2.2, 11.4], [0.6, 2.9, 11.6], ease(lt / 2.7)))
        return o
    lt = t - 4.6; k = ease(lt / 2.6)
    o.update(n=17.2, happy=1.9 + 2.5 * int((t - 1.9) / 2.5), fl=[0.08, 1.42, 11.45], flr=[0.15, 0, .05 * math.sin(t * 6)],
             cam=lerp([-0.9, 3.5, 17.6], [0.45, 2.6, 15.0], k), look=lerp([0.6, 2.9, 11.6], [0.1, 2.5, 10.7], k))
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
