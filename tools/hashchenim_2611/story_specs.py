import json,sys
sys.argv=[sys.argv[0],'clips','1707','1707']
exec(open('specs.py').read().split("D=18.0")[0])
D=7.0
reel={'dur':D,'fps':30,'clips':{k:C[k] for k in ('wide','end')},'flash':.4,'novg':.5,'vgmax':.35,'hits':[0.02,2.4,4.0],
 'seg':[{'t0':0,'t1':3.3,'clip':'wide','off':0,'zoom':.02},{'t0':3.3,'t1':D,'clip':'end','off':0,'zoom':.02}],
 'ov':[O(0,D,'T',TITLE(1707).replace('חלק 7','היום'),1),
  O(0,2.4,'M',big(f'{Y("1,707")}<br>דיירים! 🏢',70),0),
  O(2.4,4.0,'M',big(f'שתפו את<br>{Y("הריל")} 🚀',66)),
  O(4.0,D,'M',big(f'כל שיתוף =<br>{Y("+10")} דיירים!',60)),
  O(0,D,'B',BAR(24),1)]}
json.dump(reel,open('clips/story.json','w'),ensure_ascii=False)
