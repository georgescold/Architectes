# Templates HTML Essort

32 emails habillés dans la direction artistique du site : blanc, bleu #273554, logo officiel et boutons sobres. Le texte éditorial V3 et son calendrier sont conservés.

## Relire

Ouvrir `apercu-sequence.html` via le serveur local. La navigation permet de passer d’un email à l’autre, de simuler une largeur mobile et de télécharger le fichier HTML correspondant. L’aperçu ne réalise aucun envoi.

## Fichiers à intégrer

- `html/E01.html` à `html/E32.html` : un email HTML complet par message.
- `texte/E01.txt` à `texte/E32.txt` : versions texte pour l’alternative texte de l’email.
- `visuels/` : logo PNG, photos JPEG réelles déjà validées pour le site et schémas éditoriaux PNG.
- `manifest-templates.json` : identifiants, objets, aperçus, jours et fichiers associés.
- `sequence-12-mois.json` : source éditoriale conservée.

Les fichiers HTML utilisent une mise en page en tableaux, des styles en ligne, une largeur maximale de 640 px et une police système. Les boutons gardent leur texte en HTML et disposent d’une variante VML pour Outlook classique. Le message reste compréhensible si les images sont bloquées : les illustrations ont un texte alternatif et aucune information essentielle n’est disponible uniquement dans l’image.

Les 32 mails comportent un bouton vers le guide, la méthode Essort ou la réservation d’un échange. Aucun mail n’incite à répondre par retour d’email.

## Raccordement à l’outil d’envoi

1. Héberger les PNG et JPEG sur une adresse HTTPS publique stable, ou les importer dans la médiathèque de l’outil d’emailing. Remplacer `{{assets_url}}` par cette base d’URL, sans slash final. Les images locales de l’aperçu ne fonctionneraient pas chez les destinataires.
2. Importer le HTML et sa version texte, puis renseigner l’objet et l’aperçu depuis le manifeste. Ces derniers ne se paramètrent pas avec le titre HTML.
3. Remplacer `[prénom]` par la syntaxe de personnalisation de l’outil. En l’absence de prénom, afficher « Bonjour, » et retirer la variable de l’objet E01.
4. Renseigner `{{identite_expediteur}}` et `{{lien_desinscription}}`, ainsi qu’une adresse expéditeur et Reply-To réellement suivies. Aucun email de contact n’a été inventé.
5. Vérifier les liens et les conditions commerciales, envoyer des tests internes sur les messageries utilisées, puis seulement raccorder la séquence au parcours de remise du guide décrit dans `strategie-et-mise-en-place.md`.

Les fichiers de `apercus-html/` sont réservés à la relecture : leurs images utilisent des chemins locaux et leur lien de désinscription est neutralisé.

## Validation réalisée

Les 32 emails ont été rendus dans Chrome aux largeurs 1440, 390 et 320 px : aucune image manquante, aucun débordement horizontal. Logo, couverture, boutons et exemple comparatif ont été contrôlés visuellement. La taille HTML est inférieure à 30 Ko par email. Aucun JavaScript n’est inclus dans les fichiers d’envoi.

Ces contrôles ne remplacent pas les envois de test dans Gmail, Outlook et Apple Mail : leur rendu réel n’a pas été testé dans ces messageries. Aucun envoi, hébergement des nouveaux visuels ou déploiement n’a été activé.

## Maintenance

Le générateur `outils/generer_templates.py` relit la source JSON pour reconstruire les HTML, les versions texte, le manifeste et l’aperçu. Les schémas sont conçus en HTML puis rasterisés en PNG ; les fichiers HTML présents dans `visuels/` en conservent la source. Ils ne sont ni des captures de comptes publicitaires ni des résultats clients.

## Signature visuelle Essort

Le haut du mail conserve le logo, les filets et la hiérarchie typographique validés. Les photographies suivent le paragraphe concerné dans un bandeau horizontal compact (environ 310 px de haut sur ordinateur, avec des sources horizontales au format 16:9), sur la même colonne de lecture. Le recadrage est effectué dans le fichier image, sans dépendre du rendu de la messagerie. Les espacements entre les paragraphes et les images sont de 20 px. Les schémas apparaissent après leur introduction dans le texte et suivent la largeur de la colonne, jusqu’à 550 px.

Le bloc CTA associe un aplat bleu #273554, une étoile, un titre éditorial adapté à chaque sujet et un lien blanc avec une flèche. Le texte conserve le contexte concret de la destination. La signature finale est réduite à « À bientôt, Loys et Enzo — Essort ».

Les légendes génériques sous les photos ont été retirées. La provenance des médias reste documentée dans visuels/SOURCES.md. Les exemples chiffrés fictifs restent explicitement identifiés dans le contenu ; les photographies ne sont pas présentées comme des références clients.

## Export adapté à la qualification

Le téléchargement depuis l’aperçu utilise le profil sélectionné et le moteur personnalisation.js. Voir PERSONNALISATION.md pour les règles et l’export complet des 32 mails. Les fichiers html/ restent la référence commune ; exports-profils/ contient les exemples adaptés. Aucun envoi automatique n’est ajouté.
