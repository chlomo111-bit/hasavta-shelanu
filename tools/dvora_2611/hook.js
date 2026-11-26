// Ruche 26.11 soir : בננה = ברי
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
// ---- בננה ברי #6 ----
const M=(c)=>new THREE.MeshLambertMaterial({color:c});
const mDk=M(0x2a1a10),mDot=new THREE.MeshBasicMaterial({color:0xFFE24A}),mBanT=M(0x6b4a12),mStr=M(0xE8283C),mStrG=M(0x2fa84a),mPink=M(0xFF8FB8),mWhite=M(0xFFF6D8),mRed=new THREE.MeshBasicMaterial({color:0xFF3B30}),mGrn=new THREE.MeshBasicMaterial({color:0x31D158}),mSea=M(0x2E7BFF),mGray=M(0x6f8aa6),mWd=M(0x8a5a2b),mLf=M(0x3FAE4B);
function box(w,h,d,m,x,y,z){const b=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);b.position.set(x||0,y||0,z||0);return b}
const E2=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
function mkBan(){const g=new THREE.Group();const arc=1.15;const t=new THREE.Mesh(new THREE.TorusGeometry(2.4,.5,8,24,arc),M(0xFFE000));t.rotation.z=-Math.PI/2-arc/2;t.position.y=2.4;g.add(t);const t2=new THREE.Mesh(new THREE.TorusGeometry(2.4,.2,6,24,arc),mBanT);t2.rotation.z=-Math.PI/2-arc/2;t2.position.set(0,2.4,.42);g.add(t2);[-1,1].forEach(sg=>{const e=new THREE.Mesh(new THREE.SphereGeometry(.28,8,6),mBanT);const an=-Math.PI/2+sg*arc/2;e.position.set(Math.cos(an)*2.4,2.4+Math.sin(an)*2.4,0);g.add(e)});return g}
function mkStw(){const g=new THREE.Group();const c=new THREE.Mesh(new THREE.SphereGeometry(1,14,10),mStr);c.scale.set(.95,1.15,.95);g.add(c);g.add(box(1.0,.22,1.0,mStrG,0,1.1,0));g.add(box(.2,.4,.2,mStrG,0,1.4,0));return g}
const ban=mkBan(),stw=mkStw();hive.add(ban);hive.add(stw);
// ovaires : 1 point jaune pour la banane, beaucoup pour la fraise (positions en repère local)
const oDots=[];const oB=new THREE.Mesh(new THREE.SphereGeometry(.34,10,8),mDot);oB.visible=false;hive.add(oB);
const sDots=[];for(let i=0;i<14;i++){const s=new THREE.Mesh(new THREE.SphereGeometry(.14,8,6),mDot);s.visible=false;hive.add(s);sDots.push(s)}
// fleur (1 fleur) : pétales roses autour d'un centre
const flower=new THREE.Group();for(let i=0;i<6;i++){const a=i*Math.PI/3;flower.add(box(.5,.5,.12,mPink,Math.cos(a)*.6,Math.sin(a)*.6,0))}flower.add(box(.5,.5,.14,mDot,0,0,.02));hive.add(flower);flower.visible=false;
function mkMark(ok){const g=new THREE.Group();if(ok){const a=box(1.2,.35,.1,mGrn,.28,-.12,0);a.rotation.z=.9;const b=box(.35,.7,.1,mGrn,-.18,-.02,0);b.rotation.z=-.7;g.add(a,b)}else{const a=box(1.4,.34,.1,mRed,0,0,0);a.rotation.z=.8;const b=box(1.4,.34,.1,mRed,0,0,0);b.rotation.z=-.8;g.add(a,b)}hive.add(g);g.visible=false;return g}
const okM=mkMark(1),noM=mkMark(0);
// requin + arbre pour le teaser
const shark=new THREE.Group();{shark.add(box(3.4,.9,1.0,mGray,0,0,0));const n=new THREE.Mesh(new THREE.ConeGeometry(.5,1.2,4),mGray);n.rotation.z=-Math.PI/2;n.position.x=2.2;shark.add(n);const f=new THREE.Mesh(new THREE.ConeGeometry(.42,1.1,3),mGray);f.position.set(0,.95,0);shark.add(f);const t=new THREE.Mesh(new THREE.ConeGeometry(.5,1.2,3),mGray);t.rotation.z=Math.PI/2;t.position.x=-2.2;shark.add(t);shark.add(box(.15,.15,.15,mDk,1.5,.2,.52))}
const tree=new THREE.Group();tree.add(box(.7,2.2,.7,mWd,0,1.1,0));tree.add(box(2.4,1.2,2.4,mLf,0,2.7,0));tree.add(box(1.6,1.0,1.6,M(0x2d8a3a),0,3.6,0));
hive.add(shark);hive.add(tree);shark.visible=false;tree.visible=false;
const mQ=box(.5,.9,.12,mDot,0,0,0);
let tg;
const AT=(a,b,t)=>E2((t-a)/(b-a));
function hideAll(){ban.visible=false;stw.visible=false;oB.visible=false;sDots.forEach(s=>s.visible=false);flower.visible=false;okM.visible=false;noM.visible=false;shark.visible=false;tree.visible=false}
function post(gt){
  const S=window.SH,t=S.t,a=amp(t);EV.form.k=1;tg=EV.form.tg;
  for(let i=0;i<30;i++)tg[i]=HID;
  giant.visible=true;hideAll();const bob=Math.sin(t*7)*.12*(.4+a);
  const DV=(s)=>dvora(V(-1.1,16.4+bob,0),FACE+.4+Math.sin(t*2.4)*.1,Math.sin(t*3)*.05,Math.sin(t*2.2)*.06,s,a,gt);
  if(t<3.3){const k=AT(0,3.3,t);DV(2.4);
    ban.visible=true;ban.position.set(1.0,12.0+Math.sin(t*3)*.2,0);ban.rotation.set(0,t*1.2,Math.sin(t*2)*.1);ban.scale.setScalar(.8);
    stw.visible=true;stw.position.set(3.2,12.8+Math.sin(t*3+1)*.2,0);stw.rotation.y=-t*1.4;stw.scale.setScalar(.85);
    camera.position.set(Math.sin(t*.7)*.6,14.0,12.2-2.2*k);camera.lookAt(.6,13.4,0)}
  else if(t<7.6){const k=t-3.3;DV(2.2);
    ban.visible=true;ban.position.set(1.4,12.6,0);ban.rotation.set(0,.5+Math.sin(k*1.2)*.3,0);ban.scale.setScalar(.95);
    flower.visible=true;flower.position.set(1.4,16.4+Math.sin(k*3)*.15,.5);flower.rotation.z=k*.8;flower.scale.setScalar(.9+.15*Math.abs(Math.sin(k*4)));
    oB.visible=k>.7;oB.position.set(1.4,15.0,.9);oB.scale.setScalar(.9+.5*Math.abs(Math.sin(k*5)));
    if(k>2.7){okM.visible=true;okM.position.set(3.7,14.2+Math.sin(k*4)*.1,.8);okM.scale.setScalar(1.3)}
    camera.position.set(1.6+Math.sin(k*.9)*.9,14.0,8.0+Math.sin(k*.5)*.4);camera.lookAt(.9,14.0,0)}
  else if(t<11.2){const k=t-7.6;DV(2.2);
    stw.visible=true;stw.position.set(1.6,13.0+Math.sin(k*3)*.1,0);stw.rotation.y=k*.9;stw.scale.setScalar(1.35);
    sDots.forEach((s,i)=>{s.visible=k>.3+i*.12;const an=i*2.4+k*.9;s.position.set(1.6+Math.sin(an)*1.15,11.7+(i%5)*.55,Math.cos(an)*1.15);s.scale.setScalar(.9+.5*Math.abs(Math.sin(k*5+i)))});
    if(k>2.7){noM.visible=true;noM.position.set(3.9,14.2+Math.sin(k*4)*.1,.8);noM.scale.setScalar(1.3)}
    camera.position.set(1.8+Math.sin(k*.8)*1.0,13.2,7.6-.6*Math.sin(k));camera.lookAt(1.2,13.0,0)}
  else if(t<14.0){const k=t-11.2;
    dvora(V(-1.1+Math.sin(k*3)*.3,16.0+Math.abs(Math.sin(k*4))*.3,0),FACE+.4+Math.sin(k*3)*.2,Math.sin(k*4)*.08,2.3,a,gt);
    ban.visible=true;ban.position.set(0.2,12.2,0);ban.rotation.set(0,k*1.1,0);ban.scale.setScalar(.7);
    stw.visible=true;stw.position.set(3.0,12.6+Math.abs(Math.sin(k*3))*.2,0);stw.rotation.y=-k*1.3;stw.scale.setScalar(.8);
    okM.visible=true;okM.position.set(.2,15.0,.8);okM.scale.setScalar(.9);noM.visible=true;noM.position.set(3.0,15.0,.8);noM.scale.setScalar(.9);
    camera.position.set(Math.sin(k*1.1)*1.0,13.4,9.2);camera.lookAt(.9,13.4,0)}
  else {const k=t-14.0;
    dvora(V(0+Math.sin(k*2)*.2,16.2+bob,0),FACE+Math.sin(k*2.4)*.12,Math.sin(k*3)*.05,Math.sin(k*2)*.08,k>2.6?2.6:2.0,a,gt);
    shark.visible=true;shark.position.set(-.3,12.4+Math.sin(k*3)*.2,0);shark.rotation.y=.3;shark.rotation.z=Math.sin(k*3)*.06;shark.scale.setScalar(.5);
    tree.visible=true;tree.position.set(2.3,11.6,0);tree.rotation.y=Math.sin(k)*.4;tree.scale.setScalar(.5);
    camera.position.set(Math.sin(k*.6)*.8,13.3,10-1.0*E2(k/2));camera.lookAt(.5,13.2,0)}
}
