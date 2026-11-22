"""Coupe les silences de la voix (1 prise) + atempo, et donne les instants des phrases dans la voix montée. Usage : cd <dossier>; python3 cut.py"""
import subprocess,json
def build(src,out,sil,total,keep,tempo,lead=0):
    segs=[];cur=lead
    for a,b in sil: segs.append((cur,a+keep/2));cur=b-keep/2
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
SIL=[(2.66,2.86),(4.31,4.55),(4.91,5.37),(6.55,6.86),(7.27,7.65),(8.40,8.69),(9.20,9.57),(10.63,10.97),(13.44,13.93),(15.98,16.25)]
mr=build('reel_raw.mp3','reel_voice.mp3',SIL,19.12,.12,1.08)
W={"bonim":0,"kaveret":.85,"gdola":1.5,"10000":2.86,"like":4.55,"dvora1":5.37,"tguva":6.86,"shalosh":7.65,"shituf":8.69,"eser":9.57,"efes":10.97,"azru":11.9,"kitvu":13.93,"tafkid":14.8,"chamesh":16.25,"nichnasot":17.6,"END":19.0}
print(json.dumps({k:round(mr(v),2) for k,v in W.items()}))
ms=build('story_raw.mp3','story_voice.mp3',[(2.04,2.36),(3.22,3.47),(3.59,3.75)],5.92,.1,1.05)
print(json.dumps({k:round(ms(v),2) for k,v in {"efes":0,"shatfu":2.36,"eser":3.75,"END":5.85}.items()}))
