# ROUTINE — « הסבתא שלנו » (@hasavta.shelanu · savta.hakaveret.online)

## 🆕 NOUVEAU RÈGLEMENT (Shlomo, 03/11/2026 04:59) — PRIORITAIRE sur tout ce qui suit
Remplace « une vidéo du jour obligatoire chaque jour » et le créneau Shabbat fixe vendredi 16:00 → samedi 18:30.

**0. Heure du reel (Shlomo, 03/11 05:02) : la vidéo est publiée TOUS LES SOIRS À 19:00** (texte voix envoyé à Shlomo vers 15:00 ; samedi : dès que possible après la sortie de Shabbat).

**Texte voix (Shlomo, 03/11 17:45)** : TOUJOURS analyser le contenu précédent (la vidéo d'avant + tous ses commentaires + le post du jour) avant de proposer le texte. Claude ne génère jamais la voix : il donne le texte en 2 blocs (narrateur / סבתא מזל) avec les tags d'émotion Eleven v3, Shlomo génère.

**Test horaire (Shlomo, 04/11 17:54 : « trouver le meilleur moment pour devenir viral »)** — données : reels publiés
19:26–20:59 → la portée baisse jour après jour (217 → 138) quelle que soit l'heure, et les gens décrochent après 7–10 s :
l'heure compte moins que les 3 premières secondes et les partages. Test sur 4 reels, mesure à +24 h (reach, views,
avg watch time, shares) notée dans data/test_horaire.json : jeu. 5/11 18:00 · sam. 7/11 sortie de Shabbat (~18:30) ·
lun. 9/11 20:30 · mer. 11/11 13:00. Ensuite on garde le meilleur créneau. Story teaser 30 min avant chaque reel.

**1. Alternance reel / post (identique pour tous les jeux).** Mar. 3/11 = REEL (1er du règlement), mer. 4/11 = POST,
jeu. 5/11 = REEL, ven. 6/11 = POST (Shabbat), sam. 7/11 soir = REEL (toujours), dim. 8/11 = POST, puis l'alternance
reprend (lun. reel, mar. post, mer. reel, jeu. post, ven. post, sam. soir reel…). Jamais deux reels de suite, plus
aucune vidéo de remplissage.
- **Jour POST** : post 4:5 du jour publié à partir de 08:00 (production du matin), pas de reel, pas de texte voix.
- **Jour REEL** : PAS de post image ce jour-là ; le reel (19:00) est la publication du jour. Le matin, l'événement et
  les stories poussent à commenter la publication d'hier.
- **Loterie 20:00** (inchangée : 100 🪙 + le gagnant décide d'un événement fou, jamais de vrai argent) : base = la
  publication du jour. Jour post → commentateurs du post du jour. Jour reel (reel à 19:00) → commentaires écrits aujourd'hui sous le
  reel du jour OU sous le post d'hier (les deux comptent, une seule participation par personne).

**2. Structure de chaque reel (chat vidéos)** : (1) 3–5 s d'explication du jeu : « כאן אתם כותבים את החיים של סבתא
מזל » ; (2) « אתמול סבתא מזל הייתה… והיום היא… » ; (3) le commentaire du jour (@auteur, likes) ; (4) ce qui s'est passé
hier (gagnant de la loterie, vœu, paliers d'abonnés). La pause « מזל חדשות » reste au milieu. Fin : « מה יקרה עכשיו?
התגובה עם הכי הרבה לייקים קובעת ».

**3. Ton** : un épisode de série animée — émotion, humour, rebondissement, cliffhanger qui donne envie de la suite.

**4. Paliers d'abonnés** (fichier data/paliers.json, contrôlé à chaque passage avec followers_count) :
- tous les **+10 abonnés** : tous les habitants reçoivent **+20 🪙** (`update savta_players set coins = coins + 20`)
  — ou, une fois sur deux, un billet de loterie en plus pour la loterie du soir — + story « 🎉 עברנו X עוקבים! כולם
  קיבלו 20 מטבעות » ; noter le palier dans paliers.json (jamais deux fois le même) ;
- tous les **+100 abonnés** : un GRAND événement dans la vie de סבתא מזל (dans le jeu + raconté dans le prochain reel).
- Jamais de vrai argent.

**5. Shabbat** (horaires de Tel-Aviv à vérifier chaque semaine, ex. kipa.co.il) : vendredi = post normal seulement +
story « שבת שלום » 1 h avant l'entrée de Shabbat. Rien pendant Shabbat (de l'entrée à la sortie). Semaine du 6/11 :
entrée 16:26 (story 15:26), sortie samedi 17:24. Loterie du vendredi faite samedi soir après la sortie.

**6. Stories** : minimum **3 par jour en semaine**, sans maximum, en alternant photos et **petites vidéos-stories**
(5–15 s, jeu filmé + musique/bruitages, SANS voix ElevenLabs). Les vidéos-stories sont faites par le chat vidéos ;
les automatisations font les stories photo (matin, loterie, résultats, paliers). Cadrage vérifié, anti-doublon.

**7. Priorité absolue** : samedi soir, juste après la sortie de Shabbat, il y a TOUJOURS un reel (texte voix envoyé à
Shlomo le vendredi avant midi, plateau pré-filmé le vendredi ; montage et publication dès qu'il envoie les MP3 après
Shabbat). Dimanche = post, puis l'alternance reprend.


## 🔁 OBJECTIF N°1 : FAIRE REPOSTER NOS REELS (Shlomo, 01/11/2026) — RÈGLE OBLIGATOIRE POUR TOUS LES JEUX
But : que les utilisateurs repostent / partagent nos reels (story, envoi à des amis, repost). C'est la meilleure façon d'avoir de nouveaux visiteurs. Tout le contenu est pensé pour ça.
1. **Reel pensé pour être partagé** : hook dès la 1re seconde, un moment drôle ou fou que les gens ont envie de montrer, et les vrais joueurs tagués (les gens repartagent quand ils se voient dans la vidéo).
2. **Appel au partage partout**, court et pas forcé : à la fin de chaque reel, dans la légende et dans le commentaire du compte. Ex. « 🔁 שתפו בסטורי ותייגו אותנו » / « שלחו למישהו שחייב לראות את זה 👀 ». On garde aussi « מה יקרה מחר? התגובה עם הכי הרבה לייקים קובעת ».
3. **Récompense dans le jeu** : qui partage le reel du jour en story en taguant le compte reçoit un bonus dans la monnaie du jeu + un badge « 🔁 שגריר » sur son personnage, et un merci en story (repartager sa story quand c'est possible). Vérification : la mention de story arrive en message privé (INSTAGRAM_LIST_ALL_CONVERSATIONS), ou capture envoyée en DM. Jamais d'argent réel, jamais de condition « suivre le compte ».
4. **Chaque jour** : partager en story notre propre reel du jour (« פרק חדש! 👇 ») dès qu'il sort, et repartager les stories des joueurs qui nous taguent.
5. **Mesurer** : à chaque passage, relever les partages du reel du jour (INSTAGRAM_GET_IG_MEDIA_INSIGHTS, métriques `shares` et `reposts`) et noter quel type de reel est le plus partagé, pour refaire ce qui marche.
6. S'applique dès la prochaine vidéo (le chat vidéos du jeu) et dès le prochain passage (le chat automatisation du jeu).

**Règle de Shlomo (31/10/2026 22:07) : plus de vrai argent.** Samedi 31/10 = dernière fois 20 ₪ par Bit. Depuis
dimanche 1/11, le gagnant de la loterie de 20:00 reçoit 100 מטבעות זהב dans le jeu (automatique, `savta_run_lottery`)
+ un bonus : il décide d'un אירוע מטורף en plus qui arrivera dans la ville le lendemain. Plus aucun message à
Shlomo pour payer. Mêmes 2 conditions. Pas de loterie pendant Shabbat (inchangé).

**Règle de Shlomo (02/11/2026 07:19) : RIEN AVANT 08:00.** Aucune publication (post, reel, story, commentaire du compte)
avant **08:00 heure d'Israël** : ça ne sert à rien, personne ne regarde. La production du matin peut tourner tôt
(préparer l'image, la légende, l'événement, data/*.json), mais la mise en ligne du post du jour et la story du matin
se font à partir de 08:00 (programmer un send_later 08:0x dans le même chat ; anti-doublon). Si une tâche se déclenche
avant 08:00, elle prépare et programme, elle ne publie pas.

**Règle de Shlomo (01/11/2026 09:01) : PUBLICATIONS PAR JOUR.** Au maximum **1 post (image) + 1 reel par jour**,
jamais plus (le reel de l'épisode compte comme le reel du jour ; s'il sert aussi de post du jour, pas d'autre post).
Les **stories, en revanche, à volonté** : en faire beaucoup chaque jour pour faire vivre le jeu. Idées de stories
(1080×1920, style du jeu : Heebo très gras, blanc + #FFC24B, image de סבתא מזל / de la ville) :
- matin : « מה קרה בלילה בעיר? » (événement du jour) + story sondage/question liée à l'épisode ;
- midi : le commentaire le plus liké pour l'instant (« זה מוביל עכשיו… »), un nouvel habitant / meilleur commentateur ;
- après-midi : teaser du reel du soir (« הפרק עולה הערב ב-… »), rappel des 2 conditions de la loterie ;
- 19:55 « 5 דקות להגרלה! », après 20:00 le résultat (100 מטבעות + אירוע מטורף) ;
- dès qu'un reel/post sort : une story qui le partage (« פרק חדש! 👇 »).
Chaque story : une vraie idée + un hook, texte court, jamais deux fois la même image le même jour. Anti-doublon
(GET_IG_USER_STORIES) avant chaque story. Copie de chaque story dans Bureau → Jeux → הסבתא שלנו → Stories JJ-MM.

Règles décidées par Shlomo le 30/10/2026 (obligatoires pour tous ses jeux). Réponses à Shlomo en français ;
tout ce qui est joueurs / Instagram en hébreu, chaleureux et drôle. Autonomie complète, économie.

## Identifiants (ne jamais en utiliser d'autres)
- Instagram : Composio account `instagram_ensate-diacle` UNIQUEMENT. Avant toute action :
  INSTAGRAM_GET_USER_INFO (ig_user_id "me", fields id,user_id,username,followers_count) → username doit être
  exactement `hasavta.shelanu` (id 28812799228387525 / user_id 17841406206922906). Sinon STOP + PushNotification.
- Base : Composio account `supabase_restow-lise`, ref `ohvmnaymozoxfirkbntt`, SUPABASE_BETA_RUN_SQL_QUERY.
  UNIQUEMENT les tables/fonctions `savta_*` (le même projet héberge d'autres jeux : ne jamais y toucher).
- Dépôt : add_repo (owner chlomo111-bit, repo hasavta-shelanu, access push), clone, `git pull --rebase` avant
  chaque push, auteur chlomo111-bit <chlomo111-bit@users.noreply.github.com>, ligne
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. GitHub Pages sert `index.html` + `data/*.json` + `media/`.
- Pas de Lovable.

## Shabbat (règle 5)
Rien entre **vendredi 16:00 et samedi 18:30 (heure d'Israël)**. Toute tâche qui se déclenche dans ce créneau
s'arrête IMMÉDIATEMENT sans rien faire (vérifier avec `TZ=Asia/Jerusalem date`). Samedi à partir de 18:30 :
la loterie du VENDREDI d'abord (day = date du vendredi), puis celle du samedi à 20:00 ; la vidéo du vendredi
est publiée samedi soir.

## La boucle du jeu (ne pas la casser)
1. Chaque reel finit par « מה יקרה מחר? התגובה עם הכי הרבה לייקים קובעת » : le commentaire valable le plus
   liké du post/reel précédent devient l'épisode suivant (data/episodes.json) ; son auteur → `writer=true`,
   `chapters+1` dans data/citizens.json. On écarte insultant / sexuel / vraie personne / violence choquante.
2. Cadeau caché + MOT SECRET du jour (window.dailyGift(dateISO), jour = heure d'Israël − 9 h) : celui qui écrit
   le mot en commentaire → `extra.crown=true` (grade מלאך שומר). Pas d'argent pour le cadeau.
3. Grades (calculés par le site) : תושב (abonné) · שכן (a commenté) · חבר משפחה (≥ 5 commentaires) ·
   כותב (writer) · מלאך שומר (extra.crown).
4. LOTERIE chaque soir à 20:00 (un seul gagnant ; depuis le 1/11/2026 : +100 מטבעות זהב dans le jeu, crédités
   automatiquement dans `savta_players.coins` par `savta_run_lottery`, + il choisit un אירוע מטורף en plus pour
   le lendemain ; plus de vrai argent). 2 conditions :
   (a) commenter le POST DU JOUR épinglé, (b) avoir **100 cœurs ❤️ dans la journée** (date d'Israël).
   Pas de condition d'abonnement.
5. « המגיב של היום » : à 20:00, le joueur avec le plus de commentaires valables de la journée (tous les posts,
   pas de spam identique répété ; égalité = premier à atteindre ce nombre) → couronne 👑 dans le jeu jusqu'au
   lendemain 20:00 + il choisit une chose extraordinaire pour le lendemain (réponse avant 12:00).

## Cœurs ❤️ (dans le jeu, côté Supabase)
- Le joueur entre avec son @ (bouton 🚶 שחקו). Le site appelle `savta_act(h, action, arg)` :
  `daily` +20 (1×/jour) · `help` +5 près de סבתא מזל (max 10/jour, 14 s d'écart) · `find` 0..4 +10 (5 cœurs
  cachés dans la ville, positions = heartSpots(date)) · `bring` 0..4 +10 (rapporter le cœur trouvé à סבתא)
  · bonus des 3 missions du jour (`savta_missions_for`). Tables : `savta_days` (username, day, hearts, got),
  `savta_players`.
- Bouton « ❤️ x/100 · 🎟️ compte à rebours » en haut → fenêtre des 2 conditions, nombre de participants,
  dernier gagnant, meilleur commentateur. À 20:00 le site interroge `savta_lottery_info` toutes les 20 s et
  affiche le résultat (tirage « en direct »).
- `savta_daily_commenters(day, username, post_id)` = commentateurs du POST DU JOUR (rempli par les passages).
- `savta_run_lottery(d date)` (réservée au service, idempotente) → `{winner, entrants, list, coins}` (+100 dans `savta_players.coins` du gagnant) et ligne dans
  `savta_lottery(day, winner, entrants, entrants_list, best, best_comments, best_wish)`.
- Contrôle : `select savta_lottery_info('<username>')`.

## Fichiers de données
- data/citizens.json : `{username, joined_at, chapters, writer, extra:{comments, crown, secret_days, best_until,
  best_days, day_comments:{"AAAA-MM-JJ": n}}}` — ne jamais supprimer d'entrée ni baisser un compteur.
  `extra.best_until` (ISO) = couronne « המגיב של היום » visible jusqu'à cette date.
- data/replied.json : liste des comment_id déjà traités (anti-doublon). data/stats.json : abonnés.
- data/event.json : `{day, title, text, by, bonus?}` = événement extraordinaire du jour (popup ✨ dans le jeu) ; `bonus: {title, text, by}` = l'événement en plus choisi par le gagnant de la loterie de la veille.
- data/post_du_jour.json : `{"AAAA-MM-JJ": {"id": "...", "permalink": "..."}}`.
- data/episodes.json, data/news.json, data/followers.json.

## Planning (tâches programmées de CE jeu — 3 seulement)
| Tâche | Heure (Israël) | Jours |
|---|---|---|
| סבתא מזל – production du matin | 05:37 | dim–ven |
| סבתא מזל – passages | 06:00 · 12:00 · 17:00 | tous (sortie Shabbat : rattrapage par la tâche du directeur) |
| סבתא מזל – loterie 20:00 (+ passage 19:55) | 19:55 → 20:00 | dim–jeu + sam |
Vidéo du jour : mise en ligne **21:00** (après le tirage), texte voix envoyé à Shlomo à **18:30** (send_later),
c'est la SEULE chose qu'on lui demande. Vendredi : texte du vendredi envoyé au passage de 12:00, publication
samedi ~19:30 ; samedi : vidéo à 21:30.

## Production du matin (05:37)
1. Shabbat ? stop. Vérifier le compte Instagram.
2. POST DU JOUR (jamais l'oublier) : image 4:5 (1080×1350, style du jeu : capture du jeu ou fond, Heebo très
   gras blanc + #FFC24B), hébergée dans media/AAAA-MM-JJ/post.jpg. Légende : hook du jour (l'événement
   extraordinaire) + « 🎟️ הגרלה הערב ב־20:00! הזוכה מקבל 100 מטבעות זהב 🪙 בעיר + מחליט על אירוע מטורף
   שיקרה בעיר מחר! 2 תנאים: 1) הגיבו כאן 👇 2) אספו 100 לבבות ❤️ בעיר של
   סבתא מזל (הלינק בביו) » + « 👑 מי שכותב הכי הרבה תגובות היום מחליט מה יקרה מחר » + « הגיבו כאן 👇 » +
   « המבצע אינו קשור לאינסטגרם ואינו ממומן על ידה » + 5 hashtags. Publier, puis commentaire du compte
   « 👇 הגיבו כאן כדי להיכנס להגרלה של 20:00 ». L'API ne permet pas d'épingler : si le post n'est pas épinglé,
   ne pas déranger Shlomo (le lien est rappelé partout). Enregistrer l'id dans data/post_du_jour.json.
3. ÉVÉNEMENT EXTRAORDINAIRE du jour (règle 2) : inspiré du commentaire le plus liké / de la boîte à idées
   (`savta_ideas`, used=false) / du vœu du meilleur commentateur. Visible dans le jeu : data/event.json
   (+ si possible un vrai changement visuel dans index.html : décor, objet, météo, invité…, testé avec
   Playwright avant push). Le raconter dans la vidéo.
4. Brouillon du texte vidéo dans media/AAAA-MM-JJ/voix.txt et programmer avec send_later à 18:30 (vendredi :
   12:00) le message qui finalise et envoie le texte à Shlomo (voir « Vidéo »).
5. Débrief à Shlomo seulement en cas de problème grave.

## Passages (06:00 · 12:00 · 17:00 · 19:55)
1. Shabbat ? stop. Lister les médias récents (10 derniers) et TOUS leurs commentaires + réponses ; ignorer
   ceux du compte et ceux de data/replied.json. **Aucun nouveau commentaire et post du jour présent → fin
   immédiate** (règle 6).
2. Pour chaque nouveau commentaire : statut dans data/citizens.json (comme avant : nouveau → שכן,
   extra.comments+1, mot secret → extra.secret_days), `extra.day_comments[date]+1` (sauf spam identique
   répété) ; s'il est sous le post du jour : `insert into savta_daily_commenters(day, username, post_id)
   values (...) on conflict do nothing` (vérifier la contrainte ; sinon `where not exists`).
   Réponse (INSTAGRAM_POST_IG_COMMENT_REPLIES) : hébreu, 1 phrase, courte, variée, jamais copiée-collée,
   pas d'URL (→ « הקישור בביו »), rappeler selon le cas les 2 conditions de la loterie / le compte des
   cœurs / la course au « המגיב של היום ». Insultant / sexuel / vraie personne : pas de réponse, signaler.
3. Meilleur commentateur de la veille : repérer sa réponse « מה יקרה מחר בזכותך? » (avant 12:00) ; si
   valable → le mettre en place dans le jeu (data/event.json `by` + changement) et le noter dans
   `savta_lottery.best_wish` de la veille. Refuser insultant / sexuel / vraie personne / impossible en lui
   proposant une version proche. Sans réponse à 12:00 : rien.
   Gagnant de la loterie de la veille : même chose avec sa réponse « איזה אירוע מטורף יקרה מחר בעיר? »
   (avant 12:00) → si valable, l'ajouter comme événement EN PLUS dans data/event.json, champ
   `bonus: {title, text, by}` (affiché dans le popup ✨ « בונוס של הזוכה בהגרלה »). Sans réponse à 12:00 :
   la production du matin du lendemain l'intègre si elle arrive plus tard, sinon rien.
4. data/stats.json (abonnés). Vérifier que le post du jour existe (sinon le créer comme le matin).
5. Commit « Passage HH:MM (+N réponses) » + push seulement si quelque chose a changé.

## Loterie (19:55 → 20:00)
1. Shabbat ? stop. Samedi : d'abord la loterie du VENDREDI (d = date du vendredi), puis celle de samedi.
2. 19:55 = passage complet (ci-dessus) + story 1080×1920 « 5 דקות להגרלה! » avec le nombre de participants
   (`savta_lottery_info('').eligible_today`), le meilleur commentateur du moment et le rappel des 2 conditions.
3. Attendre 20:00 (sleep), puis `select savta_run_lottery('AAAA-MM-JJ'::date);` (si `already`, ne rien republier).
4. Meilleur commentateur du jour (day_comments[date] max, égalité = premier arrivé) :
   `update savta_lottery set best=..., best_comments=... where day=...` ; citizens.json :
   `extra.best_until` = demain 20:00 heure d'Israël (ISO), `extra.best_days` += date. Lui répondre sous son
   dernier commentaire : « 👑 אתם המגיבים של היום! מה יקרה מחר בזכותך? כתבו לנו עד 12:00 ».
   Les 100 מטבעות sont crédités automatiquement par `savta_run_lottery` (champ `coins` du résultat ;
   contrôle : `select coins from savta_players where username='x'`). Rien à payer, aucun message à Shlomo.
5. Story résultat : « 🎉 הזוכה של הערב: @x · 100 מטבעות + הוא מחליט מה יקרה מחר בעיר! »
   + « 👑 המגיב של היום: @y — מה יקרה מחר בזכותך? »
   + « מחר ב־20:00 עוד הגרלה · 100 לבבות + תגובה בפוסט של היום » (ou « אף אחד לא השלים את 2 התנאים… »).
6. Répondre sous le commentaire du gagnant sur le post du jour : « 🎉 זכיתם! 100 מטבעות זהב 🪙 כבר אצלכם בעיר.
   ועכשיו הבונוס: איזה אירוע מטורף יקרה מחר בעיר? כתבו לנו כאן עד 12:00 👇 ». Le vœu (avant 12:00 le
   lendemain) devient l'événement bonus de data/event.json (`bonus`, cf. passages règle 3 ; ou production du
   matin s'il est déjà là). Sans gagnant : rien.
7. Commit + push (citizens.json, media/).

## ⚠️ Règle de Shlomo (30/10/2026 13:34) — VIDÉOS
Les vidéos du jeu sont montées UNIQUEMENT dans le chat « הסבתא שלנו – vidéos » (session session_01K8i1w54KFPFJfEmEMXS7hR,
celui qui a créé le jeu). Les automatisations ne montent ni ne publient plus de vidéo : elles préparent seulement le texte
voix dans media/AAAA-MM-JJ/voix.txt et l'envoient à Shlomo à 18:30 ; Shlomo envoie les MP3 dans le chat vidéos, qui monte,
publie (21:00, samedi après Shabbat) et enregistre chaque vidéo sur le bureau du Mac (Desktop/Jeux/הסבתא שלנו/)
et dans le chat, nommée « הסבתא שלנו – יום N ».

## 📁 Règle de Shlomo (30/10/2026 15:31) — DOCUMENTS ET TÂCHES
- Tout document (textes voix, routine, automatisations, listes) et toute création/modification de tâche programmée est envoyé dans le chat vidéos (session_01K8i1w54KFPFJfEmEMXS7hR) ET enregistré sur le Mac : Bureau → Jeux → הסבתא שלנו (sous-dossier Documents ; vidéos/voix/jeu dans le même dossier). Tenir tools/TACHES_PROGRAMMEES.md à jour.

## 📺 Règle de Shlomo (30/10/2026 14:02) — PAUSE « מזל חדשות » DANS CHAQUE VIDÉO
- Au milieu de chaque vidéo quotidienne : pause de 6–8 s dans le studio TV « אולפן מזל חדשות » (dans le jeu, près de סבתא מזל). Présentateur = « מוטי חדשות », présentateur TV cubique en costume bleu marine et cravate dorée (voix ElevenLabs « James – Husky, Engaging and Bold », Eleven v3) — PAS la grand-mère. MP3 fixe réutilisé chaque jour : media/voix/moti-news.mp3 (8,8 s), style TV israélienne kitsch années 90.
- Le grand écran affiche « התגובה של היום » = le commentaire le plus liké de la veille, avec son @auteur et ses ❤️ (fichier `data/comment_of_day.json` : {day, username, text, likes}). Le gagnant est sur scène avec une couronne. Mettre à jour ce fichier à chaque passage du soir.
- Plans vidéo : capShot('studio') → capShot('studioCard') → capShot('studioWinner') + studioApplause(), puis retour à l'histoire.
- Texte voix : toujours les 2 mêmes lignes de מוטי (déjà enregistrées, media/voix/moti-news.mp3) au milieu : « ערב טוב, כאן מזל חדשות! התגובה של היום — תסתכלו על המסך! מחיאות כפיים! » puis « ועכשיו… נחזור לסבתא מזל. »

## Vidéo du jour (règle 1)
- AVANT d'écrire : lire TOUS les commentaires du post/reel précédent ; le commentaire valable le plus liké
  décide de ce qui arrive. Raconter ce qui s'est passé dans le jeu (vrais joueurs tagués, vrais chiffres :
  abonnés, cœurs, participants, gagnant d'hier, meilleur commentateur + son vœu « @x החליט ש… »,
  l'événement extraordinaire), finir par « מה יקרה מחר? התגובה עם הכי הרבה לייקים קובעת ».
- Texte écrit pour la voix (hébreu, balises Eleven v3 [excited] [laughs]…, nombres en toutes lettres,
  20–30 s, hook fou dès la 1re seconde), envoyé à Shlomo 2–3 h avant la mise en ligne (SendUserMessage +
  PushNotification) en demandant le MP3. C'est la seule chose qu'on lui demande.
- Montage : vrai jeu filmé (mode CAP, Playwright + ffmpeg 1080×1920 30 fps), voix + musique + bruitages,
  textes Heebo blanc + #FFC24B. **Couverture dédiée, jamais une image noire.** Description : « יום N », mini-
  histoire, @ tagués, 2 conditions de la loterie, « המבצע אינו קשור לאינסטגרם ואינו ממומן על ידה », 5 hashtags,
  commentaire du compte avec le CTA. Ne jamais publier un reel sans sa voix.
