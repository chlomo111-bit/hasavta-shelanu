import subprocess, json
SEGS=[(0.0,1.45),(6.46,7.50),(7.97,8.68),(8.88,9.95),(10.40,11.26),(11.56,12.22),(12.36,13.88),(14.25,15.42),(15.71,16.35),(16.56,18.10),(18.45,19.16),(19.38,21.92),(22.24,23.21),(23.46,24.11),(24.34,25.6),(25.81,29.27),(29.67,32.40),(32.68,33.69),(34.0,35.76)]
TEMPO=1.3; GAP=0.08
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(SEGS))
f+=''.join(f'[s{i}]' for i in range(len(SEGS)))+f'concat=n={len(SEGS)}:v=0:a=1,atempo={TEMPO}[o]'
subprocess.run(['ffmpeg','-v','error','-y','-i','reel_raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100','reel_voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in SEGS:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
W={"salta":0.22,"bri":6.53,"hu_omer1":8.03,"ani":8.94,"hu":10.46,"yachke_zeomer":11.62,"ata":12.42,"chaval":14.31,"zeomer3":15.77,"tagmor":16.62,"chamsa":18.51,"zeomer4":19.44,"sheaf":20.30,"baoi":22.30,"zeomer5":23.52,"altakum":24.40,"uvizchutchem":25.87,"mea":27.12,"kitvu":29.73,"veani":32.74,"veshilchu":34.06,"END":35.76}
print(json.dumps({k:round(m(v),2) for k,v in W.items()}))
