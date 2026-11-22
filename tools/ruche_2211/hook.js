// Ruche 22.11 « הכוורת הכי גדולה בעולם? » חלק 1 : ruche géante VIDE + reine géante ; démo du barème (1 / 3 / 10 abeilles qui entrent).
try{localStorage.setItem('kaveret_ev50','1');localStorage.setItem('kaveret_ev100','1')}catch(e){}
started=true;introT=END;document.getElementById('gate').hidden=true;document.getElementById('skip').hidden=true;
loop();endIntro();document.getElementById('ui').style.display='none';controls.enabled=false;treasureHit=null;foundShown=true;MET.since=-100;treasure.visible=false;
try{capEl.style.display="none"}catch(e){}
window.pickLabels=function(){shown=[];pool.forEach(s=>s.visible=false)};
window.capHook=(T)=>{try{pool.forEach(s=>s.visible=false);shown=[]}catch(e){};treasure.visible=false};
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)};
EV.form={k:1,tg:{}};
window.SH={shot:'wide',t:0};
const _ub=updateBees;updateBees=function(t,dt){post(t);_ub(t,dt)};
const HID=new THREE.Vector3(0,-300,0);
// arrivées : [indice abeille, instant, point de départ]
const C=new THREE.Vector3(0,14,0);
function arrive(i,t0,from,to,t){const k=E((t-t0)/.65);if(t<t0)return HID;return from.clone().lerp(to,k).add(new THREE.Vector3(0,Math.sin(k*3.14)*2,0))}
function post(gt){
  const S=window.SH,t=S.t;EV.form.k=1;const tg=EV.form.tg;
  for(let i=0;i<14;i++)tg[i]=HID;
  giant.visible=true;
  if(S.shot==='wide'){ // plan large : grande ruche vide, la reine géante au centre, caméra qui descend en tournant
    placeGiant(new THREE.Vector3(0,16+Math.sin(t*1.2)*.6,0),Math.PI/2+.5+t*.15,5,gt);
    const a=.6+t*.16,r=30-8*E(t/5),y=35-12*E(t/5);camera.position.set(r*Math.sin(a),y,r*Math.cos(a));camera.lookAt(0,10+3*E(t/5),0);}
  else if(S.shot==='demo'){ // barème : T1 = 1 abeille, T3 = 3, T10 = 10
    const T1=SH.T1??.7,T3=SH.T3??2.0,T10=SH.T10??3.2;
    placeGiant(new THREE.Vector3(0,17+Math.sin(t*1.2)*.4,-6),Math.PI/2+.4,2.2,gt);
    const slot=j=>new THREE.Vector3(((j%5)-2)*1.3,12.3+Math.floor(j/5)*1.3+(j%2)*.3,2+(j%3)*.4);
    tg[0]=arrive(0,T1,new THREE.Vector3(18,20,20),slot(0),t);
    for(let j=1;j<4;j++)tg[j]=arrive(j,T3+(j-1)*.12,new THREE.Vector3(-18,18+j,22),slot(j),t);
    for(let j=4;j<14;j++)tg[j]=arrive(j,T10+(j-4)*.04,new THREE.Vector3(0+(j-9)*2,30,26),slot(j),t);
    camera.position.set(Math.sin(t*.15)*2,15.5-.5*E(t/4),17-2*E(t/4));camera.lookAt(0,14,0);}
  else { // fin : retour au plan large (boucle), la reine seule
    placeGiant(new THREE.Vector3(0,13+Math.sin(t*1.2)*.6,0),Math.PI/2-t*.2,3.2,gt);
    const a=-.4-t*.12,r=24+3*E(t/6),y=16+8*E(t/6);camera.position.set(r*Math.sin(a),y,r*Math.cos(a));camera.lookAt(0,12.5,0);}
}
