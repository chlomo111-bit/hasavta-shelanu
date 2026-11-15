try{localStorage.setItem('kaveret_ev50','1');localStorage.setItem('kaveret_ev100','1')}catch(e){}
started=true;introT=END;document.getElementById('gate').hidden=true;document.getElementById('skip').hidden=true;
loop();endIntro();document.getElementById('ui').style.display='none';controls.enabled=false;treasureHit=null;foundShown=true;MET.since=-100;treasure.visible=false;
try{capEl.style.display="none"}catch(e){}
window.pickLabels=function(){shown=[];pool.forEach(s=>s.visible=false)};
// 15.11 : une couronne, elle vole d'une abeille (rose) à une autre (lunettes de soleil)
const GOLD=new THREE.MeshStandardMaterial({color:0xFFC81E,metalness:.6,roughness:.25,emissive:0xb07800,emissiveIntensity:.8});
const CR=new THREE.Group();
[[0,0,0,2.4,.4,2.1],[-.95,.45,.85,.35,.6,.35],[.95,.45,.85,.35,.6,.35],[0,.55,.85,.35,.8,.35],[-.95,.45,-.85,.35,.6,.35],[.95,.45,-.85,.35,.6,.35],[0,.55,-.85,.35,.8,.35]].forEach(c=>{const m=new THREE.Mesh(new THREE.BoxGeometry(c[3],c[4],c[5]),GOLD);m.position.set(c[0],c[1],c[2]);CR.add(m)});
const JR=new THREE.MeshBasicMaterial({color:0xff2b6a});[[-.95,1.0,.85],[.95,1.0,.85],[0,1.15,.85]].forEach(p=>{const m=new THREE.Mesh(new THREE.BoxGeometry(.3,.3,.3),JR);m.position.set(...p);m.rotation.set(.6,.6,0);CR.add(m)});
const CL=new THREE.PointLight(0xffd36b,2.2,6,2);CR.add(CL);hive.add(CR);
const SPK=[];const SM=new THREE.MeshBasicMaterial({color:0xfff2a8});for(let i=0;i<40;i++){const m=new THREE.Mesh(new THREE.BoxGeometry(.07,.07,.07),SM);m.visible=false;hive.add(m);SPK.push(m)}
const cur=new THREE.Vector3(),look=new THREE.Vector3(),pA=new THREE.Vector3(),pB=new THREE.Vector3();
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
function bee(h,out){const b=byHandle.get(h);beeWorldPos(b,out);return {b,sc:beeScale(b)*BEE_S,yw:yawArr[b.i]}}
function camAt(info,p,d,yo,up,ly){const yw=info.yw+yo;const o=new THREE.Vector3(Math.cos(yw),0,-Math.sin(yw));cur.copy(p).addScaledVector(o,d*info.sc).add(new THREE.Vector3(0,up*info.sc,0));look.copy(p).add(new THREE.Vector3(0,ly*info.sc,0))}
window.SH={shot:'pink',t:0};
window.capHook=(T)=>{try{pool.forEach(s=>s.visible=false);shown=[]}catch(e){};treasure.visible=false};
const _ub=updateBees;updateBees=function(t,dt){_ub(t,dt);post()};
function post(){
  const S=window.SH,t=S.t;const a=bee('t_romantic',pA),c=bee('t_cool',pB);
  const headA=pA.clone().add(new THREE.Vector3(0,.5*a.sc,0)),headC=pB.clone().add(new THREE.Vector3(0,.5*c.sc,0));
  let cs=.13*a.sc;SPK.forEach(m=>m.visible=false);
  if(S.shot==='pink'){ // gros plan rose : la couronne descend vers elle… puis s'envole (t>2.0)
    const up=t<2.0?(.6-0.25*E(t/1.9)):(.35+Math.pow((t-2.0)*3.2,2));
    CR.position.copy(headA).add(new THREE.Vector3(0,up*a.sc+Math.sin(t*4)*.03*a.sc,0));CR.rotation.y=t*(t<2?1.4:9);
    camAt(a,pA,3.0-0.4*E(t/2.0),.25,.5,.5);}
  else if(S.shot==='cool'){ // gros plan lunettes : la couronne tombe d'en haut et rebondit sur sa tête
    cs=.13*c.sc;const td=Math.max(0,t-.15);const drop=t<.15?3:Math.max(0,3-td*td*30);const bo=drop>0?0:.3*Math.exp(-(td-.32)*4)*Math.abs(Math.sin((td-.32)*12));
    CR.position.copy(headC).add(new THREE.Vector3(0,(-.12+drop+bo)*c.sc,0));CR.rotation.y=.3+Math.sin(t*1.5)*.2;
    camAt(c,pB,3.0-0.4*E(t/3),-.3,.5,.45);
    if(td>.3&&td<1.1)SPK.forEach((m,i)=>{const r=((td-.3)*2.4)*(.6+(i%5)*.15)*c.sc,an=i*.7;m.position.copy(headC).add(new THREE.Vector3(Math.cos(an)*r,(i%7)*.08*c.sc+(td-.3)*.3,Math.sin(an)*r));m.visible=true})}
  else if(S.shot==='pinksad'){ // retour sur la rose, sans couronne
    CR.position.set(0,-999,0);camAt(a,pA,2.6+0.2*E(t/2),.1,.45,.45);}
  CR.scale.setScalar(cs);
  camera.position.copy(cur);camera.lookAt(look);
}
