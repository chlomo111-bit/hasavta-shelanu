"""השכנים – épisode 4 (10.11) « העקבות הלבנות » : on frappe chez Dana en pleine nuit, personne derrière la porte,
seulement de petites traces blanches qui mènent à l'appartement d'Avi. Vote 1 (elle entre) / 2 (elle s'enfuit).
Voix Juniper (eleven_v4, 29 s), découpage mot à mot. Décor 3D en cubes construit ici (Three.js r128), personnages cubes
de thenoise/tools/film3d.py (mkChar).
Usage : python3 tools/hashchenim_ep4.py <node_modules> <dossier_images> [échantillon]"""
import sys, os, re, math, base64
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
FPS = 30; TOTAL = 29.6
os.makedirs(OUT, exist_ok=True)
CHAR_JS = re.search(r"CHAR_JS = r'''(.*?)'''", open('/home/claude/thenoise/tools/film3d.py').read(), re.S).group(1)
F = f'{NM}/@fontsource/heebo/files/'
b64 = lambda p: base64.b64encode(open(p, 'rb').read()).decode()

HTML = f"""<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:Heebo;font-weight:900;src:url(data:font/woff2;base64,{b64(F+'heebo-hebrew-900-normal.woff2')})}}
@font-face{{font-family:Heebo;font-weight:900;src:url(data:font/woff2;base64,{b64(F+'heebo-latin-900-normal.woff2')});unicode-range:U+0000-00FF}}
html,body{{margin:0;background:#000;overflow:hidden}}canvas{{display:block}}
#ov{{position:fixed;inset:0;pointer-events:none;font-family:Heebo;direction:rtl}}
.t{{position:absolute;left:0;right:0;text-align:center;color:#fff;text-shadow:0 4px 18px rgba(0,0,0,.9);padding:0 16px}}
.y{{color:#FFC24B}}.w{{color:#BFEFFF}}
@keyframes pop{{0%{{transform:scale(.5);opacity:0}}60%{{transform:scale(1.1);opacity:1}}100%{{transform:scale(1)}}}}.pop{{animation:pop .28s ease-out both}}
.box{{display:inline-block;background:rgba(12,10,30,.78);border-radius:24px;padding:10px 24px}}
</style></head><body>
<div id=ov><div id=oD style="position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,0,0,0) 40%,rgba(0,0,20,.65) 100%)"></div>
<div class=t id=oT style="top:9%"></div><div class=t id=oM style="top:36%"></div><div class=t id=oB style="bottom:12%"></div>
<div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div>
<div style="position:absolute;top:3%;right:4%;background:rgba(12,10,30,.75);border:2px solid #C792EA;border-radius:999px;padding:4px 14px;font:900 14px Heebo;color:#fff">🏢 השכנים · פרק 4</div></div>
<script src="http://local/three.min.js"></script><script>{CHAR_JS}</script><script>
const R=new THREE.WebGLRenderer({{antialias:true,preserveDrawingBuffer:true}});R.setPixelRatio(2);R.setSize(540,960);R.shadowMap.enabled=true;document.body.prepend(R.domElement);
const scene=new THREE.Scene();scene.background=new THREE.Color(0x0b0a1e);scene.fog=new THREE.Fog(0x0b0a1e,18,60);
const camera=new THREE.PerspectiveCamera(62,540/960,.05,200);
scene.add(new THREE.HemisphereLight(0x8fa0ff,0x201030,.55));
const M=(c,e,ei)=>new THREE.MeshStandardMaterial({{color:c,roughness:.85,emissive:e||0,emissiveIntensity:ei||0}});
const box=(w,h,d,m,x,y,z,p)=>{{const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);b.position.set(x,y,z);b.castShadow=b.receiveShadow=true;(p||scene).add(b);return b}};
// ---- couloir de l'immeuble (axe x), portes côté z=-1.6 ----
const floorM=M(0x3a2f4a),wallM=M(0xd9c7a7),wall2=M(0xb9a684),doorM=M(0x6b3e1f),doorM2=M(0x2f5d8a);
box(30,.2,4,floorM,0,-.1,0);for(let i=-7;i<8;i++)box(1.9,.02,3.6,M(i%2?0x46395a:0x3e3252),i*2,.02,0);
box(30,4,.2,wallM,0,2,-1.7);box(30,4,.2,wall2,0,2,1.9);box(30,.2,4,M(0x2a2238),0,4.05,0);
const doors={{}};[['דנה',-4,doorM,'7'],['אבי',6,doorM2,'9'],['',-10,doorM,'5'],['',1,doorM,'8'],['',11,doorM,'10']].forEach(([n,x,m,num])=>{{
  const piv=new THREE.Group();piv.position.set(x-.6,0,-1.55);scene.add(piv);box(1.2,2.4,.1,m,.6,1.2,0,piv);box(.12,.12,.12,M(0xFFC24B,0xFFC24B,.6),1.05,1.15,.1,piv);
  box(1.45,.15,.12,M(0x2a1a0e),x,2.48,-1.55);
  const c=document.createElement('canvas');c.width=256;c.height=128;const g=c.getContext('2d');g.fillStyle='#f3e6c8';g.fillRect(0,0,256,128);g.fillStyle='#2a1a0e';g.font='900 64px Heebo';g.textAlign='center';g.textBaseline='middle';g.fillText(n?num+' · '+n:num,128,68);
  const pl=new THREE.Mesh(new THREE.PlaneGeometry(.7,.35),new THREE.MeshBasicMaterial({{map:new THREE.CanvasTexture(c)}}));pl.position.set(.6,1.85,.07);piv.add(pl);
  doors[n||x]={{piv,x}}}});
// lampes du couloir (faibles, nuit)
const lamps=[];[-8,-2,4,10].forEach(x=>{{box(.6,.08,.6,M(0xfff2c0,0xfff2c0,1),x,3.95,0);const l=new THREE.PointLight(0xffd9a0,.55,7,2);l.position.set(x,3.6,0);l.castShadow=x===-2||x===4;scene.add(l);lamps.push(l)}});
const moon=new THREE.DirectionalLight(0x6c7cff,.35);moon.position.set(-5,8,6);scene.add(moon);
// traces blanches de Dana → Avi
const steps=[];const SW=new THREE.MeshBasicMaterial({{color:0xffffff,transparent:true,opacity:0}});
for(let i=0;i<16;i++){{const x=-3.4+i*.6,z=-.9+(i%2?.18:-.18);const g=new THREE.Group();g.position.set(x,.04,z);scene.add(g);
  [[0,0,.16,.22],[.13,.06,.07,.07],[.13,-.06,.07,.07]].forEach(([dx,dz,w,d])=>{{const m=new THREE.Mesh(new THREE.BoxGeometry(w,.015,d),SW);m.position.set(dx,0,dz);g.add(m)}});steps.push(g)}}
const halo=new THREE.PointLight(0xbfefff,0,4,2);halo.position.set(6,.6,-.8);scene.add(halo);
// Dana (pull rouge, cheveux longs bruns) et l'enveloppe
const dana=mkChar({{shirt:0xE5484D,hair:0x2a160c,long:true,skin:0xf1c7a2,ph:.4}});scene.add(dana.g);
const ENV=new THREE.Group();box(.5,.02,.34,M(0xf3e6c8,0xf3e6c8,.2),0,0,0,ENV);box(.08,.03,.08,M(0xa50f17,0x5a0006,.4),0,.02,0,ENV);scene.add(ENV);ENV.visible=false;
// façade de l'immeuble (plan extérieur)
const EXT=new THREE.Group();EXT.position.set(0,0,-40);scene.add(EXT);
box(14,18,6,M(0xcbb38c),0,9,0,EXT);box(40,.2,30,M(0x1c1a2a),0,0,0,EXT);
const winOn=M(0xffd98a,0xffb347,1.2),winOff=M(0x1a2236);const WIN=[];
for(let f=0;f<5;f++)for(let k=0;k<4;k++){{const w=box(1.6,1.6,.1,winOff,-4.8+k*3.2,2.6+f*3.2,3.06,EXT);WIN.push(w)}}
const ROOF=new THREE.Mesh(new THREE.BoxGeometry(14.4,.4,6.4),M(0x5a4a6a));ROOF.position.set(0,18.2,0);EXT.add(ROOF);
const stars=new THREE.Points(new THREE.BufferGeometry().setAttribute('position',new THREE.Float32BufferAttribute(Array.from({{length:900}},(_,i)=>i%3==1?20+Math.random()*40:(Math.random()-.5)*160),3)),new THREE.PointsMaterial({{color:0xffffff,size:.25}}));stars.position.z=-60;scene.add(stars);
window.S={{dana,doors,steps,SW,halo,ENV,EXT,WIN,winOn,winOff,lamps}};
let last='';
window.F=function(o){{const t=o.t;
  camera.position.set(...o.cam);camera.lookAt(...o.look);
  dana.g.visible=!!o.dana;if(o.dana){{dana.g.position.set(...o.dana);dana.g.rotation.y=o.dry;animChar(dana,t,0,'talk');if(o.scared){{dana.aL.rotation.x=-2.2;dana.aR.rotation.x=-2.2}}}}
  ENV.visible=!!o.env;if(o.env){{ENV.position.set(dana.g.position.x+.35,1.25,dana.g.position.z+.45);ENV.rotation.set(.9,Math.sin(t)*.2,0)}}
  doors['דנה'].piv.rotation.y=-o.open*1.4;doors['דנה'].piv.position.z=-1.55+(o.knock?Math.sin(t*60)*.02*o.knock:0);
  doors['אבי'].piv.rotation.y=-(o.avi||0)*.25;
  SW.opacity=o.steps;halo.intensity=o.steps*1.4+(o.avi?1.5:0);
  lamps.forEach((l,i)=>l.intensity=.55*(o.flick&&Math.sin(t*37+i*3)>.6?.2:1));
  WIN.forEach((w,i)=>w.material=((i*7+3)%5<2||i===9)?winOn:winOff);
  R.render(scene,camera);
  if(o.key!==last){{last=o.key;oT.innerHTML=o.top;oM.innerHTML=o.mid;oB.innerHTML=o.bot}}oF.style.opacity=o.flash}};
window.ready=true;
</script></body></html>"""

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)
Y = lambda s: f'<span class=y>{s}</span>'
W = lambda s: f'<span class=w>{s}</span>'
bx = lambda s, sz=46: f'<div class="box pop" style="font:900 {sz}px/1.2 Heebo">{s}</div>'
pill = lambda s, sz=40, bg='#C792EA', fg='#1a0f2a': f'<div class="pop" style="display:inline-block;background:{bg};color:{fg};border-radius:24px;padding:12px 26px;font:900 {sz}px/1.2 Heebo;text-shadow:none">{s}</div>'
HITS = [0.16, 1.68, 2.44, 3.89, 6.88, 8.48, 11.0, 12.92, 14.72, 16.24, 17.72, 19.52, 20.38, 21.84, 23.36, 25.24, 26.48]
BIG = {0.16, 12.92, 16.24, 19.52, 21.84, 23.36}

def plan(t):
    o = dict(t=t, dana=None, dry=0, env=False, open=0, knock=0, steps=0, avi=0, flick=False, scared=False)
    if t < 3.76:  # on frappe à la porte de Dana
        k = ease(t / 3.6); o.update(cam=lerp([-1.6, 1.8, 1.7], [-2.9, 1.5, .7], k), look=[-3.4, 1.3, -1.5], knock=1 if t < 2.4 else 0, flick=True)
        key = 'a' + ('1' if t >= 1.68 else '0'); top = pill('🚪 טוק… טוק… טוק…', 44, '#fff')
        bot = bx(f'מישהו דפק על הדלת<br>של {Y("דנה")}… 😨', 50) + (f'<div style="margin-top:10px">{bx("🌙 באמצע הלילה", 40)}</div>' if t >= 2.44 else '')
        return o, key, top, '', bot
    if t < 6.8:  # la façade
        lt = t - 3.76; o.update(cam=[math.sin(lt * .15) * 8, 6 + lt * .6, -40 + 44 - lt * 2.5], look=[0, 9.5, -40])
        return o, 'b', pill('🏢 השכנים', 46), bx(f'בניין ש{Y("אתם")}<br>מחליטים מה קורה בו 🗳️', 50), ''
    if t < 10.8:  # dans l'épisode précédent
        lt = t - 6.8; o.update(dana=[-4, 0, .4], dry=0, env=True, cam=lerp([-1.4, 1.9, 1.7], [-2.6, 1.8, 1.6], ease(lt / 4)), look=[-4, 1.4, .3])
        key = 'c' + ('1' if t >= 8.48 else '0'); top = pill('⏪ בפרק הקודם', 34, '#FFC24B')
        bot = bx(f'המכתב הגיע<br>ל{Y("5 עולמות")} ✉️', 50) if t >= 8.48 else ''
        return o, key, top, '', bot
    if t < 14.64:  # elle ouvre : personne
        lt = t - 10.8; op = ease((lt - .9) / 1.2)
        o.update(dana=[-3.4, 0, .5], dry=math.pi, open=op, cam=lerp([-3.0, 1.9, 1.9], [-3.3, 1.8, 1.5], ease(lt / 3.8)), look=[1.5, 1.3, -.4], flick=True)
        key = 'd' + ('1' if t >= 12.92 else '0'); top = bx('הלילה היא פתחה את הדלת…', 44)
        bot = bx(f'ולא היה שם {Y("אף אחד")}. 😶', 52) if t >= 12.92 else ''
        return o, key, top, '', bot
    if t < 17.2:  # les traces
        lt = t - 14.64; o.update(open=1, steps=min(1, lt / .8), cam=lerp([-2.4, .9, .9], [-1.2, .8, .6], ease(lt / 2.6)), look=[0.5, 0, -.9])
        key = 'e' + ('1' if t >= 16.24 else '0'); top = bx(f'רק {W("עקבות")} קטנות…', 50)
        mid = pill('לבנות. 👣', 56, '#fff') if t >= 16.24 else ''
        return o, key, top, mid, ''
    if t < 20.24:  # elles mènent chez Avi
        lt = t - 17.2; k = ease(lt / 2.6); o.update(open=1, steps=1, avi=ease((lt - 2.3) / .6), cam=lerp([-1.5, 1.0, 1.2], [4.2, 1.5, 1.4], k), look=lerp([1, .2, -.9], [6, 1.3, -1.5], k))
        key = 'f' + ('1' if t >= 19.52 else '0'); top = bx('העקבות מובילות…', 48)
        bot = bx(f'לדירה של {Y("אבי")}! 😱', 60) if t >= 19.52 else ''
        return o, key, top, '', bot
    if t < 25.04:  # entrera-t-elle ?
        lt = t - 20.24; dx = 2.6 + ease(lt / 2.2) * 1.6
        o.update(dana=[dx, 0, .3], dry=-math.pi / 2 + .5, open=1, steps=1, avi=1, cam=lerp([.4, 2.0, 1.7], [1.6, 1.8, 1.6], ease(lt / 4.8)), look=[5.2, 1.4, -1.0], scared=t >= 23.36)
        key = 'g' + ('1' if t >= 21.84 else '') + ('2' if t >= 23.36 else '')
        top = bx(f'האם {Y("דנה")} תיכנס? 🤔', 50)
        c1 = f'<div class="pop" style="display:inline-block;margin:8px;width:40%;background:#2fbf71;color:#fff;border-radius:24px;padding:14px 0;font:900 44px/1.15 Heebo;text-shadow:none">1️⃣<br>נכנסת</div>' if t >= 21.84 else ''
        c2 = f'<div class="pop" style="display:inline-block;margin:8px;width:40%;background:#E5484D;color:#fff;border-radius:24px;padding:14px 0;font:900 44px/1.15 Heebo;text-shadow:none">2️⃣<br>בורחת</div>' if t >= 23.36 else ''
        return o, key, top, '', c1 + c2
    lt = t - 25.04
    o.update(dana=[4.2, 0, .3], dry=-math.pi / 2 + .5, open=1, steps=1, avi=1, cam=lerp([1.6, 2.1, 1.7], [-.5, 2.6, 1.7], ease(lt / 4.5)), look=[5, 1.3, -1.0], flick=True)
    key = 'h' + ('1' if t >= 26.48 else '0')
    top = bx(f'כתבו {Y("1")} או {Y("2")} בתגובות 👇', 50)
    bot = pill('📩 שלחו לחבר<br>שלא היה נכנס בחיים!', 44, '#FFC24B') if t >= 26.48 else ''
    return o, key, top, '', bot

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
        pg.route('http://local/three.min.js', lambda r: r.fulfill(path=f'{NM}/three/build/three.min.js', content_type='text/javascript'))
        pg.route('http://local/', lambda r: r.fulfill(body=HTML, content_type='text/html'))
        pg.add_init_script("Math.random=(()=>{let s=777;return()=>{s=(s*16807)%2147483647;return(s-1)/2147483646}})();")
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('http://local/'); pg.wait_for_function('window.ready===true', timeout=60000); pg.wait_for_timeout(800)
        n = int(round(TOTAL * FPS))
        for i in range(n):
            if i % SAMPLE: continue
            t = i / FPS; o, key, top, mid, bot = plan(t)
            h = max([z for z in HITS if z <= t], default=-9); dt = t - h
            kick = math.exp(-dt * (5 if h in BIG else 9)) if dt < .4 else 0
            if kick: o['cam'] = [o['cam'][0] + math.sin(i * 7.1) * kick * .05, o['cam'][1] + math.cos(i * 5.3) * kick * .05, o['cam'][2]]
            o.update(key=key, top=top, mid=mid, bot=bot, flash=kick * (.3 if h in BIG else .1))
            pg.evaluate('o=>F(o)', o)
            pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
        print('images', n, 'erreurs', errs[:5]); b.close()

main()
