"""השכנים – 14.11 (מוצ״ש) « הדירה של השכן » : suite du vote (דנה נכנסת) — la porte d'Avi s'ouvre sur un appartement
plein de lapins blancs, l'un tient la clé de Dana. Plateau 3D de hashchenim_ep4.py, éclairage relevé (image claire).
Plans filmés sans texte : face | rabbits | key | vote | enter (story).
Usage : python3 film.py <node_modules> <dossier> <plan> <durée_s> [fps]"""
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
// ---------- lapins + appartement d'Avi (posé à z=+40) ----------
const RM=new THREE.Group();RM.position.set(0,0,40);scene.add(RM);
const rb=(w,h,d,m,x,y,z,p)=>box(w,h,d,m,x,y,z,p);
rb(14,.2,12,M(0x7a5a3e),0,-.1,0,RM);rb(14,6,.2,M(0x3f7f78),0,3,-6,RM);const SWM=M(0xb0566f);rb(.2,6,12,SWM,-7,3,0,RM);rb(.2,6,12,SWM,7,3,0,RM);rb(14,6,.2,SWM,0,3,6,RM);
rb(3.6,.9,1.4,M(0x5b6bd6),-2.2,.45,-4.8,RM);rb(3.6,1.2,.4,M(0x4a59c0),-2.2,1.1,-5.4,RM);rb(1.6,.9,1.2,M(0x8a5a2b),2.6,.45,-2.2,RM);
rb(1.2,2.2,.1,M(0xfff6c0,0xfff6c0,.9),3.5,3.2,-5.85,RM);
[[-3,4.8,2],[3,4.8,-2],[0,4.8,4]].forEach(([x,y,z])=>{const l=new THREE.PointLight(0xfff0d8,.55,14,1.6);l.position.set(x,y,z);RM.add(l)});
const WH=M(0xf4f4f4,0xffffff,.02),PK=M(0xff9fb6,0xff7a9a,.3),BK=M(0x111111);
function mkRabbit(s){const r=new THREE.Group();const b=new THREE.Group();r.add(b);
 rb(.36,.3,.5,WH,0,.2,0,b);rb(.3,.28,.28,WH,0,.42,.3,b);rb(.07,.32,.04,WH,-.07,.7,.27,b);rb(.07,.32,.04,WH,.07,.7,.27,b);
 rb(.04,.24,.02,PK,-.07,.7,.295,b);rb(.04,.24,.02,PK,.07,.7,.295,b);rb(.05,.05,.02,BK,-.08,.47,.445,b);rb(.05,.05,.02,BK,.08,.47,.445,b);rb(.06,.04,.02,PK,0,.4,.45,b);
 rb(.14,.14,.12,WH,0,.24,-.28,b);r.scale.setScalar(s);r.userData.b=b;return r}
const RAB=[];for(let i=0;i<46;i++){const r=mkRabbit(.9+Math.random()*.5);const a=Math.random()*6.28,d=1.2+Math.random()*5;
 r.position.set(Math.cos(a)*d*1.1,0,Math.sin(a)*d*.8-1.2);if(Math.abs(r.position.x-2.2)<1.8&&r.position.z>-3.4&&r.position.z<0.5)r.position.x-=3.6;
 r.rotation.y=Math.random()*6.28;r.userData.ph=Math.random()*6.28;r.userData.sp=5+Math.random()*4;RM.add(r);RAB.push(r)}
// lapin sur la table + la clé dorée
const KR=mkRabbit(2.2);KR.position.set(2.6,.9,-2.2);KR.rotation.y=-.3;KR.userData.ph=0;KR.userData.sp=2;RM.add(KR);
const GOLD=new THREE.MeshStandardMaterial({color:0xFFC24B,metalness:.9,roughness:.2,emissive:0xb07800,emissiveIntensity:.8});
const KEY=new THREE.Group();const ring=new THREE.Mesh(new THREE.TorusGeometry(.09,.03,10,24),GOLD);ring.position.x=-.17;KEY.add(ring);
rb(.3,.04,.04,GOLD,.05,0,0,KEY);rb(.04,.08,.03,GOLD,.15,-.05,0,KEY);rb(.04,.06,.03,GOLD,.09,-.04,0,KEY);
KEY.position.set(0,.4,.46);KR.userData.b.add(KEY);const kl=new THREE.PointLight(0xffd060,0,2.5,2);kl.position.set(0,.4,.6);KR.userData.b.add(kl);
// dans le couloir : quelques lapins qui s'échappent de chez Avi
const ESC=[];for(let i=0;i<5;i++){const r=mkRabbit(1);r.position.set(6.4+i*.35,0,-.9+i*.25);r.rotation.y=Math.PI/2+.4;r.userData.ph=i;r.userData.sp=7;scene.add(r);ESC.push(r)}
const dana2=mkChar({shirt:0xE5484D,hair:0x2a160c,long:true,skin:0xf1c7a2,ph:.9});RM.add(dana2.g);
const hop=(r,t,amp)=>{const k=Math.abs(Math.sin(t*r.userData.sp+r.userData.ph));r.userData.b.position.y=k*amp;r.userData.b.rotation.x=-k*.25};
window.F2=function(o){const t=o.t;doors['אבי'].piv.rotation.y=-1.3;doors['דנה'].piv.rotation.y=-1.2;SW.opacity=1;halo.intensity=.6;
 dana.g.visible=false;dana2.g.visible=false;ESC.forEach(r=>r.visible=false);KEY.visible=true;kl.intensity=0;
 RAB.forEach(r=>hop(r,t,.25));hop(KR,t*.3,.05);
 const L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k),E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};let cam,look;
 if(o.shot==='face'){dana.g.visible=true;dana.g.position.set(4.5,0,.3);dana.g.rotation.y=-.25;animChar(dana,t,1,'talk');
   ESC.forEach((r,i)=>{r.visible=true;r.position.x=6.6+i*.4-((t*1.2+i*.3)%2.2);hop(r,t,.18)});
   cam=L([3.7,2.25,1.75],[3.85,2.15,1.5],E(t/2.5));look=[5.2,1.65,-.6];}
 else if(o.shot==='rabbits'){const k=E(t/3);cam=L([0,3.6,45.5],[.6,2.3,41.8],k);cam[2]-=40;look=[0,.6,-1.5];cam=[cam[0],cam[1],cam[2]+40];look[2]+=40;}
 else if(o.shot==='key'){kl.intensity=2.5+Math.sin(t*6);const a=-.55+t*.14,rr=2.7-t*.25;cam=[2.6+Math.sin(a)*rr,2.25,37.8+Math.cos(a)*rr];look=[2.45,1.75,38.2];}
 else if(o.shot==='vote'){dana2.g.visible=true;dana2.g.position.set(.3,0,1.2);dana2.g.rotation.y=.25;animChar(dana2,t,1,'talk');dana2.aL.rotation.x=-2.2;dana2.aR.rotation.x=-2.2;kl.intensity=2;
   cam=L([-.6,2.4,44.6],[-1.2,3.2,46.2],E(t/3.5));look=[.6,1.4,40];}
 else if(o.shot==='enter'){dana.g.visible=true;const k=E(t/5);dana.g.position.set(3.7+k*2.4,0,.3-k*.9);dana.g.rotation.y=Math.PI/2+.25+k*.6;animChar(dana,t,0,'talk');
   ESC.forEach((r,i)=>{r.visible=true;r.position.x=6.8+i*.4-((t*1.1+i*.4)%2.4);hop(r,t,.18)});
   cam=L([1.8,2.1,1.7],[3.8,1.9,1.6],E(t/6));look=L([4,1.5,-.4],[6.2,1.3,-1.4],E(t/6));}
 camera.position.set(...cam);camera.lookAt(...look);R.render(scene,camera)};
"""
HTML = HTML.replace('window.ready=true;', EXTRA + 'window.ready=true;')
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
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
