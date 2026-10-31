# ROUTINE — « הסבתא שלנו » (@hasavta.shelanu · savta.hakaveret.online)

**Règle de Shlomo (31/10/2026 22:07) : plus de vrai argent.** Samedi 31/10 = dernière fois 20 ₪ par Bit. Depuis
dimanche 1/11, le gagnant de la loterie de 20:00 reçoit 100 מטבעות זהב dans le jeu (automatique, `savta_run_lottery`)
+ un bonus : il décide d'un אירוע מטורף en plus qui arrivera dans la ville le lendemain. Plus aucun message à
Shlomo pour payer. Mêmes 2 conditions. Pas de loterie pendant Shabbat (inchangé).

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
