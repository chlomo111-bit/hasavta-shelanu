"""השכנים 23.11 soir, חלק 4 : « המעלית ». Usage: python3 specs.py <dossier_clips> <avant> <points>"""
import json, sys, re
R=sys.argv[1]; A=int(sys.argv[2]); PTS=int(sys.argv[3])
C={k:{'dir':f'{R}/{k}','fps':10} for k in ('wide','lift','reveal','top','end')}
ISO=lambda s: re.sub(r'\+(\d+)', r'<span dir=ltr style="unicode-bidi:isolate">+\1</span>', s)
Y=lambda s:f'<span class=y>{s}</span>'
O=lambda t0,t1,pos,h,np=0:{'t0':t0,'t1':t1,'pos':pos,'html':ISO(h),'np':np}
big=lambda s,sz=66:f'<div class=box style="font:900 {sz}px/1.12 H;padding:6px 22px">{s}</div>'
def TITLE(n,extra=''):
    return (f'<div class=box style="font:900 40px/1.15 H">הבניין הכי {Y("גבוה")} בעולם?</div><br>'
            f'<div class=pill style="margin-top:10px;background:#FFC24B;color:#140c04;font:900 25px/1.2 H">🏢 <span dir=ltr style="unicode-bidi:isolate">{n:,} / 10,000</span> דיירים</div>'
            f'<div style="margin-top:6px;font:900 16px H;opacity:.85">חלק 4</div>'+extra)
TOP5=('<div class=pill style="margin-top:8px;background:rgba(10,8,24,.85);color:#fff;font:900 19px/1.4 H">🏆 בפרק הבא: <span dir=ltr style="unicode-bidi:isolate" class=y>@hillimoshe7</span> ״משהוא שר במקלחת״<br>'
      '<span dir=ltr style="unicode-bidi:isolate" class=y>@hayley645726</span> ״מה לא ריבים״ · <span class=y>מאור</span> 🎉 בפנים<br>3 מקומות פנויים</div>')
BAR='<div class=pill style="background:rgba(10,8,24,.82);color:#fff;font:900 21px/1.35 H">❤️ לייק +1 · 💬 תגובה +3<br>🔖 שמירה +5 · 🚀 שיתוף +10</div>'
SHARE='<br><div class=pill style="margin-top:8px;background:#C792EA;color:#1a0f2a;font:900 24px H">📩 שלחו לשכן שלכם</div>'
D=19.6; M={'avant':3.53,'p3end':9.28,'cnt':10.73,'cntend':12.42,'like':12.52,'tguva':13.6,'shituf':14.6,'floors':15.72,'kitvu':17.63,'hashchen':18.8}
def ramp(t0,t1,steps=14):
    out=[]
    for i in range(steps):
        a,b=t0+(t1-t0)*i/steps,t0+(t1-t0)*(i+1)/steps;k=(i+1)/steps;k=1-(1-k)**2
        out.append(O(a,b,'T',TITLE(int(round(A+(PTS-A)*k))),1))
    return out
TS=M['avant']; # debut lift
reel={'dur':D,'fps':30,'clips':C,'flash':.4,'novg':1.0,'vgmax':.35,
 'hits':[0.02,2.25,3.53,M['cnt'],M['like'],M['tguva'],M['shituf'],15.95,16.3,16.65],
 'seg':[{'t0':0,'t1':3.53,'clip':'wide','off':0,'zoom':.03},{'t0':3.53,'t1':9.28,'clip':'lift','off':0,'zoom':.02},
        {'t0':9.28,'t1':10.73,'clip':'reveal','off':0,'zoom':.03},{'t0':10.73,'t1':17.63,'clip':'top','off':0,'zoom':.02},
        {'t0':17.63,'t1':D,'clip':'end','off':0,'zoom':.02}],
 'ov':[O(0,M['cnt'],'T',TITLE(A),1)]+ramp(M['cnt'],M['cnt']+1.7)+[O(M['cnt']+1.7,M['kitvu'],'T',TITLE(PTS),1),O(M['kitvu'],D,'T',TITLE(PTS,TOP5),1),
  O(0,M['kitvu'],'B',BAR,1),O(M['kitvu'],D,'B',BAR+SHARE,1),
  O(0,2.25,'M',big(f'בונים את<br>{Y("הבניין")} הכי גבוה! 🏢',60),1),
  O(2.25,3.53,'M',big(f'{Y("10,000")}<br>דיירים!',84)),
  O(3.53,4.87,'M',big(f'אבל קודם…<br>{Y("המעלית")} 🛗',60)),
  O(4.87,6.6,'M',big(f'🛍️ הדייר<br>עם {Y("הקניות")}',58)),
  O(6.6,7.62,'M',big(f'🐕 השכנה<br>עם {Y("הכלב")}',58)),
  O(7.62,9.38,'M',big(f'הילד שלוחץ<br>על {Y("כל")} הכפתורים 😈',50)),
  O(9.38,M['cnt'],'M',big(f'מי זה {Y("אצלכם")}? 🤔',58)),
  O(M['cnt'],M['like'],'M',big(f'{Y("1,182")}<br>דיירים!',100),1),
  O(M['like'],M['tguva'],'M',big(f'לייק ❤️<br>{Y("+1")} דייר',72)),
  O(M['tguva'],M['shituf'],'M',big(f'תגובה 💬<br>{Y("+3")} דיירים',72)),
  O(M['shituf'],M['floors'],'M','<div class=box>'+big(f'שיתוף 🚀<br>{Y("+10")} בבת אחת!',66)+'</div>'),
  O(M['floors'],M['kitvu'],'M',big(f'{Y("3")} קומות<br>חדשות! 🏗️',66)),
  O(M['kitvu'],M['hashchen'],'M',big(f'כתבו את {Y("השם")}<br>שלכם 👇',54)),
  O(M['hashchen'],D,'M',big(f'והשכן החדש<br>{Y("זה אתם!")}',54))]}
json.dump(reel,open(f'{R}/reel.json','w'),ensure_ascii=False); print('ok')
