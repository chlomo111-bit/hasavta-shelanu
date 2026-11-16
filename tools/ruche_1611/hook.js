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
window.SH={shot:'drop',t:0};
window.capHook=(T)=>{try{pool.forEach(s=>s.visible=false);shown=[]}catch(e){};treasure.visible=false};
const _ub=updateBees;updateBees=function(t,dt){_ub(t,dt);post(t)};
function sparks(c,k,t){SPK.forEach((m,i)=>{const r=k*(.5+(i%5)*.18)*SC,an=i*.71;m.position.copy(c).add(new THREE.Vector3(Math.cos(an)*r,((i%7)-2)*.1*SC+k*.4,Math.sin(an)*r*.6));m.visible=k>0&&k<1.1})}
function post(gt){
  if(!A||!G){A=byHandle.get('t_romantic');G=byHandle.get('t_smart');if(!A||!G)return;}
  if(!C0){const p=new THREE.Vector3();beeWorldPos(A,p);C0=p.clone();}
  const S=window.SH,t=S.t;EV.form.k=1;
  // positions des deux abeilles (côte à côte, face caméra +z)
  let dA=.46,dG=.46,yA=0,yG=0;
  if(S.shot==='tug'){const l=.25*Math.sin(t*9);dA=.46+l*.3;dG=.46-l*.3;}
  if(S.shot==='win'||S.shot==='end'){dA=.46+.25*E((t-.2)/.6);yA=.15*Math.sin(t*14)*E(t/.4);} // la rose est poussée
  const pA=C0.clone().add(new THREE.Vector3(-dA*SC,yA*SC,0)),pG=C0.clone().add(new THREE.Vector3(dG*SC,yG*SC,0));
  EV.form.tg[A.i]=pA;EV.form.tg[G.i]=pG;
  const hA=pA.clone().add(new THREE.Vector3(0,.42*SC,0)),hG=pG.clone().add(new THREE.Vector3(0,.42*SC,0));
  const mid=hA.clone().lerp(hG,.5);
  let cs=.13*SC,cp=new THREE.Vector3(),ry=gt*3;SPK.forEach(m=>m.visible=false);
  if(S.shot==='drop'){ // la couronne tombe (déjà en mouvement à l'image 0), frappe au milieu à 0,9 s, rebondit
    const yy=t<.9?(2.6-2.6*(t/.9)*(t/.9)):(.9*Math.abs(Math.sin((t-.9)*2.6))*Math.exp(-(t-.9)*.8));
    cp.copy(mid).add(new THREE.Vector3(0,(yy+.2)*SC,0));ry=t*6;
    if(t>.9)sparks(mid.clone().add(new THREE.Vector3(0,.2*SC,0)),(t-.9)*2.2,t);
    const d=3.9-.5*E(t/2);cur.copy(mid).add(new THREE.Vector3(0,.05*SC,d*SC));look.copy(mid).add(new THREE.Vector3(0,.05*SC,0));}
  else if(S.shot==='tug'){ // ping-pong : la couronne saute d'une tête à l'autre
    const s=Math.sin(t*9);cp.copy(hA).lerp(hG,.5+.5*s).add(new THREE.Vector3(0,(.35+.35*Math.abs(Math.cos(t*9)))*SC,0));ry=t*11;
    cur.copy(mid).add(new THREE.Vector3(.15*Math.sin(t*3)*SC,0,(3.2-.2*E(t))*SC));look.copy(mid).add(new THREE.Vector3(0,.05*SC,0));}
  else if(S.shot==='win'){ // la couronne tombe sur la verte, étincelles, gros plan
    const td=Math.max(0,t-.1);const drop=Math.max(0,1.4-td*td*14);const bo=drop>0?0:.25*Math.exp(-(td-.32)*4)*Math.abs(Math.sin((td-.32)*12));
    cp.copy(hG).add(new THREE.Vector3(0,(.05+drop+bo)*SC,0));ry=.3+Math.sin(t*1.5)*.2;
    if(td>.3)sparks(hG,(td-.3)*2.2,t);
    cur.copy(hG).add(new THREE.Vector3(-.1*SC,0,(2.0-.2*E(t/1.6))*SC));look.copy(hG).add(new THREE.Vector3(0,-.1*SC,0));}
  else if(S.shot==='end'){ // plan à deux : la verte couronnée, la rose fâchée qui tremble
    cp.copy(hG).add(new THREE.Vector3(0,.05*SC,0));ry=.3+Math.sin(t*1.5)*.2;
    cur.copy(mid).add(new THREE.Vector3(0,.05*SC,(3.8-.3*E(t/2))*SC));look.copy(mid).add(new THREE.Vector3(0,.05*SC,0));}
  CR.position.copy(cp);CR.rotation.y=ry;CR.scale.setScalar(cs);
  camera.position.copy(cur);camera.lookAt(look);
}
