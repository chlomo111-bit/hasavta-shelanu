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
// ---- דבש : pot, cuillère, 12 mini-abeilles, cubes ----
const HONEY=new THREE.MeshLambertMaterial({color:0xFFB300}),HONEY2=new THREE.MeshBasicMaterial({color:0xFFC93C});
const jar=new THREE.Group();{const gl=new THREE.Mesh(new THREE.CylinderGeometry(.9,.9,1.5,20),HONEY);const lid=new THREE.Mesh(new THREE.CylinderGeometry(.95,.95,.25,20),new THREE.MeshLambertMaterial({color:0x7A4A12}));lid.position.y=.85;const lab=new THREE.Mesh(new THREE.CylinderGeometry(.93,.93,.7,20),new THREE.MeshLambertMaterial({color:0xFFF3D0}));jar.add(gl,lid,lab);hive.add(jar);jar.visible=false}
const spoon=new THREE.Group();{const bowl=new THREE.Mesh(new THREE.SphereGeometry(.9,20,12,0,Math.PI*2,0,Math.PI/2),new THREE.MeshLambertMaterial({color:0xDDDDE6,side:THREE.DoubleSide}));bowl.rotation.x=Math.PI;const h=new THREE.Mesh(new THREE.CylinderGeometry(.12,.12,3.2,10),new THREE.MeshLambertMaterial({color:0xDDDDE6}));h.rotation.z=Math.PI/2;h.position.set(2.0,.15,0);spoon.add(bowl,h);hive.add(spoon);spoon.visible=false}
const fill=new THREE.Mesh(new THREE.SphereGeometry(.86,20,12,0,Math.PI*2,0,Math.PI/2),new THREE.MeshLambertMaterial({color:0xFFB300,side:THREE.DoubleSide}));fill.rotation.x=Math.PI;spoon.add(fill);fill.scale.set(1,.1,1);
const drop=new THREE.Mesh(new THREE.SphereGeometry(.16,10,8),HONEY2);hive.add(drop);drop.visible=false;
const mb=[];for(let i=0;i<12;i++){const g=new THREE.Group();const b=new THREE.Mesh(new THREE.SphereGeometry(.34,12,10),new THREE.MeshLambertMaterial({color:0xFFC24B}));b.scale.set(1.25,1,1);const st=new THREE.Mesh(new THREE.BoxGeometry(.1,.62,.62),new THREE.MeshLambertMaterial({color:0x2a1a05}));st.position.x=.05;const w=new THREE.Mesh(new THREE.SphereGeometry(.26,8,6),new THREE.MeshBasicMaterial({color:0xcfe9ff,transparent:true,opacity:.7}));w.scale.set(1,.15,1.2);w.position.set(0,.34,0);g.add(b,st,w);g.userData.w=w;hive.add(g);g.visible=false;mb.push(g)}
const cubes=[];for(let i=0;i<7;i++){const c=new THREE.Mesh(new THREE.BoxGeometry(.55,.55,.55),new THREE.MeshLambertMaterial({color:0x5b3a1e}));c.visible=false;hive.add(c);cubes.push(c)}
const wom=new THREE.Group();{const m=new THREE.MeshLambertMaterial({color:0x9a7a55});const bd=new THREE.Mesh(new THREE.BoxGeometry(2.6,1.5,1.5),m);const hd=new THREE.Mesh(new THREE.BoxGeometry(1,1,1.2),m);hd.position.set(1.7,.15,0);const ey=[-1,1].map(s=>{const e=new THREE.Mesh(new THREE.SphereGeometry(.12,8,6),new THREE.MeshBasicMaterial({color:0x111111}));e.position.set(2.15,.4,s*.35);return e});const ns=new THREE.Mesh(new THREE.BoxGeometry(.25,.25,.5),new THREE.MeshLambertMaterial({color:0x2a1a10}));ns.position.set(2.25,.2,0);wom.add(bd,hd,ns,...ey);hive.add(wom);wom.visible=false}
let tg;
const AT=(a,b,t)=>E((t-a)/(b-a));
function hideAll(){jar.visible=false;spoon.visible=false;drop.visible=false;mb.forEach(g=>g.visible=false);cubes.forEach(c=>c.visible=false);wom.visible=false}
function post(gt){
  const S=window.SH,t=S.t,a=amp(t);EV.form.k=1;tg=EV.form.tg;
  for(let i=0;i<30;i++)tg[i]=HID;
  giant.visible=true;hideAll();const bob=Math.sin(t*7)*.12*(.4+a);
  if(t<5.45){ // 1 accroche : דבורה + cuillère qui reçoit UNE goutte
    const k=AT(0,5.4,t);
    dvora(V(-1.2,16.4+bob,0),FACE+.3+Math.sin(t*2.6)*.1,Math.sin(t*3)*.05,Math.sin(t*2.2)*.06,3.6,a,gt);
    spoon.visible=true;spoon.position.set(1.0,12.6,0);spoon.rotation.set(.25,-.5,0);fill.scale.set(1,.12+(t>2.6?Math.min(.2,(t-2.6)*.08):0),1);
    jar.visible=true;jar.position.set(2.2,15.6+Math.sin(t*2)*.1,-.5);jar.rotation.set(.9,t*.8,0);jar.scale.setScalar(1.0);
    drop.visible=true;const u=((t*.55)%1);drop.position.set(1.0,15.0-u*2.0,.3);drop.scale.setScalar(.8+.3*Math.sin(u*3.14));
    camera.position.set(Math.sin(t*.6)*.6,14.2,13.4-2.4*k);camera.lookAt(0.2,14.2,0)}
  else if(t<10.0){ // 2 : 12 mini-abeilles comptées autour de la cuillère
    const k=t-5.45;
    dvora(V(-1.4,17.2+bob,0.5),FACE+.45,0,0,1.5,a,gt);
    spoon.visible=true;spoon.position.set(0,14.2,0);spoon.rotation.set(.15,-.2,0);fill.scale.set(1,.3+.7*Math.min(1,k/3.8),1);
    mb.forEach((g,i)=>{const vis=k>.15+i*.26;g.visible=vis;const ang=i/12*Math.PI*2+k*.5,R=3.0;const ap=Math.min(1,(k-(.15+i*.26))*2.5);g.position.set(Math.cos(ang)*R*(1.6-.6*ap)*.8,14.8+Math.sin(ang)*R*.55*(1.6-.6*ap)+Math.sin(k*8+i)*.1,Math.sin(ang)*.8);g.rotation.set(0,0,0);g.scale.setScalar(.85+.15*ap);g.userData.w.scale.set(1,.15,1.2+.4*Math.sin(t*50+i))});
    camera.position.set(Math.sin(k*.5)*.8,14.6,10.8-1.0*Math.min(1,k/4));camera.lookAt(0,14.5,0)}
  else if(t<12.5){ // 3 « שלחו למי שמורח דבש בלי רחמים »
    const k=t-10.0;
    dvora(V(-1.6+Math.sin(k*3)*.3,13.8+Math.abs(Math.sin(k*4))*.3,0),FACE+.4+Math.sin(k*3)*.2,Math.sin(k*4)*.08,0,3.0,a,gt);
    jar.visible=true;jar.position.set(1.9,14.2+Math.sin(k*3)*.12,.6);jar.rotation.set(.0,k*1.4,Math.sin(k*3)*.3);jar.scale.setScalar(1.3);
    spoon.visible=true;spoon.position.set(1.6,16.4,-.3);spoon.rotation.set(.3,-.4,0);fill.scale.set(1,1,1);
    camera.position.set(Math.sin(k*1.1)*1.0,14.4,10.0);camera.lookAt(0,14.4,0)}
  else if(t<16.6){ // 4 teaser : וומבט + cubes
    const k=t-12.5;
    dvora(V(-.3+Math.sin(k*2)*.2,16.8+bob,0),FACE+.3+Math.sin(k*2.4)*.12,Math.sin(k*3)*.05,Math.sin(k*2)*.08,3.2,a,gt);
    wom.visible=true;wom.position.set(-.2,12.6+Math.abs(Math.sin(k*3))*.1,0);wom.rotation.y=-.5+Math.sin(k*1.2)*.25;wom.scale.setScalar(.55);
    cubes.forEach((c,i)=>{const s0=i*.5;const u=k-s0;c.visible=u>0;const f=Math.min(1,u/1.0);c.position.set(-1.7+(i%3)*.6,12.0+(1-f*f)*3-.0+(Math.floor(i/3))*.62*0,0+(i%2)*.4);c.position.y=11.5+Math.floor(i/3)*.58+(1-Math.min(1,u*1.6))*3;c.rotation.y=i*.4});
    camera.position.set(Math.sin(k*.6)*.8,13.8,10.4-.8*E(k/3));camera.lookAt(0,13.9,0)}
  else { // 5 appel final
    const k=t-16.6;
    dvora(V(.2+Math.sin(k*2)*.2,14.6+bob,0),FACE+Math.sin(k*2.4)*.12,Math.sin(k*3)*.05,Math.sin(k*2)*.08,3.8,a,gt);
    jar.visible=true;jar.position.set(-2.0,12.8+Math.sin(k*3)*.12,.8);jar.rotation.y=k*1.2;jar.scale.setScalar(.85);
    camera.position.set(Math.sin(k*.6)*.8,14.5,10-1.2*E(k/2));camera.lookAt(0,14.3,0)}
}
