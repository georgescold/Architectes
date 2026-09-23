# Emailing Essort — lecteurs du guide

Version éditoriale 3 · 21 septembre 2026.

32 mails sur 12 mois, pour les architectes et architectes d’intérieur indépendants ou en petite équipe ayant obtenu le leadmagnet. Chaque mail relie une idée d’acquisition aux ambitions du cabinet et se termine par une action explicite.

- [Lire les mails dans l’aperçu](apercu-sequence.html)
- [Tous les textes et le calendrier](sequence-12-mois.md)
- [Source structurée](sequence-12-mois.json)
- [Stratégie, sources et règles de mise en place](strategie-et-mise-en-place.md)

18 invitations à réserver un échange, 13 vers la méthode Essort et 1 remise du guide. Chaque mail comporte un CTA cliquable ; aucune invitation à répondre par email. Les objets sont courts ; chaque texte utilise [prénom]. E17 remplace le conseil sur le budget par un exemple fictif comparant demandes brutes et projets pertinents.

Mise en service préparée le 21 septembre 2026 : domaine `mail.essort.agency` vérifié, expéditeur `info@mail.essort.agency`, 32 modèles et parcours Resend de 12 mois configurés. Personnalisation, désinscription et registre privé anti-doublon testés.

**Mise en ligne du formulaire encore bloquée par Vercel** : le compte GitHub auteur `georgescold` n’est pas autorisé dans l’équipe Hobby `enzdos-projects`. Le code est poussé sur `Enzdo/essort`, branche `main`, commit `afde436`. Le propriétaire Enzo doit publier un nouveau commit depuis son compte GitHub relié à Vercel. Aucun lecteur réel n’a été inscrit pendant les tests.

Après déblocage : vérifier le déploiement READY, les images `/emailing/visuels/`, puis un téléchargement complet sur le site. [Documentation technique et exploitation](../site/lib/emailing/README.md). La pause sur réservation Cal.com ou signature CRM reste manuelle tant que ces événements ne sont pas raccordés.

## Habillage HTML

Les 32 messages disposent maintenant d’un template HTML Essort, de visuels réels ou de schémas explicatifs, et d’une version texte. [Guide d’intégration](README-templates.md) · [Pack HTML et visuels](essort-templates-email.zip).

L’aperçu propose les modes ordinateur et mobile ainsi que le téléchargement individuel. Les contenus V3 restent la source éditoriale. Les modèles Resend utilisent les variables de qualification et les images prévues dans le site. Leur disponibilité publique dépend du déploiement indiqué ci-dessus.

## Qualification et variantes

Le sélecteur dans l’aperçu applique les quatre réponses du site. [Règles et parcours personnalisés](PERSONNALISATION.md). Les téléchargements HTML reflètent le profil sélectionné. Un exemple complet est disponible dans `exports-profils/architecte-interieur-seul-reseaux/`. Les profils hors cible restent soumis à examen avant la séquence commerciale.
