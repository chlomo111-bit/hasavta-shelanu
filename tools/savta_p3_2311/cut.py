import subprocess, json
SEGS=[(0.0,1.98),(2.32,4.95),(5.15,8.15),(8.50,11.10),(11.20,13.55),(14.35,16.85),(17.20,19.35),(19.65,22.98),(23.2,25.3),(25.65,27.98),(28.40,31.85)]
TEMPO=1.45
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(SEGS))
f+=''.join(f'[s{i}]' for i in range(len(SEGS)))+f'concat=n={len(SEGS)}:v=0:a=1,atempo={TEMPO}[o]'
import os
if os.environ.get('CUT'): subprocess.run(['ffmpeg','-v','error','-y','-i','/root/sv/p3/raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100','/root/sv/p3/voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in SEGS:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
W={"meatayim":0.6,"nechadim":1.18,"ktavtem":2.34,"hazevel":4.34,"tikach2":5.86,"derech":7.44,"ktavtem2":8.52,"savta":9.64,"raev":10.56,"yesh":11.22,"marak":13.06,"ata":14.38,"hayom":15.22,"kodem":15.94,"tochal":16.26,"ohad":17.26,"bo":18.6,"lechol":18.76,"uma":19.68,"chanuka":20.12,"ken":21.04,"nechgog":21.88,"beyachad":22.32,"nerot":23.24,"sufg":23.76,"vsvivon":24.48,"beod":25.68,"yamim":26.52,"simanu":27.1,"byoman":27.44,"ktvu":28.42,"shemchem":28.84,"lechem":29.18,"vsavta":30.02,"lashulchan":31.14,"END":31.85}
print(json.dumps({k:round(m(v),2) for k,v in W.items()}))
print('seg ends',[round(m(b),2) for a,b in SEGS])
