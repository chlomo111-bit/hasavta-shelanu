import sys,json
sys.argv=['x'];exec(open('/home/claude/hasavta-shelanu/tools/hashchenim_2211/cut.py').read().split('mr=build')[0])
sil=[(2.86,3.26),(4.72,4.92),(5.51,5.81),(7.76,8.13),(10.83,11.21),(12.56,12.85),(13.32,13.56),(14.03,14.38),(14.96,15.16),(16.47,16.89),(17.90,18.25),(18.88,19.08),(19.86,20.34),(22.40,22.73)]
mr=build('reel_raw.mp3','reel_voice.mp3',sil,25.3,.12,1.15,lead=.05)
P={'chelek':0,'boker':3.26,'veachshav':4.92,'193':5.81,'avarnu':8.13,'like':11.21,'tguva':12.85,'shlosha':13.56,'shituf':14.38,'asara':15.16,'uma':16.89,'dfikot':18.25,'kofzim':19.08,'kitvu':20.34,'chamesh':22.73,'END':25.3}
print(json.dumps({k:round(mr(v),2) for k,v in P.items()}))
ms=build('story_raw.mp3','story_voice.mp3',[],6.0,.1,1.0)
