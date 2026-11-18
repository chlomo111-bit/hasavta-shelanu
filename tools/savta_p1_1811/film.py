"""סבתא מזל – פרק 1 « דברים שכל סבתא אומרת » (18.11) : « רק עוד ביס אחד! » cuillère vers la caméra, קציצות qui pleuvent, tour d'assiettes, סיר mystère (cliffhanger).
Usage : NOTEXT=1 DSF=1.2 NOSH=1 python3 tools/savta_p1_1811/film.py <node_modules> <dossier> 3"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
R = '/home/claude/hasavta-shelanu'; FPS = 30; TOTAL = 14.9
os.makedirs(OUT, exist_ok=True)
FONTS = ''.join(f"@font-face{{font-family:Heebo;src:url(http://local/__f/heebo-{s}-{w}-normal.woff2);font-weight:{w}}}" for s in ('hebrew', 'latin') for w in (400, 800, 900))

EXTRA = r"""
{const {scene,camera,controls,SPOT,skyGroup,renderer}=window.__S;const SP=SPOT.clone();
 const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.7,emissive:e||0,emissiveIntensity:ei||.05});
 const MB=()=>M(0x8a4a22,0x3a1a08,.12);
 const ball=r=>{const m=new THREE.Mesh(new THREE.SphereGeometry(r,16,12),MB());m.scale.y=.85;return m};
 // cuillère + קציצה
 const SPN=new THREE.Group();const h=new THREE.Mesh(new THREE.BoxGeometry(.05,.03,.7),M(0xd8dde6,0x888888,.2));h.position.z=-.38;SPN.add(h);
 const bw=new THREE.Mesh(new THREE.SphereGeometry(.13,16,10),M(0xe6ebf2,0x999999,.25));bw.scale.set(1,.35,1.3);SPN.add(bw);
 const kb=ball(.11);kb.position.y=.07;SPN.add(kb);scene.add(SPN);
 // assiette sur les genoux + קציצות qui tombent
 const PL=new THREE.Group();const pl=new THREE.Mesh(new THREE.CylinderGeometry(.5,.38,.06,32),M(0xffffff,0xffffff,.08));PL.add(pl);
 const rim=new THREE.Mesh(new THREE.TorusGeometry(.47,.025,8,32),M(0x3fa7ff,0x3fa7ff,.2));rim.rotation.x=Math.PI/2;rim.position.y=.03;PL.add(rim);
 const KS=[];const kp=[[-.15,.09,.05,.12],[.16,.09,-.04,.13],[0,.09,.18,.12],[0,.3,0,.3]];
 kp.forEach(p=>{const b=ball(p[3]);b.userData.p=p;PL.add(b);KS.push(b)});scene.add(PL);
 // tour d'assiettes pleines
 const T=new THREE.Group();T.position.set(SP.x+1.2,SP.y,SP.z+1.35);scene.add(T);
 const foods=[0xffb347,0xe8553f,0x7ccf5a,0xf5d76e,0x8a4a22,0xff8fb8];const P=[];
 for(let i=0;i<24;i++){const g=new THREE.Group();g.add(new THREE.Mesh(new THREE.CylinderGeometry(.42,.32,.05,28),M(0xffffff)));
   const f=new THREE.Mesh(new THREE.SphereGeometry(.26,16,10),M(foods[i%6],foods[i%6],.1));f.scale.set(1,.3,1);f.position.y=.05;g.add(f);
   g.userData.y=.1*i+.05;g.rotation.y=i*.7;g.position.x=Math.sin(i*1.7)*.04;T.add(g);P.push(g)}
 // סיר mystère
 const POT=new THREE.Group();const body=new THREE.Mesh(new THREE.CylinderGeometry(.72,.62,.85,32,1,true),new THREE.MeshStandardMaterial({color:0xe8432e,emissive:0x5a0c00,emissiveIntensity:.2,roughness:.4,side:THREE.DoubleSide}));body.position.y=.43;POT.add(body);
 const bot=new THREE.Mesh(new THREE.CylinderGeometry(.62,.62,.04,32),M(0xc0331f));bot.position.y=.02;POT.add(bot);
 const band=new THREE.Mesh(new THREE.TorusGeometry(.72,.035,8,40),M(0xffffff,0xffffff,.2));band.rotation.x=Math.PI/2;band.position.y=.62;POT.add(band);
 for(const s of[-1,1]){const hd=new THREE.Mesh(new THREE.TorusGeometry(.13,.04,8,16,Math.PI),M(0x222222));hd.position.set(s*.8,.7,0);hd.rotation.z=s>0?-Math.PI/2:Math.PI/2;POT.add(hd)}
 const GL=new THREE.Mesh(new THREE.CircleGeometry(.7,32),new THREE.MeshBasicMaterial({color:0xffd34d}));GL.rotation.x=-Math.PI/2;GL.position.y=.8;POT.add(GL);
 const LID=new THREE.Group();const ld=new THREE.Mesh(new THREE.SphereGeometry(.76,32,10,0,Math.PI*2,0,Math.PI/5),M(0xd8dde6,0x666666,.25));ld.position.y=-.58;LID.add(ld);
 const kn=new THREE.Mesh(new THREE.SphereGeometry(.09,12,10),M(0x222222));kn.position.y=.05;LID.add(kn);LID.position.y=.85;POT.add(LID);
 const LT=new THREE.PointLight(0xffc640,0,6);LT.position.y=1.2;POT.add(LT);
 const RAYS=[];for(let i=0;i<10;i++){const r=new THREE.Mesh(new THREE.BoxGeometry(.05,1.8,.05),new THREE.MeshBasicMaterial({color:0xffe27a,transparent:true,opacity:0}));const a=i/10*Math.PI*2;r.position.set(Math.cos(a)*.55,1.6,Math.sin(a)*.55);r.rotation.set(Math.sin(a)*.4,0,-Math.cos(a)*.4);POT.add(r);RAYS.push(r)}
 const STM=[];for(let i=0;i<6;i++){const s=new THREE.Mesh(new THREE.SphereGeometry(.13,10,8),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.5}));POT.add(s);STM.push(s)}
 POT.position.set(SP.x-1.15,SP.y,SP.z+1.45);scene.add(POT);
 window.BD={SPN,PL,KS,T,P,POT,LID,GL,LT,RAYS,STM,SP};
 const ov=document.createElement('div');ov.id='ov';ov.style.cssText='position:fixed;inset:0;z-index:9999;pointer-events:none';document.body.appendChild(ov);
 const css=document.createElement('style');css.textContent=`body.cap *:not(canvas):not(#ov):not(#ov *){visibility:hidden}`;document.head.appendChild(css);
 ov.innerHTML='<div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div>';
 console.log('SP',SP.x,SP.y,SP.z);
}
"""

STEP = r"""o=>{const B=window.BD,S=B.SP,{camera,controls,skyGroup,renderer,scene}=window.__S;
 capHook(o.t+0.4);
 const W=window.__S;W.rc.visible=false;W.sgn.visible=false;W.tears.forEach(x=>x.visible=false);const C=W.getCit();(C.meshes||[]).forEach(m=>m.visible=false);(C.list||[]).forEach(p=>{if(p.sprite)p.sprite.visible=false;if(p.glow)p.glow.visible=false});
 B.SPN.visible=!!o.spn;if(o.spn){B.SPN.position.set(...o.spn);B.SPN.lookAt(camera.position);B.SPN.rotateY(Math.PI);B.SPN.rotateZ(.15*Math.sin(o.t*7));B.SPN.scale.setScalar(1.5)}
 B.PL.visible=o.pl>0;B.PL.position.set(S.x+.08,1.45,11.55);B.PL.scale.setScalar(Math.max(.001,o.pl));
 B.KS.forEach((b,i)=>{const p=b.userData.p,d=o.kt[i];b.visible=d>0;if(d>0){const f=Math.max(0,1-d/.35);const bo=d>.35?Math.exp(-(d-.35)*8)*Math.abs(Math.sin((d-.35)*20))*.08:0;b.position.set(p[0],p[1]+f*f*2.2+bo,p[2])}});
 B.P.forEach((g,i)=>{const k=Math.max(0,Math.min(1,o.np-i));g.visible=k>0;g.position.y=g.userData.y+(1-k)*1.4;g.scale.setScalar(.001+k*(1+.2*Math.sin(k*Math.PI)))});
 B.T.rotation.z=o.wob*Math.sin(o.t*5);
 B.POT.visible=o.pot>0;B.POT.scale.setScalar(Math.max(.001,o.pot));B.POT.rotation.z=o.shk*Math.sin(o.t*41);
 B.LID.position.y=.85+o.lid;B.LID.rotation.z=o.shk*2*Math.sin(o.t*53);B.LID.rotation.x=o.lid*.6;
 B.GL.visible=o.glow>0;B.LT.intensity=o.glow*3;B.RAYS.forEach((r,i)=>{r.material.opacity=o.glow*.55*(.6+.4*Math.sin(o.t*9+i))});
 B.STM.forEach((s,i)=>{const u=((o.t*.7+i/6)%1);s.position.set(Math.sin(i*2.1+o.t*2)*.25,.9+u*1.3,Math.cos(i*1.3)*.2);s.scale.setScalar(.6+u*1.6);s.material.opacity=o.stm*.5*(1-u)});
 if(o.happy!=null)window.__S.setHappy(o.happy+0.4);
 camera.position.set(...o.cam);controls.target.set(...o.look);camera.lookAt(controls.target);skyGroup.position.copy(camera.position);
 document.getElementById('oF').style.opacity=o.flash;
 renderer.render(scene,camera)}"""

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)

# voix (après coupe) : ביס 0 | עור ועצמות 1.44 | קציצה 4.02 | ועוד 5.02 | ועוד! 5.85 | שבעתם 6.67 | רגע 7.8 | לא הולכים 8.61 | סבתא הכינה 10.0 | עוד משהו 10.78 | החלטה 11.31 | שלחו 13.12
HITS = [0.0, 4.15, 5.15, 6.0, 7.04, 8.7, 11.45]
BIG = {6.0, 11.45}
FACE_C, FACE_L = [0.4, 2.6, 14.6], [0.1, 2.5, 10.7]
def plan(t):
    o = dict(t=t, spn=None, pl=0, kt=[0, 0, 0, 0], np=0, wob=0, pot=0, lid=0, shk=0, glow=0, stm=0, happy=None)
    kt = lambda: [max(0, t - x) if t >= x else 0 for x in (4.02, 5.02, 5.0, 5.85)]
    if t < 1.44:  # cuillère qui fonce vers la caméra
        k = ease(t / 1.44)
        cam = lerp([0.4, 2.6, 14.1], [0.33, 2.58, 13.8], k)
        o.update(cam=cam, look=FACE_L, happy=0, spn=lerp([0.15, 2.0, 12.0], [0.32, 2.42, 13.15], ease(min(1, (t + .35) / 1.6))))
        return o
    if t < 4.02:  # elle rit, assiette sur les genoux
        k = ease((t - 1.44) / 2.6)
        o.update(cam=lerp([1.4, 2.4, 14.3], [0.9, 2.3, 13.9], k), look=[0.1, 1.9, 11.0], pl=1, happy=1.44, kt=[0, 0, 0, 0])
        return o
    if t < 6.67:  # קציצות qui tombent, la géante à 5.85
        k = ease((t - 4.02) / 2.65)
        o.update(cam=lerp([0.3, 2.6, 13.6], [0.6, 2.9, 14.6], k), look=[0.1, 1.75, 11.4], pl=1, kt=kt(), happy=1.44)
        return o
    if t < 7.8:  # « שבעתם?! » : la tour d'assiettes jaillit
        lt = t - 6.67
        o.update(cam=lerp([-0.6, 2.7, 15.8], [-0.9, 3.4, 17.4], ease(lt / 1.13)), look=[0.6, 2.6, 11.6], pl=1, kt=kt(), np=min(24, max(0, (t - 6.9) * 30)), wob=.04, happy=6.67)
        return o
    if t < 10.0:  # « רגע… לא הולכים לשום מקום » : gros plan visage puis le סיר monte
        lt = t - 7.8
        o.update(np=24, wob=.02, pl=1, kt=kt(), pot=ease((t - 8.6) / .5) * (1 + .15 * math.sin(max(0, t - 8.6) * 9) * math.exp(-max(0, t - 9.1) * 4)) if t > 8.6 else 0,
                 cam=lerp([0.35, 2.6, 14.2], [-1.6, 2.6, 15.6], ease((lt - .7) / 1.5)), look=lerp(FACE_L, [-0.5, 1.9, 11.4], ease((lt - .7) / 1.5)), happy=7.8, stm=.4)
        return o
    if t < 11.5:  # CLIFFHANGER : gros plan du סיר, couvercle qui tremble, lumière dorée, il se soulève…
        lt = t - 10.0; k = ease(lt / 1.5)
        P = [-1.05, 0, 12.5]
        o.update(np=24, pl=1, kt=kt(), pot=1, shk=.02 + .03 * k, lid=max(0, (t - 10.75) * .22), glow=ease((t - 10.6) / .8), stm=1,
                 cam=lerp([-1.1, 2.4, 15.2], [-1.1, 2.25, 14.6], k), look=[-1.05, 1.0, 12.4], happy=10.0)
        return o
    # fin : on revient sur סבתא + le סיר fermé qui tremble (pas de révélation)
    lt = t - 11.5; k = ease(lt / 3.3)
    o.update(np=24, pl=1, kt=kt(), pot=1, shk=.03, lid=0, glow=.35, stm=1, happy=11.5,
             cam=lerp([-1.4, 2.8, 16.2], [-0.9, 2.7, 15.4], k), look=[-0.3, 2.0, 11.3])
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
