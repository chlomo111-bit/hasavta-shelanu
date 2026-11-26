"""השכנים 25.11 matin, חלק 7 : « קבוצת הוואטסאפ של הבניין ». Usage: python3 specs.py <dossier_clips> <avant> <points>"""
import json, sys, re
R=sys.argv[1]; A=int(sys.argv[2]); PTS=int(sys.argv[3])
C={k:{'dir':f'{R}/{k}','fps':(30 if k in ('wide','end') else 10)} for k in ('wide','door','door2','ride2','end')}
ISO=lambda s: re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', s)
Y=lambda s:f'<span class=y>{s}</span>'
O=lambda t0,t1,pos,h,np=0:{'t0':t0,'t1':t1,'pos':pos,'html':ISO(h),'np':np}
big=lambda s,sz=66,mt=0:f'<div class=box style="font:900 {sz}px/1.12 H;padding:6px 22px;margin-top:{mt}px">{s}</div>'
L=lambda u:f'<span dir=ltr style="unicode-bidi:isolate">{u}</span>'
def TITLE(n,extra=''):
    return (f'<div class=box style="font:900 40px/1.15 H">הבניין הכי {Y("גבוה")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🏢 <span dir=ltr style="unicode-bidi:isolate">{n:,} / 10,000</span> דיירים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 7</div>'+extra)
TOP5=('<div class=pill style="margin-top:8px;background:rgba(10,8,24,.88);color:#fff;font:900 18px/1.45 H">🏆 5 התגובות הכי טובות נכנסות לפרק הבא:<br>'
      +'<span class=y>'+L('@hillimoshe7')+'</span> ״משהוא שר במקלחת״<br><span class=y>'+L('@hayley645726')+'</span> ״מה לא ריבים״<br><span class=y>'+L('@____alonii____')+'</span> ״השכן עם הסיפורים המוזרים״<br>2 מקומות פנויים – תהיו הראשונים!</div>')
def BAR(sz=21): return f'<div class=pill style="background:rgba(10,8,24,.84);color:#fff;font:900 {sz}px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
SHARE='<br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 22px H">📩 שלחו לשכן שמבקש דברים ב-22:00</div>'
def bubble(sender,txt,sz=40,col='#DCF8C6'):
    return (f'<div class=pill style="background:{col};color:#10230f;text-align:right;padding:10px 24px;box-shadow:0 6px 20px rgba(0,0,0,.5)">'
            f'<div style="font:900 20px H;color:#0a7d5a">{sender}</div><div style="font:900 {sz}px/1.15 H">{txt}</div></div>')
HDR='<div class=pill style="background:#075E54;color:#fff;font:900 22px H;padding:6px 20px;margin-bottom:10px">👥 קבוצת הדיירים</div><br>'
D=18.0
def ramp(t0,t1,steps=8):
    out=[]
    for i in range(steps):
        a,b=t0+(t1-t0)*i/steps,t0+(t1-t0)*(i+1)/steps;k=(i+1)/steps;k=1-(1-k)**2
        out.append(O(a,b,'T',TITLE(int(round(A+(PTS-A)*k))),1))
    return out
PAL='<div class=pill style="background:#FF8FB8;color:#2a0a18;font:900 24px/1.2 H;margin-bottom:8px">🏗️ קומה חדשה! עברנו את 1,700</div><br>'
cuts=[0,2.95,5.2,9.3,13.65,D]
names=['wide','door','door2','ride2','end']
reel={'dur':D,'fps':30,'clips':C,'flash':.4,'novg':1.0,'vgmax':.35,
 'hits':[0.02,2.95,4.18,5.2,9.3,13.65],
 'seg':[{'t0':cuts[i],'t1':cuts[i+1],'clip':names[i],'off':0,'zoom':.02} for i in range(5)],
 'ov':[O(0,1.4,'T',TITLE(A),1)]+ramp(1.4,2.95)+[O(2.95,13.65,'T',TITLE(PTS),1),O(13.65,D,'T',TITLE(PTS,TOP5),1),
  O(0,1.4,'B',BAR(),1),O(1.4,2.95,'B',PAL+BAR(26),1),O(2.95,13.7,'B',BAR(),1),O(13.7,D,'B',BAR()+SHARE,1),
  O(0,1.4,'M',big('בונים 🏗️',84),1),
  O(1.4,2.95,'M',big(f'{Y("10,000")}<br>דיירים!',80)),
  O(2.95,3.55,'M',big('אבל קודם…',72)),
  O(3.55,4.18,'M',big(f'{Y("22:00")} 🌙',84)),
  O(4.18,5.2,'M',big(f'🔔 {Y("דינג")} דונג!',70)),
  O(5.2,5.65,'M',bubble('אתם','מי זה?! 😳',60,'#E1F5FE')),
  O(5.65,6.15,'M',bubble('השכן','זה השכן! 👋',60,'#FFF3C4')),
  O(6.15,7.28,'M',bubble('השכן 🧑','סליחה, יש לך קצת סוכר? 🍬',40,'#FFF3C4')),
  O(7.28,8.45,'M',big(f'אחרי {Y("5")} דקות…',60)),
  O(8.45,9.3,'M',bubble('השכן 🧑','ועוד קצת מלח? 🧂',46,'#FFF3C4')),
  O(9.3,10.6,'M',big(f'הדיירים {Y("האמיתיים")}<br>כותבים:',46)),
  O(10.6,11.68,'M',bubble(L('@hillimoshe7'),'משהוא שר במקלחת 🚿',44)),
  O(11.68,12.3,'M',bubble(L('@hayley645726'),'מה לא ריבים 😅',48,'#E1F5FE')),
  O(12.3,13.65,'M',bubble(L('@____alonii____'),'השכן עם הסיפורים המוזרים',40,'#FFF3C4')),
  O(13.65,15.5,'M',big(f'כתבו מה {Y("השכנים")}<br>שומעים מהדירה שלכם 👇',36,70)),
  O(15.5,16.6,'M',big(f'וכתבו את {Y("השם")}<br>שלכם ✍️',44,70)),
  O(16.6,D,'M',big(f'ואתם בפרק {Y("הבא!")} 🏆',44,70))]}
json.dump(reel,open(f'{R}/reel.json','w'),ensure_ascii=False); print('ok')
