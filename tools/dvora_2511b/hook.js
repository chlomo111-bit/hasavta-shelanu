// Ruche 25.11 soir : פרפרים טועמים ברגליים
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
// ---- פרפרים #5 ----
const M=(c)=>new THREE.MeshLambertMaterial({color:c});
const mO=M(0xFF8A1F),mB=M(0x2E7BFF),mDk=M(0x2a1a10),mLeaf=M(0x3FAE4B),mLeaf2=M(0x2d8a3a),mDot=new THREE.MeshBasicMaterial({color:0xFFE24A}),mJ=new THREE.MeshBasicMaterial({color:0xFF9FC8}),mEgg=M(0xFFF6D8);
const mCone=M(0xE2B36B),mIce=M(0xFF8FB8),mBan=M(0xFFE14A),mBanT=M(0x6b4a12),mStr=M(0xE8283C),mStrG=M(0x2fa84a);
function box(w,h,d,m,x,y,z){const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);b.position.set(x||0,y||0,z||0);return b}
// papillon : corps, tête, 4 ailes (pivots), antennes, 6 pattes (avec points jaunes = récepteurs)
function makeBf(){const g=new THREE.Group();const body=box(.34,.34,1.5,mDk,0,0,0);g.add(body);g.add(box(.42,.42,.42,mDk,0,.05,.95));
 g.add(box(.05,.5,.05,mDk,.14,.45,1.15));g.add(box(.05,.5,.05,mDk,-.14,.45,1.15));
 const wings=[];[[1,.45,0,1.5,1.3,mO],[-1,.45,0,1.5,1.3,mO],[1,-.2,-.5,1.1,.95,mB],[-1,-.2,-.5,1.1,.95,mB]].forEach(a=>{const p=new THREE.Group();p.position.set(a[0]*.18,.1,a[1]*1-.0);const w=box(a[3],.07,a[4],a[5],a[0]*a[3]/2,0,-a[1]*0+a[2]*0);w.position.z=a[2]-.0;p.add(w);const sp=box(.3,.09,.3,M(0xFFF3D0),a[0]*a[3]*.55,0,a[2]+.15);p.add(sp);p.userData.s=a[0];g.add(p);wings.push(p)});
 const legs=[],dots=[];for(let i=0;i<6;i++){const s=i%2?1:-1,z=.35-Math.floor(i/2)*.4;const l=new THREE.Group();l.position.set(s*.15,-.15,z);l.add(box(.07,.07,.9,mDk,0,0,0));l.children[0].position.set(s*.35,-.3,0);l.children[0].geometry=new THREE.BoxGeometry(.7,.07,.07);l.children[0].position.set(s*.35,-.15,0);const t=box(.07,.55,.07,mDk,s*.72,-.42,0);l.add(t);const d=new THREE.Mesh(new THREE.SphereGeometry(.13,8,6),mDot);d.position.set(s*.72,-.75,0);l.add(d);dots.push(d);g.add(l);legs.push(l)}
 g.userData={wings,legs,dots};return g}
function flap(g,t,sp,amp,base){g.userData.wings.forEach(w=>{w.rotation.z=w.userData.s*((base==null?.35:base)+Math.sin(t*sp)*amp)})}
const bf=makeBf();hive.add(bf);bf.visible=false;
const leaf=new THREE.Group();leaf.add(box(5.2,.3,3.4,mLeaf,0,0,0));leaf.add(box(.2,.32,3.0,mLeaf2,0,.02,0));for(let i=-2;i<=2;i++){if(i)leaf.add(box(.15,.32,1.2,mLeaf2,i*.9,.02,.9));if(i)leaf.add(box(.15,.32,1.2,mLeaf2,i*.9,.02,-.9))}
hive.add(leaf);leaf.visible=false;
const juice=[];for(let i=0;i<8;i++){const s=new THREE.Mesh(new THREE.SphereGeometry(.12,8,6),mJ);s.visible=false;hive.add(s);juice.push(s)}
const eggs=[];for(let i=0;i<6;i++){const e=new THREE.Mesh(new THREE.SphereGeometry(.2,10,8),mEgg);e.scale.set(1,1.25,1);e.visible=false;hive.add(e);eggs.push(e)}
const ice=new THREE.Group();ice.add(box(.9,.1,.9,mCone,0,0,0));{const c=new THREE.Mesh(new THREE.ConeGeometry(.75,1.8,4),mCone);c.rotation.x=Math.PI;c.rotation.y=Math.PI/4;c.position.y=-.9;ice.add(c);const s1=new THREE.Mesh(new THREE.SphereGeometry(.85,14,10),mIce);s1.position.y=.55;ice.add(s1);const s2=new THREE.Mesh(new THREE.SphereGeometry(.6,12,8),M(0xFFF1B8));s2.position.y=1.35;ice.add(s2)}
hive.add(ice);ice.visible=false;
const ban=new THREE.Group();{const arc=1.15;const t=new THREE.Mesh(new THREE.TorusGeometry(2.4,.5,8,24,arc),M(0xFFE000));t.rotation.z=-Math.PI/2-arc/2;t.position.y=2.4;ban.add(t);const t2=new THREE.Mesh(new THREE.TorusGeometry(2.4,.2,6,24,arc),mBanT);t2.rotation.z=-Math.PI/2-arc/2;t2.position.set(0,2.4,.42);ban.add(t2);[-1,1].forEach(sg=>{const e=new THREE.Mesh(new THREE.SphereGeometry(.28,8,6),mBanT);const an=-Math.PI/2+sg*arc/2;e.position.set(Math.cos(an)*2.4,2.4+Math.sin(an)*2.4,0);ban.add(e)})}
hive.add(ban);ban.visible=false;
const stw=new THREE.Group();{const c=new THREE.Mesh(new THREE.SphereGeometry(1,14,10),mStr);c.scale.set(.95,1.15,.95);stw.add(c);stw.add(box(1.0,.22,1.0,mStrG,0,1.1,0));stw.add(box(.2,.4,.2,mStrG,0,1.4,0));for(let i=0;i<9;i++){const a=i*2.4;stw.add(box(.1,.1,.1,mDot,Math.sin(a)*.8,-.7+(i%4)*.45,Math.cos(a)*.8))}}
hive.add(stw);stw.visible=false;
const chk=box(1.2,.35,.1,M(0x31D158),0,0,0);const chk2=box(.35,.7,.1,M(0x31D158),0,0,0);const tick=new THREE.Group();chk.position.set(.28,-.12,0);chk.rotation.z=.9;chk2.position.set(-.18,-.02,0);chk2.rotation.z=-.7;tick.add(chk,chk2);hive.add(tick);tick.visible=false;
let tg;
const AT=(a,b,t)=>E((t-a)/(b-a));
function hideAll(){bf.visible=false;leaf.visible=false;juice.forEach(s=>s.visible=false);eggs.forEach(s=>s.visible=false);ice.visible=false;ban.visible=false;stw.visible=false;tick.visible=false}
function bfPose(p,yaw,s){bf.visible=true;bf.position.copy(p);bf.rotation.set(0,yaw,0);bf.scale.setScalar(s)}
function legsPose(t,amt,ph){bf.userData.legs.forEach((l,i)=>{l.rotation.x=Math.sin(t*14+i*1.3+ph)*amt})}
function post(gt){
  const S=window.SH,t=S.t,a=amp(t);EV.form.k=1;tg=EV.form.tg;
  for(let i=0;i<30;i++)tg[i]=HID;
  giant.visible=true;hideAll();const bob=Math.sin(t*7)*.12*(.4+a);const OX=1.0;
  if(t<2.5){
    const k=AT(0,2.5,t);
    dvora(V(-1.1,16.4+bob,0),FACE+.35+Math.sin(t*2.6)*.1,Math.sin(t*3)*.05,Math.sin(t*2.2)*.06,2.5,a,gt);
    bfPose(V(1.5,13.0+Math.sin(t*3)*.3,0),-.45+Math.sin(t*1.6)*.25,1.2);flap(bf,t,18,.7,.45);legsPose(t,.15,0);
    camera.position.set(Math.sin(t*.6)*.4,14.0,12.4-1.8*k);camera.lookAt(0,13.8,0)}
  else if(t<5.5){
    const k=t-2.5;
    dvora(V(-1.1,16.4+bob,0),FACE+.4,0,0,2.2,a,gt);
    leaf.visible=true;leaf.position.set(OX,11.6,0);leaf.rotation.set(0,.3,0);leaf.scale.setScalar(.8);
    bfPose(V(OX,12.4,0),-.55+Math.sin(k*.8)*.12,1.15);flap(bf,k,4,.16,1.25);legsPose(k,.12,0);bf.position.y+=Math.sin(k*5)*.05;
    bf.userData.dots.forEach((d,i)=>{const p=.8+.6*Math.abs(Math.sin(k*5+i*.8));d.scale.setScalar(p*(k>.6?1:.001+k/.6))});
    camera.position.set(1.0,13.2,8.2-1.4*AT(0,2.5,k));camera.lookAt(.5,13.3,0)}
  else if(t<8.3){
    const k=t-5.5,u=AT(0,1.3,k);
    dvora(V(-1.1,16.4+bob,0),FACE+.4,0,0,2.2,a,gt);
    leaf.visible=true;leaf.position.set(OX,11.6,0);leaf.rotation.set(0,.3,0);leaf.scale.setScalar(.8);
    bfPose(V(OX,12.4+(1-u)*2.8,0),-.55,1.15);flap(bf,k,16,.7*(1-u)+.12,1.3-(1-u)*.9);legsPose(k,.05+.1*(1-u),0);
    juice.forEach((s,i)=>{const q=((k*.7+i/8)%1);s.visible=k>1.0;s.position.set(OX-1.4+i*.4,11.9+q*.6,Math.sin(i)*.5);s.scale.setScalar(1-q*.5)});
    bf.userData.dots.forEach((d,i)=>d.scale.setScalar(.8+.6*Math.abs(Math.sin(k*5+i))));
    camera.position.set(Math.sin(k*.7)*1.0+1.4,13.6,8.2);camera.lookAt(.5,13.4,0)}
  else if(t<11.7){
    const k=t-8.3;
    dvora(V(-1.1,16.4+bob,0),FACE+.4,0,0,2.2,a,gt);
    leaf.visible=true;leaf.position.set(OX,11.6,0);leaf.rotation.set(0,.3,0);leaf.scale.setScalar(.8);
    bfPose(V(OX,12.4,0),-.55,1.15);flap(bf,k,4,.14,1.25);bf.position.y+=Math.sin(k*6)*.05;
    bf.userData.legs.forEach((l,i)=>{l.rotation.x=(k<1.9?Math.max(0,Math.sin(k*13+i))*.9:.05)});
    eggs.forEach((e,i)=>{const s=2.0+i*.22;e.visible=k>s;e.position.set(OX-1.1+(i%3)*.5,11.9,.9+Math.floor(i/3)*.45)});
    if(k>3.0){tick.visible=true;tick.position.set(OX+1.6,14.1+Math.sin(k*4)*.1,1.0);tick.scale.setScalar(1.1)}
    camera.position.set(1.8+Math.sin(k*1.2)*.9,13.5+Math.sin(k*.9)*.3,8.0);camera.lookAt(.5,13.3,0)}
  else if(t<14.0){
    const k=t-11.7;
    dvora(V(-1.1+Math.sin(k*3)*.3,16.0+Math.abs(Math.sin(k*4))*.3,0),FACE+.4+Math.sin(k*3)*.2,Math.sin(k*4)*.08,0,2.3,a,gt);
    ice.visible=true;ice.position.set(1.7,12.4,0);ice.rotation.y=k*.9;ice.scale.setScalar(1.0);
    bfPose(V(1.7,13.6,0),-.5,1.0);flap(bf,k,5,.14,1.25);legsPose(k,.1,0);
    bf.userData.dots.forEach((d,i)=>d.scale.setScalar(.8+.6*Math.abs(Math.sin(k*7+i))));
    camera.position.set(Math.sin(k*1.1)*.8,13.3,9.0);camera.lookAt(.3,13.8,0)}
  else {
    const k=t-14.0;
    dvora(V(0+Math.sin(k*2)*.2,16.0+bob,0),FACE+Math.sin(k*2.4)*.12,Math.sin(k*3)*.05,Math.sin(k*2)*.08,k>3.5?3.2:2.0,a,gt);
    ban.visible=true;ban.position.set(-.8,12.2,0);ban.rotation.set(0,Math.sin(k*1.5)*.3,.1+Math.sin(k*3)*.05);ban.scale.setScalar(.7);
    stw.visible=true;stw.position.set(1.6,12.0+Math.abs(Math.sin(k*3))*.15,0);stw.rotation.y=k*1.2;stw.scale.setScalar(.9);
    if(k>1.6){tick.visible=true;tick.position.set(-1.4,11.3,.8);tick.scale.setScalar(1.0)}
    camera.position.set(Math.sin(k*.6)*.8,13.4,10-1.0*E(k/2));camera.lookAt(.2,13.2,0)}
}
