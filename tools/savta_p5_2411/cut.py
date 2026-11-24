import subprocess, json, os
SEGS=[(0.0,2.6),(2.8,4.7),(4.85,6.2),(6.5,8.05),(8.2,9.6),(9.9,11.45),(11.7,12.95),(13.0,14.55),(14.8,15.5),(15.7,18.0),(18.3,19.3),(19.6,23.75)]
TEMPO=1.15
D='/root/sv/p5'
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(SEGS))
f+=''.join(f'[s{i}]' for i in range(len(SEGS)))+f'concat=n={len(SEGS)}:v=0:a=1,atempo={TEMPO}[o]'
if os.environ.get('CUT'): subprocess.run(['ffmpeg','-v','error','-y','-i',D+'/raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100',D+'/voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in SEGS:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
W={"ani":0.08,"tzricha":0.3,"eseret":0.76,"alafim":1.34,"nechadim":1.74,"achalt":2.86,"lo":3.86,"achalt2":4.04,"shev":4.92,"tochal":5.3,"od":5.7,"like":6.58,"nechad":7.22,"echad":7.54,"tgova":8.28,"shlosha":9.06,"shitуf":10.0,"asara":10.72,"briut":11.78,"shev2":13.08,"tochal2":13.3,"hu":13.8,"yechake":13.9,"chamsa":14.88,"et":15.78,"kol":16.0,"ele":16.28,"atem":16.62,"ktavtem":17.06,"li":17.66,"achshav":18.36,"torchem":18.72,"ktvu":19.7,"mishpat":20.04,"shesavta":20.56,"shelachem":21.1,"tamid":21.52,"omeret":21.8,"uvou":22.72,"leechol":23.06}
if __name__=='__main__':
    print(json.dumps({k:round(m(v),2) for k,v in W.items()}, ensure_ascii=False))
    print('END',round(m(23.75),2))
