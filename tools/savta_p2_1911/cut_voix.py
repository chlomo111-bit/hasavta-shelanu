S=[('A',.10,1.98),('B',2.94,4.14),('C',4.48,5.26),('D',5.66,6.24),('E',6.72,7.56),('F',7.88,8.90),('G',9.36,10.22),('H',10.62,11.70),('I',12.04,14.02),('J',14.78,15.58),('K',15.80,16.72),('L',17.02,18.00),('M',18.24,19.46),('N',19.72,20.86),('P',22.22,23.80)]
GAP={'J':.2,'L':.25}
TEMPO=1.24
parts=[];t=0;out=[]
for i,(n,a,b) in enumerate(S):
    g=0 if i==0 else GAP.get(n,.1)
    if g: parts.append(f"anullsrc=r=44100:cl=mono,atrim=0:{g}[g{i}]"); t+=g
    out.append((n,round(t/TEMPO,2),round((t+b-a)/TEMPO,2))); t+=b-a
f=[]
lab=[]
for i,(n,a,b) in enumerate(S):
    f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aformat=sample_rates=44100:channel_layouts=mono[s{i}]")
    if i: lab.append(f"[g{i}]")
    lab.append(f"[s{i}]")
fc=';'.join(f+parts)+';'+''.join(lab)+f"concat=n={len(lab)}:v=0:a=1,atempo={TEMPO},apad=pad_dur=0.2[o]"
import subprocess
subprocess.run(['ffmpeg','-y','-v','error','-i','raw.mp3','-filter_complex',fc,'-map','[o]','-ar','44100','voix.wav'],check=True)
for o in out: print(o)
print('total',round(t/TEMPO,2))
