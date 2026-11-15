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
mr=build('reel_raw.mp3','reel_voice.mp3',[(2.07,2.38),(2.61,2.91),(4.03,4.48),(4.94,5.23),(5.76,6.14),(6.65,6.91),(7.43,7.77)],8.7,.1,1.1)
ms=build('story_raw.mp3','story_voice.mp3',[(1.34,1.87),(3.14,3.91),(4.66,5.15),(6.03,6.33),(7.03,7.35)],9.2,.12,1.12)
RW=[("המפתח",.14),("פתח",.98),("שמונה",1.72),("ומשהו",2.92),("יצא",3.34),("אחת",4.48),("נכנסת",5.22),("שתיים",6.22),("טורקת",6.92),("כתבו",7.78),("שכן",8.1),("END",8.6)]
SW=[("הילי",.06),("ודלת",1.86),("נפתחה",2.66),("מה",3.9),("בריל",5.24),("כתבו",6.34),("והשם",7.4),("END",9.1)]
print({w:round(mr(t),2) for w,t in RW});print({w:round(ms(t),2) for w,t in SW})
