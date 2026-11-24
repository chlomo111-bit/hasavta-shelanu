"""השכנים 24.11 matin, חלק 5 : « השכן של חדר המדרגות ». Usage: python3 specs.py <dossier_clips> <avant> <points>"""
import json, sys, re
R=sys.argv[1]; A=int(sys.argv[2]); PTS=int(sys.argv[3])
C={k:{'dir':f'{R}/{k}','fps':10} for k in ('wide','stair','top','end')}
ISO=lambda s: re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', s)
Y=lambda s:f'<span class=y>{s}</span>'
O=lambda t0,t1,pos,h,np=0:{'t0':t0,'t1':t1,'pos':pos,'html':ISO(h),'np':np}
big=lambda s,sz=66,mt=0:f'<div class=box style="font:900 {sz}px/1.12 H;padding:6px 22px;margin-top:{mt}px">{s}</div>'
def TITLE(n,extra=''):
    return (f'<div class=box style="font:900 40px/1.15 H">הבניין הכי {Y("גבוה")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🏢 <span dir=ltr style="unicode-bidi:isolate">{n:,} / 10,000</span> דיירים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 5</div>'+extra)
L=lambda u:f'<span dir=ltr style="unicode-bidi:isolate" class=y>{u}</span>'
TOP5=('<div class=pill style="margin-top:8px;background:rgba(10,8,24,.88);color:#fff;font:900 18px/1.45 H">🏆 5 התגובות הכי טובות נכנסות לפרק הבא:<br>'
      +L('@hillimoshe7')+' ״משהוא שר במקלחת״<br>'+L('@hayley645726')+' ״מה לא ריבים״<br>'+L('@____alonii____')+' ״השכן עם הסיפורים המוזרים״<br>2 מקומות פנויים</div>')
BAR='<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
SHARE='<br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 24px H">📩 שלחו לשכן שלכם</div>'
D=19.4
M={'avant':2.61,'mdrg':3.16,'olim':4.38,'rak':6.61,'esrim':7.43,'glida':8.19,'mi':9.1,'ehad':9.77,'top':11.99,'cnt':12.44,'cntend':14.16,'komot':14.23,'matan':15.48,'end':16.94,'name':18.4}
def ramp(t0,t1,steps=14):
    out=[]
    for i in range(steps):
        a,b=t0+(t1-t0)*i/steps,t0+(t1-t0)*(i+1)/steps;k=(i+1)/steps;k=1-(1-k)**2
        out.append(O(a,b,'T',TITLE(int(round(A+(PTS-A)*k))),1))
    return out
CARD=('<div class=pill style="background:rgba(10,8,24,.9);color:#fff;font:900 26px/1.4 H">💬 אחד מכם כתב:<br>'+L('@____alonii____')+'<br><span class=y style="font-size:38px">״השכן עם הסיפורים המוזרים״</span></div>')
reel={'dur':D,'fps':30,'clips':C,'flash':.4,'novg':1.0,'vgmax':.35,
 'hits':[0.02,M['avant'],M['rak'],M['glida'],M['cnt'],13.0,13.6,M['komot'],14.6,14.95,15.3,M['end']],
 'seg':[{'t0':0,'t1':M['avant'],'clip':'wide','off':0,'zoom':.03},{'t0':M['avant'],'t1':M['top'],'clip':'stair','off':0,'zoom':.02},
        {'t0':M['top'],'t1':M['end'],'clip':'top','off':0,'zoom':.02},{'t0':M['end'],'t1':D,'clip':'end','off':0,'zoom':.02}],
 'ov':[O(0,M['cnt'],'T',TITLE(A),1)]+ramp(M['cnt'],M['cntend'])+[O(M['cntend'],15.42,'T',TITLE(PTS),1),O(15.42,D,'T',TITLE(PTS,TOP5),1),
  O(0,M['end'],'B',BAR,1),O(M['end'],D,'B',BAR+SHARE,1),
  O(0,1.3,'M',big(f'בונים את<br>{Y("הבניין")} הכי גבוה! 🏢',58),1),
  O(1.3,M['avant'],'M',big(f'{Y("10,000")}<br>דיירים!',80)),
  O(M['avant'],M['mdrg'],'M',big(f'אבל קודם…',70)),
  O(M['mdrg'],M['olim'],'M',big(f'{Y("השכן")} מחדר<br>המדרגות 🪜',56)),
  O(M['olim'],M['rak'],'M',big(f'עולים עם {Y("שקיות")}<br>וגלידה 🍦',54)),
  O(M['rak'],M['esrim'],'M',big(f'״רק {Y("דקה")}!״',86)),
  O(M['esrim'],M['glida'],'M',big(f'⏰ 20 {Y("דקות")}<br>אחרי…',62)),
  O(M['glida'],M['mi'],'M',big(f'הגלידה {Y("נמסה")} 😭',54)),
  O(M['mi'],M['ehad'],'M',big(f'מי זה {Y("אצלכם")}? 🤔',60)),
  O(M['ehad'],M['top'],'M',CARD),
  O(M['top'],M['cnt'],'M',big(f'ועכשיו…',74)),
  O(M['cnt'],13.0,'M',big(f'לייק ❤️<br>{Y("+1")} דייר',70)),
  O(13.0,13.6,'M',big(f'תגובה 💬<br>{Y("+3")} דיירים',70)),
  O(13.6,M['komot'],'M',big(f'שמירה {Y("+5")} · שיתוף {Y("+10")}',40)),
  O(M['komot'],M['matan'],'M',big(f'{Y("5")} קומות<br>חדשות! 🏗️',66)),
  O(M['matan'],M['end'],'M',big(f'🎉 {Y("מתן")} · {Y("הדר")} · {Y("מאור")}<br>אתם בפנים!',44,44)),
  O(M['end'],M['name'],'M',big(f'כתבו את {Y("השם")}<br>שלכם 👇',54,44)),
  O(M['name'],D,'M',big(f'והשכן החדש<br>{Y("זה אתם!")}',54,44))]}
json.dump(reel,open(f'{R}/reel.json','w'),ensure_ascii=False); print('ok')
