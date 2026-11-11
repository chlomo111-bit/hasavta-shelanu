import json
R='/tmp/claude-0/-home-claude/8fda15b7-8351-5060-afa7-6568bbec7e14/scratchpad/reels/r1111'
C={k:{'dir':f'{R}/{k}'} for k in ['ruche','bateau','noise','hash']}; C['savta']={'dir':f'{R}/savta','fps':15}
bx=lambda s,sz=30:f'<div class=box style="font:900 {sz}px/1.2 H">{s}</div>'
pill=lambda s,sz=30,bg='#FFC24B',fg='#140c04':f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y=lambda s:f'<span class=y>{s}</span>'
O=lambda t0,t1,pos,h:{'t0':t0,'t1':t1,'pos':pos,'html':h}
reel={'dur':26.3,'clips':C,'flash':.4,'hits':[0.08,1.8,4.16,5.73,8.24,11.04,14.51,17.76,21.1,22.32,24.68],
'seg':[{'t0':0,'t1':1.1,'clip':'ruche','off':0},{'t0':1.1,'t1':2.2,'clip':'bateau','off':3.2},{'t0':2.2,'t1':3.3,'clip':'noise','off':1.5},{'t0':3.3,'t1':4.4,'clip':'savta','off':2.6},{'t0':4.4,'t1':5.6,'clip':'hash','off':.6},
 {'t0':5.6,'t1':8.2,'clip':'ruche','off':1.3},{'t0':8.2,'t1':11.0,'clip':'bateau','off':2.9},{'t0':11.0,'t1':14.2,'clip':'noise','off':.4},{'t0':14.2,'t1':17.3,'clip':'savta','off':1.3},{'t0':17.3,'t1':21.0,'clip':'hash','off':1.9},
 {'t0':21.0,'t1':22.0,'clip':'ruche','off':3.0,'zoom':.1},{'t0':22.0,'t1':23.0,'clip':'bateau','off':3.6,'zoom':.1},{'t0':23.0,'t1':24.0,'clip':'noise','off':2.6,'zoom':.1},{'t0':24.0,'t1':25.1,'clip':'savta','off':3.6,'zoom':.1},{'t0':25.1,'t1':26.3,'clip':'hash','off':4.4,'zoom':.1}],
'ov':[O(0,1.75,'B',bx('יש לך <span class=y>חבר אחד</span>…',46)),O(1.75,4.1,'B',bx('שהיית לוקח איתך<br><span class=y>לכל עולם</span> 🌍',44)),
 O(4.1,5.6,'M',pill('👀 תחשוב עליו עכשיו',40)),O(0,5.6,'T',pill('5 עולמות · חבר אחד',22,'rgba(10,8,24,.8)','#fff')),
 O(5.6,8.2,'T',bx('🐝 לכוורת',40)),O(6.5,8.2,'B',bx('שיילחם איתך<br>על <span class=y>הכתר</span> 👑',44)),
 O(8.2,11.0,'T',bx('🚢 לספינה',40)),O(9.1,11.0,'B',bx('שיטבע איתך<br><span class=b>עד הסוף</span> 🌊',44)),
 O(11.0,14.2,'T',bx('🎤 לבמה',40)),O(11.8,14.2,'B',bx('שישיר איתך… גם כשאתם<br><span class=y>מזייפים</span> 😂',40)),
 O(14.2,17.3,'T',bx('👵 לסבתא מזל',40)),O(15.45,17.3,'B',bx('שיזכור את<br><span class=p>יום ההולדת</span> שלה 🎂',44)),
 O(17.3,21.0,'T',bx('🏢 ולבניין…',40)),O(18.85,21.0,'B',bx('שייכנס איתך<br>לדירה של <span class=y>אבי</span> 😱',44)),
 O(21.0,26.3,'T',bx('אל תחשוב יותר מדי…',36)),O(22.3,26.3,'M',pill('📩 שלח לו את זה<br>עכשיו',46)),O(23.6,26.3,'B',bx('ותשאל אותו:<br><span class=y>איזה עולם אתה?</span> 🌍',44))]}
json.dump(reel,open(f'{R}/reel.json','w'),ensure_ascii=False)
ST={
'ruche':(6.2,'ruche',0.5,[O(0,6.2,'T',pill('👑 מרוץ הכתר',30)),O(0,2.2,'B',bx('שלי <span class=y>מובילה</span><br>במרוץ לכתר…',44)),O(2.2,3.7,'B',bx('מי יעצור אותה? 🤔',46)),O(3.7,6.2,'B',bx('כתבו את השם שלכם<br><span class=y>בריל</span> 👇',44))]),
'bateau':(5.9,'bateau',1.0,[O(0,5.9,'T',pill('🏴‍☠️ 100 עוקבים',30,'#8FD3FF')),O(0,2.7,'B',bx('הפיראטים עדיין<br><span class=y>ליד הספינה</span>…',44)),O(2.7,5.9,'B',bx('את מי הייתם לוקחים<br>ל<span class=b>סירת ההצלה</span>? 🛟',42))]),
'noise':(6.2,'noise',.5,[O(0,6.2,'T',pill('🎭 THE NOISE',30,'#C9A8FF')),O(0,4.0,'B',bx('עדיין <span class=y>אף אחד</span> לא ניחש<br>מי מאחורי המסכה…',42)),O(4.0,6.2,'B',bx('אתם תהיו<br><span class=y>הראשונים</span>? 👇',46))]),
'savta':(8.5,'savta',1.6,[O(0,8.5,'T',pill('🎂 סבתא מזל',30,'#FF8FB8')),O(0,2.55,'B',bx('סבתא מזל<br><span class=p>עדיין מחכה</span>…',46)),O(2.55,4.35,'B',bx('עם נר אחד בלבד 🕯️',44)),O(4.35,6.1,'B',bx('כתבו לה <span class=y>מזל טוב</span><br>בריל 👇',44)),O(6.1,8.5,'B',bx('כל ברכה =<br><span class=y>עוד נר</span> 🕯️',48))]),
'hash':(7.0,'hash',2.5,[O(0,7.0,'T',pill('🏢 השכנים · פרק 4',28,'#C792EA')),O(0,3.3,'B',bx('הקול הראשון הגיע…<br><span class=y>“נכנסת”</span> ❤️',44)),O(3.3,4.7,'B',bx('אתם בטוחים? 🤔',48)),O(4.7,7.0,'B',bx('דנה תעשה<br><span class=y>מה שתחליטו</span>',46))]),
}
for k,(d,clip,off,ov) in ST.items():
    json.dump({'dur':d,'clips':C,'flash':.25,'hits':[0.05],'seg':[{'t0':0,'t1':d,'clip':clip,'off':off,'speed':.75 if k!='savta' else .9,'zoom':.07}],'ov':ov},open(f'{R}/st_{k}.json','w'),ensure_ascii=False)
print('ok')
