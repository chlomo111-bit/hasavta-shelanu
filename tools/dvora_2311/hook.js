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
function followers(t,mode,ctr){ // 12 abeilles qui regardent / dansent autour
  for(let i=0;i<12;i++){const k=i/12*Math.PI*2+.4,r=5.5+(i%3)*1.2;let y=ctr.y-.5+(i%4)*.9+Math.sin(t*3+i)*.35;
    if(mode==='dance')y+=Math.abs(Math.sin(t*5+i*.7))*1.4;
    tg[i]=V(ctr.x+Math.cos(k)*r*(mode==='dance'?1.0:.8),y,ctr.z-3-Math.abs(Math.sin(k))*4)}}
let tg;
function post(gt){
  const S=window.SH,t=S.t,a=amp(t);EV.form.k=1;tg=EV.form.tg;
  for(let i=0;i<30;i++)tg[i]=HID;
  giant.visible=true;
  const bob=Math.sin(t*7)*.12*(.4+a);
  if(S.shot==='test'){dvora(V(0,14,0),FACE,0,0,3,a,gt);camera.position.set(S.cx||0,S.cy||14.5,S.cz||5);camera.lookAt(0,14,0);return}
  if(t<4.8){ // 1. accroche : gros plan face caméra, push-in, balancement
    const k=E(t/4.8);dvora(V(Math.sin(t*2.2)*.5,14+bob,0),FACE+Math.sin(t*2.6)*.12,Math.sin(t*3)*.06,Math.sin(t*2.2)*.07,2.9,a,gt);
    followers(t,'watch',P0);
    camera.position.set(Math.sin(t*.5)*1.6,14.7-.3*k,10.5-2.6*k);camera.lookAt(0,14.1,0)}
  else if(t<7.0){ // 2. « זה נקרא ריקוד הזנב » : elle se met en position, caméra latérale basse
    const k=E((t-4.8)/2.2);dvora(V(-2.2*k,13.6+.4*k+bob,0),FACE+.9*k,.35*k,0,2.8,a,gt);
    followers(t,'watch',P0);
    camera.position.set(4-3*k,12.8+.4*k,9-1*k);camera.lookAt(-1*k,14,0)}
  else if(t<9.5){ // 3. direction : course en zigzag (waggle) vers le haut-droite
    const u=E((t-7.0)/2.3),w=Math.sin((t-7)*18.85);
    dvora(V(-2.4+4.8*u,13.2+2.4*u+bob*.3,0),-.05+w*.30,.55,w*.08,2.6,a,gt);
    followers(t,'watch',P0);
    camera.position.set(Math.sin(t*.7)*2.2,14.6,10.2-.8*Math.sin((t-7)));camera.lookAt(0,14.4,0)}
  else if(t<11.9){ // 4. durée : course plus longue, plus lente, puis boucle de retour
    const u=E((t-9.5)/2.4),w=Math.sin((t-9.5)*18.85),ret=Math.max(0,(t-11.0)/.9);
    const x=-3.6+7.2*u,y=12.8+3.4*u;
    dvora(V(x-ret*2,y-ret*1.5+bob*.3,0),-.05+w*.30,.55,w*.08,2.6,a,gt);
    followers(t,'watch',P0);
    camera.position.set(-1.5+Math.sin((t-9.5)*.6)*2,15,11-1.2*E((t-9.5)/2.4));camera.lookAt(0,14.6,0)}
  else if(t<14.4){ // 5. « שלחו לחבר שרוקד בכל חתונה » : face caméra, la danseuse + tout le monde saute
    const k=(t-11.9);dvora(V(Math.sin(k*3)*.9,13.8+Math.abs(Math.sin(k*4))*.45,0),FACE+Math.sin(k*3)*.35,Math.sin(k*4)*.1,0,2.7,a,gt);
    followers(t,'dance',P0);
    camera.position.set(Math.sin(k*1.2)*3,14.2,8.3-2*Math.min(1,k/2.5));camera.lookAt(0,14.2,0)}
  else { // 6. fin : plan moyen, teaser « מחר », elle salue
    const k=(t-14.4);dvora(V(Math.sin(k*2)*.4,14+bob,0),FACE+Math.sin(k*2.4)*.15,Math.sin(k*3)*.07,Math.sin(k*2)*.1,3.2,a,gt);
    followers(t,'watch',P0);
    camera.position.set(Math.sin(k*.6)*1.4,14.6,9.2-2.4*E(k/4.4));camera.lookAt(0,14.1,0)}
}
