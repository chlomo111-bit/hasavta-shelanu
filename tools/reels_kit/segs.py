import subprocess,re,sys
def segs(f,th=-35,d=0.18):
    o=subprocess.run(['ffmpeg','-hide_banner','-i',f,'-af',f'silencedetect=noise={th}dB:d={d}','-f','null','-'],capture_output=True,text=True).stderr
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    S=[float(x) for x in re.findall(r'silence_start: ([0-9.]+)',o)];E=[float(x) for x in re.findall(r'silence_end: ([0-9.]+)',o)]
    out=[];t=0
    for s,e in zip(S,E+[dur]):
        if s-t>0.05: out.append((round(t,2),round(s,2)))
        t=e
    if dur-t>0.1: out.append((round(t,2),round(dur,2)))
    return out
if __name__=='__main__':
    for f in sys.argv[1:]: print(f,[ (a,b,round(b-a,2)) for a,b in segs(f)])
