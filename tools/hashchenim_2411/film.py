"""השכנים – 23.11 matin, חלק 3 : « מה שומעים בבניין » — coupe d'immeuble (maison de poupée) de 8 étages.
Plans : wide | ride | top | end. Usage : DSF=1.4 python3 film.py <node_modules> <dossier> <plan> <durée_s> [fps]"""
import sys, os, re
from playwright.sync_api import sync_playwright
NM, OUT, SHOT, DUR = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]); FPS = int(sys.argv[5]) if len(sys.argv) > 5 else 10
os.makedirs(OUT, exist_ok=True)
CHAR_JS = re.search(r"CHAR_JS = r'''(.*?)'''", open('/home/claude/thenoise/tools/film3d.py').read(), re.S).group(1)
HTML = """<!doctype html><html><head><meta charset=utf-8><style>html,body{margin:0;background:#000;overflow:hidden}canvas{display:block}</style></head><body>
<script src="http://local/three.min.js"></script><script>""" + CHAR_JS + r"""</script><script>
const R=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});R.setPixelRatio(window.devicePixelRatio);R.setSize(540,960);document.body.prepend(R.domElement);
const scene=new THREE.Scene();
const sc=document.createElement('canvas');sc.width=4;sc.height=256;const sg=sc.getContext('2d');const gr=sg.createLinearGradient(0,0,0,256);
gr.addColorStop(0,'#2a2f8a');gr.addColorStop(.5,'#7a4fb0');gr.addColorStop(.85,'#f0789c');gr.addColorStop(1,'#ffc08a');sg.fillStyle=gr;sg.fillRect(0,0,4,256);
const sky=new THREE.Mesh(new THREE.SphereGeometry(900,32,16),new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(sc),side:THREE.BackSide,fog:false}));scene.add(sky);
scene.fog=new THREE.Fog(0x7a5ab0,160,700);
const camera=new THREE.PerspectiveCamera(60,540/960,.1,2000);
scene.add(new THREE.HemisphereLight(0xffffff,0x6a5a80,.55));const sun=new THREE.DirectionalLight(0xfff0d8,.7);sun.position.set(-30,60,80);scene.add(sun);
const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.8,emissive:e||0,emissiveIntensity:ei||0});
const box=(w,h,d,m,x,y,z,p)=>{const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);b.position.set(x,y,z);(p||scene).add(b);return b};
function txtTex(t,bg,fg,w,h,f){const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');g.fillStyle=bg;g.fillRect(0,0,w,h);g.fillStyle=fg;g.font=f;g.textAlign='center';g.textBaseline='middle';g.fillText(t,w/2,h/2);return new THREE.CanvasTexture(c)}
const FH=3.2,W=12,DP=8,NFL=8;
box(500,.2,500,M(0x2f2a4a),0,-.1,0);
// ville autour
function cityTex(seed){const c=document.createElement('canvas');c.width=64;c.height=256;const g=c.getContext('2d');g.fillStyle='#2e3262';g.fillRect(0,0,64,256);let s=seed;const r=()=>{s=(s*16807)%2147483647;return s/2147483647};
 for(let y=4;y<256;y+=10)for(let x=4;x<64;x+=10)if(r()<.62){g.fillStyle=r()<.8?'#ffd98a':'#9fd8ff';g.fillRect(x,y,6,6)}return new THREE.CanvasTexture(c)}
let s=91;const rnd=()=>{s=(s*16807)%2147483647;return s/2147483647};
for(let i=0;i<46;i++){const a=rnd()*Math.PI*2,rr=34+rnd()*160;const x=Math.cos(a)*rr,z=Math.sin(a)*rr-30;if(Math.abs(x)<18&&z>-20)continue;
 const h=14+rnd()*55,w=7+rnd()*10;const t=cityTex(i*7+3);t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(w/16,h/40);
 box(w,h,w,new THREE.MeshStandardMaterial({map:t,emissive:0xffffff,emissiveMap:t,emissiveIntensity:.8,roughness:.9}),x,h/2,z)}
// immeuble en coupe, 11 étages (8 anciens + 3 nouveaux construits à l'écran)
const WALLS=[0xF6D6A8,0xBFE3FF,0xFFC7D9,0xCDEBB5,0xFFE59A,0xE2CCFF,0xFFD0A8,0xFFE08A,0xFFD76A,0xFFC24B,0xFFE08A,0xBFE3FF,0xFFC7D9,0xCDEBB5,0xE2CCFF,0xFFD76A];
const rooms=[];const NF=16;
for(let f=0;f<NF;f++){const y=f*FH;const g=new THREE.Group();g.position.y=y;scene.add(g);
  const gold=f>=7;
  box(W+.6,.3,DP+.4,gold?M(0xFFC24B,0xb07800,.9):M(0xa59ec8),0,.15,0,g);
  box(W,FH-.3,.3,M(WALLS[f]),0,.3+(FH-.3)/2,-DP/2,g);
  box(.3,FH-.3,DP,M(gold?0xFFD76A:0x8d86a8),-W/2,.3+(FH-.3)/2,0,g);box(.3,FH-.3,DP,M(gold?0xFFD76A:0x8d86a8),W/2,.3+(FH-.3)/2,0,g);
  const L=new THREE.PointLight(0xfff0c8,.45,14,1.6);L.position.set(0,FH-.6,2);g.add(L);
  box(3,1.6,.1,new THREE.MeshBasicMaterial({color:0xffe9a8}),f%2?-2.6:2.6,1.9,-DP/2+.2,g);
  rooms.push(g)}
const roof=new THREE.Group();scene.add(roof);
box(W+1,.6,DP+1,M(0x44406a),0,.3,0,roof);
const sign=new THREE.Mesh(new THREE.PlaneGeometry(11,3.4),new THREE.MeshBasicMaterial({map:txtTex('10,000','#140c04','#FFC24B',800,250,'900 190px sans-serif'),side:THREE.DoubleSide}));scene.add(sign);
const ch={};
const mk=(k,o,x,f,z,sc)=>{const c=mkChar(o);c.g.scale.setScalar(sc||1.0);c.g.position.set(x,f*FH+.3,z||0);c.y0=c.g.position.y;scene.add(c.g);ch[k]=c;return c};
box(3,2.4,.2,M(0x6b3e1f),0,1.5,DP/2-.1,rooms[0]);
mk('argA',{shirt:0xE5484D,hair:0x5a2a10,long:true,skin:0xe8b48a,ph:.7},-2.2,2,0);
mk('argB',{shirt:0x3fa7ff,hair:0x2a160c,skin:0xf1c7a2,ph:.1},-.2,2,0);
mk('l1',{shirt:0xC792EA,hair:0x2a160c,skin:0xf1c7a2,ph:.9},-3,4,0);mk('l2',{shirt:0xFFC24B,hair:0x5a2a10,long:true,skin:0xe8b48a,ph:.2},-1,5,0);mk('l3',{shirt:0x3fa7ff,hair:0x111111,skin:0xd9a37a,ph:1.3},-2,6,0);
mk('jump',{shirt:0xFF9F1C,hair:0x2a160c,skin:0xf1c7a2,ph:.3},-2,1,0);
mk('drill',{shirt:0x2fbf71,hair:0x111111,skin:0xd9a37a,ph:.5},-2,3,0);

const CX=4.7,car=new THREE.Group(),bagA=new THREE.Group(),bagB=new THREE.Group(),dog=new THREE.Group();
const P1={g:new THREE.Group()},P2={g:new THREE.Group()},P3={g:new THREE.Group()};
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)},L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k);
// escalier + palier a l'etage 2 (cote droit) : le residant et le voisin bavard
const SF=2,SY=SF*FH+.3;
for(let i=0;i<7;i++)box(1.1,.2,1.6,M(0xd9c7a0),-5.2+i*.5,SY-2.6+i*.4,-1.8,scene);

// rampe

// horloge murale sur le mur du fond
const clk=new THREE.Group();clk.position.set(-1.6,SY+2.3,-DP/2+.3);scene.add(clk);
const face=new THREE.Mesh(new THREE.CylinderGeometry(.8,.8,.12,32),new THREE.MeshBasicMaterial({color:0xffffff}));face.rotation.x=Math.PI/2;clk.add(face);
const rim=new THREE.Mesh(new THREE.TorusGeometry(.8,.07,8,32),new THREE.MeshBasicMaterial({color:0xE5484D}));clk.add(rim);
const hh=new THREE.Group();hh.position.z=.09;clk.add(hh);const hmin=box(.07,.55,.04,new THREE.MeshBasicMaterial({color:0x111111}),0,.28,0,hh);
const hh2=new THREE.Group();hh2.position.z=.1;clk.add(hh2);box(.09,.38,.04,new THREE.MeshBasicMaterial({color:0x111111}),0,.18,0,hh2);
const RES=mk('res',{shirt:0x3fa7ff,hair:0x2a160c,skin:0xf1c7a2,ph:.3},0.4,SF,.2,1.0);
const NEI=mk('nei',{shirt:0xFFC24B,hair:0x5a2a10,skin:0xe8b48a,ph:.9,pants:0x3a3a60},2.4,SF,.2,1.0);
const bagG=box(.55,.75,.4,M(0x2fbf71),0,0,0),bagY=box(.5,.65,.4,M(0xFFC24B),0,0,0);
const cone=new THREE.Group();scene.add(cone);box(.22,.5,.22,M(0xd9a86a),0,-.3,0,cone);const sc1=new THREE.Mesh(new THREE.SphereGeometry(.3,16,12),M(0xff9ec7,0xff6fa8,.25));sc1.position.y.set;sc1.position.set(0,.05,0);cone.add(sc1);
const drip=box(.14,.4,.14,M(0xff9ec7),0,-.6,0,cone);
const SEATS=[];const GOLDL=new THREE.PointLight(0xffd070,0,40,1.2);GOLDL.position.set(0,12*FH,10);scene.add(GOLDL);
const NEW=[];for(let i=0;i<5;i++){NEW.push(mk('n'+i,{shirt:[0xE5484D,0x3fa7ff,0xC792EA,0x2fbf71,0xFF9F1C][i],hair:0x2a160c,skin:0xf1c7a2,ph:i*.7},-3+i*1.5,11+i,0,.9))}
window.F=function(o){const t=o.t,T=o.dur;let cam,look;
 animChar(ch.argA,t,.8,'talk');animChar(ch.argB,t+.4,.8,'talk');ch.argA.g.rotation.y=.5;ch.argB.g.rotation.y=-.5;
 animChar(ch.jump,t,.5,'talk');ch.jump.g.position.y=ch.jump.y0+Math.abs(Math.sin(t*7))*.5;
 animChar(ch.drill,t,.3,'talk');animChar(ch.l1,t,.1,'talk');animChar(ch.l2,t+.5,.1,'talk');animChar(ch.l3,t+1,.1,'talk');
 car.visible=false;[P1,P2,P3,bagA,bagB,dog].forEach(x=>{(x.g||x).visible=false});
 const sh=o.shot;ch.argA.g.visible=ch.argB.g.visible=(sh!=='stair');const stairShot=(sh==='stair');
 [RES,NEI,bagG,bagY,cone,clk].forEach(x=>{(x.g||x).visible=stairShot});
 const bt=o.BT;let grow=[1,1,1,1,1];
 if(sh==='top'){grow=bt.map(b=>E((t-b)/.4))}else if(sh==='wide'||sh==='stair'){grow=[0,0,0,0,0]}
 for(let f=0;f<NF;f++){const g=rooms[f];if(f<11){g.visible=true;g.scale.y=1}else{const k=grow[f-11];g.visible=k>0.02;g.scale.y=Math.max(.02,k)}}
 let acc=11*FH;for(let i=0;i<5;i++){const g=rooms[11+i];g.position.y=acc;acc+=g.visible?FH*grow[i]:0}
 roof.position.y=acc;sign.position.set(0,acc+3.4,0);sign.lookAt(camera.position.x,acc+3.4,camera.position.z);sign.visible=(sh!=='stair');
 NEW.forEach((c,i)=>{c.g.visible=(sh==='top'&&grow[i]>.95)||sh==='end';animChar(c,t,.4,'cheer')});
 GOLDL.intensity=(sh==='top'||sh==='end')?1.6:0;
 if(sh==='wide'){const k=E(t/T);cam=[Math.sin(k*1.2)*6,2+k*16,34-4*k];look=[0,8+k*20,0];}
 else if(sh==='stair'){
   const u=t/T; // 0..1
   // clock : accelere
   hmin.parent.rotation.z=-(u*u*40);hh2.rotation.z=-(u*u*3.3);
   const talk=.6+.4*Math.abs(Math.sin(t*9));
   animChar(NEI,t,talk,'talk');animChar(RES,t,.1,'talk');
   RES.g.position.set(0.4,SY,.4);NEI.g.position.set(2.4,SY,.4);NEI.g.rotation.y=-.9;RES.g.rotation.y=.9;
   NEI.aR.rotation.x=-1.2+Math.sin(t*10)*.5;
   bagG.position.set(-.3,SY+.9,.8);bagY.position.set(.9,SY+.85,.8);
   RES.aL.rotation.x=-.9;
   cone.position.set(.05,SY+1.95,.75);
   const melt=E((u-.35)/.5);sc1.scale.set(1+melt*.4,1-melt*.6,1+melt*.4);drip.scale.y=.3+melt*3;drip.position.y=-.6-melt*.45;
   cam=[1.2+Math.sin(t*.8)*.25,SY+2.6,11.5-u*3.2];look=[1.2,SY+3.1,0];}
 else if(sh==='top'){const k=E(t/T);cam=L([4,11*FH+8,30],[8,acc+2,50],k);look=L([0,11*FH+4,0],[0,acc-10,0],k);}
 else{const k=E(t/T);cam=[-Math.sin((1-k)*1.2)*7,acc*.5-k*2,acc*.9+14+k*10];look=[0,acc*.55,0];}
 camera.position.set(...cam);camera.lookAt(...look);R.render(scene,camera)};

window.ready=true;
</script></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=float(os.environ.get('DSF', 1.4)))
    pg.route('http://local/three.min.js', lambda r: r.fulfill(path=f'{NM}/three/build/three.min.js', content_type='text/javascript'))
    pg.route('http://local/', lambda r: r.fulfill(body=HTML, content_type='text/html'))
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('http://local/'); pg.wait_for_function('window.ready===true', timeout=60000); pg.wait_for_timeout(300)
    n = int(round(DUR * FPS))
    for i in range(int(os.environ.get('START', 0)), int(os.environ.get('END', n))):
        pg.evaluate('o=>F(o)', {'shot': SHOT, 't': i / FPS, 'dur': DUR, 'T0': float(os.environ.get('T0', 2.08)), 'T1': float(os.environ.get('T1', 3.02)), 'T2': float(os.environ.get('T2', 4.22)), 'BT': [float(x) for x in os.environ.get('BT', '4.5,5.0,5.5').split(',')]})
        pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
    print(SHOT, 'images', n, 'erreurs', errs[:5]); b.close()
