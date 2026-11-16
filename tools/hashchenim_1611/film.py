"""השכנים – 16.11 (format A) : le lapin géant s'enfuit avec la clé. Plans : run | key | face.
Ancien en-tête : 15.11 « המפתח פתח את דלת 8 » : Dana tient la clé dorée, la porte 8 s'ouvre, un lapin géant aux yeux rouges sort.
Plans : face | door | react. Usage : DSF=1.5 python3 film.py <node_modules> <dossier> <plan> <durée_s> [fps]"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT, SHOT, DUR = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]); FPS = int(sys.argv[5]) if len(sys.argv) > 5 else 30
os.makedirs(OUT, exist_ok=True)
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'hashchenim_ep4.py')).read()
src = src[:src.index('def lerp')].replace('NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1', 'pass').replace('os.makedirs(OUT, exist_ok=True)', '')
g = {'NM': NM, 'sys': sys, '__name__': 'x'}; exec(src, g); HTML = g['HTML']
HTML = (HTML.replace('scene.add(new THREE.HemisphereLight(0x8fa0ff,0x201030,.55))', 'scene.add(new THREE.HemisphereLight(0xd8dcff,0x504060,1.25))')
        .replace('scene.background=new THREE.Color(0x0b0a1e);scene.fog=new THREE.Fog(0x0b0a1e,18,60)', 'scene.background=new THREE.Color(0x2a2550)')
        .replace('new THREE.PointLight(0xffd9a0,.55,7,2)', 'new THREE.PointLight(0xffd9a0,1.3,10,2)'))
EXTRA = r"""
// ---------- 16.11 : le lapin géant s'enfuit dans le couloir avec la clé ----------
const WH=M(0xe4e4ee),PK=M(0xff9fb6,0xff7a9a,.3),RE=M(0xff2050,0xff2050,1.6);
function mkRabbit(s){const r=new THREE.Group();const b=new THREE.Group();r.add(b);
 box(.36,.3,.5,WH,0,.2,0,b);box(.3,.28,.28,WH,0,.42,.3,b);const e1=box(.07,.32,.04,WH,-.07,.7,.27,b);const e2=box(.07,.32,.04,WH,.07,.7,.27,b);
 box(.04,.24,.02,PK,-.07,.7,.295,b);box(.04,.24,.02,PK,.07,.7,.295,b);box(.05,.05,.02,RE,-.08,.47,.445,b);box(.05,.05,.02,RE,.08,.47,.445,b);box(.06,.04,.02,PK,0,.4,.45,b);
 box(.14,.14,.12,WH,0,.24,-.28,b);r.scale.setScalar(s);r.userData.b=b;return r}
const GR=mkRabbit(2.6);scene.add(GR);
const GOLD=new THREE.MeshStandardMaterial({color:0xFFC24B,metalness:.9,roughness:.2,emissive:0xb07800,emissiveIntensity:1.1});
const KEY=new THREE.Group();const ring=new THREE.Mesh(new THREE.TorusGeometry(.1,.035,10,24),GOLD);ring.position.y=.2;KEY.add(ring);
box(.045,.32,.045,GOLD,0,0,0,KEY);box(.09,.045,.04,GOLD,.06,-.13,0,KEY);box(.07,.045,.04,GOLD,.05,-.05,0,KEY);
KEY.scale.setScalar(.45);KEY.position.set(.02,.36,.47);KEY.rotation.z=Math.PI/2;GR.userData.b.add(KEY);
const kl=new THREE.PointLight(0xffc24b,0,3,2);scene.add(kl);
const fill=new THREE.PointLight(0xfff0e0,0,8,1.5);scene.add(fill);
window.F2=function(o){const t=o.t;const L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k),E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
 doors['אבי'].piv.rotation.y=0;doors['דנה'].piv.rotation.y=0;SW.opacity=0;halo.intensity=0;ENV.visible=false;
 dana.g.visible=false;doors[1].piv.rotation.y=-1.45;GR.visible=true;GR.rotation.set(0,-Math.PI/2,0);
 dana.aL.rotation.set(0,0,0);dana.aR.rotation.set(0,0,0);let cam,look;const hop=Math.abs(Math.sin(t*6.5));
 if(o.shot==='run'){const x=.9-1.6*t;GR.position.set(x,.55*hop,.1);GR.userData.b.rotation.x=(hop-.5)*.35;
   kl.position.set(x-1.6,1.4,.3);kl.intensity=1.6;fill.position.set(x-3,2.6,1.2);fill.intensity=.9;
   cam=[-5.6+.3*t,1.1,.55];look=[x-.6,1.05,-.05];}
 else if(o.shot==='key'){GR.position.set(-1.0,.12*Math.abs(Math.sin(t*3)),0);GR.userData.b.rotation.x=-.08+Math.sin(t*5)*.04;GR.rotation.y=-Math.PI/2+.35+Math.sin(t*2)*.08;
   kl.position.set(-2.4,1.2,.5);kl.intensity=2.2;fill.position.set(-3.2,2.2,1.4);fill.intensity=.8;
   cam=L([-4.6,1.45,1.25],[-4.1,1.35,1.0],E(t/2.5));look=[-1.8,1.15,.15];}
 else if(o.shot==='face'){dana.g.visible=true;dana.g.position.set(-3.0,0,-.55);dana.g.rotation.y=.25;animChar(dana,t,.4,'talk');
   dana.aL.rotation.x=-2.3;dana.aR.rotation.x=-2.3;dana.aL.rotation.z=.3;dana.aR.rotation.z=-.3;
   const x=2.5-3.2*t;GR.position.set(x,.5*hop,.6);kl.position.set(x-1.5,1.3,.6);kl.intensity=1.2;
   fill.position.set(-2.3,2.6,1.4);fill.intensity=.6;
   cam=L([-2.45,2.05,2.0],[-2.6,1.95,1.55],E(t/2.5));look=[-2.95,1.68,-.6];}
 camera.position.set(...cam);camera.lookAt(...look);R.render(scene,camera)};
"""
HTML = HTML.replace('window.ready=true;', EXTRA + 'window.ready=true;')
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=float(os.environ.get('DSF',2)))
    pg.route('http://local/three.min.js', lambda r: r.fulfill(path=f'{NM}/three/build/three.min.js', content_type='text/javascript'))
    pg.route('http://local/', lambda r: r.fulfill(body=HTML, content_type='text/html'))
    pg.add_init_script("Math.random=(()=>{let s=777;return()=>{s=(s*16807)%2147483647;return(s-1)/2147483646}})();")
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('http://local/'); pg.wait_for_function('window.ready===true', timeout=60000); pg.wait_for_timeout(500)
    pg.add_style_tag(content='#ov{display:none!important}')
    n = int(round(DUR * FPS)); step = int(os.environ.get('STEP', 1))
    for i in range(0, n, step):
        pg.evaluate('o=>F2(o)', {'shot': SHOT, 't': i / FPS})
        pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
    print(SHOT, 'images', n, 'erreurs', errs[:5]); b.close()
