import subprocess,json
# mots (début,fin) utiles du scribe ; on SAUTE le barème parlé 21.08-27.70 (il est joué en images)
W=[(0.08,0.48),(0.56,0.88),(0.96,1.2),(1.24,1.28),(1.36,1.76),(1.84,2.24),(2.32,2.56),(2.64,3.36),(3.52,3.76),(3.92,4.16),(4.507,4.88),(5,5.2),(5.24,6),(6.16,6.347),(6.373,6.56),(6.6,6.64),(6.72,7.2),(7.32,7.92),(8.08,8.2),(8.24,8.48),(8.56,9.12),(9.173,9.28),(9.36,10.16),(10.28,10.48),(10.52,10.72),(10.8,11.2),(11.627,12),(12.04,12.76),(13.04,13.12),(13.16,13.2),(13.24,13.84),(14.24,14.48),(14.52,14.72),(14.96,15.36),(15.52,16),(16.04,16.08),(16.12,16.56),(16.6,17.28),(17.813,18.32),(18.72,18.88),(18.96,19.12),(19.2,19.36),(19.44,19.76),(19.84,20.08),(20.16,21.04),(27.76,28.08),(28.16,28.4),(28.48,29.36),(29.44,29.76),(29.88,30.24),(30.56,30.72),(30.8,31.52),(31.64,31.8),(31.84,31.92),(31.96,32.16),(32.24,32.72),(32.8,33.2),(33.24,33.76),(33.84,33.92),(34.08,34.64)]
TOTAL=34.7;KEEP=.1;TEMPO=1.35
sil=[(W[i][1],W[i+1][0]) for i in range(len(W)-1) if W[i+1][0]-W[i][1]>.2]
segs=[];cur=0
for a,b in sil: segs.append((cur,a+KEEP/2));cur=b-KEEP/2
segs.append((cur,TOTAL))
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(segs))
f+=''.join(f'[s{i}]' for i in range(len(segs)))+f'concat=n={len(segs)}:v=0:a=1,atempo={TEMPO}[o]'
subprocess.run(['ffmpeg','-v','error','-y','-i','raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100','reel_voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in segs:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
P={'obj':0.08,'avant':3.52,'mdrg':4.507,'kodem_end':6.0,'olim':6.16,'rak':9.173,'esrim':10.28,'glida':11.627,'nimsa_end':12.76,'mi':13.04,'ehad':14.24,'hasachen':15.52,'moz_end':17.28,'vaata':17.813,'elef':18.72,'dayarim_end':21.04,'hamesh':27.76,'komot_end':29.36,'matan':29.44,'bifnim_end':31.52,'ktvu':31.64,'END':34.64}
print(json.dumps({k:round(m(v),2) for k,v in P.items()}))
