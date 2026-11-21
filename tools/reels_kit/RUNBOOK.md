# Pilote automatique des 5 jeux (חמשת העולמות)

Ce fichier est pour la séance programmée qui gère seule les jeux de Shlomo. Il a été écrit le 11.11.2026, sur son ordre : « à partir de maintenant tu te gères tout seul : stories, reels, posts, commentaires ».

## Règles absolues
- **Aucun vrai argent**, sous aucune forme (pas de gain, de loterie ni de promesse).
- **Ne rien publier avant 08:00.** Rien pendant Shabbat, du vendredi au coucher du soleil jusqu'au samedi soir après la sortie.
- **Toujours passer l'id du compte Composio.** Ne jamais utiliser `instagram_unhave-raband`, `instagram_caper-freon` (ce sont des comptes @chlomo_assouline) ni `instagram_mush-raff`.

  | Jeu | Id Composio |
  |---|---|
  | Ruche (@hakaveret_shelanu) | `instagram_recoup-katar` |
  | Bateau (@tovim_beyachad) | `instagram_odoom-cither` |
  | The Noise (@the_noise_2026) | `instagram_howel-rootle` |
  | סבתא מזל (@hasavta.shelanu) | `instagram_ensate-diacle` |
  | השכנים (@hashchenim) | `instagram_rare-hanna` |

- **Commentaires anti-spam :**
  - une seule réponse du compte par commentaire ;
  - ne pas répondre à un point, un emoji seul, « קדימה » ou un vote répété ;
  - pas d'annonce dans le fil d'un joueur ;
  - si quelqu'un écrit « הארנב » (le mot secret de l'énigme), répondre seulement « רשמנו 👀 נגלה בקרוב… ».
- **Ne jamais toucher** aux autres automatisations, à Meta Ads, ni aux publications existantes.
- **Prévenir Shlomo seulement si c'est grave** : commentaire haineux ou dangereux, compte bloqué, échec de publication répété.
- Rester économe en crédits : une seule prise de voix ElevenLabs par texte.

## Stratégie
Un univers, 5 mondes. Chaque compte a son rôle :
- **השכנים** : la série mystère, épisodes avec votes 1/2.
- **Ruche** : la course à la couronne, avec votes et titres.
- **Bateau** : le défi collectif, où chaque partage est un coup contre le bateau.
- **The Noise** : les vraies voix des abonnés.
- **סבתא מזל** : l'émotion et les conseils de grand-mère, « שלחו לסבתא שלכם ».

**Récompense = apparaître dans le jeu** : le nom du joueur dans la vidéo, un titre, ou le choix du prochain rebondissement.

**Calendrier : un reel par jour, sur un seul compte.**

| Jour | Compte du reel |
|---|---|
| Dimanche | השכנים |
| Lundi | Ruche |
| Mardi | Bateau |
| Mercredi | The Noise |
| Jeudi | סבתא מזל |
| Vendredi | Pas de reel. Sur chaque compte, sa propre story « שבת שלום » (au moins 1 h avant l'entrée), puis bilan de la semaine dans le journal |
| Samedi soir | השכנים |

Chaque jour, chaque compte publie aussi une story « famille » de 6 à 8 s avec voix qui renvoie au reel du jour ou au vote en cours. Le dimanche, le reel « ברוכים הבאים » cite le nom des nouveaux commentateurs.

## Stratégie « RECORD DU MONDE » du 21.11.2026 — PRIORITAIRE SUR TOUT (remplace les épisodes « 1 או 2 » du 18.11)
Shlomo, 21.11 22:32, après analyse du reel viral de @lifeofhyro (« THE BIGGEST BAND IN THE WORLD? ») : « applique tout, fais de nos chaînes des comptes viraux ». Constat : nos vidéos demandent au spectateur de SUIVRE une histoire ; les siennes lui demandent de PARTICIPER à un record. Le spectateur devient un joueur. Ce qui reste valable du 18.11 : contrôle viral (point 0), 1re seconde pour un inconnu, plateau 3D filmé, anti-gel, voix 1 prise, rien avant 08:00 ni pendant Shabbat, aucun vrai argent.

1. UN OBJECTIF GÉANT PAR COMPTE, compris en 1 seconde par un inconnu (titre en haut de l'écran, toute la vidéo) :
   - Bateau @tovim_beyachad : « הספינה הכי גדולה בעולם? » — objectif 10,000 נוסעים → à 10,000 la ספינה coule (fin de saison). Commentaire demandé : « כתבו מה אתם לוקחים איתכם לספינה 👇 ».
   - Ruche @hakaveret_shelanu : « הכוורת הכי גדולה בעולם? » — 10,000 דבורים. Commentaire : « כתבו איזה תפקיד אתם רוצים בכוורת 👇 » (מלכה, שומרת, מכינה דבש, עצלנית…).
   - The Noise @the_noise_2026 : « המקהלה הכי מזייפת בעולם? » — 10,000 זמרים. Commentaire : « כתבו איזה כלי אתם מנגנים (או איזה שיר אתם מזייפים) 👇 ».
   - השכנים @hashchenim : « הבניין הכי גבוה בעולם? » — 10,000 דיירים (le bâtiment monte d'un étage tous les 100). Commentaire : « כתבו מה השכנים שומעים מהדירה שלכם 👇 ».
   - סבתא @hasavta.shelanu : « הסבתא עם הכי הרבה נכדים בעולם? » — 10,000 נכדים. Commentaire : « כתבו משפט שסבתא שלכם תמיד אומרת 👇 ».
2. LE COMPTEUR EST RÉEL, jamais inventé. Départ 0 le 22.11.2026 pour chaque compte. Points = somme, sur toutes les publications du fil publiées depuis le 22.11 : like_count ×1 + commentaires d'autres personnes que le compte ×3 + saved ×5 + shares ×10 (GET_IG_USER_MEDIA + GET_IG_MEDIA_INSIGHTS). La séance recalcule, écrit la valeur dans tools/reels_kit/RECORD.json (compte, date, points, détail) et dans JOURNAL.md. Dans la vidéo, le compteur monte de la valeur du reel précédent à la valeur réelle d'aujourd'hui (jamais au-delà). Si rien n'a bougé, il reste fixe avec « עזרו לנו לעבור את X! ». Petit chiffre = on l'assume : « התחלנו מאפס – כל לייק זה עוד נוסע ».
3. LE BARÈME À L'ÉCRAN dans chaque reel et chaque story : « לייק +1 · תגובה +3 · שמירה +5 · שיתוף +10 » (bandeau du bas, icônes). Le partage vaut le plus : c'est voulu.
4. TOP 5 : les 5 commentaires les plus likés du reel précédent (égalité → le plus ancien ; jamais les commentaires du compte) apparaissent dans le reel suivant : pseudo réel + ce qu'ils ont écrit, sur un personnage du plateau (le passager avec son objet, la dabora avec son rôle, le musicien avec son instrument, le voisin à sa fenêtre, le petit-enfant à la table de סבתא qui répète la phrase). Moins de 5 → seulement les vrais ; 0 → « המקומות פנויים – תהיו הראשונים ». Jamais de pseudo inventé. Écran de fin : « 5 התגובות הכי טובות נכנסות לפרק הבא 🏆 ».
5. STRUCTURE DU REEL (15 à 20 s, numéro discret « חלק N ») :
   0–1 s : titre-question + plan large spectaculaire (foule, bateau énorme, bâtiment géant) + compteur visible.
   1–4 s : la voix annonce l'objectif (« אנחנו בונים את הספינה הכי גדולה בעולם… ») — UN gros mot à l'écran à la fois (Heebo 900, blanc, mots clés #FFC24B, zone centrale), coupe toutes les 1 s.
   4–10 s : le barème joué en images (לייק → un personnage arrive ; תגובה → 3 ; שיתוף → une foule de 10), le compteur monte jusqu'à la vraie valeur.
   10–14 s : le Top 5 du reel précédent entre dans le monde (pseudos lisibles).
   14–18 s : « כתבו ___ 👇 » + barème + « 5 התגובות הכי טובות נכנסות לפרק הבא ». Fin qui boucle avec le début (pas d'écran noir, pas de gel).
   Musique rythmée qui monte (music.py), drop au moment où le compteur bondit.
6. RÉPONSES AUX COMMENTAIRES : chaque commentateur reçoit une réponse qui confirme ses points (« +3 נוסעים בזכותך! 🚢 », varier) et, s'il est dans le Top 5, « אתה בפרק הבא! ». Plus de vote 1/2, plus de mots d'entrée (שכן, דבורה…) : le commentaire demandé au point 1 les remplace.
7. STORIES : (a) le compteur du jour + barème + « שתפו את הריל = +10 », (b) le Top 5 en cours (pseudos réels) ou la question du point 1. Toujours bien centrées.
8. PALIERS : à chaque centaine franchie (100, 200…), un événement visible dans le monde au reel suivant (nouvel étage, nouveau pont, nouvelle rangée de chanteurs…) et annoncé en story. Jamais de récompense en argent.
9. COLLAB : si Shlomo fournit un créateur partenaire, « ft. @pseudo » en haut, comme la référence. Les séances ne contactent personne.
11. APPEL AUX PARTENAIRES (Shlomo, 21.11 23:42 : « on vous cherche pour devenir notre partenaire ») : une fois par semaine et par compte, lors de sa PREMIÈRE séance de la semaine (dimanche ; lundi pour The Noise), une story EN PLUS, image 1080×1920 centrée, plan spectaculaire du monde du compte : « 🤝 מחפשים שותפים! / יש לכם עמוד, טיקטוק או ערוץ? / תהיו דמות קבועה בסדרה – עם השם שלכם על המסך / כתבו "שותף" בתגובות לריל האחרון 👇 ». Aucune promesse d'argent ni de chiffres. Chaque séance (et le passage du soir) qui voit un commentaire « שותף » : réponse « מעולה! שלמה יחזור אליך בהודעה 🙌 », puis ajoute une ligne dans tools/reels_kit/PARTENAIRES.md (date, compte, pseudo, ce qu'il a écrit, nombre d'abonnés si INSTAGRAM business discovery le donne) et PRÉVIENS SHLOMO (c'est important) : c'est lui qui contacte, jamais les séances. Quand Shlomo confirme un partenaire, il entre dans le monde comme personnage récurrent et le reel affiche « ft. @pseudo » en haut.
10. CONTRÔLE VIRAL (point 0 du 18.11) : en plus des 3 questions, vérifier : objectif compris en 1 s ? barème visible ? compteur réel ? Top 5 réel ? Sinon on ne publie pas.

## Stratégie virale du 18.11.2026 — remplacée en partie par « RECORD DU MONDE » du 21.11 (le point 0, la 1re seconde et le point 7 restent valables ; les épisodes « 1 או 2 » et les formats tendance sont remplacés)
Shlomo, 18.11 : « je m'en fous des crédits, je veux un maximum de vues », « on peut faire beaucoup mieux » → validé (« parfait ») : SÉRIES À SUSPENSE décidées par les commentaires + formats tendance + collaboration influenceur. Les 5 comptes restent à fond. Pas de TikTok/YouTube pour l'instant.
Constat 15–18.11 : reels de 7 s = 0 partage sur 15 reels, 62–85 % partent tout de suite, 2,5–4,5 s regardées, plafond ~150 vues ; les meilleurs reels de l'histoire des comptes duraient 12–15 s et racontaient une vraie histoire (השכנים ép. 4 : 538 vues, 6 partages ; bateau « סערה » : 673 vues, 19 comm. ; סבתא ép. 7 : 663 vues, 14 s regardées).

0. CONTRÔLE VIRAL OBLIGATOIRE AVANT CHAQUE PUBLICATION (Shlomo, 18.11.2026 14:45 : « toujours avant de poster, analyse le contenu et demande-toi pourquoi cette vidéo sera virale ; si tu n'as pas de réponse, c'est que la vidéo n'est pas assez bonne »). Regarde la vidéo finale en entier, puis écris dans ta réponse ET dans JOURNAL.md, en 3 lignes : (a) pourquoi un INCONNU s'arrête dans la 1re seconde, (b) pourquoi il regarde jusqu'à la fin, (c) qui va l'envoyer à qui et pourquoi. Si une seule de ces réponses est faible ou vague → la vidéo n'est PAS assez bonne : retravaille (accroche, rythme, chute, cliffhanger) et refais le contrôle. Ne publie jamais une vidéo qui n'a pas passé ce contrôle (si l'heure prévue est dépassée, publie plus tard plutôt que publier une vidéo faible). Valable pour les reels ET les stories vidéo.
1. DURÉE : reels de 12 à 15 s (fini les 6–8 s). Stories vidéo : 6–8 s, inchangé.
2. LA 1re SECONDE parle à un INCONNU : une situation que tout le monde reconnaît ou un choc visuel, jamais un mot interne du jeu (pas de nom de jeu, de score, de « 5 עולמות »). Test : quelqu'un qui n'a jamais vu le compte comprend-il en 1 s ? Sinon refaire.
3. SÉRIE : chaque reel = « פרק N » d'une histoire continue par compte (numéro discret en haut). Structure : 0–1 s choc/situation universelle → 1–2 s « בפרק הקודם… » ultra-court (résultat du vote précédent) → 2–10 s l'action monte (quelque chose change toutes les 1–2 s) → 10–13 s CLIFFHANGER (on coupe juste avant la révélation) → fin : « אתם מחליטים: 1 או 2? בתגובות 👇 ». La suite du lendemain applique VRAIMENT le choix majoritaire des commentaires (et le dit en citant un vrai joueur). Jamais de faux vote : 0 voix → la séance choisit et ne prétend pas que c'est un vote.
4. FORMATS TENDANCE avec nos personnages 3D (un par semaine minimum et par compte, en alternance avec l'épisode) : « POV: … », « תייגו חבר ש… », « מה הייתם עושים? », « אף אחד: / סבתא: », avant/après, classement « 3 סוגים של… ». Musique rythmée style tendance (music.py, montée + drop calé sur le choc). Jamais de son protégé.
5. PARTAGE : chaque reel contient UNE raison claire d'envoyer à quelqu'un (« שלחו לסבתא שלכם », « תייגו את השכן הכי רועש »…) — écrire avant le rendu « qui envoie à qui, pourquoi ».
6. CONCEPT par compte (la série suit ce thème) :
   - סבתא : « דברים שכל סבתא אומרת » + feuilleton de sa vie (la famille, le נכד qui ne rappelle pas…), drôle, jamais triste en accroche.
   - השכנים : les voisins qu'on a tous (bruit à minuit, place de parking, odeur de cuisine) + le mystère des portes/lapins comme fil rouge.
   - Ruche : « איזה סוג של חברה את? » / drames d'amies dans la ruche, pour taguer sa copine.
   - Bateau : « את מי אתם מצילים ראשון? », dilemmes et catastrophes, cliffhanger avant le naufrage.
   - The Noise : les pires fausses notes (mariage, karaoké, douche) + juge qui réagit.
7. Le reste ne change pas : plateau 3D filmé, anti-gel (check_fluide), voix eleven_v4 1 prise, sous-titres calés, couverture lisible, 1 publication fil/jour, 2 stories, vrai joueur cité, aucun vrai argent, rien avant 08:00 ni pendant Shabbat.
8. Mesure : chaque vendredi, garder les formats au skip < 55 % ou avec partages, abandonner les autres.
9. Collaboration influenceur : préparée par Shlomo (message prêt dans la conversation de direction) ; les séances ne contactent personne.

## Système v2 (12.11.2026) — prioritaire sur tout le reste
Document complet : https://claude.ai/artifact/RhjDxLbCBHw2YZBMCwms1h

**Règle n°1, la première seconde.** Avant de publier, vérifier chaque point. Un seul raté = refaire le début.
1. Image 1 claire et lumineuse : pas de fond noir, pas de dégradé sombre (dans compose.py, mettre `vg` à 0 sur les 2 premières secondes).
2. Gros plan : visage, objet ou action.
3. 3 à 5 gros mots à l'écran dès 0,0 s, compréhensibles par un inconnu.
4. Voix à 0,0 s, sans intro musicale.
5. Aucun prénom ni mot interne (couronne, שלי…) dans l'accroche.
6. Durée 7 à 12 s, surprise avant 5 s, question de fin affichée aussi au début (boucle).

**Test de l'inconnu.** Si quelqu'un qui ne connaît pas le compte ne comprend pas en 2 s, ce n'est pas un reel mais une story. Votes, classements et prénoms vont dans les stories et les réponses ; dans le reel, seulement après l'accroche.

**Rejoindre le jeu.** Chaque reel finit par « כתבו X ותיכנסו ». Le mot X : השכנים « שכן », ruche « דבורה », bateau « עולה », Noise « במה », סבתא « נכד/נכדה ». Le compte répond à chaque personne qui écrit le mot, et son prénom apparaît dans la story suivante.

**Mesure.** Chaque vendredi, noter dans le journal pour chaque reel de la semaine : reels_skip_rate, ig_reels_avg_watch_time, shares. Objectifs : skip < 45 %, ≥ 10 partages par reel. Le format du reel qui a le skip le plus bas devient le modèle de la semaine suivante.

**Jamais le même reel sur plusieurs comptes.**

## Vidéos fluides — anti-gel (15.11.2026, PRIORITAIRE)
Shlomo a vu de petits gels dans les vidéos. Cause mesurée : le plateau 3D est filmé à 10 ou 15 i/s et la vidéo finale est à 30 i/s → chaque image est répétée 2 ou 3 fois (50 à 67 % d'images répétées), ce qui donne des saccades sur Instagram.
- `reels_kit/compose.py` corrige maintenant tout seul : un plan dont `fps` < 30 est interpolé à 30 i/s (dossier `<plan>_i30`, ~1 min pour 80 images). Toujours indiquer le vrai `fps` du plan dans la spec.
- **Avant CHAQUE publication (reel ou story vidéo)** : `python3 tools/reels_kit/check_fluide.py final.mp4`. S'il répond « SACCADÉ », ne pas publier : interpoler les images propres puis refaire le montage :
  `ffmpeg -framerate 10 -i dossier/f%04d.jpg -vf "minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" -q:v 3 dossier_i30/f%04d.jpg`
  (remplacer 10 par la vraie cadence du tournage).
- Les scripts qui montent eux-mêmes leur vidéo sans compose.py (stories, reel_akalt, etc.) passent aussi par ce contrôle.
- Filmer chaque plan au moins aussi long que son segment : sinon compose.py le fait repartir à l'envers (message « [attention] »).

## Audit du 15.11.2026 — remplacé en partie par la « Stratégie virale du 18.11 » (durée 12–15 s) (Shlomo : « tu as l'autorisation de tout appliquer »)
**Constat :** les 5 reels du samedi soir (14.11) : 36 à 130 vues, 0 partage, 68 à 78 % des gens partent avant 3 s, durée regardée 2,8 à 4,3 s. Le gros plan + texte au centre ne suffit pas : le problème reste les 3 premières secondes.

**Règles qui changent :**
1. **Plus aucun carrousel sur השכנים et Bateau** (portée 8 à 24). Comptes légers : 1 carrousel par semaine maximum.
2. **Reels de 6 à 8 s** (plus 10–12) : la durée regardée moyenne est de 3 à 4 s ; un reel court qui boucle garde mieux.
3. **Test de la 1re seconde, à faire tourner pendant 1 semaine** (noter le format A ou B dans le journal, avec le skip) :
   - A = ACTION dès l'image 0 (quelque chose tombe, explose, quelqu'un crie ou court), texte en HAUT (zone T), petit (2 à 4 mots), le centre de l'image reste libre ;
   - B = gros plan visage + texte au centre (format actuel).
   Lundi, mercredi, vendredi = A ; dimanche, mardi, jeudi = B. Le bilan du vendredi garde le gagnant.
4. **Une seule réponse par joueur et par publication**, même s'il commente 7 fois (cas shellydor20 « שלי » ×7 le 14.11).
5. **URL des médias** : toujours `https://raw.githubusercontent.com/chlomo111-bit/<dépôt>/<SHA du commit>/<chemin>` (avec /main, 404 pendant quelques minutes).
6. **Vitesse de rendu** : 10 images/s suffisent (compose.py `fps: 10`), DSF 1,2 à 1,5. 2 processeurs seulement : jamais plus de 2 rendus en parallèle.

**Outils à jour :**
- Bateau : `tovim-beyachad/tools/video_bateau_1411.py` (pirates qui tirent, 9:16, ciel clair). `reel_pirates.py` donne un bateau vide : ne plus l'utiliser.
- השכנים : `hasavta-shelanu/tools/hashchenim_1411/` (film.py + specs.py + cut.py).
- סבתא : `reel_akalt_1211.py` ou `reel_anniv_1011.py` avec `DSF=1.2`, échantillon 3 (10 i/s). Les pseudos des passants s'affichent : préférer des plans serrés sur סבתא.
- Montage : copier `reels_kit/compose.py` ; `novg` = secondes sans dégradé sombre au début ; dans une pastille colorée, ne pas mettre de mot en jaune (invisible).

**Joueurs entrés par le mot (à citer dans la prochaine story de leur jeu) :** @asaf.2509 (סבתא, 13.11) · @bdvy214 (Noise « במה », 14.11) · @hillimoshe7 (השכנים « שכן », 14.11). Commentaire sensible à garder en tête : @bdvy214 sous le reel סבתא « היא מתה לפני 8 שנים » → réponse de soutien faite ; ne jamais en faire un contenu.

## Moteurs et comptes légers (12.11.2026 16:00, Shlomo : « applique tout ») — PRIORITAIRE
**But de l'audience :** השכנים = la série phare (vers YouTube et des collaborations plus tard) ; les 4 autres jeux = portes d'entrée qui font connaître l'univers.

| Compte | Statut | Séances (publication dans le fil + 2 stories) | Les autres jours |
|---|---|---|---|
| השכנים | MOTEUR | dim.–jeu. 09:17 + sam. soir | — |
| Bateau | MOTEUR | dim.–jeu. 11:09 | — |
| Ruche | léger | dim., lun., mer. 10:13 | 1 story image légère au passage du soir |
| The Noise | léger | lun., mer., jeu. 12:21 | idem |
| סבתא מזל | léger | dim., mar. 13:33 + jeu. 10:44 (grand reel) | idem |

**Formats fixes (on ne réinvente plus chaque jour, on varie seulement le contenu) :**
- השכנים : « une porte, un secret, vote 1 ou 2 » ; l'épisode suivant donne le résultat du vote. Scène concrète la nuit (on frappe, des traces, une ombre). Jamais de lettres ni de « 5 עולמות ».
- Bateau : « un événement contre la coque + compteur de partages visible » (tempête, baleine, boulet de canon), question « מתי היא טובעת? ». Les comms viennent d'un événement concret.
- The Noise : « un candidat masqué chante faux + gros plan de la réaction d'UN juge », 10 s. Format du 10.11 (skip 41 %, le meilleur).
- סבתא מזל : « une phrase que toutes les grands-mères disent + un objet qui grossit » (ex. « אכלת משהו? » + tour d'assiettes). Public 25–34 ans.
- Ruche : « 2 abeilles, 1 couronne » en visuel, SANS prénom ni score dans l'accroche ; prénoms seulement en story.

**Leçons du bilan du 13.11 (à appliquer) :** les carrousels n'atteignent presque personne (portée 8 à 22, contre 50 à 450 pour les reels) → sur השכנים et Bateau, faire un reel court (7–10 s) tous les jours, plus de carrousel ; sur les comptes légers, le carrousel reste possible au maximum 1 fois par semaine. Format modèle de la semaine : « UN personnage en gros plan qui rate quelque chose + sa réaction », 7–10 s. Chaque reel cite un vrai joueur dès qu'il en existe un (ex. @asaf.2509 pour סבתא).

**Règle d'arrêt (bilan du vendredi) :** pour chaque compte, noter abonnés, skip moyen, partages. Un compte léger qui ne gagne aucun abonné ET reste au-dessus de 60 % de skip pendant 3 vendredis de suite → le bilan propose de le mettre en pause (Shlomo décide). Un compte léger qui passe sous 45 % de skip avec des partages → il redevient moteur.

**En attente de Shlomo :** ouvrir les comptes TikTok et YouTube de השכנים (la séance השכנים y reposte alors chaque reel) ; 5 à 10 proches qui écrivent le mot pour entrer la première semaine.

## Ordres par jeu (12.11.2026) — chaque jeu séparément, jamais de vidéo mélangée
| Jeu | Jour | Contenu du reel | Base 3D | Mot pour entrer | Fin |
|---|---|---|---|---|---|
| השכנים | dim. + sam. soir | UN secret derrière une porte, vote 1/2 ; samedi = résultat du vote + nouveau secret | `hashchenim_ep4.py` | שכן | « שלחו לשכן שלכם » |
| Ruche | lun. | duel visuel simple (« 2 בנות, כתר אחד »), résultat avant 5 s | `capture_reel.py` + `couronne_1011.js` | דבורה | « שלחו לחברה שלכם » |
| Bateau | mar. | chaque partage frappe la coque, compteur visible, événement spectaculaire compréhensible sans son | `reel_pirates.py` | עולה | « שלחו לחבר שלכם » |
| The Noise | mer. | performance ratée et drôle + réaction du jury en gros plan (vraie note vocale seulement si envoyée pour le jeu) | `film_masque_1011.py` | במה | « שלחו לחבר שמזייף » |
| סבתא מזל | jeu. | une phrase de grand-mère universelle, émouvante ou drôle ; public 25–34 ans ; voix de סבתא possible | `reel_anniv_1011.py` | נכד / נכדה | « שלחו לסבתא שלכם » |

Stories « famille » du jour : uniquement sur le compte du jeu du jour (vote, classement, prénoms des nouveaux joueurs). Les autres comptes ne repartagent plus le reel d'un autre jeu.

**Verrou anti-doublon.** Avant de fabriquer le reel d'un jeu, `git pull` puis regarde si `media/AAAA-MM-JJ/LOCK_<jeu>` existe. S'il existe, une autre séance fait déjà ce reel : fais seulement le passage commentaires de ce jeu et arrête. Sinon, crée ce fichier, commit et push tout de suite (si le push est refusé, pull et revérifie). Vérifie aussi avec `GET_IG_USER_MEDIA` qu'aucun reel n'a déjà été publié aujourd'hui sur ce compte.

**Chaque compte est indépendant (12.11, ordre de Shlomo) : chaque jour, sur CHAQUE compte, une publication dans le fil (reel ou carrousel, en alternance ; grand reel 3D le jour principal du jeu) + 2 stories.** Une séance par compte et par jour.

**Tâches programmées des jeux :**
- « Jeux – השכנים (chaque jour) » dim.–jeu. 09:17 · « Jeux – Bateau (chaque jour) » dim.–jeu. 11:09 · « Jeux – השכנים (samedi soir) » 18:19.
- « Jeux – Ruche (dim., lun., mer.) » 10:13 · « Jeux – The Noise (lun., mer., jeu.) » 12:21 · « Jeux – סבתא מזל (dim., mar.) » 13:33 · « Jeux – סבתא מזל (jeu.) » 10:44.
- « Jeux – passage commentaires du soir » dim.–jeu. 19:47 (+ story image légère des comptes légers sans séance).
- « Jeux – vendredi (שבת שלום + bilan) » vendredi 09:47 seulement (depuis le 15.11) : story « שבת שלום » propre à chaque compte, passage commentaires, bilan de la semaine (format A/B gagnant, règle d'arrêt), message de 5 lignes à Shlomo.

## Le reel : 7 à 12 s
- La surprise ou la question dans les 2 premières secondes.
- Un vrai joueur nommé, ou une vraie phrase tirée des commentaires.
- Une fin avec une question à réponse courte, plus « שלחו לחבר… ».
- Sous-titres toujours, quelque chose qui change toutes les 1 à 3 s, une couverture lisible dans la grille, une légende courte avec 5 hashtags.
- Avant d'écrire, analyser la veille : vues, partages, commentaires. Se demander : « qui va envoyer ça à qui ? ».

## Fabrication
1. **Cloner les dépôts** `chlomo111-bit/{hakaveret,tovim-beyachad,thenoise,hasavta-shelanu}` dans `/home/claude`.
2. **Installer les outils :**
   ```
   mkdir -p /root/three3 && cd /root/three3 && npm init -y && npm i three@0.128.0 @fontsource/heebo@5.0.8
   ```
   Chromium et Playwright sont déjà installés.
3. **Filmer le monde en 3D, sans texte** (frames 1080×1920 en JPG). `<NM>` = `/root/three3/node_modules`.
   - **Ruche :** `GAME=index.html BEES=<json> HOOK=<journal.js + ton hook> OUT=<dir> python3 tools/capture_reel.py /root N`. Pour l'exemple de hook, voir `hakaveret/tools/hooks/couronne_1011.js`. Pour enlever le texte, ajouter à la fin du hook : `[T,M,B,badge,band].forEach(d=>d.style.display='none')`.
   - **Bateau :** `NOTEXT=1 ONLY=s4 PAX=<json> python3 tools/reel_pirates.py /root/three3 <dir>`. On peut copier le script et écrire d'autres scènes.
   - **The Noise :** `NOTEXT=1 RANGE=a,b python3 tools/film_masque_1011.py <NM> <dir>`.
   - **השכנים :** `NOTEXT=1 RANGE=a,b python3 tools/hashchenim_ep4.py <NM> <dir>`.
   - **סבתא מזל :** `NOTEXT=1 RANGE=a,b DSF=1.5 NOSH=1 python3 tools/reel_anniv_1011.py <NM> <dir> 2`. Cette ville est lente : environ 5 s par image, donc filmer à 15 i/s.

   Pour une nouvelle histoire, copier le script le plus proche et changer les scènes et les personnages. Ne jamais faire une photo fixe.
4. **Voix :**
   - ElevenLabs `creative_generate_speech`, `model_id=eleven_v4`, voix Juniper `aMSt68OGf4xUZAnLpTU8`, `generations_count=1`. Pour la vraie voix de סבתא מזל : `YJOuplmxlZRZei0YyoPu`.
   - Ajouter des tags d'émotion : [whispers], [excited], [sad]…
   - Ensuite `creative_transcribe_audio` (scribe) pour avoir l'horodatage mot à mot.
   - Télécharger les mp3.
5. **Montage :** écrire un fichier spec JSON (voir `exemple_specs_1111.py` : plans, textes T/M/B calés sur les mots, coups de flash), puis :
   ```
   THREE3=/root/three3 python3 compose.py spec.json frames/
   python3 music.py show|tender|suspense bed.wav DUREE "whoosh:1.2,ding:3"
   ./mix.sh "frames/f%04d.jpg" bed.wav voix.mp3 out.mp4 0.5
   ```
6. **Couverture :** `python3 cover.py bg.jpg cover.jpg 'titre <span>mot</span>' 'sous-titre' '#FFC24B'`. Prendre une image de la vidéo comme fond : il sera flouté automatiquement.
7. **Ré-encoder l'audio en 48 kHz**, sinon Instagram refuse :
   ```
   ffmpeg -i out.mp4 -c:v copy -c:a aac -ar 48000 -ac 2 -movflags +faststart final.mp4
   ```
   Pousser `final.mp4` et la couverture dans `hasavta-shelanu/media/AAAA-MM-JJ/`. Le message de commit doit se terminer par les lignes d'attribution de la séance.
8. **Publier :**
   - `INSTAGRAM_POST_IG_USER_MEDIA` avec `media_type=REELS` (ou `STORIES`), `video_url` et `cover_url` en `https://raw.githubusercontent.com/chlomo111-bit/hasavta-shelanu/main/media/...`, `caption`, `share_to_feed=true` ;
   - puis `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` avec `creation_id` et `max_wait_seconds=240`.

## Passage commentaires
1. Pour chaque compte, prendre les 3 dernières publications : `INSTAGRAM_GET_IG_MEDIA_COMMENTS`.
2. Pour chaque commentaire, vérifier avec `INSTAGRAM_GET_IG_COMMENT_REPLIES` que le compte n'a pas déjà répondu.
3. Répondre avec `INSTAGRAM_POST_IG_COMMENT_REPLIES` : en hébreu, humain, court, en reprenant le nom du joueur ou ce qu'il a dit. Attendre 2 s entre deux réponses.
4. Noter les idées des joueurs pour le reel suivant.

## Journal
Ajouter une ligne par jour dans `hasavta-shelanu/tools/reels_kit/JOURNAL.md` : date, ce qui a été publié, les chiffres de la veille (vues, partages, abonnés par compte), les décisions prises. Lire ce journal avant chaque séance.
