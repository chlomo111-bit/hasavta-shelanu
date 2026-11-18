try{localStorage.setItem('kaveret_ev50','1');localStorage.setItem('kaveret_ev100','1')}catch(e){}
started=true;introT=END;document.getElementById('gate').hidden=true;document.getElementById('skip').hidden=true;
loop();endIntro();document.getElementById('ui').style.display='none';controls.enabled=false;treasureHit=null;foundShown=true;MET.since=-100;treasure.visible=false;
try{capEl.style.display="none"}catch(e){}
window.pickLabels=function(){shown=[];pool.forEach(s=>s.visible=false)};
// 16.11 (format A) : « 2 בנות, כתר אחד » — la couronne tombe entre la rose et la verte, rebondit, ping-pong, finit sur la verte.
// 18.11 soir — פרק 1 « אותה שמלה בדיוק » : deux abeilles arrivent à la fête avec la même robe rose.
const PINK=new THREE.MeshStandardMaterial({color:0xff4f9a,roughness:.5,emissive:0x7a0e3c,emissiveIntensity:.35});
const DOT=new THREE.MeshBasicMaterial({color:0xffffff});
function mkDress(){const g=new THREE.Group();
  const sk=new THREE.Mesh(new THREE.CylinderGeometry(.42,.95,.85,10,1,true),PINK);sk.material.side=THREE.DoubleSide;g.add(sk);
  const top=new THREE.Mesh(new THREE.CylinderGeometry(.44,.44,.18,10),PINK);top.position.y=.45;g.add(top);
  for(let i=0;i<10;i++){const a=i/10*Math.PI*2,r=.8;const d=new THREE.Mesh(new THREE.BoxGeometry(.12,.12,.12),DOT);d.position.set(Math.cos(a)*r,-.3,Math.sin(a)*r);g.add(d)}
  const bow=new THREE.Mesh(new THREE.BoxGeometry(.5,.22,.15),new THREE.MeshBasicMaterial({color:0xffe14d}));bow.position.set(0,.45,.47);g.add(bow);
  hive.add(g);return g}
const DA=mkDress(),DG=mkDress();
const SPK=[];const SM=new THREE.MeshBasicMaterial({color:0xfff2a8});for(let i=0;i<40;i++){const m=new THREE.Mesh(new THREE.BoxGeometry(.08,.08,.08),SM);m.visible=false;hive.add(m);SPK.push(m)}
const SPOT=new THREE.PointLight(0xff6fb0,0,9,2);hive.add(SPOT);
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
let A=null,G=null,C0=null;const SC=BEE_S*.9;
EV.form={k:1,tg:{}};
const cur=new THREE.Vector3(),look=new THREE.Vector3();
window.SH={shot:'meet',t:0};
window.capHook=(T)=>{try{pool.forEach(s=>s.visible=false);shown=[]}catch(e){};treasure.visible=false};
const _ub=updateBees;updateBees=function(t,dt){_ub(t,dt);post(t)};
function sparks(c,k){SPK.forEach((m,i)=>{const r=k*(.5+(i%5)*.18)*SC,an=i*.71;m.position.copy(c).add(new THREE.Vector3(Math.cos(an)*r,((i%7)-2)*.1*SC+k*.4,Math.sin(an)*r*.6));m.visible=k>0&&k<1.1})}
function post(gt){
  if(!A||!G){A=byHandle.get('t_romantic');G=byHandle.get('t_smart');if(!A||!G)return;}
  if(!C0){const p=new THREE.Vector3();beeWorldPos(A,p);C0=p.clone();}
  const S=window.SH,t=S.t;EV.form.k=1;const V=(x,y,z)=>new THREE.Vector3(x*SC,y*SC,z*SC);
  let pA,pG;SPK.forEach(m=>m.visible=false);SPOT.intensity=0;
  const mid=()=>pA.clone().lerp(pG,.5);
  if(S.shot==='meet'){ // les deux arrivent des deux côtés et s'arrêtent net, côte à côte (choc à 0,5 s)
    const k=E(t/.5);pA=C0.clone().add(V(-.5-1.6*(1-k),0,0));pG=C0.clone().add(V(.5+1.6*(1-k),0,0));
    if(t>.45&&t<1.1)sparks(mid().add(V(0,.1,0)),(t-.45)*2);
    cur.copy(mid()).add(V(0,.15,3.9-.3*E(t/2)));look.copy(mid()).add(V(0,-.05,0));}
  else if(S.shot==='dress'){ // travelling bas sur les deux robes identiques
    pA=C0.clone().add(V(-.5,0,0));pG=C0.clone().add(V(.5,0,0));
    const x=-.6+1.2*E(t/1.8);cur.copy(C0).add(V(x,-.25,1.9));look.copy(C0).add(V(x*.6,-.3,0));}
  else if(S.shot==='lookA'||S.shot==='lookG'){ // gros plan, chacune qui tremble de colère
    pA=C0.clone().add(V(-.5+.03*Math.sin(t*35),0,0));pG=C0.clone().add(V(.5+.03*Math.sin(t*33),0,0));
    const f=S.shot==='lookA'?pA:pG;cur.copy(f).add(V(S.shot==="lookA"?.3:-.3,.1,2.1-.2*E(t/1)));look.copy(f).add(V(0,.25,0));}
  else if(S.shot==='crowd'){ // recul rapide : toute la ruche autour
    pA=C0.clone().add(V(-.5,0,0));pG=C0.clone().add(V(.5,0,0));
    const k=E(t/1.4);cur.copy(mid()).add(V(.3*k,.2+1.2*k,2.4+4.5*k));look.copy(mid());}
  else if(S.shot==='close'){ // la rose s'approche lentement, lumière rose, ça tremble
    const k=E(t/2.6);pA=C0.clone().add(V(-.9+.55*k,0,0));pG=C0.clone().add(V(.5,0,0));SPOT.intensity=2.5*k;SPOT.position.copy(mid()).add(V(0,1,1));
    const sh=.02*k*Math.sin(t*40);cur.copy(mid()).add(V(sh,.2,2.6-.9*k));look.copy(mid()).add(V(0,.1,0));}
  else { // end : plan à deux, les « jumelles »
    pA=C0.clone().add(V(-.48,.04*Math.sin(t*3),0));pG=C0.clone().add(V(.48,.04*Math.sin(t*3+1),0));
    cur.copy(mid()).add(V(0,.15,4.1-.3*E(t/2)));look.copy(mid()).add(V(0,-.05,0));}
  EV.form.tg[A.i]=pA;EV.form.tg[G.i]=pG;
  [[DA,pA],[DG,pG]].forEach(([d,p])=>{d.position.copy(p).add(V(0,-.22,0));d.scale.setScalar(.5*SC);d.rotation.y=gt*.0});
  camera.position.copy(cur);camera.lookAt(look);
}
