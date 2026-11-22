"""סבתא מזל – פרק 2 (19.11) : « רגע! יש גם קינוח! » le סיר s'ouvre → gâteau géant 6 étages, bougies, « זה בשביל מי שלא מתקשר », דינג דונג, la porte s'ouvre (cliffhanger).
Usage : NOTEXT=1 DSF=1.2 NOSH=1 python3 tools/savta_p2_1911/film.py <node_modules> <dossier> 3"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
R = '/home/claude/hasavta-shelanu'; FPS = 30; TOTAL = 19.3
os.makedirs(OUT, exist_ok=True)
FONTS = ''.join(f"@font-face{{font-family:Heebo;src:url(http://local/__f/heebo-{s}-{w}-normal.woff2);font-weight:{w}}}" for s in ('hebrew', 'latin') for w in (400, 800, 900))

EXTRA = r"""
{const {scene,camera,controls,SPOT,skyGroup,renderer}=window.__S;const SP=SPOT.clone();
 const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.7,emissive:e||0,emissiveIntensity:ei||.08});
 const TY=SP.y+1.05, TZ=SP.z+0.2, X0=SP.x-1.3, LEN=70, N=60, DX=1.05;
 const T=new THREE.Group();scene.add(T);
 const top=new THREE.Mesh(new THREE.BoxGeometry(LEN,.08,1.7),M(0xfffaf0,0xfff3dd,.25));top.position.set(X0-LEN/2,TY,TZ);T.add(top);
 const skirt=new THREE.Mesh(new THREE.BoxGeometry(LEN,.55,1.72),M(0xd94c5a,0x5a0c14,.15));skirt.position.set(X0-LEN/2,TY-.3,TZ);T.add(skirt);
 const run=new THREE.Mesh(new THREE.BoxGeometry(LEN,.085,.38),M(0xffc24b,0xffc24b,.2));run.position.set(X0-LEN/2,TY+.005,TZ);T.add(run);
 const SEATS=[];const SH=[0xff5c8a,0x3fa7ff,0x52c96b,0xa77bff,0xff7a3d,0x2fd1c5,0xffc24b,0xe8432e];const HAIR=[0x3b2314,0x111111,0xc98a3c,0x6b3b1c,0xe0b060];
 const SK=[0xf3c9a5,0xe0ac80,0xc68d63,0x9a6a45];
 function kid(i){const g=new THREE.Group();const c=SH[i%SH.length];
   const b=new THREE.Mesh(new THREE.CylinderGeometry(.2,.26,.62,14),M(c,c,.12));b.position.y=.31;g.add(b);
   const h=new THREE.Mesh(new THREE.SphereGeometry(.22,16,12),M(SK[i%4]));h.position.y=.83;g.add(h);
   const hr=new THREE.Mesh(new THREE.SphereGeometry(.235,16,10,0,Math.PI*2,0,Math.PI/2.1),M(HAIR[i%5]));hr.position.y=.86;hr.rotation.x=-.25;g.add(hr);
   for(const s of[-1,1]){const e=new THREE.Mesh(new THREE.SphereGeometry(.035,8,6),M(0x111111));e.position.set(s*.08,.85,.2);g.add(e);
     const a=new THREE.Mesh(new THREE.CylinderGeometry(.06,.06,.45,8),M(c,c,.12));a.position.set(s*.25,.42,.1);a.rotation.x=-.9;g.add(a);g.userData['a'+s]=a}
   const m=new THREE.Mesh(new THREE.TorusGeometry(.06,.018,6,12,Math.PI),M(0x8a2020));m.position.set(0,.76,.205);m.rotation.z=Math.PI;g.add(m);
   g.scale.setScalar(1.25);return g}
 function chair(){const g=new THREE.Group();const s=new THREE.Mesh(new THREE.BoxGeometry(.55,.07,.55),M(0x8a5a2b));s.position.y=.62;g.add(s);
   const bk=new THREE.Mesh(new THREE.BoxGeometry(.55,.75,.07),M(0x8a5a2b));bk.position.set(0,1.0,-.26);g.add(bk);
   for(const [x,z] of [[-.23,-.23],[.23,-.23],[-.23,.23],[.23,.23]]){const l=new THREE.Mesh(new THREE.BoxGeometry(.05,.62,.05),M(0x6b4220));l.position.set(x,.31,z);g.add(l)}return g}
 function plate(){const g=new THREE.Group();const p=new THREE.Mesh(new THREE.CylinderGeometry(.2,.15,.03,20),M(0xffffff,0xffffff,.2));g.add(p);
   const f=new THREE.Mesh(new THREE.SphereGeometry(.11,10,8),M(0xffa64d,0x803300,.15));f.scale.y=.5;f.position.y=.03;g.add(f);return g}
 let k=0;for(let i=0;i<N;i++){for(const side of[-1,1]){const x=X0-.6-i*DX, z=TZ+side*1.2;
   const ch=chair();ch.position.set(x,SP.y,z);ch.rotation.y=side>0?Math.PI:0;T.add(ch);
   const pl=plate();pl.position.set(x,TY+.06,TZ+side*.55);T.add(pl);
   const kd=kid(k);kd.position.set(x,SP.y+.68,z+side*-.05);kd.rotation.y=side>0?Math.PI:0;kd.visible=false;T.add(kd);
   const glow=new THREE.Mesh(new THREE.CylinderGeometry(.32,.32,3.2,20,1,true),new THREE.MeshBasicMaterial({color:0xffd34d,transparent:true,opacity:0,side:THREE.DoubleSide,depthWrite:false}));glow.position.set(x,SP.y+.62+1.6,z);T.add(glow);
   SEATS.push({x,z,side,kd,glow,i});k++}}
 // marmite géante en bout de table, près de סבתא
 const POT=new THREE.Group();const body=new THREE.Mesh(new THREE.CylinderGeometry(.5,.44,.6,28),M(0xe8432e,0x5a0c00,.2));body.position.y=.3;POT.add(body);
 const GL=new THREE.Mesh(new THREE.CircleGeometry(.48,28),new THREE.MeshBasicMaterial({color:0xffd34d}));GL.rotation.x=-Math.PI/2;GL.position.y=.61;POT.add(GL);
 POT.position.set(X0-1.6,TY+.04,TZ-.15);T.add(POT);
 const LT=new THREE.PointLight(0xffd080,1.2,30);LT.position.set(X0-6,TY+4,TZ+3);scene.add(LT);
 window.BD={SEATS,SP,T,POT};
 const ov=document.createElement('div');ov.id='ov';ov.style.cssText='position:fixed;inset:0;z-index:9999;pointer-events:none';document.body.appendChild(ov);
 const css=document.createElement('style');css.textContent=`body.cap *:not(canvas):not(#ov):not(#ov *){visibility:hidden}`;document.head.appendChild(css);
 ov.innerHTML='<div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div>';
 console.log('SP',SP.x,SP.y,SP.z);
}
"""

STEP = r"""o=>{const B=window.BD,S=B.SP,{camera,controls,skyGroup,renderer,scene}=window.__S;
 capHook(o.t+0.4);
 const W=window.__S;W.rc.visible=false;W.sgn.visible=false;W.tears.forEach(x=>x.visible=false);const C=W.getCit();(C.meshes||[]).forEach(m=>m.visible=false);(C.list||[]).forEach(p=>{if(p.sprite)p.sprite.visible=false;if(p.glow)p.glow.visible=false});
 // o.seat : liste [index, phase 0..1 (arrivée), mode 0=assis/pop 1=course]
 B.SEATS.forEach(s=>{s.kd.visible=false;s.glow.material.opacity=0});
 for(const [j,ph,mode] of o.seat){const s=B.SEATS[j];if(!s||ph<=0)continue;s.kd.visible=true;const k=Math.min(1,ph);
   if(mode==1){const d=(1-k);s.kd.position.set(s.x-d*9,S.y+.68*k+Math.abs(Math.sin(ph*14))*.3*d,s.z);s.kd.rotation.y=d>0.02?Math.PI/2:(s.side>0?Math.PI:0);s.kd.scale.setScalar(1.25)}
   else{const pop=k<1?k*(1+.4*Math.sin(k*Math.PI)):1;s.kd.position.set(s.x,S.y+.68+(1-k)*.9,s.z);s.kd.rotation.y=s.side>0?Math.PI:0;s.kd.scale.setScalar(Math.max(.001,1.25*pop))}
   const sw=Math.sin(o.t*8+j)*.35;s.kd.userData['a-1'].rotation.x=-.9+sw;s.kd.userData['a1'].rotation.x=-.9-sw}
 for(const j of o.free){const s=B.SEATS[j];s.glow.material.opacity=.32+.12*Math.sin(o.t*6+j)}
 if(o.happy!=null)window.__S.setHappy(o.happy+0.4);
 if(!window.__F0)window.__F0=camera.fov;camera.fov=o.fov||window.__F0;camera.updateProjectionMatrix();camera.position.set(...o.cam);controls.target.set(...o.look);camera.lookAt(controls.target);skyGroup.position.copy(camera.position);
 document.getElementById('oF').style.opacity=o.flash;
 renderer.render(scene,camera)}"""

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)
import json as _j
HITS = [0.0, 2.13, 4.33, 5.73, 6.63, 7.12, 8.14, 8.78, 9.42, 10.02, 11.9, 13.86, 17.3]
BIG = {5.73, 10.02}
G0, G1 = [6, 3.4, 13], [5.2, 3.1, 12.6]; GL = [-12, 0.8, 10]
FACE_L = [0, 2.4, 10.6]
def seats(t):
    out = []
    if t >= 7.12: out.append([2, (t - 7.12) / .35, 0])
    for k, j in enumerate((4, 6, 8)):
        t0 = 8.78 + k * .12
        if t >= t0: out.append([j, (t - t0) / .35, 0])
    for k, j in enumerate(range(10, 30, 2)):
        t0 = 9.95 + k * .07
        if t >= t0: out.append([j, (t - t0) / 1.0, 1])
    return out
def plan(t):
    o = dict(t=t, seat=seats(t), free=[], happy=None, fov=None)
    def sh(t0, t1, c0, c1, l0, l1, fov=None):
        k = ease((t - t0) / (t1 - t0)); o.update(cam=lerp(c0, c1, k), look=lerp(l0, l1, k), fov=fov)
    if t < 2.13: sh(0, 2.13, G0, G1, GL, GL, 60); o['happy'] = 0
    elif t < 4.33: sh(2.13, 4.33, [-2, 2.7, 12.9], [-13, 2.7, 12.9], [-9, 1.0, 10.4], [-20, 1.0, 10.4], 60)
    elif t < 6.05: sh(4.33, 6.05, [0.6, 2.7, 14.2], [0.35, 2.6, 13.5], FACE_L, FACE_L)
    elif t < 8.14: sh(6.05, 8.14, [1.8, 2.9, 14.6], [1.4, 2.8, 14.0], [-1.8, 1.5, 10.4], [-2.2, 1.5, 10.4], 58)
    elif t < 9.42: sh(8.14, 9.42, [1.2, 3.0, 14.2], [0.6, 3.0, 14.0], [-3.2, 1.4, 10.4], [-3.8, 1.4, 10.4], 60)
    elif t < 11.9: sh(9.42, 11.9, [3.2, 4.4, 16.4], [2.6, 3.9, 15.4], [-5, 1.0, 10.2], [-5.5, 1.0, 10.2], 66); o['happy'] = 9.9 if t > 9.9 else None
    elif t < 13.86: sh(11.9, 13.86, [-1.0, 2.3, 15.6], [-1.6, 2.2, 15.0], [-3.6, 0.9, 12.0], [-4.0, 0.9, 12.0], 56); o['free'] = [1, 3, 5, 7, 9]
    elif t < 17.3: sh(13.86, 17.3, [0.55, 2.7, 14.5], [0.3, 2.6, 13.4], FACE_L, FACE_L)
    else: sh(17.3, 19.3, G1, G0, GL, GL, 60)
    if 9.9 <= t < 11.9 and o['happy'] is not None: o['happy'] = 9.9
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
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: print('LOG', m.text) if m.text.startswith('SP') else None)
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
