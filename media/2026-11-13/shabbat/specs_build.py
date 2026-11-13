import json
S='/tmp/claude-0/-home-claude/291bfbec-5172-5e0a-ba27-7b07de62f057/scratchpad'
bx=lambda s,sz=44:f'<div class=box style="font:900 {sz}px/1.25 H">{s}</div>'
pill=lambda s,sz=30,bg='#FFC24B',fg='#140c04':f'<div class=pill style="background:{bg};color:{fg};font:900 {sz}px/1.2 H">{s}</div>'
Y=lambda s:f'<span class=y>{s}</span>'
O=lambda t0,t1,pos,h:{'t0':t0,'t1':t1,'pos':pos,'html':h}
def caps(L,end): # L: [(t0,html)]
    return [O(t,(L[i+1][0] if i+1<len(L) else end),'B',bx(h)) for i,(t,h) in enumerate(L)]
ST={
'hash':(8.9,'#C792EA','🏢 השכנים',[(0,f'🕯️ שבת שלום<br>{Y("מהבניין")}…'),(2.25,f'מישהו דפק הלילה<br>על הדלת של {Y("דנה")} 🚪'),(4.75,'מה היא עושה?'),(5.6,f'{Y("1")} נכנסת · {Y("2")} בורחת'),(6.85,f'במוצאי שבת<br>{Y("נגלה")} 👀')],
  [O(7.2,8.9,'M',pill('📩 שלחו לשכן שלכם',38))]),
'ruche':(9.5,'#FFC24B','🐝 הכוורת שלנו',[(0,f'🕯️ שבת שלום<br>{Y("מהכוורת")}!'),(1.8,f'כבר יש לנו {Y("שתי מלכות")} 👑<br>שלי ושחר'),(4.95,f'ומי תהיה {Y("המלכה")}<br>של השבוע הבא?'),(7.4,f'כתבו {Y("דבורה")}<br>ותיכנסו 🐝')],[]),
'bateau':(8.9,'#8FD3FF','🚢 טובעים ביחד',[(0,f'🕯️ שבת שלום<br>{Y("מהספינה")}!'),(1.7,f'{Y("41")} נוסעים<br>על הסיפון 🧍'),(4.1,f'בשבת {Y("עוגנים")} ⚓'),(5.7,f'ובמוצאי שבת –<br>{Y("ממשיכים להפליג")} 🌊')],
  [O(7.0,8.9,'M',pill('כתבו עולה ותיכנסו 🧍',36))]),
'noise':(8.2,'#C9A8FF','🎤 THE NOISE',[(0,f'🕯️ שבת שלום<br>{Y("מהבמה")}!'),(1.7,'השופטים נחים… 😴'),(3.1,f'אבל {Y("אתם")} –'),(4.2,f'איזה {Y("שופט")} אתם?'),(5.4,f'{Y("<span style=\"display:inline-block;direction:ltr;unicode-bidi:bidi-override\">1 · 2 · 3 · 4</span>")}<br>כתבו בתגובות 👇')],[]),
'savta':(8.7,'#FF8FB8','👵 סבתא מזל',[(0,f'🕯️ שבת שלום,<br>{Y("נשמות שלי")}!'),(2.7,f'ואסף… 💛'),(3.78,f'ד״ש חם ל{Y("סבתא שרה")}<br>ול{Y("סבתא לילי")}'),(6.6,f'💌 שלחו את זה<br>{Y("לסבתא שלכם")}')],[]),
}
for k,(d,col,brand,L,extra) in ST.items():
    ov=[O(0,d,'T',pill(brand+' · שבת שלום 🕯️🕯️',28,col))]+caps(L,d)+extra
    spec={'dur':d,'clips':{k:{'dir':f'{S}/f_{k}/frames' if k=='ruche' else f'{S}/f_{k}','fps':15}},'flash':.25,'hits':[0.05],
          'seg':[{'t0':0,'t1':d,'clip':k,'off':0,'speed':1,'zoom':.06}],'ov':ov}
    json.dump(spec,open(f'{S}/st/{k}.json','w'),ensure_ascii=False)
print('ok')
