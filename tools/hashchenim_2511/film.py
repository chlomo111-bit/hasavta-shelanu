"""השכנים – 25.11 matin, חלק 6 : « קבוצת הוואטסאפ של הבניין ».
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

const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)},L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k);
const SF=2,SY=SF*FH+.3;
for(let i=0;i<7;i++)box(1.1,.2,1.6,M(0xd9c7a0),-5.2+i*.5,SY-2.6+i*.4,-1.8,scene);
// cartons empiles sur le palier de l'etage 2
const BOXES=[];const cb=M(0xC89A5E),cb2=M(0xB5864A),tape=M(0xE8D9A8);
[[-2.2,0,.9,.9,.9],[-1.2,0,.8,1,.8],[-.2,0,1,.8,.9],[-1.7,.9,.8,.7,.8],[-.6,.8,.9,.9,.8],[-1.2,1.6,.7,.7,.7],[.9,0,.8,.7,.8]].forEach((b,i)=>{const bx=box(b[2],b[3],b[4],i%2?cb:cb2,b[0],SY+b[1]+b[3]/2,.6);box(b[2]+.02,.12,b[4]+.02,tape,0,0,0,bx);bx.children[0].position.y=b[3]/2-.05;BOXES.push(bx)});
const mkPhone=(c,col)=>{const p=box(.5,.8,.06,new THREE.MeshStandardMaterial({color:0x111111,emissive:col||0x25D366,emissiveIntensity:1.2}),0,0,0);scene.add(p);return p};
const RES=mk('res',{shirt:0x3fa7ff,hair:0x2a160c,skin:0xf1c7a2,ph:.3},1.3,SF,1.2,1.0);const rph=mkPhone();
const RUN=[];const cols=[0xE5484D,0x3fa7ff,0xC792EA,0x2fbf71,0xFF9F1C,0xFFC24B,0xff7aa8,0x4fd1c5];
for(let i=0;i<8;i++){const f=3+i;const c=mk('r'+i,{shirt:cols[i],hair:[0x2a160c,0x5a2a10,0x111111][i%3],long:i%2==1,skin:[0xf1c7a2,0xe8b48a,0xd9a37a][i%3],ph:i*.8},i%2?2.3:-2.3,f,.2,1.0);c.phone=mkPhone(0,i%3==0?0x25D366:0x34B7F1);RUN.push(c)}
const NEW=[];for(let i=0;i<5;i++){NEW.push(mk('n'+i,{shirt:[0xE5484D,0x3fa7ff,0xC792EA,0x2fbf71,0xFF9F1C][i],hair:0x2a160c,skin:0xf1c7a2,ph:i*.7},-3+i*1.5,11+i,0,.9))}
const GOLDL=new THREE.PointLight(0xffd070,1.6,60,1.2);GOLDL.position.set(0,12*FH,12);scene.add(GOLDL);
const outer0=x=>x==='wide'||x==='end';const acc=16*FH;roof.position.y=acc;sign.position.set(0,acc+3.4,0);
window.F=function(o){const t=o.t,T=o.dur,sh=o.shot;let cam,look;
 sign.lookAt(camera.position.x,acc+3.4,camera.position.z);GOLDL.intensity=outer0(sh)?1.6:0;
 const outer=(sh==='wide'||sh==='end');
 NEW.forEach(c=>{c.g.visible=outer;animChar(c,t,.4,'cheer')});
 RES.g.visible=rph.visible=(sh==='cart'||sh==='cart2');
 BOXES.forEach(b=>b.visible=(sh==='cart'||sh==='cart2'||outer));
 RUN.forEach((c,i)=>{c.g.visible=(sh==='ride'||sh==='ride2'||outer);c.phone.visible=c.g.visible;
   const pos=c.g.position;c.phone.position.set(pos.x+(i%2?-.35:.35),pos.y+1.2,pos.z+.5);c.phone.rotation.y=0;
   const fl=.6+.4*Math.abs(Math.sin(t*5+i*1.7));c.phone.material.emissiveIntensity=.7+fl;
   animChar(c,t,.2,'talk');c.g.rotation.y=(i%2?-.5:.5);
   if(sh==='ride'&&i<3){const bt=[0.0,.68,1.38][i];const u=t-bt;if(u>0&&u<.7){c.g.rotation.y=Math.sin(u*22)*.9}}});
 if(sh==='wide'){const k=t/T;cam=[Math.sin(k*1.2)*6,2+k*16,34-4*k];look=[0,8+k*20,0]}
 else if(sh==='end'){const k=1-t/T;cam=[Math.sin(k*1.2)*6,2+k*16,34-4*k];look=[0,8+k*20,0]}
 else if(sh==='cart'||sh==='cart2'){
   const u=t/T;const talk=.5+.5*Math.abs(Math.sin(t*9));animChar(RES,t,.15,'talk');
   RES.g.position.set(1.3,SY,1.4);RES.g.rotation.y=-.35;rph.position.set(.95,SY+1.5,1.9);rph.material.emissiveIntensity=1+Math.sin(t*8)*.5;
   BOXES.forEach((b,i)=>{b.rotation.z=sh==='cart2'?Math.sin(t*9+i)*.02:0});
   if(sh==='cart'){cam=[L([4,SY+3,16],[.6,SY+2,9.5],E(u))[0],L([4,SY+3,16],[.6,SY+2,9.5],E(u))[1],L([4,SY+3,16],[.6,SY+2,9.5],E(u))[2]];look=[-.4,SY+1.2,0]}
   else{const k=E(u);cam=L([.8,SY+2.1,10],[-.2,SY+1.7,6.3],k);look=[-.5,SY+1.3,0]}}
 else if(sh==='ride'){const k=E(t/T);cam=[0,3*FH+3.2+k*2*FH,10];look=[0,3*FH+3.2+k*2*FH,0]}
 else{const k=E(t/T);cam=[Math.sin(k*1.4-.7)*1.8,6*FH+3.2-k*3*FH,10];look=[0,6*FH+3.2-k*3*FH,0]}
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
        pg.evaluate('o=>F(o)', {'shot': SHOT, 't': i / FPS, 'dur': DUR, 'BT':[]})
        pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
    print(SHOT, 'images', n, 'erreurs', errs[:5]); b.close()
