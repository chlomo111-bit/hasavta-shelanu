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
sil=[(2.05,2.48),(3.08,3.40),(4.76,5.17),(5.75,5.96),(6.67,7.06),(7.65,7.84),(9.55,10.12),(11.45,11.93),(12.78,13.42),(15.61,15.98),(16.32,16.53),(17.02,17.37),(17.84,18.04),(18.69,18.94),(19.46,19.63),(20.34,20.78)]
mr=build('reel_raw.mp3','reel_voice.mp3',sil,23.44,.1,1.1,lead=.0)
P={'koma2':2.48,'dfikot':3.40,'shlishit':5.17,'rivim':5.96,'revi':7.06,'mikdach':7.84,'umi':10.12,'hashachen':11.93,'anachnu':13.42,'like':15.98,'plus1':16.53,'tguva':17.37,'plus3':18.04,'shituf':18.94,'plus10':19.63,'kitvu':20.78,'END':23.44}
print(json.dumps({k:round(mr(v),2) for k,v in P.items()}))
