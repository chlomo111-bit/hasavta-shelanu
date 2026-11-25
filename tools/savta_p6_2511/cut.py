import subprocess, json, os
SEGS=[(0.0,2.68),(3.60,11.48),(14.0,27.2)]
TEMPO=1.2
D='/root/sv/p6'
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(SEGS))
f+=''.join(f'[s{i}]' for i in range(len(SEGS)))+f'concat=n={len(SEGS)}:v=0:a=1,atempo={TEMPO}[o]'
if os.environ.get('CUT'): subprocess.run(['ffmpeg','-v','error','-y','-i',D+'/raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100',D+'/voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in SEGS:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
if __name__=='__main__':
    for k,v in dict(n352=1.84,afad=3.64,lo=4.4,yadaim=5.28,kupsa1=6.77,od=7.68,vod=8.64,like=10.05,tg=10.32,sh=10.88,end_b=11.48,q1=14.09,q2=16.32,q3=18.08,han=20.45,han_e=22.08,kt=22.24,end=27.2).items(): print(k,round(m(v),2))
