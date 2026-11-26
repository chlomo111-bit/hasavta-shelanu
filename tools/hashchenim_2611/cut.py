import subprocess,json
words="""בונים 0.14 0.4|את 0.44 0.52|הבניין 0.54 0.98|הכי 1.06 1.42|גבוה 1.48 1.76|בעולם 1.8 2.32|עשרת 2.62 3.08|אלפים 3.1 3.4|דיירים 3.44 3.94|אבל 4.36 4.54|קודם 4.6 5.04|עשר 5.54 5.8|בלילה 5.84 6.26|מצלצלים 6.78 7.4|בדלת 7.44 8.04|מי 8.56 8.68|זה 8.72 8.9|זה 9.42 9.5|השכן 9.52 10.08|סליחה 10.5 10.8|יש 11.06 11.18|לך 11.2 11.32|קצת 11.42 11.6|סוכר 11.64 12.02|ואחרי 13.04 13.38|חמש 13.46 13.7|דקות 13.72 14.0|הוא 14.02 14.08|חוזר 14.12 14.5|ועוד 15.1 15.42|קצת 15.46 15.68|מלח 15.74 16.12|והדיירים 16.66 17.22|האמיתיים 17.24 17.78|כותבים 17.82 18.24|משהוא 18.66 18.98|שר 19.02 19.22|במקלחת 19.26 19.92|מה 20.28 20.42|לא 20.46 20.56|ריבים 20.62 21.02|והשכן 21.3 21.78|עם 21.8 21.88|הסיפורים 21.9 22.38|המוזרים 22.4 23.0|כתבו 23.48 23.84|מה 23.92 24.04|השכנים 24.08 24.48|שומעים 24.54 24.84|מהדירה 24.86 25.26|שלכם 25.32 25.74|וכתבו 25.98 26.32|גם 26.36 26.44|את 26.48 26.54|השם 26.56 26.82|שלכם 26.88 27.3|ואתם 27.56 28.14|בפרק 28.2 28.58|הבא 28.64 28.86"""
W=[(w.split()[0],float(w.split()[1]),float(w.split()[2])) for w in words.split('|')]
TOTAL=29.0;KEEP=.1;TEMPO=1.3
sil=[(W[i][2],W[i+1][1]) for i in range(len(W)-1) if W[i+1][1]-W[i][2]>.2]
segs=[];cur=0
for a,b in sil: segs.append((cur,a+KEEP/2));cur=b-KEEP/2
segs.append((cur,TOTAL))
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(segs))
f+=''.join(f'[s{i}]' for i in range(len(segs)))+f'concat=n={len(segs)}:v=0:a=1,atempo={TEMPO}[o]'
subprocess.run(['ffmpeg','-v','error','-y','-i','raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100','reel_voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in segs:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
out=[(w,round(m(a),2),round(m(b),2)) for w,a,b in W]
json.dump(out,open('words_mapped.json','w'),ensure_ascii=False)
for w,a,b in out: print(w,a,b)
