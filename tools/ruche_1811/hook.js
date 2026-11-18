try{localStorage.setItem('kaveret_ev50','1');localStorage.setItem('kaveret_ev100','1')}catch(e){}
started=true;introT=END;document.getElementById('gate').hidden=true;document.getElementById('skip').hidden=true;
loop();endIntro();document.getElementById('ui').style.display='none';controls.enabled=false;treasureHit=null;foundShown=true;MET.since=-100;treasure.visible=false;
try{capEl.style.display="none"}catch(e){}
window.pickLabels=function(){shown=[];pool.forEach(s=>s.visible=false)};
// 16.11 (format A) : « 2 בנות, כתר אחד » — la couronne tombe entre la rose et la verte, rebondit, ping-pong, finit sur la verte.
const GOLD=new THREE.MeshStandardMaterial({color:0xFFC81E,metalness:.6,roughness:.25,emissive:0xb07800,emissiveIntensity:.8});
const CR=new THREE.Group();
[[0,0,0,2.4,.4,2.1],[-.95,.45,.85,.35,.6,.35],[.95,.45,.85,.35,.6,.35],[0,.55,.85,.35,.8,.35],[-.95,.45,-.85,.35,.6,.35],[.95,.45,-.85,.35,.6,.35],[0,.55,-.85,.35,.8,.35]].forEach(c=>{const m=new THREE.Mesh(new THREE.BoxGeometry(c[3],c[4],c[5]),GOLD);m.position.set(c[0],c[1],c[2]);CR.add(m)});
const JR=new THREE.MeshBasicMaterial({color:0xff2b6a});[[-.95,1.0,.85],[.95,1.0,.85],[0,1.15,.85]].forEach(p=>{const m=new THREE.Mesh(new THREE.BoxGeometry(.3,.3,.3),JR);m.position.set(...p);m.rotation.set(.6,.6,0);CR.add(m)});
const CL=new THREE.PointLight(0xffd36b,2.4,7,2);CR.add(CL);hive.add(CR);
const SPK=[];const SM=new THREE.MeshBasicMaterial({color:0xfff2a8});for(let i=0;i<46;i++){const m=new THREE.Mesh(new THREE.BoxGeometry(.08,.08,.08),SM);m.visible=false;hive.add(m);SPK.push(m)}
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
let A=null,G=null;
let C0=null;const SC=BEE_S*.9;
EV.form={k:1,tg:{}};
const cur=new THREE.Vector3(),look=new THREE.Vector3();
window.SH={shot:'steal',t:0};
window.capHook=(T)=>{try{pool.forEach(s=>s.visible=false);shown=[]}catch(e){};treasure.visible=false};
const _ub=updateBees;updateBees=function(t,dt){_ub(t,dt);post(t)};
function sparks(c,k,t){SPK.forEach((m,i)=>{const r=k*(.5+(i%5)*.18)*SC,an=i*.71;m.position.copy(c).add(new THREE.Vector3(Math.cos(an)*r,((i%7)-2)*.1*SC+k*.4,Math.sin(an)*r*.6));m.visible=k>0&&k<1.1})}
function post(gt){
  if(!A||!G){A=byHandle.get('t_romantic');G=byHandle.get('t_smart');if(!A||!G)return;}
  if(!C0){const p=new THREE.Vector3();beeWorldPos(A,p);C0=p.clone();}
  const S=window.SH,t=S.t;EV.form.k=1;const V=(x,y,z)=>new THREE.Vector3(x*SC,y*SC,z*SC);
  // 18.11 (format A) : « היא גנבה את הכתר! » — la rose (A) arrache la couronne de la tête de la verte (G), poursuite, la couronne glisse et retombe sur la verte.
  let pA,pG,cp,ry=gt*3,cs=.13*SC;SPK.forEach(m=>m.visible=false);
  const head=p=>p.clone().add(V(0,.42,0));
  if(S.shot==='steal'){
    const k=E(t/.45);pG=C0.clone().add(V(.35,0,0)).add(V(.04*Math.sin(t*30)*E((t-.5)/.3),0,0));
    const hG=head(pG);
    if(t<.45){pA=C0.clone().add(V(1.2-.85*k,.35+.25*k,.25));cp=hG.clone().add(V(0,.05,0));ry=.3;}
    else{const u=E((t-.45)/1.1);pA=C0.clone().add(V(.35-.95*u,.6+.2*u,.25+.5*u));cp=head(pA).add(V(0,.05,0));ry=t*5;}
    if(t>.4&&t<1.0)sparks(hG,(t-.4)*2.2,t);
    const mid=C0.clone().add(V(.15-.3*E((t-.4)/1.2),.4,0));cur.copy(mid).add(V(.1,0,3.1-.35*E(t/2)));look.copy(mid);}
  else if(S.shot==='chase'){
    const x=1.4-2.8*(t/1.6);pA=C0.clone().add(V(x-.45,.5+.25*Math.sin(t*9),.3));pG=C0.clone().add(V(x+.55,.35+.25*Math.sin(t*9+1.3),.3));
    cp=head(pA).add(V(0,.05+.06*Math.abs(Math.sin(t*12)),0));ry=t*8;
    const mid=pA.clone().lerp(pG,.5);cur.copy(mid).add(V(.6,.1,3.2));look.copy(mid);}
  else if(S.shot==='drop'){
    pG=C0.clone().add(V(0,0,0));pA=C0.clone().add(V(-.7-.5*E(t/.8),1.0+.3*E(t/.8),-.2));
    const hG=head(pG);const td=Math.max(0,t-.05);const dr=Math.max(0,.6-td*td*6);const bo=dr>0?0:.22*Math.exp(-(td-.33)*4)*Math.abs(Math.sin((td-.33)*12));
    cp=hG.clone().add(V(-.1*dr,.05+dr+bo,0));ry=t*(dr>0?9:1)+.3;
    if(td>.32)sparks(hG,(td-.32)*2.2,t);
    cur.copy(hG).add(V(-.1,.15,2.4-.3*E(t/1.6)));look.copy(hG).add(V(0,-.05,0));}
  else { // end : plan à deux, la verte couronnée, la rose fâchée qui tremble
    pG=C0.clone().add(V(.46,0,0));pA=C0.clone().add(V(-.6+.05*Math.sin(t*4),.08*Math.sin(t*5),0));cp=head(pG).add(V(0,.05,0));ry=.3+Math.sin(t*1.5)*.2;
    const mid=C0.clone().add(V(-.05,.4,0));cur.copy(mid).add(V(0,0,3.8-.3*E(t/2)));look.copy(mid);}
  EV.form.tg[A.i]=pA;EV.form.tg[G.i]=pG;
  CR.position.copy(cp);CR.rotation.y=ry;CR.scale.setScalar(cs);
  camera.position.copy(cur);camera.lookAt(look);
}
