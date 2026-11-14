import json,subprocess,sys
def build(src,out,sil,total,keep,tempo):
    segs=[];cur=0
    for a,b in sil:
        segs.append((cur,a+keep/2));cur=b-keep/2
    segs.append((cur,total))
    f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(segs))
    f+=''.join(f'[s{i}]' for i in range(len(segs)))+f'concat=n={len(segs)}:v=0:a=1,atempo={tempo}[o]'
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-filter_complex',f,'-map','[o]','-ar','44100',out],check=True)
    def m(t):
        acc=0
        for a,b in segs:
            if t<=b: return (acc+max(0,t-a))/tempo
            acc+=b-a
        return acc/tempo
    return m
mr=build('reel_raw.mp3','reel_voice.mp3',[(1.736,2.067),(2.361,2.641),(4.063,4.364),(6.400,6.898),(7.581,8.122),(9.428,9.722),(11.113,11.576),(12.918,13.362)],14.8,.12,1.1)
ms=build('story_raw.mp3','story_voice.mp3',[(2.22,2.755),(3.505,4.115),(4.997,5.352)],8.32,.15,1.0)
RW=[("נכנסתי",.08),("לדירה",.72),("השכן",1.24),("והיא",2.68),("מלאה",2.96),("בארנבים",3.36),("ואחד",4.4),("מחזיק",5.12),("המפתח",5.56),("שלי",6.08),("מה",6.93),("עושה",7.16),("אחת",8.08),("לוקחת",9.01),("שתיים",9.76),("בורחת",10.64),("כתבו",11.52),("שכן",11.92),("ותיכנסו",12.32),("ושלחו",13.4),("שלכם",14.28),("END",14.88)]
SW=[("הילי",.08),("הצביעה",.36),("ודנה",1.12),("נכנסה",1.6),("מה",2.72),("מצאה",3.0),("בריל",4.08),("כתבו",5.36),("שכן",5.68),("והשם",6.56),("הבא",7.68),("END",8.32)]
print({w:round(mr(t),2) for w,t in RW});print({w:round(ms(t),2) for w,t in SW})
