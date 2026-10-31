# Automatisations du jeu (sauvegarde du directeur des jeux, 30/10/2026 12:45)

Inventaire de toutes les tâches programmées actives de ce jeu avant remise à zéro.
Les textes complets des tâches restent consultables dans les tâches désactivées (même ID) ;
la logique détaillée est dans tools/ROUTINE.md.

Règles communes (30/10) : vidéo du jour (le commentaire le plus liké décide), un événement extraordinaire par jour,
loterie à 20:00 (commentaire sur le post du jour + seuil de monnaie, pas d'abonnement obligatoire) ;
règle de Shlomo 31/10/2026 22:07 : plus de vrai argent depuis le 1/11 — le gagnant reçoit 100 מטבעות זהב dans le
jeu (automatique, savta_run_lottery) + choisit un אירוע מטורף en plus pour le lendemain (data/event.json `bonus`),
« המגיב של היום » (badge + pouvoir de choisir un événement le lendemain), passages 6:00 / 12:00 / 17:00 / 19:55,
Shabbat : rien de vendredi 16:00 à samedi 18:30, tout est décalé à samedi 18:30.

| ID | Nom | Horaire (heure d'Israël) | Rôle |
|---|---|---|---|
| trig_01UNY4RdyhimikYYvkkPf4Nx | סבתא מזל – texte du jour (voix) | 7:55 dim.–ven. | Épisode du jour, texte voix, story du matin, reel 21:00 |
| trig_01Ram1iRCj8xn4QoKGLMqeRQ | סבתא מזל – passages | 6:00 · 12:00 · 17:00 dim.–jeu. | Réponses, statuts, post du jour, inscrits loterie |
| trig_0163DxMi7GFwk3SitHXmSuBW | סבתא מזל – loterie (+ passage 19:55) | 19:55 dim.–jeu. + sam. | Passage, story 5 דקות, tirage 20:00, meilleur commentateur |
| trig_01WuqatMyWYSzrRBvM1hPMGk | סבתא מזל – habitants | 13:37 · 22:37 dim.–jeu. | Abonnés + commentateurs → habitants (lecture seule Instagram) |
| trig_01PQqSuMg8PEQPSpNUJnnUca | סבתא מזל – story « The Noise arrive » | sam. 31/10 19:11 (ponctuel) | Story + news vers The Noise |

Seuil : 100 cœurs (cadeau caché + mot secret gardés, sans argent)

## Tâches du directeur qui touchent ce jeu
| ID | Nom | Horaire | Rôle |
|---|---|---|---|
| trig_01CKRu6aTLCyHxQjn1bZYJsZ | Jeux – passages du vendredi | ven. 7:50 · 13:50 | Déclenche ruche + savta |
| trig_016xihjQtAaUGjNW17P6RXG2 | Jeux – décaler Shabbat | ven. 15:45 | Décale les ponctuels à sam. 18:30 |
| trig_01SweqkEFqGvYW3p6ffWU83f | Jeux – rattrapage sortie de Shabbat | sam. 18:30 | Tirage du vendredi ruche + passages ruche/savta |

## Mise à jour 30/10/2026 13:10 (rangement demandé par le directeur)
- Textes complets des anciennes tâches copiés dans tools/ANCIENNES_TACHES.md.
- Suppression refusée par les autorisations : trig_01UNY4RdyhimikYYvkkPf4Nx, trig_01Ram1iRCj8xn4QoKGLMqeRQ,
  trig_0163DxMi7GFwk3SitHXmSuBW et trig_01WuqatMyWYSzrRBvM1hPMGk restent **désactivées** (ne tournent plus).
- Chat d'automatisation du jeu : celui qui porte le réveil trig_01Age5P9L76NPzr2nsHLVr91
  (« סבתא מזל – réveil sam. 18:30 rattrapage », samedi 31/10 18:30). C'est lui qui fait la sortie de Shabbat,
  la loterie du vendredi + samedi, le passage et la vidéo « יום 2 » (texte : media/2026-10-31/voix.txt).
- Story « The Noise arrive » samedi 19:11 : encore faite par trig_01PQqSuMg8PEQPSpNUJnnUca (une seule publication).
  Si le chat d'automatisation la transfère en send_later, il doit désactiver cette tâche juste après.
