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
| Vendredi | « השבוע בחמשת העולמות », sur les 5 comptes, plus une story « שבת שלום » sur chaque compte |
| Samedi soir | השכנים |

Chaque jour, chaque compte publie aussi une story de 6 à 8 s avec voix qui renvoie au reel du jour ou au vote en cours. Le dimanche, le reel « ברוכים הבאים » cite le nom des nouveaux commentateurs.

## Le reel : 10 à 15 s
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
