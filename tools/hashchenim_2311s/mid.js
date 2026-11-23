// immeuble en coupe, 11 étages (8 anciens + 3 nouveaux construits à l'écran)
const WALLS=[0xF6D6A8,0xBFE3FF,0xFFC7D9,0xCDEBB5,0xFFE59A,0xE2CCFF,0xFFD0A8,0xFFE08A,0xFFD76A,0xFFC24B,0xFFE08A];
const rooms=[];const NF=11;
for(let f=0;f<NF;f++){const y=f*FH;const g=new THREE.Group();g.position.y=y;scene.add(g);
  const gold=f>=7;
  box(W+.6,.3,DP+.4,gold?M(0xFFC24B,0xb07800,.9):M(0xa59ec8),0,.15,0,g);
  box(W,FH-.3,.3,M(WALLS[f]),0,.3+(FH-.3)/2,-DP/2,g);
  box(.3,FH-.3,DP,M(gold?0xFFD76A:0x8d86a8),-W/2,.3+(FH-.3)/2,0,g);box(.3,FH-.3,DP,M(gold?0xFFD76A:0x8d86a8),W/2,.3+(FH-.3)/2,0,g);
  const L=new THREE.PointLight(0xfff0c8,.45,14,1.6);L.position.set(0,FH-.6,2);g.add(L);
  box(3,1.6,.1,new THREE.MeshBasicMaterial({color:0xffe9a8}),f%2?-2.6:2.6,1.9,-DP/2+.2,g);
  rooms.push(g)}
const roof=new THREE.Group();scene.add(roof);
box(W+1,.6,DP+1,M(0x44406a),0,.3,0,roof);
const sign=new THREE.Mesh(new THREE.PlaneGeometry(11,3.4),new THREE.MeshBasicMaterial({map:txtTex('10,000','#140c04','#FFC24B',800,250,'900 190px sans-serif'),side:THREE.DoubleSide}));scene.add(sign);
const ch={};
const mk=(k,o,x,f,z,sc)=>{const c=mkChar(o);c.g.scale.setScalar(sc||1.0);c.g.position.set(x,f*FH+.3,z||0);c.y0=c.g.position.y;scene.add(c.g);ch[k]=c;return c};
box(3,2.4,.2,M(0x6b3e1f),0,1.5,DP/2-.1,rooms[0]);
mk('argA',{shirt:0xE5484D,hair:0x5a2a10,long:true,skin:0xe8b48a,ph:.7},-2.2,2,0);
mk('argB',{shirt:0x3fa7ff,hair:0x2a160c,skin:0xf1c7a2,ph:.1},-.2,2,0);
mk('l1',{shirt:0xC792EA,hair:0x2a160c,skin:0xf1c7a2,ph:.9},-3,4,0);mk('l2',{shirt:0xFFC24B,hair:0x5a2a10,long:true,skin:0xe8b48a,ph:.2},-1,5,0);mk('l3',{shirt:0x3fa7ff,hair:0x111111,skin:0xd9a37a,ph:1.3},-2,6,0);
mk('jump',{shirt:0xFF9F1C,hair:0x2a160c,skin:0xf1c7a2,ph:.3},-2,1,0);
mk('drill',{shirt:0x2fbf71,hair:0x111111,skin:0xd9a37a,ph:.5},-2,3,0);
// ascenseur
const CX=4.7,CW=2.5;
const car=new THREE.Group();scene.add(car);
box(CW,.15,2.6,M(0x666a80),0,0,0,car);
const glass=new THREE.MeshStandardMaterial({color:0x9fd8ff,transparent:true,opacity:.28,roughness:.1});
box(CW,2.7,.08,glass,0,1.4,1.3,car);box(.08,2.7,2.6,glass,-CW/2,1.4,0,car);box(CW,.12,2.6,M(0xFFC24B),0,2.78,0,car);
box(.1,2.7,.1,M(0xFFC24B),-CW/2,1.4,1.3,car);box(.1,2.7,.1,M(0xFFC24B),CW/2,1.4,1.3,car);
const btn=[];for(let i=0;i<8;i++){btn.push(box(.2,.2,.1,new THREE.MeshBasicMaterial({color:0x333344}),CW/2-.1,.9+(i%4)*.35,-.6+Math.floor(i/4)*.45,car))}
const cable=box(.08,40,.08,M(0x333344),0,22,0,car);
const P1=mk('p1',{shirt:0xE5484D,hair:0x2a160c,skin:0xf1c7a2,ph:.2},2.6,0,0);
const bagA=box(.5,.7,.35,M(0x2fbf71),0,0,0),bagB=box(.5,.6,.35,M(0xFFC24B),0,0,0);
const P2=mk('p2',{shirt:0xC792EA,hair:0x5a2a10,long:true,skin:0xe8b48a,ph:.6},2.6,1,0);
const dog=new THREE.Group();scene.add(dog);box(.9,.5,.4,M(0xb5651d),0,.45,0,dog);box(.4,.4,.4,M(0xb5651d),.6,.75,0,dog);box(.12,.35,.1,M(0x6b3a10),.55,.95,.15,dog);box(.12,.35,.1,M(0x6b3a10),.55,.95,-.15,dog);
[[-.3,.1],[.3,.1],[-.3,-.1],[.3,-.1]].forEach(p=>box(.12,.3,.12,M(0x6b3a10),p[0],.15,p[1],dog));
const P3=mk('p3',{shirt:0x3fa7ff,hair:0x111111,skin:0xd9a37a,ph:1.1},2.6,3,0,.62);
const SEATS=[];for(let i=0;i<10;i++){const x=-W/2+1.2+i*(W-2.4)/9;const p=box(.8,.8,.1,M(0x22284a),x,1.8,DP/2-.4,rooms[7]);SEATS.push(p)}
const GOLDL=new THREE.PointLight(0xffd070,0,30,1.2);GOLDL.position.set(0,7*FH+3,6);scene.add(GOLDL);
const nb7=mkChar({shirt:0xFFC24B,hair:0x2a160c,skin:0xf1c7a2,ph:.4});nb7.g.scale.setScalar(.85);scene.add(nb7.g);
const E=k=>{k=Math.max(0,Math.min(1,k));return k*k*(3-2*k)},L=(a,b,k)=>a.map((x,i)=>x+(b[i]-x)*k);
const KF=[[0,0],[.16,0],[.3,1],[.44,1],[.58,3],[.72,3],[1,7]];
function carF(u){for(let i=0;i<KF.length-1;i++){const a=KF[i],b=KF[i+1];if(u<=b[0])return a[1]+(b[1]-a[1])*E((u-a[0])/(b[0]-a[0]));}return 7}
const BD=[.06,.34,.62];// instants d'embarquement (fraction)
function setLift(u,t){const cf=carF(u),cy=cf*FH+.3;car.position.set(CX,cy,0);
 const ride=(P,bd,off,fl)=>{const k=E((u-bd)/.07);const x=2.6+(CX+off-2.6)*k;const y=k>=1?cy+.15:fl*FH+.3;P.g.position.set(k>=1?CX+off:x,y,0);return k};
 ride(P1,BD[0],-.7,0);const k1=P1.g.position.x;bagA.position.set(P1.g.position.x+.55,P1.g.position.y+.75,.5);bagB.position.set(P1.g.position.x-.5,P1.g.position.y+.7,.5);
 const k2=ride(P2,BD[1],.2,1);dog.position.set(P2.g.position.x-.9,P2.g.position.y,.7);dog.visible=true;
 const k3=ride(P3,BD[2],.9,3);
 animChar(P1,t,.2,'talk');animChar(P2,t,.6,'talk');animChar(P3,t,1.1,'talk');
 P3.aR.rotation.x=-1.4+Math.sin(t*14)*.5;
 const crazy=u>BD[2]+.07;btn.forEach((b,i)=>b.material.color.setHex(crazy&&((Math.floor(t*10)+i)%2)?0xFFC24B:0x333344));
 return cy}
window.F=function(o){const t=o.t,T=o.dur;let cam,look;const NV=parseInt(o.NV||8);
 animChar(ch.argA,t,.8,'talk');animChar(ch.argB,t+.4,.8,'talk');ch.argA.g.rotation.y=.5;ch.argB.g.rotation.y=-.5;
 animChar(ch.jump,t,.5,'talk');ch.jump.g.position.y=ch.jump.y0+Math.abs(Math.sin(t*7))*.5;
 animChar(ch.drill,t,.3,'talk');animChar(ch.l1,t,.1,'talk');animChar(ch.l2,t+.5,.1,'talk');animChar(ch.l3,t+1,.1,'talk');
 SEATS.forEach(p=>p.material.color.setHex(0x22284a));nb7.g.visible=false;GOLDL.intensity=0;
 // etages visibles
 let tops=[0,0,0];const bt=o.BT;let nvis=8,grow=[1,1,1];
 if(o.shot==='top'){for(let i=0;i<3;i++){const k=(t-bt[i])/.45;grow[i]=E(k);}}
 else if(o.shot==='end'){grow=[1,1,1]}
 else grow=[0,0,0];
 for(let f=0;f<NF;f++){const g=rooms[f];if(f<8){g.visible=true;g.scale.y=1}else{const k=grow[f-8];g.visible=k>0.02;g.scale.y=Math.max(.02,k);}}
 const topY=8*FH+(grow[0]>0.02?grow[0]*FH:0)+(grow[1]>0.02?grow[1]*FH:0)+(grow[2]>0.02?grow[2]*FH:0);
 // les etages en croissance se posent l'un sur l'autre
 let acc=8*FH;for(let i=0;i<3;i++){const g=rooms[8+i];g.position.y=acc;acc+=g.visible?FH*grow[i]:0}
 roof.position.y=acc;sign.position.set(0,acc+3.4,0);sign.lookAt(camera.position.x,acc+3.4,camera.position.z);sign.visible=(o.shot!=='top'||t>bt[2]+.4);
 car.visible=(o.shot==='lift'||o.shot==='reveal');[P1,P2,P3,bagA,bagB,dog].forEach(x=>{(x.g||x).visible=car.visible});
 if(!car.visible){P1.g.visible=false;}
 if(o.shot==='wide'){const k=E(t/T);cam=[Math.sin(k*1.2)*6,2+k*15,44-12*k];look=[0,6+k*10,0];}
 else if(o.shot==='lift'){const u=t/T;const cy=setLift(u,t);cam=[2.2+Math.sin(t*.6)*.4,cy+3.0,15.5];look=[2.8,cy+2.2,0];}
 else if(o.shot==='reveal'){const cy=setLift(1,t);const k=E(t/T);cam=[CX-.3+Math.sin(t*3)*.05,cy+2.0,10-3.5*k];look=[CX,cy+1.5,0];}
 else if(o.shot==='top'){const n=t<o.T0?0:(t<o.T1?1:(t<o.T2?3:10));
   if(t<bt[0]-.2){nb7.g.visible=true;nb7.g.position.set(0,7*FH+.3,-.5);animChar(nb7,t,.6,n===10?'cheer':'talk');
     const order=[4,5,3,6,2,7,1,8,0,9];SEATS.forEach((p,i)=>{const on=order.indexOf(i)<n;p.material.color.setHex(on?(n===10?((Math.floor(t*6)+i)%2?0xFFC24B:0xFFF1B0):0xffd98a):0x22284a)});GOLDL.intensity=n===10?4:1.5;
     const k=E(t/bt[0]);cam=L([3,25,21],[-2.5,25.6,15.5],k);look=L([0,25.2,0],[-.5,25.4,0],k);}
   else{const k=E((t-(bt[0]-.2))/(T-bt[0]+.2));SEATS.forEach(p=>p.material.color.setHex(0xFFC24B));GOLDL.intensity=3;cam=L([-2.5,25.6,15.5],[4,acc-2,30],k);look=L([-.5,25.4,0],[0,acc-3,0],k);}
 }
 else{const k=E(t/T);cam=[-Math.sin((1-k)*1.2)*5,17-k*2,29+k*18];look=[0,16,0];}
 camera.position.set(...cam);camera.lookAt(...look);R.render(scene,camera)};
