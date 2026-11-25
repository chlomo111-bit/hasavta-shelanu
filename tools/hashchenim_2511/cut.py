import subprocess,json
words="""בונים 0.08 0.4|את 0.44 0.48|הבניין 0.56 0.96|הכי 1.04 1.44|גבוה 1.52 1.76|בעולם 1.84 2.52|עשרת 2.64 3.12|אלפים 3.2 3.44|דיירים 3.52 4.2|אבל 4.4 4.64|קודם 4.8 5.28|קבוצת 5.44 5.76|הוואטסאפ 5.84 6.24|של 6.32 6.4|הבניין 6.44 7.12|מישהו 7.36 7.6|השאיר 7.64 7.92|קרטונים 8.04 8.48|בחדר 8.6 8.88|המדרגות 8.933 9.76|לא 9.84 9.92|אני 10.08 10.4|לא 10.48 10.56|אני 10.72 11.04|גם 11.2 11.44|לא 11.48 11.52|אני 11.6 12.2|והדיירים 12.48 13.04|האמיתיים 13.08 13.6|כותבים 13.72 14.16|משהוא 14.56 14.88|שר 14.96 15.12|במקלחת 15.2 15.92|מה 16.24 16.4|לא 16.48 16.56|ריבים 16.6 17.2|והשכן 17.36 17.84|עם 17.88 17.92|הסיפורים 17.96 18.4|המוזרים 18.44 19.24|והקרטונים 19.44 20.32|עדיין 20.48 20.88|שם 21.04 21.28|כתבו 21.76 22.08|מה 22.16 22.24|השכנים 22.32 22.72|שומעים 22.76 23.04|מהדירה 23.12 23.44|שלכם 23.52 24.08|וכתבו 24.2 24.48|גם 24.56 24.64|את 24.68 24.72|השם 24.8 25.04|שלכם 25.16 25.76|ואתם 25.88 26.24|בפרק 26.4 26.8|הבא 26.84 27.36"""
W=[(w.split()[0],float(w.split()[1]),float(w.split()[2])) for w in words.split('|')]
TOTAL=27.36;KEEP=.1;TEMPO=1.3
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
