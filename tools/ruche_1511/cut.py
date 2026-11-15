"""Coupe les silences de la voix (reel + story) et donne le minutage des mots après coupe."""
import subprocess
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
mr=build('reel_raw.mp3','reel_voice.mp3',[(1.76,2.02),(2.17,2.46),(2.77,3.13),(3.56,3.86),(5.57,5.94)],7.52,.08,1.08)
ms=build('story_raw.mp3','story_voice.mp3',[(1.88,2.28),(3.47,3.81),(4.74,5.12),(5.87,6.16)],7.28,.1,1.05)
RW=[("רק",.16),("gasp",2.0),("רגע",2.48),("מה",3.36),("laugh",3.84),("אחת",4.56),("שתיים",5.12),("כתבו",6.04),("END",7.52)]
SW=[("שלי",.16),("אבל",2.44),("הכתר",3.84),("מי",5.25),("כתבו",6.16),("END",7.28)]
print({w:round(mr(t),2) for w,t in RW});print({w:round(ms(t),2) for w,t in SW})
