"""סבתא מזל – פרק 2 (19.11) : « רגע! יש גם קינוח! » le סיר s'ouvre → gâteau géant 6 étages, bougies, « זה בשביל מי שלא מתקשר », דינג דונג, la porte s'ouvre (cliffhanger).
Usage : NOTEXT=1 DSF=1.2 NOSH=1 python3 tools/savta_p2_1911/film.py <node_modules> <dossier> 3"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
R = '/home/claude/hasavta-shelanu'; FPS = 30; TOTAL = 15.2
os.makedirs(OUT, exist_ok=True)
FONTS = ''.join(f"@font-face{{font-family:Heebo;src:url(http://local/__f/heebo-{s}-{w}-normal.woff2);font-weight:{w}}}" for s in ('hebrew', 'latin') for w in (400, 800, 900))

EXTRA = r"""
{const {scene,camera,controls,SPOT,skyGroup,renderer}=window.__S;const SP=SPOT.clone();
 const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.6,emissive:e||0,emissiveIntensity:ei||.05});
 // סיר (même que פרק 1)
 const POT=new THREE.Group();const body=new THREE.Mesh(new THREE.CylinderGeometry(.72,.62,.85,32,1,true),new THREE.MeshStandardMaterial({color:0xe8432e,emissive:0x5a0c00,emissiveIntensity:.2,roughness:.4,side:THREE.DoubleSide}));body.position.y=.43;POT.add(body);
 const bot=new THREE.Mesh(new THREE.CylinderGeometry(.62,.62,.04,32),M(0xc0331f));bot.position.y=.02;POT.add(bot);
 const band=new THREE.Mesh(new THREE.TorusGeometry(.72,.035,8,40),M(0xffffff,0xffffff,.2));band.rotation.x=Math.PI/2;band.position.y=.62;POT.add(band);
 for(const s of[-1,1]){const hd=new THREE.Mesh(new THREE.TorusGeometry(.13,.04,8,16,Math.PI),M(0x222222));hd.position.set(s*.8,.7,0);hd.rotation.z=s>0?-Math.PI/2:Math.PI/2;POT.add(hd)}
 const GL=new THREE.Mesh(new THREE.CircleGeometry(.7,32),new THREE.MeshBasicMaterial({color:0xffd34d}));GL.rotation.x=-Math.PI/2;GL.position.y=.8;POT.add(GL);
 const LID=new THREE.Group();const ld=new THREE.Mesh(new THREE.SphereGeometry(.76,32,10,0,Math.PI*2,0,Math.PI/5),M(0xd8dde6,0x666666,.25));ld.position.y=-.58;LID.add(ld);
 const kn=new THREE.Mesh(new THREE.SphereGeometry(.09,12,10),M(0x222222));kn.position.y=.05;LID.add(kn);POT.add(LID);
 const LT=new THREE.PointLight(0xffc640,0,7);LT.position.y=1.4;POT.add(LT);
 const RAYS=[];for(let i=0;i<10;i++){const r=new THREE.Mesh(new THREE.BoxGeometry(.05,1.8,.05),new THREE.MeshBasicMaterial({color:0xffe27a,transparent:true,opacity:0}));const a=i/10*Math.PI*2;r.position.set(Math.cos(a)*.55,1.6,Math.sin(a)*.55);r.rotation.set(Math.sin(a)*.4,0,-Math.cos(a)*.4);POT.add(r);RAYS.push(r)}
 const STM=[];for(let i=0;i<6;i++){const s=new THREE.Mesh(new THREE.SphereGeometry(.13,10,8),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.5}));POT.add(s);STM.push(s)}
 // עוגה ענקית : 6 קומות qui sortent du סיר
 const CK=new THREE.Group();POT.add(CK);const TI=[];const cols=[0xff8fb8,0xfff3e0,0xff8fb8,0xfff3e0,0xff8fb8,0xfff3e0];
 for(let i=0;i<6;i++){const g=new THREE.Group();const r=.62-.07*i;
   g.add(new THREE.Mesh(new THREE.CylinderGeometry(r,r,.32,36),M(cols[i],cols[i],.18)));
   const fr=new THREE.Mesh(new THREE.TorusGeometry(r,.045,8,36),M(0xffffff,0xffffff,.3));fr.rotation.x=Math.PI/2;fr.position.y=.16;g.add(fr);
   for(let j=0;j<8;j++){const a=j/8*Math.PI*2+i;const d=new THREE.Mesh(new THREE.SphereGeometry(.045,8,6),M([0xe8432e,0x3fa7ff,0x7ccf5a,0xffc24b][j%4],0,.1));d.position.set(Math.cos(a)*r,0,Math.sin(a)*r);g.add(d)}
   g.userData.y=.62+.32*i;CK.add(g);TI.push(g)}
 const CAN=[];for(let j=0;j<5;j++){const a=j/5*Math.PI*2;const c=new THREE.Group();c.add(new THREE.Mesh(new THREE.CylinderGeometry(.03,.03,.22,8),M(0x3fa7ff,0x3fa7ff,.3)));
   const fl=new THREE.Mesh(new THREE.SphereGeometry(.05,8,8),new THREE.MeshBasicMaterial({color:0xff8a1c}));fl.scale.set(1.5,2.6,1.5);fl.position.y=.2;c.add(fl);c.userData.fl=fl;
   c.position.set(Math.cos(a)*.16,.62+.32*5+.27,Math.sin(a)*.16);CK.add(c);CAN.push(c)}
 const CL=new THREE.PointLight(0xffb84d,0,4);CL.position.y=2.6;CK.add(CL);
 POT.position.set(SP.x-1.15,SP.y,SP.z+1.45);scene.add(POT);
 // הדלת : façade + porte qui s'ouvre + lumière + silhouette
 const DR=new THREE.Group();DR.position.set(SP.x+2.1,SP.y,SP.z+1.0);scene.add(DR);
 const wall=new THREE.Mesh(new THREE.BoxGeometry(2.6,3.0,.2),M(0xf2e2c4,0x332211,.08));wall.position.set(0,1.5,-.12);DR.add(wall);
 const hole=new THREE.Mesh(new THREE.PlaneGeometry(1.0,2.2),new THREE.MeshBasicMaterial({color:0x2a1a10}));hole.position.set(0,1.1,-.01);DR.add(hole);
 const LIT=new THREE.Mesh(new THREE.PlaneGeometry(1.0,2.2),new THREE.MeshBasicMaterial({color:0xfff6d8,transparent:true,opacity:0}));LIT.position.set(0,1.1,0);DR.add(LIT);
 for(const [w,h,x,y] of [[.14,2.4,-.57,1.2],[.14,2.4,.57,1.2],[1.28,.14,0,2.3]]){const f=new THREE.Mesh(new THREE.BoxGeometry(w,h,.16),M(0x6b3b1c));f.position.set(x,y,.02);DR.add(f)}
 const SIL=new THREE.Group();const sb=new THREE.Mesh(new THREE.CylinderGeometry(.22,.3,1.3,16),new THREE.MeshBasicMaterial({color:0x140c18}));sb.position.y=.75;SIL.add(sb);
 const sh=new THREE.Mesh(new THREE.SphereGeometry(.2,16,12),new THREE.MeshBasicMaterial({color:0x140c18}));sh.position.y=1.62;SIL.add(sh);SIL.position.set(.22,0,-.15);DR.add(SIL);
 const PIV=new THREE.Group();PIV.position.set(-.5,0,.05);DR.add(PIV);
 const pan=new THREE.Mesh(new THREE.BoxGeometry(1.0,2.2,.07),M(0x8a4a22,0x2a1206,.12));pan.position.set(.5,1.1,0);PIV.add(pan);
 const knb=new THREE.Mesh(new THREE.SphereGeometry(.05,10,8),M(0xffc24b,0xffc24b,.4));knb.position.set(.88,1.05,.06);PIV.add(knb);
 const bell=new THREE.Mesh(new THREE.CylinderGeometry(.07,.07,.04,16),M(0xffc24b,0xffc24b,.5));bell.rotation.x=Math.PI/2;bell.position.set(.8,1.3,.04);DR.add(bell);
 const DL=new THREE.SpotLight(0xfff0c0,0,8,.7,.5);DL.position.set(0,1.6,-.6);DL.target.position.set(0,0,3);DR.add(DL);DR.add(DL.target);
 window.BD={POT,LID,GL,LT,RAYS,STM,TI,CAN,CL,DR,PIV,LIT,SIL,DL,bell,SP};
 const ov=document.createElement('div');ov.id='ov';ov.style.cssText='position:fixed;inset:0;z-index:9999;pointer-events:none';document.body.appendChild(ov);
 const css=document.createElement('style');css.textContent=`body.cap *:not(canvas):not(#ov):not(#ov *){visibility:hidden}`;document.head.appendChild(css);
 ov.innerHTML='<div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div>';
 console.log('SP',SP.x,SP.y,SP.z);
}
"""

STEP = r"""o=>{const B=window.BD,S=B.SP,{camera,controls,skyGroup,renderer,scene}=window.__S;
 capHook(o.t+0.4);
 const W=window.__S;W.rc.visible=false;W.sgn.visible=false;W.tears.forEach(x=>x.visible=false);const C=W.getCit();(C.meshes||[]).forEach(m=>m.visible=false);(C.list||[]).forEach(p=>{if(p.sprite)p.sprite.visible=false;if(p.glow)p.glow.visible=false});
 B.POT.rotation.z=o.shk*Math.sin(o.t*41);
 B.LID.visible=o.lid<6;B.LID.position.set(-o.lid*.45,.85+o.lid*1.1,-o.lid*.2);B.LID.rotation.set(o.lid*1.3,o.lid*2,o.lid*.8);
 B.GL.visible=o.glow>0;B.LT.intensity=o.glow*3;B.RAYS.forEach((r,i)=>{r.material.opacity=o.glow*.55*(.6+.4*Math.sin(o.t*9+i))});
 B.STM.forEach((s,i)=>{const u=((o.t*.7+i/6)%1);s.position.set(Math.sin(i*2.1+o.t*2)*.25,.9+u*1.3,Math.cos(i*1.3)*.2);s.scale.setScalar(.6+u*1.6);s.material.opacity=o.stm*.5*(1-u)});
 B.TI.forEach((g,i)=>{const k=Math.max(0,Math.min(1,o.nt-i));g.visible=k>0;const pop=k<1?k*(1+.35*Math.sin(k*Math.PI)):1;g.scale.set(Math.max(.001,pop),Math.max(.001,k),Math.max(.001,pop));g.position.y=g.userData.y-(1-k)*.3;g.rotation.y=o.t*.3});
 B.CAN.forEach((c,i)=>{c.visible=o.nt>=5.99;c.userData.fl.visible=o.cand>i*.2;c.userData.fl.scale.set(1.5,2.4+.4*Math.sin(o.t*17+i),1.5)});B.CL.intensity=o.cand*2;
 B.DR.visible=o.door>0;B.DR.scale.setScalar(Math.max(.001,o.door));B.DR.rotation.z=o.dshk*Math.sin(o.t*47);
 B.PIV.rotation.y=-o.open*1.7;B.LIT.material.opacity=Math.min(1,o.open*2.5);B.SIL.visible=o.open>.05;B.DL.intensity=o.open*4;
 B.bell.material.emissiveIntensity=.5+o.ring*2;
 if(o.happy!=null)window.__S.setHappy(o.happy+0.4);
 camera.position.set(...o.cam);controls.target.set(...o.look);camera.lookAt(controls.target);skyGroup.position.copy(camera.position);
 document.getElementById('oF').style.opacity=o.flash;
 renderer.render(scene,camera)}"""

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)

# voix (coupée + atempo 1.24) : רגע 0 | הסיר רעד 1.6 | ומה יצא 2.65 | עוגה 3.35 | ועוד קומה 3.9 / 4.66 | והנרות 5.56 | זה לא יום הולדת 6.34 | בשביל מי שלא מתקשר 7.29 | דינג דונג 9.05 | מי בדלת 9.77 | אתם מחליטים 10.72 | אחת הנכד 11.59 | שתיים השכנה 12.65 | שלחו 13.65 | fin 14.93
HITS = [3.4, 3.95, 4.7, 5.6, 9.05, 10.62]
BIG = {3.4, 10.62}
FACE_C, FACE_L = [0.4, 2.6, 14.6], [0.1, 2.5, 10.7]
DOORC, DOORL = [2.2, 2.0, 15.0], [2.15, 1.4, 11.9]
def plan(t):
    o = dict(t=t, shk=0, lid=0, glow=0, stm=0, nt=0, cand=0, door=1, dshk=0, open=0, ring=0, happy=None)
    if t < 1.6:  # « רגע! יש גם קינוח! » : le couvercle saute, lumière dorée
        k = ease(t / 1.6)
        o.update(lid=(t + .3) ** 1.2 * 6, glow=min(1, .4 + t * 3), stm=.25, shk=.03 * max(0, 1 - t * 2), happy=0,
                 cam=lerp([-0.75, 2.35, 14.9], [-0.85, 2.3, 14.3], k), look=[-0.6, 1.65, 11.6])
        return o
    if t < 3.35:  # « הסיר רעד… ומה יצא? » : gros plan du סיר ouvert qui tremble
        k = ease((t - 1.6) / 1.75)
        o.update(lid=9, glow=1, stm=1, shk=.02 + .02 * k, happy=0,
                 cam=lerp([-1.1, 2.5, 15.0], [-1.1, 2.15, 14.3], k), look=[-1.05, 1.0, 12.4])
        return o
    if t < 5.56:  # « עוגה! ועוד קומה… ועוד קומה! »
        k = ease((t - 3.35) / 2.2)
        o.update(lid=9, glow=max(.3, 1 - (t - 3.35)), stm=.3, nt=min(6, 1.6 + max(0, t - 3.4) * 2.2) if t >= 3.4 else (t - 3.35) * 32,
                 cam=lerp([-1.2, 2.2, 15.4], [-0.5, 3.4, 18.2], k), look=lerp([-1.0, 1.4, 12.4], [-0.7, 2.1, 12.0], k), happy=3.35)
        return o
    if t < 6.34:  # « והנרות… » : gros plan des bougies qui s'allument
        k = ease((t - 5.56) / .78)
        o.update(lid=9, glow=.3, nt=6, cand=min(1, (t - 5.6) * 2), cam=lerp([-1.0, 3.6, 14.9], [-1.05, 3.45, 14.3], k), look=[-1.15, 2.85, 12.4], happy=3.35)
        return o
    if t < 9.05:  # « זה לא יום הולדת… בשביל מי שלא מתקשר » : gros plan visage
        k = ease((t - 6.34) / 2.7)
        o.update(lid=9, glow=.3, nt=6, cand=1, cam=lerp([0.0, 2.65, 15.0], [0.3, 2.6, 14.2], k), look=lerp([-0.2, 2.4, 10.7], FACE_L, k), happy=None)
        return o
    if t < 9.77:  # « דינג דונג! » : la caméra file vers la porte qui vibre
        k = ease((t - 9.05) / .45)
        o.update(lid=9, glow=.3, nt=6, cand=1, ring=max(0, 1 - (t - 9.05) * 1.5), dshk=.012,
                 cam=lerp([0.3, 2.6, 14.4], DOORC, k), look=lerp(FACE_L, DOORL, k))
        return o
    if t < 10.62:  # « מי בדלת?! » : la porte s'ouvre, lumière, silhouette → CLIFFHANGER
        k = ease((t - 9.77) / .85)
        o.update(lid=9, glow=.3, nt=6, cand=1, open=.8 * k, cam=lerp(DOORC, [2.2, 1.85, 14.3], k), look=DOORL)
        return o
    # fin : plan large סבתא + עוגה + porte entrouverte (silhouette), sans révélation
    k = ease((t - 10.62) / 4.5)
    o.update(lid=9, glow=.3, nt=6, cand=1, open=.8, cam=lerp([1.0, 2.9, 18.3], [1.0, 2.8, 17.6], k), look=[0.9, 1.75, 11.8])
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
