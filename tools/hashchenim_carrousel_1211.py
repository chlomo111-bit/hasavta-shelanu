"""השכנים – carrousel 12.11 « 5 רמזים: מי דפק על הדלת? » : 7 slides 1080×1350 tirées du plateau 3D de hashchenim_ep4.py
(couloir, porte de Dana, traces blanches, porte d'Avi, façade). Éclairage relevé pour une image claire.
Usage : python3 tools/hashchenim_carrousel_1211.py <node_modules> <dossier_sortie>"""
import sys, os, re, math
from playwright.sync_api import sync_playwright
NM, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hashchenim_ep4.py')).read()
src = src[:src.index('def main')]
src = src.replace('NM, OUT = sys.argv[1], sys.argv[2]', 'pass').replace("os.makedirs(OUT, exist_ok=True)", '')
src = src.replace('R.setSize(540,960)', 'R.setSize(540,675)').replace('540/960', '540/675')
src = src.replace('scene.add(new THREE.HemisphereLight(0x8fa0ff,0x201030,.55))', 'scene.add(new THREE.HemisphereLight(0xc8d0ff,0x403050,1.15))')
src = src.replace('scene.background=new THREE.Color(0x0b0a1e)', 'scene.background=new THREE.Color(0x1d1940)')
g = {'NM': NM, 'sys': sys, '__name__': 'x'}
exec(src, g)
HTML, ease, lerp = g['HTML'], g['ease'], g['lerp']
HTML = HTML.replace('l.intensity=.55*', 'l.intensity=1.1*').replace("new THREE.PointLight(0xffd9a0,.55,7,2)", "new THREE.PointLight(0xffd9a0,1.1,9,2)")

Y = lambda s: f'<span style="color:#FFC24B">{s}</span>'
CSS = """#my{position:fixed;inset:0;pointer-events:none;font-family:Heebo;direction:rtl;color:#fff}
#my .t{position:absolute;left:0;right:0;text-align:center;padding:0 22px;text-shadow:0 3px 14px rgba(0,0,0,.95),0 0 4px rgba(0,0,0,.8)}
#my .h{font:900 46px/1.12 Heebo}#my .s{font:900 30px/1.2 Heebo}
#my .tag{display:inline-block;background:#FFC24B;color:#1a0f2a;border-radius:999px;padding:6px 20px;font:900 24px Heebo;text-shadow:none}
#my .band{position:absolute;left:0;right:0;height:34%;}
#my .num{position:absolute;bottom:2.5%;left:4%;font:900 18px Heebo;color:#fff;opacity:.85;text-shadow:0 2px 6px #000}
#my .brand{position:absolute;top:2.5%;right:4%;background:rgba(12,10,30,.75);border:2px solid #C792EA;border-radius:999px;padding:3px 12px;font:900 15px Heebo}
#my .v{display:inline-block;width:42%;margin:6px;border-radius:22px;padding:12px 0;font:900 38px/1.15 Heebo;text-shadow:none}
"""
TOPBAND = '<div class=band style="top:0;background:linear-gradient(rgba(10,8,30,.8),rgba(10,8,30,0))"></div>'
BOTBAND = '<div class=band style="bottom:0;background:linear-gradient(rgba(10,8,30,0),rgba(10,8,30,.85))"></div>'

base = dict(t=0, dana=None, dry=0, env=False, open=0, knock=0, steps=0, avi=0, flick=False, scared=False, flash=0, key='x', top='', mid='', bot='')
SLIDES = [
    # 1 : accroche – la porte de Dana, gros plan
    (dict(cam=[-2.6, 1.55, 1.4], look=[-3.45, 1.35, -1.5]),
     TOPBAND + BOTBAND + f'<div class="t h" style="top:9%">מישהו דפק בדלת<br>ב־{Y("3 בלילה")} 🚪</div>'
     + f'<div class="t h" style="bottom:15%">…ולא היה שם<br>{Y("אף אחד")} 😨</div>'
     + '<div class="t s" style="bottom:6%">5 רמזים · מי זה? ←</div>'),
    # 2 : l'enveloppe
    (dict(dana=[-4, 0, .4], dry=.7, env=True, cam=[-1.2, 2.0, 1.6], look=[-3.75, 1.75, .2]),
     TOPBAND + BOTBAND + '<div class="t" style="top:7%"><span class=tag>רמז 1</span></div>'
     + f'<div class="t h" style="top:14%">{Y("מכתב")} ✉️</div>'
     + f'<div class="t s" style="bottom:8%">חיכה לדנה בדירה הריקה…<br>עם {Y("השם שלה")} עליו</div>'),
    # 3 : les traces
    (dict(open=1, steps=1, cam=[-2.1, 1.3, 1.1], look=[0.2, 0, -.9]),
     TOPBAND + BOTBAND + '<div class="t" style="top:7%"><span class=tag>רמז 2</span></div>'
     + f'<div class="t h" style="top:14%">{Y("עקבות לבנות")} 👣</div>'
     + f'<div class="t s" style="bottom:8%">קטנות מדי<br>בשביל {Y("בן אדם")}…</div>'),
    # 4 : la porte d'Avi
    (dict(open=1, steps=1, avi=1, cam=[3.9, 1.45, 1.5], look=[6.0, 1.2, -1.5]),
     TOPBAND + BOTBAND + '<div class="t" style="top:7%"><span class=tag>רמז 3</span></div>'
     + f'<div class="t h" style="top:14%">הן נעצרות ב…</div>'
     + f'<div class="t h" style="bottom:8%">דירה 9 של {Y("אבי")} 😱</div>'),
    # 5 : la façade – les lapins
    (dict(cam=[2.5, 7.5, -16], look=[0, 9.5, -40]),
     TOPBAND + BOTBAND + '<div class="t" style="top:7%"><span class=tag>רמז 4</span></div>'
     + f'<div class="t h" style="top:14%">השבוע ראו<br>{Y("ארנבים")} בבניין 🐰</div>'
     + f'<div class="t s" style="bottom:8%">והאור אצל אבי<br>{Y("לא כבה")} כל הלילה 💡</div>'),
    # 6 : Dana devant chez Avi – le vote
    (dict(dana=[4.0, 0, .3], dry=-math.pi / 2 + .6, open=1, steps=1, avi=1, cam=[0.6, 2.05, 1.5], look=[4.3, 1.75, 0.1]),
     TOPBAND + BOTBAND + '<div class="t" style="top:7%"><span class=tag>רמז 5</span></div>'
     + f'<div class="t h" style="top:14%">הדלת של אבי<br>{Y("פתוחה")}… 🚪</div>'
     + '<div class="t" style="bottom:12%"><div class="v" style="background:#2fbf71">1️⃣<br>דנה נכנסת</div><div class="v" style="background:#E5484D">2️⃣<br>דנה בורחת</div></div>'
     + '<div class="t s" style="bottom:4%">תענו 1 או 2 👇</div>'),
    # 7 : entrer dans le jeu
    (dict(cam=[-3.0, 6.5, -14], look=[0, 8.5, -40]),
     TOPBAND + BOTBAND + f'<div class="t h" style="top:9%">רוצים לגור<br>{Y("בבניין")}? 🏢</div>'
     + f'<div class="t h" style="bottom:17%">כתבו {Y("שכן")}<br>ותיכנסו 👇</div>'
     + f'<div class="t s" style="bottom:7%">📩 שלחו לשכן שלכם</div>'),
]

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': 540, 'height': 675}, device_scale_factor=2)
        pg.route('http://local/three.min.js', lambda r: r.fulfill(path=f'{NM}/three/build/three.min.js', content_type='text/javascript'))
        pg.route('http://local/', lambda r: r.fulfill(body=HTML, content_type='text/html'))
        pg.add_init_script("Math.random=(()=>{let s=777;return()=>{s=(s*16807)%2147483647;return(s-1)/2147483646}})();")
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('http://local/'); pg.wait_for_function('window.ready===true', timeout=60000); pg.wait_for_timeout(800)
        pg.add_style_tag(content='#ov{display:none!important}' + CSS)
        pg.evaluate("()=>{const d=document.createElement('div');d.id='my';document.body.appendChild(d)}")
        only = os.environ.get('ONLY')
        for i, (cfg, html) in enumerate(SLIDES, 1):
            if only and str(i) not in only.split(','): continue
            o = dict(base); o.update(cfg); o['t'] = 1.3
            pg.evaluate('o=>F(o)', o)
            pg.evaluate('h=>{document.getElementById("my").innerHTML=h}', html + f'<div class=brand>🏢 השכנים</div><div class=num>{i}/{len(SLIDES)}</div>')
            pg.wait_for_timeout(300)
            pg.screenshot(path=f'{OUT}/slide{i}.jpg', type='jpeg', quality=92)
        print('slides', len(SLIDES), 'erreurs', errs[:5]); b.close()

main()
