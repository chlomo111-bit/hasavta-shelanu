"""Ruche 16.11 : coupe les silences de la voix (reel + story) et donne le minutage des mots après coupe. À lancer dans le dossier des mp3."""
import subprocess
def build(src,out,sil,total,keep,tempo,start=0):
    segs=[];cur=start
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
mr=build('reel_raw.mp3','reel_voice.mp3',[(.92,1.17),(2.27,2.45),(5.11,5.34),(5.95,6.31),(7.31,7.63)],9.1,.08,1.15,start=.12)
ms=build('story_raw.mp3','story_voice.mp3',[(2.62,2.89),(4.02,4.28),(6.43,6.78),(7.58,7.93),(8.6,8.75)],10.32,.08,1.18,start=.14)
RW=[("שתי",.18),("כתר",1.22),("מי",2.52),("laugh",3.3),("הירוקה",4.16),("מגיע",5.38),("אחת",6.32),("כתבו",7.64),("ותיכנסו",8.4),("END",9.1)]
SW=[("שלי",.22),("אבל",2.88),("שתי",4.42),("מי",6.84),("כתבו",7.94),("והשם",8.8),("END",10.32)]
print({w:round(mr(t),2) for w,t in RW});print({w:round(ms(t),2) for w,t in SW})
