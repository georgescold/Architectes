# Séquences selon les réponses de qualification

Les variantes utilisent exactement les clés du formulaire de ressources : `metier`, `departement`, `structure`, `origine_projets`. L’aperçu permet de sélectionner les quatre réponses et de télécharger le HTML adapté au profil affiché.

## Ce qui change

| Réponse | Adaptation |
|---|---|
| Architecte DE / DPLG | Exemples de rénovation de maison, transformation de l’existant, extension ; présentation du cabinet d’architecture. |
| Architecte d’intérieur | Exemples d’agencement, de volumes, d’usages et de réaménagement d’appartements. Pas d’extension proposée comme exemple de mission ; schéma E30 adapté. |
| Travaille seul | Préserver le temps de conception, éviter d’ajouter la gestion publicitaire aux journées, garder une relation directe avec les prospects. |
| Petite équipe | Désigner un interlocuteur, rendre le suivi commun et éviter de disperser le pilotage publicitaire dans l’équipe. |
| Recommandations | Ajouter une source de découverte au réseau existant, sans présumer que les recommandations diminuent. |
| Plateformes | Développer un parcours direct au nom du cabinet, sans accusation sur la revente de contacts ou le coût réel de sa plateforme. |
| Réseaux sociaux | Partir des contenus et projets déjà obtenus ; distinguer audience, diffusion locale et demandes. |
| Google / fiche établissement | Compléter une recherche déjà formulée par la découverte sur Meta, sans faire abandonner Google. |
| Publicité payante | Parler de pilotage et de qualité des demandes plutôt que convaincre de commencer la publicité. Le formulaire ne précise pas quelle régie est utilisée. |
| Département | Contextualiser E13 et E22 avec le département déclaré. La zone d’intervention est à préciser, elle n’est pas assimilée à tout le département. Aucun revenu, budget, concurrence ou potentiel local n’est inféré. |

52 règles éditoriales, appliquées aux passages utiles. Une même cadence et une même progression sont conservées : changer le vocabulaire et les exemples ne doit pas casser la continuité entre les mails. Les prix et les conditions de l’offre restent identiques. Tous les CTA restent cliquables ; aucune invitation à répondre par email.

## Entrée et exclusions

- Métier architecte DE ou architecte d’intérieur, structure seul ou petite équipe, quatre réponses complètes : variante commerciale éligible, sous réserve des autres règles de remise du guide et de communication.
- Maître d’œuvre, autre métier, ou six personnes et plus : examen humain préalable. Le guide peut être remis après qualification ; la séquence commerciale n’est pas activée automatiquement.
- Réponse absente ou option inconnue : pas d’inscription automatique. L’aperçu signale le profil incomplet.
- Version commune : référence de relecture, pas une autorisation d’envoi sans qualification.

Un clic sur « Télécharger ce HTML » télécharge la version du profil choisi. Pour un profil hors cible, seul E01 est exportable ; les autres mails affichent « Séquence en attente ». Un profil incomplet reste à compléter avant tout envoi.

## Livrables

- `personnalisation-regles.json` : textes et conditions éditoriales, modifiables.
- `personnalisation.js` : moteur partagé par l’aperçu et les exports ; échappement du département dans le HTML.
- `outils/exporter_profil.cjs` : création des 32 HTML et versions texte pour un profil complet, ou seulement E01 pour un profil à examiner.
- `profil-exemple.json` : profil de démonstration, sans données personnelles réelles.
- `exports-profils/architecte-interieur-seul-reseaux/` : exemple complet prêt à relire pour un architecte d’intérieur indépendant, origine réseaux sociaux, département Morbihan.

Pour produire un profil : renseigner un fichier JSON sur le modèle fourni, puis exécuter `node outils/exporter_profil.cjs profil-exemple.json` depuis le dossier emailing. Les exports conservent les variables d’hébergement, d’identité expéditeur, de prénom et de désinscription à raccorder à l’outil d’envoi.

## Branchement ultérieur

Le site envoie actuellement les réponses dans une notification et remet le guide. Ce travail n’ajoute ni stockage des abonnements ni envoi de séquence. Il faut conserver durablement les réponses avec le contact, confirmer la remise du guide, vérifier les préférences de communication puis choisir la variante avant l’envoi. Une mise à jour réelle du profil doit être appliquée aux messages encore en attente, sans relancer E01 ni recommencer l’année.

Le moteur est indépendant de l’outil d’envoi. La personnalisation du prénom et les quatre réponses de qualification sont deux choses distinctes. L’outil d’envoi doit fournir les deux.

## Vérifications

Les 60 combinaisons d’options métier × structure × origine ont été évaluées : 20 profils dans la cible et 40 à examiner. Les contenus ne demandent aucun retour par email. L’aperçu personnalisé a été contrôlé sur ordinateur et mobile, ainsi que le blocage hors cible et l’échappement d’une saisie de département contenant du HTML. Aucun envoi activé.
