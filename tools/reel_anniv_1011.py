"""סבתא מזל – reel 10.11 « יום ההולדת שאף אחד לא זכר » : Savta seule sur son banc, Elia revient avec un petit gâteau et une bougie.
Voix : narratrice Juniper (eleven_v4) + réplique de Savta (voix « mazal meme »), découpage mot à mot.
Filmé dans la vraie ville 3D (index.html, mode CAP) ; Elia (monstre violet), le gâteau et les bougies sont ajoutés par le script.
Usage : python3 tools/reel_anniv_1011.py <node_modules> <dossier_images> [échantillon]"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
R = '/home/claude/hasavta-shelanu'; FPS = 30; TOTAL = 33.4
os.makedirs(OUT, exist_ok=True)
FONTS = ''.join(f"@font-face{{font-family:Heebo;src:url(http://local/__f/heebo-{s}-{w}-normal.woff2);font-weight:{w}}}" for s in ('hebrew', 'latin') for w in (400, 800, 900))

EXTRA = r'''
{const {scene,camera,controls,SPOT,skyGroup,renderer}=window.__S;const SP=SPOT.clone();
 const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.8,emissive:e||0,emissiveIntensity:ei||0});
 // Elia : monstre violet en cubes, gros yeux, petite corne
 const E=new THREE.Group();const pur=M(0x8a3ffc,0x2a0a5e,.25),pur2=M(0x6b25d6);
 const bx=(w,h,d,m,x,y,z,p)=>{const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);b.position.set(x,y,z);b.castShadow=true;(p||E).add(b);return b};
 bx(1.3,1.6,1.0,pur,0,1.25,0);bx(.4,.6,.4,pur2,-.35,.3,0);bx(.4,.6,.4,pur2,.35,.3,0);
 for(let i=0;i<14;i++){bx(.18,.18,.18,pur2,(Math.random()-.5)*1.3,.5+Math.random()*1.5,.48)}
 const eyeW=M(0xffffff,0xffffff,.2),pupil=M(0x111111);
 const eyes=[-.28,.28].map(x=>{const g=new THREE.Group();g.position.set(x,1.65,.52);E.add(g);bx(.36,.36,.06,eyeW,0,0,0,g);bx(.16,.16,.04,pupil,0,-.02,.04,g);return g});
 bx(.5,.12,.05,M(0x2a0010),0,1.22,.52);bx(.12,.35,.12,M(0xfff1c8),0,2.2,0);
 const armL=new THREE.Group();armL.position.set(-.75,1.6,0);E.add(armL);bx(.3,.9,.3,pur,0,-.4,0,armL);
 const armR=new THREE.Group();armR.position.set(.75,1.6,0);E.add(armR);bx(.3,.9,.3,pur,0,-.4,0,armR);
 E.scale.setScalar(.8);scene.add(E);E.visible=false;
 // gâteau + bougies
 const CK=new THREE.Group();const c1=new THREE.Mesh(new THREE.CylinderGeometry(.34,.34,.26,24),M(0xf7d9e3));c1.position.y=.13;CK.add(c1);
 const c2=new THREE.Mesh(new THREE.CylinderGeometry(.36,.36,.06,24),M(0xff5c8a,0x5a0020,.3));c2.position.y=.27;CK.add(c2);
 const plate=new THREE.Mesh(new THREE.CylinderGeometry(.46,.46,.03,24),M(0xffffff));CK.add(plate);
 const C=[];for(let i=0;i<24;i++){const g=new THREE.Group();const a=i?(i*2.39996):0,r=i?.08+.22*Math.sqrt(i/24):0;g.position.set(Math.cos(a)*r,.3,Math.sin(a)*r);
   const s=new THREE.Mesh(new THREE.BoxGeometry(.035,.16,.035),M([0xffffff,0x6ec6ff,0xffd34d,0xff7ab0][i%4]));s.position.y=.08;g.add(s);
   const f=new THREE.Mesh(new THREE.SphereGeometry(.035,8,6),new THREE.MeshBasicMaterial({color:0xffc04d}));f.scale.set(1,1.7,1);f.position.y=.2;g.add(f);g.userData.f=f;g.visible=false;CK.add(g);C.push(g)}
 const glow=new THREE.PointLight(0xffb04d,0,5,2);glow.position.y=.6;CK.add(glow);
 scene.add(CK);CK.visible=false;
 window.BD={E,eyes,armL,armR,CK,C,glow,SP};
 const ov=document.createElement('div');ov.id='ov';ov.style.cssText='position:fixed;inset:0;z-index:9999;pointer-events:none;font-family:Heebo;direction:rtl';document.body.appendChild(ov);
 const css=document.createElement('style');css.textContent=`#ov .t{position:absolute;left:0;right:0;text-align:center;color:#fff;text-shadow:0 4px 18px rgba(0,0,0,.9);padding:0 16px}#ov .y{color:#FFC24B}#ov .k{color:#FF8FB8}@keyframes pop{0%{transform:scale(.5);opacity:0}60%{transform:scale(1.1);opacity:1}100%{transform:scale(1)}}#ov .pop{animation:pop .3s ease-out both}#ov .box{display:inline-block;background:rgba(20,8,24,.74);border-radius:24px;padding:10px 24px}body.cap *:not(canvas):not(#ov):not(#ov *){visibility:hidden}`;document.head.appendChild(css);
 ov.innerHTML='<div id=oD style="position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,0,0,0) 45%,rgba(0,0,0,.6) 100%)"></div><div class=t id=oT style="top:10%"></div><div class=t id=oM style="top:38%"></div><div class=t id=oB style="bottom:12%"></div><div id=oF style="position:absolute;inset:0;background:#fff;opacity:0"></div><div style="position:absolute;top:3%;right:4%;background:rgba(20,8,24,.75);border:2px solid #FF8FB8;border-radius:999px;padding:4px 14px;font:900 14px Heebo;color:#fff">👵 סבתא מזל · יום 9</div>';
 window.OVL={last:''};
 window.ovl=function(key,top,mid,bot,flash){const O=window.OVL;if(key!==O.last){O.last=key;document.getElementById('oT').innerHTML=top;document.getElementById('oM').innerHTML=mid;document.getElementById('oB').innerHTML=bot}document.getElementById('oF').style.opacity=flash};
}
'''

STEP = r'''o=>{const B=window.BD,S=B.SP,{camera,controls,skyGroup,renderer,scene}=window.__S;
 capHook(o.t);
 B.E.visible=o.eShow;if(o.eShow){B.E.position.set(S.x+o.ex,S.y,S.z+1.4);B.E.rotation.y=o.ery;const w=Math.sin(o.t*9)*.06;B.E.position.y+=Math.abs(Math.sin(o.t*6))*o.walk*.12;
   B.armL.rotation.x=o.hold?-1.2:Math.sin(o.t*6)*.5*o.walk;B.armR.rotation.x=o.hold?-1.2:-Math.sin(o.t*6)*.5*o.walk;B.eyes.forEach(e=>e.scale.y=((o.t+.3)%3.2)<.12?.15:1)}
 B.CK.visible=o.cake>0;if(o.cake>0){if(o.hold&&o.eShow){B.CK.position.set(B.E.position.x+Math.sin(B.E.rotation.y)*.75,S.y+1.05,B.E.position.z+Math.cos(B.E.rotation.y)*.75)}else B.CK.position.set(o.ckx,S.y+o.cky,S.z+o.ckz)}
 B.C.forEach((c,i)=>{c.visible=i<o.cand;c.userData.f.scale.set(1+.15*Math.sin(o.t*20+i),1.7+.4*Math.sin(o.t*17+i*2),1)});B.glow.intensity=o.cand>0?1.2+o.cand*.08:0;
 if(o.happy!=null)window.__S.setHappy(o.happy);
 camera.position.set(...o.cam);controls.target.set(...o.look);camera.lookAt(controls.target);skyGroup.position.copy(camera.position);
 ovl(o.key,o.top,o.mid,o.bot,o.flash);
 renderer.render(scene,camera)}'''

def lerp(a, b, k): return [x + (y - x) * k for x, y in zip(a, b)]
def ease(k): k = max(0, min(1, k)); return k * k * (3 - 2 * k)
Y = lambda s: f'<span class=y>{s}</span>'
K = lambda s: f'<span class=k>{s}</span>'
box = lambda s, sz=46: f'<div class="box pop" style="font:900 {sz}px/1.2 Heebo">{s}</div>'
pill = lambda s, sz=40: f'<div class="pop" style="display:inline-block;background:#FF8FB8;color:#2a0a18;border-radius:24px;padding:12px 28px;font:900 {sz}px/1.2 Heebo;text-shadow:none">{s}</div>'
HITS = [0.24, 3.12, 4.88, 9.1, 13.96, 15.68, 17.28, 18.6, 20.25, 22.3, 24.44, 26.52, 27.9, 29.18, 31.04]
BIG = {0.24, 13.96, 17.28, 24.44}
FACE = ([0.35, 2.75, 15.4], [0, 2.55, 10.7])

def plan(t):
    o = dict(t=t, eShow=False, ex=0, ery=0, walk=0, hold=False, cake=0, cand=0, ckx=0, cky=0, ckz=0, happy=None)
    if t < 4.8:  # hook : gros plan triste
        k = ease(t / 4.6); o.update(cam=lerp([1.4, 2.9, 14.6], [0.25, 2.7, 13.2], k), look=[0, 2.45, 10.7])
        key = 'a' + ('1' if t >= 3.12 else '0'); top = box(f'🎂 היום יום ההולדת<br>של {K("סבתא מזל")}…', 50)
        bot = box(f'ואף אחד {Y("לא זכר")}. 💔', 56) if t >= 3.12 else ''
        return o, key, top, '', bot
    if t < 9.04:  # la rue, large
        a = (t - 4.8) * .05; o.update(cam=[14 * math.cos(a) - 2, 9 - (t - 4.8) * .4, 30 - (t - 4.8) * 1.2], look=[0, 1.6, 11])
        key = 'b'; top = box(f'כאן {Y("אתם")} כותבים<br>את החיים של סבתא מזל ✍️', 44)
        bot = box('👵 סבתא שגרה ברחוב', 44) if t >= 7.3 else ''
        return o, key + ('1' if bot else '0'), top, '', bot
    if t < 13.96:  # seule sur le banc, avec l'enveloppe
        k = ease((t - 9.04) / 4.9); o.update(cam=lerp([-3.2, 2.2, 14.8], [-1.4, 2.5, 13.0], k), look=[0, 2.0, 10.7])
        key = 'c' + ('1' if t >= 10.96 else '0'); top = box('היא ישבה לבד על הספסל…', 46)
        bot = box(f'✉️ עם המעטפה<br>ש{Y("אליה")} הביא לה', 44) if t >= 10.96 else ''
        return o, key, top, '', bot
    if t < 18.6:  # Elia revient avec le gâteau
        lt = t - 13.96; k = min(1, lt / 2.8)
        o.update(eShow=True, ex=lerp([-6], [-1.25], ease(k))[0], ery=1.2 if k < 1 else .6, walk=1 if k < 1 else 0, hold=True, cake=1, cand=1 if t >= 17.28 else 0)
        o.update(cam=lerp([2.6, 2.4, 16.5], [1.6, 2.3, 14.4], ease(lt / 4.6)), look=[-0.7, 1.7, 11.6])
        key = 'd' + ('1' if t >= 15.68 else '') + ('2' if t >= 17.28 else ''); top = box(f'ואז {Y("אליה")} חזר… 💜', 50)
        mid = ''; bot = box(f'עם עוגה קטנה… 🎂' + (f'<br>ו{Y("נר אחד")} 🕯️' if t >= 17.28 else ''), 48) if t >= 15.68 else ''
        return o, key, top, mid, bot
    if t < 24.25:  # Savta émue
        lt = t - 18.6; o.update(eShow=True, ex=-1.25, ery=.6, hold=True, cake=1, cand=1, happy=20.1 if t >= 20.1 else None)
        o.update(cam=lerp([1.4, 2.6, 15.2], [0.7, 2.5, 14.3], ease(lt / 5.6)), look=[-.6, 2.0, 11.0])
        key = 'e' + ('1' if t >= 22.3 else '0')
        bot = box(f'“אף פעם… אף פעם<br>{K("לא חגגו לי")}”', 50) + (f'<div style="margin-top:12px">{box("“תודה, נשמה שלי” 🥹", 44)}</div>' if t >= 22.3 else '')
        return o, key, '', '', bot
    # appel : chaque commentaire = une bougie
    lt = t - 24.25; n = 1 if t < 27.9 else min(24, 1 + int((t - 27.9) * 7))
    o.update(eShow=True, ex=-1.25, ery=.6, hold=False, cake=1, cand=n, ckx=-.45, cky=.62, ckz=.95, happy=20.1)
    o.update(cam=lerp([1.4, 2.3, 15.0], [0.8, 3.4, 16.8], ease(lt / 8.5)), look=[-0.5, 1.4 + ease(lt / 8.5) * .5, 11.2])
    key = 'f' + ('1' if t >= 26.52 else '') + ('2' if t >= 29.18 else '') + ('3' if t >= 31.04 else '')
    top = box(f'בואו נעשה לה<br>{Y("יום הולדת אמיתי")} 🎉', 48)
    mid = (f'<div style="margin-top:6px">{box("כל ברכה בתגובות = " + Y("עוד נר") + " 🕯️", 40)}</div>' if t >= 26.52 else '') + (f'<div class="pop" style="margin-top:14px;font:900 64px Heebo;color:#FFC24B">נגיע ל־80 נרות?</div>' if t >= 29.18 else '')
    bot = pill('💌 שלחו את זה<br>לסבתא שלכם', 46) if t >= 31.04 else ''
    return o, key, top, mid, bot

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
            h = h.replace('window.capHook = function(t){', 'window.__S={scene,camera,controls,SPOT,skyGroup,renderer,applyTime,setHappy:v=>{happyStart=v}};\nwindow.capHook = function(t){', 1)
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
        pg.evaluate("try{window.__S.applyTime(19.2)}catch(e){};if(window.SHADOWS_OFF)window.__S.renderer.shadowMap.enabled=false;0")
        pg.evaluate(EXTRA + ";0")
        pg.evaluate("window.requestAnimationFrame=()=>0;0"); pg.wait_for_timeout(500)
        n = int(os.environ.get('MAXF') or round(TOTAL * FPS))
        for i in range(n):
            if i % SAMPLE: continue
            t = i / FPS
            o, key, top, mid, bot = plan(t)
            h = max([z for z in HITS if z <= t], default=-9); dt = t - h
            kick = math.exp(-dt * (5 if h in BIG else 9)) if dt < .4 else 0
            o.update(key=key, top=top, mid=mid, bot=bot, flash=kick * (.35 if h in BIG else .12))
            import time as _t; _a=_t.time(); pg.evaluate(STEP, o); _b=_t.time()
            pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
            if os.environ.get('MAXF'): print('eval %.1f shot %.1f'%(_b-_a,_t.time()-_b), flush=True)
        print('images', n, 'erreurs', errs[:5]); b.close()

main()
