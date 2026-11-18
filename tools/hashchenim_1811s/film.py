"""השכנים – 18.11 soir, « פרק 1 » de la série « les voisins qu'on a tous » : bruit à 2 h du matin → porte 10 → lapins → deux yeux géants (cliffhanger).
Plans F3 : pour | face ; plans F4 : wake | glow | nerv | eyes.
(ancien en-tête) השכנים – 18.11 (format A) : la porte 10 s'ouvre d'un coup, des dizaines de lapins sortent dans la lumière rose ; Dana éclairée en rose, vote 1 נכנסת / 2 קוראת לשכנים.
Plans : pour | pourlow | face. Usage : DSF=1.5 python3 film.py <node_modules> <dossier> <plan> <durée_s> [fps]"""
import sys, os, math
from playwright.sync_api import sync_playwright
NM, OUT, SHOT, DUR = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]); FPS = int(sys.argv[5]) if len(sys.argv) > 5 else 30
os.makedirs(OUT, exist_ok=True)
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'hashchenim_ep4.py')).read().replace('פרק 4','פרק 1')
src = src[:src.index('def lerp')].replace('NM, OUT = sys.argv[1], sys.argv[2]; SAMPLE = int(sys.argv[3]) if len(sys.argv) > 3 else 1', 'pass').replace('os.makedirs(OUT, exist_ok=True)', '')
g = {'NM': NM, 'sys': sys, '__name__': 'x'}; exec(src, g); HTML = g['HTML']
HTML = (HTML.replace('scene.add(new THREE.HemisphereLight(0x8fa0ff,0x201030,.55))', 'scene.add(new THREE.HemisphereLight(0xd8dcff,0x504060,1.25))')
        .replace('scene.background=new THREE.Color(0x0b0a1e);scene.fog=new THREE.Fog(0x0b0a1e,18,60)', 'scene.background=new THREE.Color(0x2a2550)')
        .replace('new THREE.PointLight(0xffd9a0,.55,7,2)', 'new THREE.PointLight(0xffd9a0,1.3,10,2)'))
EXTRA = r"""
// ---------- 17.11 : le lapin entre dans la porte 10 ----------
const WH=M(0xe4e4ee),PK=M(0xff9fb6,0xff7a9a,.3),RE=M(0xff2050,0xff2050,1.6);
function mkRabbit(s){const r=new THREE.Group();const b=new THREE.Group();r.add(b);
 box(.36,.3,.5,WH,0,.2,0,b);box(.3,.28,.28,WH,0,.42,.3,b);box(.07,.32,.04,WH,-.07,.7,.27,b);box(.07,.32,.04,WH,.07,.7,.27,b);
 box(.04,.24,.02,PK,-.07,.7,.295,b);box(.04,.24,.02,PK,.07,.7,.295,b);box(.05,.05,.02,RE,-.08,.47,.445,b);box(.05,.05,.02,RE,.08,.47,.445,b);box(.06,.04,.02,PK,0,.4,.45,b);
 box(.14,.14,.12,WH,0,.24,-.28,b);r.scale.setScalar(s);r.userData.b=b;return r}
const GR=mkRabbit(2.3);scene.add(GR);
const GOLD=new THREE.MeshStandardMaterial({color:0xFFC24B,metalness:.9,roughness:.2,emissive:0xb07800,emissiveIntensity:1.1});
const KEY=new THREE.Group();const ring=new THREE.Mesh(new THREE.TorusGeometry(.1,.035,10,24),GOLD);ring.position.y=.2;KEY.add(ring);
box(.045,.32,.045,GOLD,0,0,0,KEY);box(.09,.045,.04,GOLD,.06,-.13,0,KEY);
KEY.scale.setScalar(.45);KEY.position.set(.02,.36,.47);KEY.rotation.z=Math.PI/2;GR.userData.b.add(KEY);
const PGLOW=new THREE.MeshBasicMaterial({color:0xff6fb0});const pin=box(1.18,2.38,.02,PGLOW,11,1.2,-1.585);
const strip=box(1.2,.05,.25,PGLOW,11,.03,-1.42);
const pl=new THREE.PointLight(0xff5aa8,0,9,1.6);pl.position.set(11,1.2,-1.1);scene.add(pl);
const fill=new THREE.PointLight(0xfff0e0,0,8,1.5);scene.add(fill);

const BUN=[];for(let i=0;i<14;i++){const r=mkRabbit(.75+((i*37)%5)*.08);r.visible=false;scene.add(r);BUN.push(r)}
window.F3=function(o){const t=o.t;const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
 doors['אבי'].piv.rotation.y=0;doors['דנה'].piv.rotation.y=0;SW.opacity=0;halo.intensity=0;ENV.visible=false;GR.visible=false;
 const D10=doors[11].piv;D10.position.z=-1.55;D10.rotation.y=.5+1.0*E(t/.25);dana.g.visible=false;
 BUN.forEach((r,i)=>{const ph=((t*.55+i*.071)%1);const sx=10.55+((i*53)%9)*.1;const ex=9.6+((i*29)%11)*.28;
   r.visible=o.shot!=='face';r.position.set(sx+(ex-sx)*ph,.5*Math.abs(Math.sin(t*7+i*1.3)),-1.45+3.4*ph);
   r.rotation.set(0,(ex-sx)*.25,0);r.scale.setScalar((.75+((i*37)%5)*.08)*Math.min(1,ph*6));r.userData.b.rotation.x=(Math.abs(Math.sin(t*7+i*1.3))-.5)*.35});
 pl.position.set(11,1.2,-1.1);pl.intensity=3.2+.6*Math.sin(t*11);fill.intensity=.45;let cam,look;
 if(o.shot==='pour'){fill.position.set(11,2.6,1.6);cam=[11.0-.2*E(t/3),1.05,1.65-.25*E(t/3)];look=[11,.85,-1.3];}
 else if(o.shot==='pourlow'){fill.position.set(10,2.6,1.6);cam=[9.5,.6,1.75];look=[10.9,.6,-1.2];}
 else {dana.g.visible=true;dana.g.position.set(9.4,0,-.4);dana.g.rotation.y=.45;animChar(dana,t,.4,'talk');
   dana.aL.rotation.x=-2.3;dana.aR.rotation.x=-2.3;dana.aL.rotation.z=.3;dana.aR.rotation.z=-.3;
   pl.position.set(10.6,1.6,-.3);pl.intensity=1.5+.4*Math.sin(t*9);fill.position.set(9.0,2.4,1.2);fill.intensity=.5;
   cam=[10.3-.1*E(t/3),2.0,1.55-.2*E(t/3)];look=[9.45,1.72,-.4];}
 camera.position.set(...cam);camera.lookAt(...look);R.render(scene,camera)};
window.F2=function(o){const t=o.t;const L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k),E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
 doors['אבי'].piv.rotation.y=0;doors['דנה'].piv.rotation.y=0;SW.opacity=0;halo.intensity=0;ENV.visible=false;
 const D10=doors[11].piv;D10.rotation.y=0;D10.position.z=-1.55;dana.g.visible=false;GR.visible=true;GR.scale.setScalar(2.3);
 dana.aL.rotation.set(0,0,0);dana.aR.rotation.set(0,0,0);let cam,look;const hop=Math.abs(Math.sin(t*6.5));
 if(o.shot==='door10'){const k=E(t/1.1);const x=9.2+1.8*k;GR.rotation.set(0,Math.PI/2+1.57*E((t-.65)/.35),0);
   let z=-.2-1.4*E((t-.9)/.5);GR.position.set(Math.min(x,11),.45*hop*(t<1.5?1:0),z);GR.userData.b.rotation.x=(hop-.5)*.3;
   const op=E((t-.5)/.5)*(1-E((t-1.75)/.4));D10.rotation.y=1.45*op;GR.scale.setScalar(2.3*(1-E((t-1.0)/.5))+.001);
   pl.intensity=.6+2.6*op;fill.position.set(8.5,2.6,1.2);fill.intensity=1.0;
   cam=L([6.0,1.5,1.5],[6.7,1.4,1.25],E(t/2.5));look=[10.4,1.05,-1.0];}
 else if(o.shot==='glow'){GR.visible=false;D10.position.z=-1.55+Math.sin(t*55)*.025*(Math.sin(t*3)>0?1:0);
   pl.position.set(11,.25,-1.1);pl.intensity=1.6+.6*Math.sin(t*9);fill.position.set(11,2.4,1.5);fill.intensity=.9;
   cam=L([11.2,1.25,.95],[11.15,1.15,.55],E(t/2.5));look=[11,1.05,-1.55];}
 else if(o.shot==='face'){GR.visible=false;dana.g.visible=true;dana.g.position.set(8.0,0,-.55);dana.g.rotation.y=.25;animChar(dana,t,.4,'talk');
   dana.aL.rotation.x=-2.3;dana.aR.rotation.x=-2.3;dana.aL.rotation.z=.3;dana.aR.rotation.z=-.3;
   pl.position.set(10.5,1.4,-.6);pl.intensity=.7+.3*Math.sin(t*7);fill.position.set(8.6,2.6,1.4);fill.intensity=.15;
   cam=L([8.55,2.0,1.75],[8.45,1.95,1.5],E(t/3));look=[8.05,1.72,-.6];}
 camera.position.set(...cam);camera.lookAt(...look);R.render(scene,camera)};

const HOLE=new THREE.MeshBasicMaterial({color:0x07040c});const hole=box(1.18,2.38,.02,HOLE,11,1.2,-1.57);hole.visible=false;
const EYEM=new THREE.MeshBasicMaterial({color:0xff2a3a});const EY=[box(.16,.09,.02,EYEM,10.72,1.62,-1.55),box(.16,.09,.02,EYEM,11.28,1.62,-1.55)];EY.forEach(e=>e.visible=false);
const rl=new THREE.PointLight(0xff2040,0,5,1.6);rl.position.set(11,1.6,-1.2);scene.add(rl);
window.F4=function(o){const t=o.t;const L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k),E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
 doors['אבי'].piv.rotation.y=0;doors['דנה'].piv.rotation.y=0;SW.opacity=0;halo.intensity=0;ENV.visible=false;GR.visible=false;BUN.forEach(r=>r.visible=false);
 hole.visible=false;EY.forEach(e=>e.visible=false);rl.intensity=0;pin.visible=true;
 const D10=doors[11].piv;D10.rotation.y=0;D10.position.z=-1.55;dana.g.visible=false;
 dana.aL.rotation.set(0,0,0);dana.aR.rotation.set(0,0,0);
 const beat=Math.pow(Math.max(0,Math.cos(t*Math.PI*2/.5)),8);let cam,look,sh=0;
 if(o.shot==='wake'){dana.g.visible=true;dana.g.position.set(-4,0,-.5);dana.g.rotation.y=-.35;animChar(dana,t,.35+.25*beat,'talk');
   dana.aL.rotation.x=-2.3;dana.aR.rotation.x=-2.3;dana.aL.rotation.z=.3;dana.aR.rotation.z=-.3;
   pl.position.set(-3.2,1.2,-1.0);pl.intensity=.8+1.8*beat;fill.position.set(-4.6,2.4,1.3);fill.intensity=.55;
   cam=L([-4.9,2.0,1.45],[-4.8,1.95,1.15],E(t/2.8));look=[-4.05,1.72,-.5];sh=.03*beat;}
 else if(o.shot==='glow'){D10.position.z=-1.55+Math.sin(t*60)*.035*(.3+beat);D10.rotation.y=.03*beat;
   pl.position.set(11,.2,-1.1);pl.intensity=1.5+3*beat;fill.position.set(11,2.4,1.5);fill.intensity=.9;
   cam=L([11.25,1.3,1.4],[11.1,1.15,.6],E(t/2.4));look=[11,1.0,-1.55];sh=.025*beat;}
 else if(o.shot==='nerv'){dana.g.visible=true;dana.g.position.set(9.2,0,-.35);dana.g.rotation.y=-.45+.55*E(t/.8);animChar(dana,t,.25,'talk');
   pl.position.set(10.6,.6,-1.0);pl.intensity=1.3+1.2*beat;fill.position.set(8.3,2.4,1.3);fill.intensity=.6;
   cam=L([8.45,1.95,1.5],[8.55,1.9,1.25],E(t/1));look=[9.2,1.7,-.35];}
 else if(o.shot==='eyes'){D10.rotation.y=1.25;pin.visible=false;hole.visible=true;
   const on=E((t-.5)/.35);const bl=(t>2.6&&t<2.75)?.1:1;EY.forEach(e=>{e.visible=on>0;e.scale.set(on,on*bl,1)});rl.intensity=2.2*on;
   pl.intensity=0;fill.position.set(10.2,2.6,1.4);fill.intensity=.35;
   cam=L([11,1.35,1.65],[11,1.5,.3],E(t/5.4));look=[11,1.5,-1.6];sh=t<.6?0:.004*Math.sin(t*23);}
 camera.position.set(cam[0]+sh*Math.sin(t*91),cam[1]+sh*Math.cos(t*77),cam[2]);camera.lookAt(...look);R.render(scene,camera)};
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
    for i in range(int(os.environ.get('START', 0)), int(os.environ.get('END', n)), step):
        pg.evaluate('o=>((o.shot=="pour"||o.shot=="face")?F3:F4)(o)', {'shot': SHOT, 't': i / FPS})
        pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
    print(SHOT, 'images', n, 'erreurs', errs[:5]); b.close()
