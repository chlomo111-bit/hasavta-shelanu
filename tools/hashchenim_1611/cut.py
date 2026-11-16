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
mr=build('reel_raw.mp3','reel_voice.mp3',[(1.27,1.51),(2.88,3.33),(5.95,6.25)],7.2,.1,1.08)
ms=build('story_raw.mp3','story_voice.mp3',[(1.58,2.12),(3.88,4.47),(5.63,5.85),(6.6,6.86)],8.8,.12,1.08)
RW=[("הוא",.06),("והוא",1.56),("המפתח",2.04),("אחת",3.34),("שתיים",4.84),("כתבו",6.26),("END",7.05)]
SW=[("הילי",.08),("והארנב",2.12),("ראיתם",4.52),("כתבו",5.86),("והשם",6.9),("END",8.5)]
print({w:round(mr(t),2) for w,t in RW});print({w:round(ms(t),2) for w,t in SW})
