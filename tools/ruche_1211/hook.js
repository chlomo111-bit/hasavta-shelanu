try{localStorage.setItem('kaveret_ev50','1');localStorage.setItem('kaveret_ev100','1')}catch(e){}
started=true;introT=END;document.getElementById('gate').hidden=true;document.getElementById('skip').hidden=true;
loop();endIntro();document.getElementById('ui').style.display='none';controls.enabled=false;treasureHit=null;foundShown=true;MET.since=-100;treasure.visible=false;
try{capEl.style.display="none"}catch(e){}
window.pickLabels=function(){shown=[];pool.forEach(s=>s.visible=false)};
const cur=new THREE.Vector3(0,16,26),look=new THREE.Vector3(0,8,0);
window.SHOT={k:'wide'};
window.capHook=(t)=>{
  try{pool.forEach(s=>s.visible=false);shown=[]}catch(e){}
  treasure.visible=false;
  const S=window.SHOT;
  if(S.k==='wide'){const a=S.a||0.6;cur.set(Math.sin(a)*(S.R||22),S.y||12,Math.cos(a)*(S.R||22));look.set(0,S.ly||8,0)}
  else if(S.k==='bee'){const b=byHandle.get(S.h);if(b){const p=beeWorldPos(b,new THREE.Vector3());const yw=yawArr[b.i]+(S.yo||0)+Math.sin(t*(S.spin||0))*(S.amp||0);const d0=(S.d||3.2)+(S.zoom?Math.max(0,(S.zoom-t*S.zoom*0.4)):0);const out=new THREE.Vector3(Math.cos(yw),0,-Math.sin(yw));
     const d=d0;cur.copy(p).addScaledVector(out,d).add(new THREE.Vector3(0,S.up||0.5,0));
     const L=Math.hypot(cur.x,cur.z);if(L>31){cur.x*=31/L;cur.z*=31/L}
     look.copy(p).add(new THREE.Vector3(0,S.ly||0.1,0))}}
  camera.position.copy(cur);camera.lookAt(look);
};
