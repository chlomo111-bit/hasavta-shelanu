# Stories « שבת שלום » du vendredi 20.11.2026 — une image 1080x1920 par jeu, Heebo, texte centré.
# usage : python3 build.py <dossier_frames> <dossier_sortie>
import sys, base64, io
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

SRC, OUT = sys.argv[1], sys.argv[2]
HEEBO = '/root/three3/node_modules/@fontsource/heebo/files/heebo-hebrew-{w}-normal.woff2'
HEEBO_L = '/root/three3/node_modules/@fontsource/heebo/files/heebo-latin-{w}-normal.woff2'

# y0 = fraction du haut à couper (zone où l'ancien texte du reel apparaissait)
STORIES = {
  'ruche': dict(win=(.13,.70), accent='#FFC24B', pill='שבת שלום מהכוורת 🐝',
      big='אותה שמלה בדיוק… 👗', when='ביום ראשון – פרק 2!',
      ask='מה היא עושה? <b>1</b> הולכת להחליף · <b>2</b> מצטלמות תאומות<br>כתבו בתגובות לריל 👇',
      who='🐝 ברוכה הבאה לכוורת <span dir="ltr">@hyll.khbsvb</span>'),
  'bateau': dict(win=(.18,.80), accent='#5EC8FF', pill='שבת שלום מהספינה ⚓',
      big='הלוויתן פותח את הפה… 🐋', when='ביום ראשון – פרק 3!',
      ask='מה הטבח מציל? <b>1</b> העוגה 🎂 · <b>2</b> הקפטן 🧭<br>כתבו בתגובות לריל 👇',
      who='⚓ על הסיפון: <span dir="ltr">@amit_azulay23</span>'),
  'noise': dict(win=(.22,.80), accent='#FF5A6E', pill='שבת שלום מהבמה 🎤',
      big='היד על הכפתור… 🔴', when='ביום רביעי – פרק 2!',
      ask='<span dir="ltr">@jewels_by_girlz</span> כבר הצביעה: לוחץ!<br>ואתם? <b>1</b> לוחץ · <b>2</b> נותן לסיים 👇',
      who='🎤 על הבמה: <span dir="ltr">@bdvy214</span>'),
  'savta': dict(win=(.24,.92), accent='#FFB3C7', pill='שבת שלום מסבתא 🕯️🕯️',
      big='מי בדלת של סבתא? 🚪', when='ביום ראשון סבתא פותחת!',
      ask='בינתיים מוביל: <b>1</b> הנכד שלא מתקשר 📵<br>ואתם? 1 או 2 בתגובות לריל 👇',
      who='💛 תודה שהצבעתם!<br><span dir="ltr">@kaplan_mei · @yanai_nisim_lavi</span>'),
}

def b64(im):
    b = io.BytesIO(); im.save(b, 'JPEG', quality=92)
    return base64.b64encode(b.getvalue()).decode()

def imgs(k, win):
    im = Image.open(f'{SRC}/full_{k}.jpg').convert('RGB')
    w, h = im.size
    blur = im.filter(ImageFilter.GaussianBlur(28))           # fond flou : l'ancien texte du reel devient illisible
    window = im.crop((0, int(h * win[0]), w, int(h * win[1])))  # zone sans texte, personnages nets
    return b64(blur), b64(window)

def font(w, path):
    return base64.b64encode(open(path.format(w=w), 'rb').read()).decode()

FONTS = ''.join(
    f"@font-face{{font-family:H;font-weight:{w};src:url(data:font/woff2;base64,{font(w,HEEBO)})}}"
    f"@font-face{{font-family:H;font-weight:{w};src:url(data:font/woff2;base64,{font(w,HEEBO_L)});unicode-range:U+0000-00FF}}"
    for w in (500, 800, 900))

TPL = """<!doctype html><html dir="rtl"><head><meta charset="utf-8"><style>{fonts}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden}}
body{{background:#222 url(data:image/jpeg;base64,{bg}) center/cover;font-family:H,'Noto Color Emoji',sans-serif;color:#fff;
 display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px}}
.win{{width:620px;border-radius:48px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.35);border:6px solid {accent};line-height:0}}
.win img{{width:100%;display:block}}
.card{{width:900px;box-sizing:border-box;padding:40px 44px 40px;border-radius:56px;background:rgba(18,20,34,.80);
 text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35)}}
.pill{{display:inline-block;background:{accent};color:#1b1b28;font-weight:900;font-size:50px;padding:14px 40px;border-radius:999px}}
.big{{font-weight:900;font-size:66px;line-height:1.15;margin:30px 0 18px}}
.when{{font-weight:900;font-size:62px;color:{accent};margin-bottom:30px}}
.ask{{font-weight:500;font-size:40px;line-height:1.45;opacity:.95}}
.ask b{{color:{accent};font-weight:900}}
.who{{margin-top:34px;font-weight:800;font-size:38px;background:rgba(255,255,255,.12);border-radius:28px;padding:16px 20px}}
</style></head><body><div class="win"><img src="data:image/jpeg;base64,{win}"></div><div class="card"><div class="pill">{pill}</div><div class="big">{big}</div>
<div class="when">{when}</div><div class="ask">{ask}</div><div class="who">{who}</div></div></body></html>"""

with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920})
    for k, d in STORIES.items():
        if len(sys.argv) > 3 and k not in sys.argv[3:]: continue
        bgi, wi = imgs(k, d['win']); dd = {x: v for x, v in d.items() if x != 'win'}
        pg.set_content(TPL.format(fonts=FONTS, bg=bgi, win=wi, **dd)); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{OUT}/story_{k}.png')
        Image.open(f'{OUT}/story_{k}.png').convert('RGB').save(f'{OUT}/story_{k}.jpg', quality=92)
        print('ok', k)
    br.close()
