// Ruche 22.11 « הכוורת הכי גדולה בעולם? » חלק 1 : ruche géante VIDE + reine géante ; démo du barème (1 / 3 / 10 abeilles qui entrent).
try{localStorage.setItem('kaveret_ev50','1');localStorage.setItem('kaveret_ev100','1')}catch(e){}
started=true;introT=END;document.getElementById('gate').hidden=true;document.getElementById('skip').hidden=true;
loop();endIntro();document.getElementById('ui').style.display='none';controls.enabled=false;treasureHit=null;foundShown=true;MET.since=-100;treasure.visible=false;
try{capEl.style.display="none"}catch(e){}
window.pickLabels=function(){shown=[];pool.forEach(s=>s.visible=false)};
window.capHook=(T)=>{try{pool.forEach(s=>s.visible=false);shown=[]}catch(e){};treasure.visible=false};
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
EV.form={k:1,tg:{}};
window.SH={shot:'test',t:0};
const _ub=updateBees;updateBees=function(t,dt){post(t);_ub(t,dt)};
const HID=new THREE.Vector3(0,-300,0);
// דבורה = la grande abeille « professeure » : couronne cachée, lunettes rondes, bouche qui s'ouvre avec la voix
giant.children.forEach(c=>{if(c.isMesh&&c.material===accMat)c.visible=false});
const glasses=new THREE.Mesh(ACC.glasses,accMat);glasses.position.set(.622,.08,0);giant.add(glasses);
const mouth=new THREE.Mesh(merge([boxGeo(.03,.06,.15,0,0,0,"#D81F4B")]),accMat);mouth.position.set(.615,-.075,0);giant.add(mouth);
const amp=t=>{const AMP=(window.SHX&&window.SHX.amp)||[];const i=Math.floor(t*30);return AMP[Math.max(0,Math.min(AMP.length-1,i))]||0};
const P0=new THREE.Vector3(0,14,0),V=(x,y,z)=>new THREE.Vector3(x,y,z);
const FACE=-Math.PI/2; // tête vers la caméra (+z)
function dvora(pos,yaw,pitch,roll,s,a,gt){placeGiant(pos,yaw,s*(1+.07*a),gt);giant.rotation.set(roll,yaw,pitch);const m=Math.min(1,a);mouth.scale.set(1,.45+1.5*m,1+.25*m)}

// ---- תמנון 3D ----
const OCT=new THREE.Group();hive.add(OCT);
const mPink=new THREE.MeshLambertMaterial({color:0x9B2FB0,transparent:true,opacity:1,depthWrite:true});
const mPink2=new THREE.MeshLambertMaterial({color:0x7E2092});
const mWhite=new THREE.MeshBasicMaterial({color:0xffffff}),mBlack=new THREE.MeshBasicMaterial({color:0x111111});
const mHeart=new THREE.MeshBasicMaterial({color:0xB0001A}),mHeartB=new THREE.MeshBasicMaterial({color:0xC8102E});
const head=new THREE.Mesh(new THREE.SphereGeometry(1.7,28,20),mPink);head.scale.set(1,1.2,1);OCT.add(head);
const eyes=[];for(const sx of[-1,1]){const e=new THREE.Mesh(new THREE.SphereGeometry(.42,16,12),mWhite);e.position.set(sx*.72,-.15,1.42);OCT.add(e);const p=new THREE.Mesh(new THREE.SphereGeometry(.2,12,10),mBlack);p.position.set(sx*.72,-.15,1.78);OCT.add(p);eyes.push(e,p)}
const smile=new THREE.Mesh(new THREE.TorusGeometry(.38,.07,8,16,Math.PI),mBlack);smile.rotation.z=Math.PI;smile.position.set(0,-.78,1.55);OCT.add(smile);
const heartShape=new THREE.Shape();heartShape.moveTo(0,-.5);heartShape.bezierCurveTo(-.9,.1,-.55,.8,0,.35);heartShape.bezierCurveTo(.55,.8,.9,.1,0,-.5);
const hg=new THREE.ExtrudeGeometry(heartShape,{depth:.35,bevelEnabled:true,bevelSize:.06,bevelThickness:.06,bevelSegments:2});hg.translate(0,0,-.17);
const hearts=[0,1,2].map(i=>{const h=new THREE.Mesh(hg,i===1?mHeart:mHeartB);h.renderOrder=5;OCT.add(h);return h});
const HP=[V(-1.15,.15,.2),V(0,.55,.2),V(1.15,.15,.2)]; // 2 petits (zimes) + 1 grand (corps)
const tent=[];const NT=8,NS=11;
for(let i=0;i<NT;i++){const a=i/NT*Math.PI*2,row=[];for(let j=0;j<NS;j++){const r=.36-.026*j;const s=new THREE.Mesh(new THREE.SphereGeometry(Math.max(.07,r),10,8),j%2?mPink:mPink2);OCT.add(s);row.push(s)}tent.push({a,row})}
const drops=[];for(let i=0;i<14;i++){const d=new THREE.Mesh(new THREE.SphereGeometry(.16,8,6),new THREE.MeshBasicMaterial({color:i<7?0x4FC3F7:0xFF4D6A}));d.visible=false;OCT.add(d);drops.push(d)}
const floaters=[];for(let i=0;i<8;i++){const h=new THREE.Mesh(hg,mHeartB);h.scale.setScalar(.5);h.visible=false;hive.add(h);floaters.push(h)}
function octo(pos,s,t,o){ // o={xray,beat:[b0,b1,b2],flow,wave,yaw}
  OCT.visible=true;OCT.position.copy(pos);OCT.scale.setScalar(s);OCT.rotation.set(0,o.yaw||0,0);
  head.scale.set(1,1.2+Math.sin(t*3)*.02,1);
  mPink.opacity=o.xray?0.3:1;mPink.depthWrite=!o.xray;
  eyes.forEach(e=>e.visible=!!(!o.xray||o.eyes));smile.visible=!!(!o.xray||o.eyes);
  hearts.forEach((h,i)=>{h.visible=!!o.xray||o.hs;const b=(o.beat&&o.beat[i])||0,pul=1+.16*Math.sin(t*8+i)+b*.5;const sc=(i===1?.95:.62)*pul*(o.hscale||1);h.scale.setScalar(sc);h.position.copy(HP[i]);h.position.z+=.9})
  tent.forEach((T,i)=>{for(let j=0;j<NS;j++){const u=j/(NS-1),R=1.05+u*.9;const ph=t*2.2+i*.8-j*.45,wv=(o.wave&&i===(o.wave|0)?1.6:.45);
    T.row[j].position.set(Math.cos(T.a)*(R*.75)+Math.sin(ph)*.35*u*wv*1.6,-1.75-u*3.0+(o.wave&&i===(o.wave|0)?u*2.3:0),Math.sin(T.a)*(R*.75)*.7+Math.cos(ph)*.3*u)}});
  drops.forEach((d,k)=>{const f=o.flow|0;const blue=k<8,on=blue?(f&1):(f&2);if(!on){d.visible=false;return}d.visible=true;const u=((t*1.1+k*.19)%1);
    if(blue){const s2=k<4?-1:1;d.position.set(s2*(1.0+u*1.7),.3+(u-.5)*.6,1.3);d.material.color.setHex(0x4FC3F7)}
    else{d.position.set(Math.sin(k)*.3*u,.7-u*3.4,1.2-u*.2);d.material.color.setHex(0xFF4D6A)}d.scale.setScalar(.8+.6*Math.sin(u*3.14))});
  floaters.forEach((f,i)=>{if(!o.fl){f.visible=false;return}f.visible=true;const u=((t*.45+i/8)%1);f.position.set(pos.x+Math.sin(i*2.1+t)*3.2,pos.y-2+u*9,pos.z+1.5+Math.cos(i)*1.0);f.rotation.y=Math.sin(t*2+i)*.6;f.scale.setScalar(.35+.2*Math.sin(i))})}
const jar=new THREE.Group();{const gl=new THREE.Mesh(new THREE.CylinderGeometry(.9,.9,1.5,20),new THREE.MeshLambertMaterial({color:0xFFB300}));const lid=new THREE.Mesh(new THREE.CylinderGeometry(.95,.95,.25,20),new THREE.MeshLambertMaterial({color:0x7A4A12}));lid.position.y=.85;const lab=new THREE.Mesh(new THREE.CylinderGeometry(.93,.93,.7,20),new THREE.MeshLambertMaterial({color:0xFFF3D0}));jar.add(gl,lid,lab);hive.add(jar);jar.visible=false}
let tg;
function followers(t,mode,ctr){}
const AT=(a,b,t)=>E((t-a)/(b-a));
function post(gt){
  const S=window.SH,t=S.t,a=amp(t);EV.form.k=1;tg=EV.form.tg;
  for(let i=0;i<30;i++)tg[i]=HID;
  giant.visible=true;jar.visible=false;const bob=Math.sin(t*7)*.12*(.4+a);
  const K={c1:2.5,c2:4.65,c3:7.4,c4:9.8};
  if(t<K.c1){ // 1 accroche : דבורה en haut parle, תמנון au centre
    const k=AT(0,K.c1,t);
    dvora(V(-2.0,16.6+bob,0),FACE+.3+Math.sin(t*2.6)*.1,Math.sin(t*3)*.05,Math.sin(t*2.2)*.06,2.5,a,gt);
    octo(V(.5,13.0+Math.sin(t*3)*.12,0),.95,t,{hs:false,yaw:-.15,wave:3});
    camera.position.set(Math.sin(t*.6)*.5,14.6,14.2-2.0*k);camera.lookAt(0,14.4,0)}
  else if(t<K.c2){ // 2 rayons X : 3 cœurs comptés
    const k=AT(K.c1,K.c2,t),tt=t-K.c1;
    const bt=i=>Math.max(0,1-Math.abs(tt-(.2+i*.45))*3);
    dvora(V(-2.5,12.2+bob,2.5),FACE+.6,0,0,.9,a,gt);
    octo(V(0,15.0,0),1.1,t,{xray:true,flow:tt>1.2?1:0,beat:[bt(0),bt(1),bt(2)],yaw:0,wave:-1});
    camera.position.set(Math.sin(t*.8)*.4,14.9,9.8-1.2*k);camera.lookAt(0,14.9,0)}
  else if(t<K.c3){ // 3 flux : 2 -> זימים (bleu), 1 -> גוף (rouge)
    const k=AT(K.c2,K.c3,t);
    dvora(V(-2.5,12.2+bob,2.5),FACE+.6,0,0,.9,a,gt);
    octo(V(0,15.0,0),1.1,t,{xray:true,flow:t<4.65?1:2,beat:[0,0,0],eyes:true});
    camera.position.set(-1+k*2,14.5,8.6+Math.sin(t*.6)*.3);camera.lookAt(0,14.2,0)}
  else if(t<K.c4){ // 4 « שלחו לחבר עם לב ענק »
    const k=t-K.c3;
    dvora(V(-1.4+Math.sin(k*3)*.3,13.6+Math.abs(Math.sin(k*4))*.3,0),FACE+.4+Math.sin(k*3)*.2,Math.sin(k*4)*.08,0,1.9,a,gt);
    octo(V(1.7,16.6,-2),.6,t,{hs:true,hscale:.5,fl:true,wave:2,yaw:-.3,beat:[0,0,0]});
    camera.position.set(Math.sin(k*1.1)*1.2,14.4,10.5);camera.lookAt(0,14.6,0)}
  else { // 5 teaser : דבורה + pot de miel
    const k=t-K.c4;
    dvora(V(.7+Math.sin(k*2)*.2,14.2+bob,0),FACE+Math.sin(k*2.4)*.12,Math.sin(k*3)*.05,Math.sin(k*2)*.08,2.2,a,gt);
    octo(V(1.9,17.6,-2),.45,t,{hs:false,yaw:-.4,wave:5});
    jar.visible=true;jar.position.set(-1.7,12.6+Math.sin(k*3)*.12,.8);jar.rotation.y=k*1.2;jar.scale.setScalar(.85);
    camera.position.set(Math.sin(k*.6)*.8,14.5,10-1.4*E(k/4));camera.lookAt(0,14.3,0)}
}
