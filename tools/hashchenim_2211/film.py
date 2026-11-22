"""השכנים – 22.11 « הבניין הכי גבוה בעולם? » (stratégie RECORD DU MONDE).
Tour de 100 étages (objectif 10,000 דיירים, 1 étage / 100) : seul le rez-de-chaussée est construit, les 99 étages
au-dessus sont en « plan » (verre translucide + arêtes lumineuses), couronne « 10,000 » au sommet, ville de nuit allumée autour.
Plans : rise | demo | empty | end. Usage : DSF=1.5 python3 film.py <node_modules> <dossier> <plan> <durée_s> [fps]"""
import sys, os, re
from playwright.sync_api import sync_playwright
NM, OUT, SHOT, DUR = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]); FPS = int(sys.argv[5]) if len(sys.argv) > 5 else 30
os.makedirs(OUT, exist_ok=True)
CHAR_JS = re.search(r"CHAR_JS = r'''(.*?)'''", open('/home/claude/thenoise/tools/film3d.py').read(), re.S).group(1)
HTML = """<!doctype html><html><head><meta charset=utf-8><style>html,body{margin:0;background:#000;overflow:hidden}canvas{display:block}</style></head><body>
<script src="http://local/three.min.js"></script><script>""" + CHAR_JS + r"""</script><script>
const R=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});R.setPixelRatio(window.devicePixelRatio);R.setSize(540,960);document.body.prepend(R.domElement);
const scene=new THREE.Scene();
// ciel du soir dégradé (clair en bas, pas de noir)
const sc=document.createElement('canvas');sc.width=4;sc.height=256;const sg=sc.getContext('2d');const gr=sg.createLinearGradient(0,0,0,256);
gr.addColorStop(0,'#1b1d5e');gr.addColorStop(.55,'#5a3f9a');gr.addColorStop(.85,'#e0709a');gr.addColorStop(1,'#ffb27a');sg.fillStyle=gr;sg.fillRect(0,0,4,256);
const skyT=new THREE.CanvasTexture(sc);const sky=new THREE.Mesh(new THREE.SphereGeometry(900,32,16),new THREE.MeshBasicMaterial({map:skyT,side:THREE.BackSide,fog:false}));scene.add(sky);
scene.fog=new THREE.Fog(0x6a4aa0,250,900);
const camera=new THREE.PerspectiveCamera(60,540/960,.1,2000);
scene.add(new THREE.HemisphereLight(0xc8ccff,0x403050,.75));const sun=new THREE.DirectionalLight(0xffc8a0,.8);sun.position.set(-60,80,120);scene.add(sun);
const M=(c,e,ei)=>new THREE.MeshStandardMaterial({color:c,roughness:.8,emissive:e||0,emissiveIntensity:ei||0});
const box=(w,h,d,m,x,y,z,p)=>{const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);b.position.set(x,y,z);(p||scene).add(b);return b};
const FH=3,W=20,DP=12,NF=100;
// sol + rue
box(600,.2,600,M(0x2a2540),0,-.1,0);box(600,.05,10,M(0x3a3550),0,.01,16);
// rez-de-chaussée construit (étage 0) : façade crème, 10 fenêtres chaudes
box(W,FH,DP,M(0xc9a97e),0,FH/2,0);
const WARM=new THREE.MeshBasicMaterial({color:0xffc870}),DARKW=M(0x22284a,0x101030,.2);
// porte d'entrée + auvent
box(3,2.4,.3,M(0x6b3e1f),0,1.2,DP/2+.1);box(5,.25,1.6,M(0xC792EA,0x8a50c0,.5),0,2.7,DP/2+.8);
// enseigne « השכנים »
function txtTex(t,bg,fg,w,h,f){const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');g.fillStyle=bg;g.fillRect(0,0,w,h);g.fillStyle=fg;g.font=f;g.textAlign='center';g.textBaseline='middle';g.fillText(t,w/2,h/2);return new THREE.CanvasTexture(c)}
// étages « en projet » : verre translucide + arêtes
const ghostM=new THREE.MeshStandardMaterial({color:0x7fd0ff,transparent:true,opacity:.16,emissive:0x2a6aa0,emissiveIntensity:.5,depthWrite:false});
const ghost=box(W,FH*(NF-1),DP,ghostM,0,FH+FH*(NF-1)/2,0);
const edgeM=new THREE.LineBasicMaterial({color:0x9fe4ff,transparent:true,opacity:.55});
for(let f=1;f<NF;f++){const y=f*FH;const geo=new THREE.EdgesGeometry(new THREE.BoxGeometry(W,.01,DP));const l=new THREE.LineSegments(geo,edgeM);l.position.set(0,y,0);scene.add(l)}
[[-W/2,-DP/2],[W/2,-DP/2],[-W/2,DP/2],[W/2,DP/2]].forEach(([x,z])=>box(.35,FH*NF,.35,M(0xbfefff,0x6fc8ff,.9),x,FH*NF/2,z));
// fenêtres-fantômes (cases) sur la façade avant, tous les étages : instanced
const winG=new THREE.PlaneGeometry(1.3,1.6);const gwM=new THREE.MeshBasicMaterial({color:0xbfe8ff,transparent:true,opacity:.22,depthWrite:false});
const IM=new THREE.InstancedMesh(winG,gwM,(NF-1)*10);let k=0;const mt=new THREE.Matrix4();
for(let f=1;f<NF;f++)for(let i=0;i<10;i++){mt.makeTranslation(-W/2+1+i*2,f*FH+1.6,DP/2+.02);IM.setMatrixAt(k++,mt)}scene.add(IM);
// fenêtres réelles du RDC + 1er étage de démonstration (allumables)
const RDC=[],DEMO=[];
for(let i=0;i<10;i++){const x=-W/2+1+i*2;
  if(Math.abs(x)>1.6){const w=box(1.3,1.5,.08,DARKW,x,1.7,DP/2+.05);RDC.push(w)} else RDC.push(null);
  const d=box(1.3,1.6,.08,new THREE.MeshBasicMaterial({color:0x22284a}),x,FH+1.6,DP/2+.06);d.visible=false;DEMO.push(d)}
// panneaux « פנוי » sur 5 fenêtres du RDC
const FREE=[];[0,1,2,7,8].forEach(i=>{const x=-W/2+1+i*2;const p=new THREE.Mesh(new THREE.PlaneGeometry(1.2,.5),new THREE.MeshBasicMaterial({map:txtTex('?','#2fbf71','#fff',256,108,'900 90px sans-serif')}));p.position.set(x,1.7,DP/2+.11);p.visible=false;scene.add(p);FREE.push(p)});
const rdcL=new THREE.PointLight(0xffc070,0,30,1.5);rdcL.position.set(0,2,DP/2+5);scene.add(rdcL);
// couronne au sommet + panneau 10,000
const TOP=FH*NF;const crown=new THREE.Group();crown.position.set(0,TOP,0);scene.add(crown);
const GOLD=new THREE.MeshStandardMaterial({color:0xFFC24B,metalness:.8,roughness:.25,emissive:0xb07800,emissiveIntensity:1.2});
box(W+1,1,DP+1,GOLD,0,.5,0,crown);for(let i=0;i<5;i++){const s=box(1.2,4,1.2,GOLD,-8+i*4,3,0,crown);s.rotation.y=.785}
const sign=new THREE.Mesh(new THREE.PlaneGeometry(16,5),new THREE.MeshBasicMaterial({map:txtTex('10,000','#140c04','#FFC24B',800,250,'900 190px sans-serif'),side:THREE.DoubleSide}));sign.position.set(0,TOP+8,DP/2);scene.add(sign);
const beam=new THREE.PointLight(0xffd070,3,60,1.2);beam.position.set(0,TOP+6,8);scene.add(beam);
// ville autour : tours aux fenêtres allumées (texture procédurale)
function cityTex(seed){const c=document.createElement('canvas');c.width=64;c.height=256;const g=c.getContext('2d');g.fillStyle='#262a52';g.fillRect(0,0,64,256);let s=seed;const r=()=>{s=(s*16807)%2147483647;return s/2147483647};
 for(let y=4;y<256;y+=10)for(let x=4;x<64;x+=10)if(r()<.62){g.fillStyle=r()<.8?'#ffd98a':'#9fd8ff';g.fillRect(x,y,6,6)}return new THREE.CanvasTexture(c)}
let s=91;const rnd=()=>{s=(s*16807)%2147483647;return s/2147483647};
for(let i=0;i<70;i++){const a=rnd()*Math.PI*2,rr=40+rnd()*220;const x=Math.cos(a)*rr,z=Math.sin(a)*rr-40;if(Math.abs(x)<26&&z>-30&&z<60)continue;
 const h=15+rnd()*(rr<90?70:120),w=8+rnd()*12;const t=cityTex(i*7+3);t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(w/16,h/40);
 box(w,h,w,new THREE.MeshStandardMaterial({map:t,emissive:0xffffff,emissiveMap:t,emissiveIntensity:.9,roughness:.9}),x,h/2,z)}
// voisin de démonstration (apparaît dans la 1re fenêtre allumée)
const nb=mkChar({shirt:0xE5484D,hair:0x2a160c,long:true,skin:0xf1c7a2,ph:.4});nb.g.scale.setScalar(.9);scene.add(nb.g);nb.g.visible=false;
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)},L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k);
function lit(m,on,col){m.material.color.setHex(on?col:0x22284a)}
window.F=function(o){const t=o.t;let cam,look;
 RDC.forEach(w=>w&&(w.material=WARM));rdcL.intensity=1.2;FREE.forEach(p=>p.visible=false);DEMO.forEach(d=>{d.visible=false});nb.g.visible=false;
 sign.lookAt(camera.position.x,TOP+8,camera.position.z);
 if(o.shot==='rise'){const k=E(t/o.dur);const y=2+ (TOP+4)*Math.pow(k,1.25);
   cam=[Math.sin(k*1.2)*8, y, 40-14*k];look=[0, Math.min(TOP+8,y+30+30*(1-k)), 0];}
 else if(o.shot==='demo'){DEMO.forEach(d=>d.visible=true);
   // 0-1.6 s : 1 fenêtre (like) ; 1.6-3.2 : 3 (comment) ; 3.2+ : 10 (share)
   const T1=o.T1||1.6,T2=o.T2||3.2;const n=t<T1?1:(t<T2?3:10);const pop=t<T1?t:(t<T2?t-T1:t-T2);
   DEMO.forEach((d,i)=>{const order=[4,5,3,6,2,7,1,8,0,9];const on=order.indexOf(i)<n;lit(d,on,n===10?0xFFC24B:0xffd98a);
     const sc=on&&order.indexOf(i)>=(n===1?0:n===3?1:3)?Math.min(1,.4+pop*4):1;d.scale.set(sc,sc,1)});
   nb.g.visible=true;nb.g.position.set(-W/2+1+4*2,FH+.25,DP/2-.6);nb.g.rotation.y=0;animChar(nb,t,.4,'talk');nb.g.position.set(0,FH+.1,DP/2+.7);
   cam=L([2,FH+1.8,15],[0,FH+1.6,12.5],E(t/o.dur));look=[0,FH+1.4,0];}
 else if(o.shot==='empty'){FREE.forEach((p,i)=>{p.visible=t>i*.25;p.scale.setScalar(Math.min(1,(t-i*.25)*5))});
   cam=L([-12,2.2,13],[8,2.0,12],E(t/o.dur));look=L([-6,1.7,0],[4,1.7,0],E(t/o.dur));}
 else { const k=E(t/o.dur);const y=(TOP*.55)*(1-k)+2;cam=[-Math.sin((1-k)*1.2)*8,y,26+14*k];look=[0,y+30+30*k,0];}
 camera.position.set(...cam);camera.lookAt(...look);R.render(scene,camera)};
window.ready=true;
</script></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=float(os.environ.get('DSF', 1.5)))
    pg.route('http://local/three.min.js', lambda r: r.fulfill(path=f'{NM}/three/build/three.min.js', content_type='text/javascript'))
    pg.route('http://local/', lambda r: r.fulfill(body=HTML, content_type='text/html'))
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('http://local/'); pg.wait_for_function('window.ready===true', timeout=60000); pg.wait_for_timeout(300)
    n = int(round(DUR * FPS)); step = int(os.environ.get('STEP', 1))
    for i in range(int(os.environ.get('START', 0)), int(os.environ.get('END', n)), step):
        pg.evaluate('o=>F(o)', {'shot': SHOT, 't': i / FPS, 'dur': DUR, 'T1': float(os.environ.get('T1', 1.6)), 'T2': float(os.environ.get('T2', 3.2))})
        pg.screenshot(path=f'{OUT}/f{i:04d}.jpg', type='jpeg', quality=90, timeout=240000)
    print(SHOT, 'images', n, 'erreurs', errs[:5]); b.close()
