import subprocess, json, os
SEGS=[(0.0,2.1),(2.5,5.8),(6.15,8.3),(8.7,11.0),(11.45,13.4),(13.8,15.85),(16.1,17.8),(18.1,20.2),(20.75,23.1),(23.5,24.4),(24.65,29.05)]
TEMPO=1.3
D='/root/sv/p4'
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[s{i}];' for i,(a,b) in enumerate(SEGS))
f+=''.join(f'[s{i}]' for i in range(len(SEGS)))+f'concat=n={len(SEGS)}:v=0:a=1,atempo={TEMPO}[o]'
if os.environ.get('CUT'): subprocess.run(['ffmpeg','-v','error','-y','-i',D+'/raw.mp3','-filter_complex',f,'-map','[o]','-ar','44100',D+'/voice.mp3'],check=True)
def m(t):
    acc=0
    for a,b in SEGS:
        if t<=b: return (acc+max(0,t-a))/TEMPO
        acc+=b-a
    return acc/TEMPO
W={"avarnu":0.06,"shalosh":0.66,"meot":1.06,"nechadim":1.3,"veohad":2.58,"katav":3.1,"ani":3.94,"chayav":4.18,"lazuz":4.48,"yesh":5.06,"tisa":5.38,"shev":6.22,"tochal":6.8,"hu":7.52,"yechake":7.68,"umishehu":8.8,"katav2":9.3,"briut":10.04,"briut2":11.52,"briut3":12.08,"metukim":12.54,"sheli":13.06,"vyesh":13.88,"mi":14.14,"shekatav":14.26,"boi":15.04,"tochli":15.32,"az":16.18,"bou":16.38,"bou2":16.92,"leechol":17.16,"chamsa":18.2,"chamsa2":18.58,"shelo":19.16,"ayin":19.68,"hara":19.9,"veim":20.82,"ata":21.06,"lo":21.34,"nechad":21.56,"az2":22.34,"mi2":22.54,"ken":22.76,"ata2":23.56,"nechad2":23.84,"ktvu":24.72,"mishpat":25.08,"shesavta":25.52,"shelachem":26.06,"tamid":26.5,"omeret":26.84,"vshilchu":27.7,"lasavta":28.36}
if __name__=='__main__':
    print(json.dumps({k:round(m(v),2) for k,v in W.items()}))
    print('END',round(m(29.05),2),'seg ends',[round(m(b),2) for a,b in SEGS])
