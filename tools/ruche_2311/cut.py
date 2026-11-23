"""Ruche 23.11 matin : garde les phrases utiles de la voix (1 prise), silences coupés + atempo, et donne les instants des mots dans la voix montée.
Usage : cd <dossier>; python3 cut.py   (reel_raw.mp3 -> reel_voice.mp3, tm.json)"""
import subprocess,json
TEMPO=1.28
SEGS=[(0.04,2.14),(5.08,8.14),(8.28,12.26),(12.44,15.34),(15.80,18.98),(19.16,21.58),(21.72,23.78),('sil',1.75),(28.04,31.04)]
f='';n=0;tl=[];cur=0
for s in SEGS:
    if s[0]=='sil':
        f+=f'anullsrc=r=44100:cl=mono,atrim=0:{s[1]}[s{n}];';tl.append(('sil',cur,cur+s[1]/TEMPO,None))
        cur+=s[1]/TEMPO
    else:
        f+=f'[0:a]atrim={s[0]}:{s[1]},asetpts=PTS-STARTPTS[s{n}];';d=(s[1]-s[0])/TEMPO;tl.append((s[0],cur,cur+d,s[1]));cur+=d
    n+=1
f+=''.join(f'[s{i}]' for i in range(n))+f'concat=n={n}:v=0:a=1,atempo={TEMPO}[o]'
subprocess.run(['ffmpeg','-v','error','-y','-i','reel_raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100','reel_voice.mp3'],check=True)
def m(t):
    for a,o0,o1,b in tl:
        if a!='sil' and a<=t<=b+1e-6: return round(o0+(t-a)/TEMPO,2)
    return None
W={"hakavoret":0.08,"gdola":1.12,"olam":1.44,"kolit":5.12,"achat":6.2,"hodaot":6.8,"kolyot":7.28,"romantit":8.32,"ani":9.49,"baderech":9.92,"adayin":10.88,"bamita":11.4,"chakhama":12.48,"ra'ata":13.68,"lo":14.52,"anta":14.8,"balyanit":15.84,"mi":16.93,"hadsmooth":17.28,"nealma":18.08,"malka":19.2,"megenet":20.28,"kulan":21.2,"anachnu":21.76,"esrim":22.28,"dvorim":23.04,"kitvu":28.08,"tafkid":28.6,"atren":29.04,"tagu":29.48,"chavera":29.96,"shelachen":30.44}
out={k:m(v) for k,v in W.items()};out['tl']=[(round(a,2) if a!='sil' else a,round(o0,2),round(o1,2)) for a,o0,o1,b in tl];out['END']=round(cur,2)
json.dump(out,open('tm.json','w'),ensure_ascii=False);print(json.dumps(out,ensure_ascii=False))
