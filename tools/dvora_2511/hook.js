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
// ---- וומבט #4 : קוביות ----
const mBrown=new THREE.MeshLambertMaterial({color:0x5b3a1e}),mTan=new THREE.MeshLambertMaterial({color:0x6f6258}),mGut=new THREE.MeshLambertMaterial({color:0xFF7FA0}),mStiff=new THREE.MeshLambertMaterial({color:0x8FA3B8}),mStr=new THREE.MeshLambertMaterial({color:0xFF6B8B});
const mBox=new THREE.MeshLambertMaterial({color:0xC89B5A}),mXr=new THREE.MeshLambertMaterial({color:0x5a4d44,transparent:true,opacity:.55,depthWrite:false});
const wom=new THREE.Group();let womBody;{const bd=new THREE.Mesh(new THREE.BoxGeometry(2.8,1.7,1.7),mTan);womBody=bd;const hd=new THREE.Mesh(new THREE.BoxGeometry(1.1,1.1,1.3),mTan);hd.position.set(1.75,.2,0);
 const ey=[-1,1].map(s=>{const e=new THREE.Mesh(new THREE.SphereGeometry(.14,8,6),new THREE.MeshBasicMaterial({color:0x111111}));e.position.set(2.3,.45,s*.38);return e});
 const ns=new THREE.Mesh(new THREE.BoxGeometry(.3,.28,.55),new THREE.MeshLambertMaterial({color:0x2a1a10}));ns.position.set(2.35,.22,0);
 const ears=[-1,1].map(s=>{const e=new THREE.Mesh(new THREE.BoxGeometry(.25,.3,.25),mTan);e.position.set(1.55,.85,s*.5);return e});
 const legs=[[-.9,.7],[-.9,-.7],[.9,.7],[.9,-.7]].map(p=>{const l=new THREE.Mesh(new THREE.BoxGeometry(.5,.6,.45),mTan);l.position.set(p[0],-1.05,p[1]);return l});
 wom.add(bd,hd,ns,...ey,...ears,...legs);hive.add(wom);wom.visible=false}
const cubes=[];for(let i=0;i<10;i++){const c=new THREE.Mesh(new THREE.BoxGeometry(.62,.62,.62),mBrown);c.visible=false;hive.add(c);cubes.push(c)}
const ball=new THREE.Mesh(new THREE.SphereGeometry(.34,14,10),mBrown);ball.visible=false;hive.add(ball);
const gut=[];for(let i=0;i<14;i++){const s=new THREE.Mesh(new THREE.SphereGeometry(.3,10,8),mGut);s.visible=false;wom.add(s);gut.push(s)}
const gcube=[];for(let i=0;i<4;i++){const c=new THREE.Mesh(new THREE.BoxGeometry(.5,.5,.5),mBrown);c.visible=false;wom.add(c);gcube.push(c)}
const ring=[];for(let i=0;i<8;i++){const b=new THREE.Mesh(new THREE.BoxGeometry(.6,.4,.5),i%4<2?mStr:mStiff);b.visible=false;hive.add(b);ring.push(b)}
const sph=new THREE.Mesh(new THREE.SphereGeometry(.62,16,12),mBrown);sph.visible=false;hive.add(sph);
const core=new THREE.Mesh(new THREE.BoxGeometry(1,1,1),mBrown);core.visible=false;hive.add(core);
const boxes=[];for(let i=0;i<9;i++){const b=new THREE.Mesh(new THREE.BoxGeometry(.9,.9,.9),mBox);const st=new THREE.Mesh(new THREE.BoxGeometry(.92,.12,.92),new THREE.MeshLambertMaterial({color:0xE9D3A0}));st.position.y=.2;b.add(st);b.visible=false;hive.add(b);boxes.push(b)}
let tg;
const AT=(a,b,t)=>E((t-a)/(b-a));
function hideAll(){wom.visible=false;cubes.forEach(c=>c.visible=false);ball.visible=false;gut.forEach(c=>c.visible=false);gcube.forEach(c=>c.visible=false);ring.forEach(c=>c.visible=false);core.visible=false;sph.visible=false;boxes.forEach(c=>c.visible=false);womBody.material=mTan}
function post(gt){
  const S=window.SH,t=S.t,a=amp(t);EV.form.k=1;tg=EV.form.tg;
  for(let i=0;i<30;i++)tg[i]=HID;
  giant.visible=true;hideAll();const bob=Math.sin(t*7)*.12*(.4+a);
  if(t<2.5){ // 1 accroche : דבורה en haut, וומבט au centre, cubes qui tombent
    const k=AT(0,2.5,t);
    dvora(V(-1.6,17.0+bob,0),FACE+.3+Math.sin(t*2.6)*.1,Math.sin(t*3)*.05,Math.sin(t*2.2)*.06,2.3,a,gt);
    wom.visible=true;wom.position.set(.2,13.3+Math.abs(Math.sin(t*3))*.08,0);wom.rotation.y=-.9+Math.sin(t*1.4)*.2;wom.scale.setScalar(.8);
    cubes.forEach((c,i)=>{const u=t-.5-i*.28;c.visible=u>0;const f=Math.min(1,u/.5);c.position.set(-2.0+(i%3)*.75,11.75+Math.floor(i/3)*.64+(1-f*f)*3.5,.4+(i%2)*.3);c.rotation.y=i*.5});
    camera.position.set(Math.sin(t*.6)*.5,14.2,12.8-1.8*k);camera.lookAt(0,14.2,0)}
  else if(t<4.65){ // 2 rayons X : l'intestin, la fin = cubes
    const k=t-2.5;
    dvora(V(.4,16.6+bob,0),FACE+.4,0,0,1.7,a,gt);
    wom.visible=true;wom.position.set(.3,14.3,0);wom.rotation.y=-.2;wom.scale.setScalar(1.15);womBody.material=mXr;
    gut.forEach((s,i)=>{const u=i/13;s.visible=u<.62+.38*Math.min(1,k/1.4)-.0;s.position.set(1.1-u*2.3,.25+Math.sin(u*14)*.45,0);s.scale.setScalar(u>.72?.001:1)});
    gcube.forEach((c,i)=>{const u=.74+i*.075;c.visible=k>.4+i*.2;c.position.set(1.1-u*2.3,.25+Math.sin(u*14)*.45,0);c.rotation.y=i});
    camera.position.set(.3,14.6,8.6-.6*AT(0,2,k));camera.lookAt(.2,14.3,0)}
  else if(t<8.1){ // 3 coupe : parois qui s'étirent -> coins
    const k=t-4.65;
    dvora(V(.4,16.8+bob,0),FACE+.4,0,0,1.7,a,gt);
    const f=Math.min(1,k/2.4);
    ring.forEach((b,i)=>{b.visible=true;const ang=i/8*Math.PI*2+Math.PI/8;const stretch=(i%4<2)?(.35+.35*Math.sin(k*4)):0;const R=1.25+stretch;b.position.set(Math.cos(ang)*R,14.4+Math.sin(ang)*R,0);b.rotation.z=ang+Math.PI/2;b.scale.set(1,1,1)});
    core.visible=true;core.position.set(0,14.4,0);const sq=1.15;core.scale.set(sq,sq,sq);if(f<.55){core.visible=false;sph.visible=true;sph.position.set(0,14.4,0);sph.scale.setScalar(1.1)}else sph.visible=false;core.rotation.z=(1-f)*.0+Math.PI/4*(1-f)*0;
    core.material=mBrown;
    camera.position.set(0,14.4,8.0);camera.lookAt(0,14.4,0)}
  else if(t<12.4){ // 4 קוביות לא מתגלגלות : boule qui roule, cubes qui restent
    const k=t-8.1;
    dvora(V(-1.0,17.0+bob,0),FACE+.35+Math.sin(k*2.6)*.1,Math.sin(k*3)*.05,0,2.0,a,gt);
    wom.visible=true;wom.position.set(2.0,12.6,-.5);wom.rotation.y=-1.0;wom.scale.setScalar(.55);
    cubes.forEach((c,i)=>{c.visible=true;c.position.set(-1.8+(i%3)*.75,11.4+Math.floor(i/3)*.64,.2);c.rotation.y=i*.5;c.scale.setScalar(.9)});
    ball.visible=true;const r=Math.min(1,k/2.6);ball.position.set(-.2-r*6.0,11.12+Math.max(0,(1-r)*0),1.6);ball.rotation.z=-k*6;
    camera.position.set(Math.sin(k*.5)*.5,13.3,10.2);camera.lookAt(-.4,13.2,0)}
  else if(t<15.1){ // 5 שלחו למי שמסדר בקופסאות : cubes dans des cartons
    const k=t-12.4;
    dvora(V(-1.6+Math.sin(k*3)*.3,14.0+Math.abs(Math.sin(k*4))*.3,0),FACE+.4+Math.sin(k*3)*.2,Math.sin(k*4)*.08,0,2.0,a,gt);
    boxes.forEach((b,i)=>{b.visible=true;b.position.set(.5+(i%3)*1.0,11.9+Math.floor(i/3)*.95,.2);b.rotation.y=Math.sin(k*3+i)*.08});
    camera.position.set(Math.sin(k*1.1)*.8,13.6,10.2);camera.lookAt(0,13.4,0)}
  else { // 6 appel final
    const k=t-15.1;
    dvora(V(.0+Math.sin(k*2)*.2,14.8+bob,0),FACE+Math.sin(k*2.4)*.12,Math.sin(k*3)*.05,Math.sin(k*2)*.08,3.4,a,gt);
    wom.visible=true;wom.position.set(-2.4,12.0,0);wom.rotation.y=.9;wom.scale.setScalar(.45);
    camera.position.set(Math.sin(k*.6)*.8,14.5,10-1.2*E(k/2));camera.lookAt(0,14.3,0)}
}
