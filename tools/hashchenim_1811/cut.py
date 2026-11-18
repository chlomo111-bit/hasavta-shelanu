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
mr=build('reel_raw.mp3','reel_voice.mp3',[(1.47,1.72),(3.04,3.45),(4.14,4.69),(5.16,5.51),(6.09,6.45),(6.96,7.24),(8.02,8.46)],10.02,.1,1.12)
ms=build('story_raw.mp3','story_voice.mp3',[(4.50,5.06),(6.23,6.41),(7.14,7.39)],9.0,.12,1.12)
RW=[("הדלת",0),("ארנבים",1.72),("מה",3.45),("אחת",4.69),("נכנסת",5.51),("שתיים",6.45),("קוראת",7.24),("כתבו",8.46),("END",10.0)]
SW=[("הילי",0),("ראיתם",5.06),("כתבו",6.41),("והשם",7.39),("END",9.0)]
print({w:round(mr(t),2) for w,t in RW});print({w:round(ms(t),2) for w,t in SW})
