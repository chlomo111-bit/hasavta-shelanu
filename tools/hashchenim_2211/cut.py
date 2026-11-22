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
mr=build('reel_raw.mp3','reel_voice.mp3',[(2.64,2.90),(4.24,4.42),(5.07,5.32),(5.88,6.27),(6.67,7.09),(8.18,8.45),(8.86,9.16),(9.68,10.05),(10.58,10.91),(12.42,13.25),(15.80,16.33),(18.37,18.73)],21.6,.1,1.1,lead=.25)
W={"אנחנו":.343,"גבוה":1.4,"עשרת":2.96,"וכל":4.56,"לייק":6.32,"דייר":7.12,"תגובה":8.4,"שלושה":9.2,"שיתוף":10.08,"קומה":10.92,"אפס":13.28,"עזרו":14.56,"כתבו":16.32,"שומעים":17.16,"חמש":18.93,"נכנסות":20.28,"END":21.68}
print(json.dumps({k:round(mr(v),2) for k,v in W.items()},ensure_ascii=False))
ms=build('story_raw.mp3','story_voice.mp3',[(1.86,2.04),(3.41,3.70),(4.53,4.91)],7.52,.1,1.08)
