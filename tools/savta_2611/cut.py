import subprocess, json, os
# Segments gardés de la prise unique (temps d'origine, secondes)
SEGS=[(0.06,2.22),(2.46,5.16),(7.70,9.54),(9.76,11.38),(11.74,13.94),(18.08,20.30),(22.48,24.28),(25.86,27.18),(28.42,30.40),(32.16,34.60),(34.94,37.70)]
TEMPO=1.2
D='/root/sv/p7'
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={b-a-0.03:.3f}:d=0.03[s{i}];' for i,(a,b) in enumerate(SEGS))
f+=''.join(f'[s{i}]' for i in range(len(SEGS)))+f'concat=n={len(SEGS)}:v=0:a=1,atempo={TEMPO}[o]'
if os.environ.get('CUT'): subprocess.run(['ffmpeg','-v','error','-y','-i',D+'/raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100',D+'/voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in SEGS:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
def seg_start(i):
    return sum(b-a for a,b in SEGS[:i])/TEMPO
TOTAL=sum(b-a for a,b in SEGS)/TEMPO
if __name__=='__main__': print('total',round(TOTAL,2),[round(seg_start(i),2) for i in range(len(SEGS))])
