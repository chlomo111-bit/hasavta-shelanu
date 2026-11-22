import sys,json
sys.argv=['x'];exec(open('/home/claude/hasavta-shelanu/tools/hashchenim_2211/cut.py').read().split('mr=build')[0])
sil=[(0.972,1.128),(2.62,3.48),(6.083,6.576),(7.858,8.338),(8.516,9.047),(9.145,9.308),(9.365,10.296),(10.819,11.261),(11.776,12.09),(13.285,13.759),(14.356,14.57),(15.224,15.63),(16.3,16.681),(18.882,19.25),(20.298,20.521),(21.544,21.961),(24.504,24.955),(26.369,26.626)]
mr=build('reel_raw.mp3','reel_voice.mp3',sil,27.75,.1,1.2,lead=.15)
W={"ani":.2,"asseret":.8,"alafim":1.44,"nechadim":1.84,"hasavta":3.52,"hachi":4.44,"harbe":4.88,"baolam":5.52,"veachshav":6.56,"efes":9.04,"az":10.32,"like":11.36,"neched":12.16,"tguva":13.76,"shlosha":14.64,"shituf":15.72,"asara":16.72,"ratsim":17.76,"hamekomot":19.24,"tihyu":20.587,"kitvu":22.04,"shesavta":22.84,"tamid":23.76,"vehachamisha":25.0,"baim":26.667,"leechol":26.96,"END":27.75}
print(json.dumps({k:round(mr(v),2) for k,v in W.items()}))
ms=build('story_raw.mp3','story_voice.mp3',[(1.802,2.1),(3.152,3.504)],5.95,.1,1.05)
SW={"anachnu":0,"efes":1.0,"shatfu":2.1,"asara":3.6,"END":5.95}
print(json.dumps({k:round(ms(v),2) for k,v in SW.items()}))
