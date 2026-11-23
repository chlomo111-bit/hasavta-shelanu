import subprocess,json
W=[(0.08,0.38),(0.42,0.66),(0.68,0.76),(0.8,1.22),(1.28,1.64),(1.68,1.98),(2.02,2.58),(2.86,3.38),(3.42,3.72),(3.76,4.28),(4.78,4.96),(5.02,5.52),(5.92,6.54),(6.98,7.32),(7.34,7.94),(7.98,8.16),(8.26,8.42),(8.44,8.94),(9.34,9.76),(9.78,9.86),(9.88,10.44),(10.84,11.3),(11.36,11.72),(11.76,11.9),(12.0,12.16),(12.18,12.84),(13.7,13.78),(13.82,13.88),(13.9,14.4),(14.94,15.52),(15.74,16.08),(16.14,16.38),(16.44,16.74),(16.76,17.26),(17.28,17.76),(18.22,18.54),(18.78,19.02),(19.06,19.4),(19.68,20.14),(20.36,20.76),(21.16,21.7),(21.88,22.38),(22.88,23.28),(23.32,23.6),(23.64,24.18),(24.58,24.8),(24.84,24.9),(24.94,25.2),(25.26,25.7),(25.84,26.26),(26.28,26.82),(26.98,27.06),(27.08,27.54)]
TOTAL=27.76;KEEP=.12;TEMPO=1.2
sil=[(W[i][1],W[i+1][0]) for i in range(len(W)-1) if W[i+1][0]-W[i][1]>.25]
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
P={'obj':0.08,'10k':2.86,'avant':4.78,'p1':6.98,'p2':9.34,'kid':10.84,'mizeh':13.7,'veat':14.94,'cnt':15.74,'cntend':17.76,'like':18.22,'tguva':19.68,'shituf':21.16,'plus10':21.88,'floors':22.88,'floorsend':24.18,'kitvu':24.58,'hashchen':25.84,'END':27.54}
print(json.dumps({k:round(m(v),2) for k,v in P.items()}))
