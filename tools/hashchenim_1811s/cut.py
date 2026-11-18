import subprocess,sys
def build(src,out,sil,total,keep,tempo):
    segs=[];cur=0
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
R=[(1.319,1.572),(2.918,3.503),(4.643,5.311),(5.830,6.194),(7.165,7.660),(8.940,9.388),(10.476,10.739),(11.990,12.520),(13.303,13.590),(14.788,15.041),(15.550,15.745)]
mr=build('reel_raw.mp3','reel_voice.mp3',R,16.8,.12,1.04)
ms=build('story_raw.mp3','story_voice.mp3',[(1.524,1.906),(3.327,3.742),(4.545,5.029)],6.0,.14,1.0)
pts=[0,1.57,3.5,5.31,6.19,7.66,9.39,10.74,12.52,13.59,15.04,15.75,16.62]
print([round(mr(t),2) for t in pts]); print([round(ms(t),2) for t in [0.2,1.906,3.742,5.029,5.75]])
