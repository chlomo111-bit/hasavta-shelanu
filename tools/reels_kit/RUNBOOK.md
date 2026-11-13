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
- « Jeux – contenu du jour (5 mondes) » dim.–ven. 09:47 : dim.–jeu., le verrou montre que le reel est déjà fait → seulement le passage commentaires du jeu du jour, rien publié. Vendredi : stories « שבת שלום » de chaque compte + bilan de la semaine avec la règle d'arrêt.

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
