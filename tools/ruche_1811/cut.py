"""Ruche 18.11 : coupe les silences de la voix (reel + story) et donne le minutage des mots après coupe. À lancer dans le dossier des mp3."""
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
mr=build('reel_raw.mp3','reel_voice.mp3',[(1.31,1.55),(3.27,3.56),(3.88,4.13),(4.98,5.34),(6.35,6.87),(7.54,7.76),(8.76,9.13)],10.64,.08,1.18,start=0)
# story : on coupe le prénom deviné du début (0–0,6 s) : le vrai prénom de @hyll.khbsvb est inconnu
ms=build('story_raw.mp3','story_voice.mp3',[(1.81,2.32),(3.47,3.85),(5.04,5.56),(6.27,6.49)],9.01,.08,1.12,start=.6)
RW=[("היא",0),("רדיפה",1.55),("אוי",3.56),("הכתר",4.13),("בחזרה",5.34),("מי",6.87),("אחת",7.76),("כתבו",9.13),("END",10.64)]
SW=[("נכנסת",.6),("אבל",2.32),("מי",5.56),("כתבו",6.49),("END",9.01)]
print({w:round(mr(t),2) for w,t in RW});print({w:round(ms(t),2) for w,t in SW})
