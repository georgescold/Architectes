# La lettre du cabinet — séquence Essort sur 12 mois

Version éditoriale 3 du 21 septembre 2026. Textes proposés, aucun envoi ni branchement réalisé.

## Le choix éditorial

32 emails sur 365 jours, uniquement pour les lecteurs ayant obtenu le guide après qualification. Le guide ouvre une relation ; la séquence aide le lecteur à prendre des décisions pour son cabinet, puis à choisir ce qu’il souhaite déléguer.

Nom proposé : **La lettre du cabinet**. L’objet reste le sujet concret du message, sans numéro d’épisode ni préfixe répétitif.

Promesse : des idées utiles pour attirer les missions souhaitées, rendre son expertise compréhensible et structurer son acquisition tout en préservant le temps de conception.

Expéditeur proposé : **Loys et Enzo — Essort**. Même identité tout au long de la séquence, adresse professionnelle authentifiée et boîte de réponse réellement suivie à renseigner lors du paramétrage. Les messages sont signés à deux ; aucun récit personnel fictif.

## Ce qui vient de Valère, et son adaptation

| Principe de la base Valère | Traduction pour Essort |
|---|---|
| Encourager les rêves | Un premier échange intéressant, des missions choisies, du temps pour concevoir. |
| Dissocier les résultats de l’identité | Expliquer le rôle d’un message ou d’un canal sans juger les compétences du cabinet ni présumer une difficulté. |
| Réduire les peurs | Décrire les rôles, la plateforme de suivi, le budget et le déroulement du premier échange. |
| Confirmer les doutes | Distinguer clics, demandes et missions ; expliquer ce qui permet de juger un outil. |
| Un obstacle partagé | Le flou dans les messages et le suivi, la dispersion des actions. Pas d’attaque contre des confrères ou d’autres métiers. |
| Un mécanisme compréhensible | Priorités du cabinet → annonces et diffusion → formulaire → échanges → retours pour ajuster. |
| Une idée et une suite par mail | Une idée utile sur l’acquisition, puis un CTA explicite relié au sujet. Pas de conseil métier évident ni de catalogue de liens. |
| Séquence puis newsletter | Un parcours fini de 12 mois, suivi d’une lettre régulière uniquement pour ceux qui souhaitent poursuivre. |
| Urgence / rareté | Remplacées par le calendrier réel du cabinet. Aucune fausse échéance, place limitée ou offre qui expire. |
| Preuve | Démonstration d’un raisonnement et d’un processus. Aucune statistique, signature client, témoignage ou capture de résultat inventé. |

La base Valère recommande notamment une séquence courte et très dense. Nous conservons sa progression de persuasion, mais pas sa fréquence ni son agressivité : décision B2B, rythme de production des cabinets et préférence exprimée pour la confiance.

## Cadence proposée

- J0 : remise du guide, intégrée à l’email de livraison existant pour éviter un doublon.
- J2, J5, J9, J14 : reconnaissance du besoin, valeur du cabinet et compréhension du mécanisme.
- J21 à J56 : un message par semaine.
- J70 à J322 : un message toutes les deux semaines.
- J343 et J365 : bilan et invitation à préparer la suite lors d’un rendez-vous. La séquence se termine à J365.

Ce rythme est une hypothèse éditoriale, pas une performance annoncée. Pour les mails après J0, départ proposé à 10 h, heure de Paris, un jour ouvré. Si l’échéance tombe le week-end, reporter au lundi ; ne jamais rattraper plusieurs messages le même jour. L’heure se teste ensuite sur les réponses et rendez-vous, pas sur une prétendue heure idéale universelle.

Chaque mail comporte un CTA explicite. Répartition : 1 remise du guide, 13 invitations à découvrir la méthode sur le site et sa vidéo de présentation, 18 invitations à réserver un rendez-vous. Aucune invitation à répondre par email : chaque message propose un bouton cliquable. Le premier rendez-vous est proposé à J21. Les invitations précisent la raison de l’échange : définir les missions, comprendre le suivi, choisir un périmètre ou préparer le calendrier. Les liens vers la méthode mènent à la page Essort existante, sans annoncer une vidéo thématique qui n’existe pas.

## Public et vocabulaire

Architectes et architectes d’intérieur, seuls ou en petite équipe. On parle de missions, de demandes de projets, de secteur, de cabinet, d’honoraires et de temps de conception. On ne présume ni la composition raciale du cabinet, ni son revenu, ni son niveau de difficulté.

Le texte valorise l’autonomie : « vous fixez les priorités », « vous choisissez les missions », « vous déléguez ». Pas de « sauver votre cabinet », « avouer un échec », « vous ne savez pas vendre », « être accompagné » ou « 1 à 5 » dans les mails.

L’offre principale reste la gestion Meta à 999 €/mois. Les prestations site, SEO et acquisition globale sont distinctes, sur devis. L’accès à la plateforme de suivi est inclus dans la présentation de la gestion conformément à la dernière instruction commerciale. Aucun reporting en temps réel ni synchronisation automatique de dépenses n’est promis.

Le non-paiement d’Essort n’est pas un argument dans les emails, conformément à la formulation validée sur le site. Les critères des quatre opportunités, les deux délais de 48 h et les conditions de l’essai sont explicités dans les messages qui présentent l’offre, sans inventer de remboursement, de fiscalité HT/TTC, d’exclusivité ou de durée contractuelle.

## Entrée dans la séquence : exclusivement après remise du guide

Le code actuel du site traite deux actions séparées : saisie du contact, puis qualification complète. L’intitulé de la notification interne « Nouveau téléchargement » apparaît dès la première étape ; il ne prouve donc pas un téléchargement.

Le deuxième appel envoie le guide et ouvre son téléchargement, mais aucun historique persistant de téléchargement ni abonnement à cette séquence n’a été constaté dans ce point d’entrée. La réponse de l’API peut aussi être positive même si l’email de livraison échoue. Il faut distinguer ces états lors de l’intégration.

Règle à implémenter ultérieurement :
1. Identifier précisément la ressource `guide-acquisition-2026`.
2. Confirmer les quatre réponses et enregistrer un événement durable de remise / accès au guide pour ce contact. Un clic ou une réponse réseau ne garantit pas l’enregistrement du fichier sur son ordinateur ; ne pas le présenter comme une preuve de lecture.
3. Vérifier que le contact peut recevoir les messages prévus et respecter son choix de communication.
4. Exclure les désinscrits, plaintes, adresses invalides, comptes de test et doublons.
5. Définir J0 à partir de cet accès et inscrire le contact une seule fois.

Si « uniquement les personnes qui ont cliqué pour obtenir le guide » est le critère retenu, journaliser explicitement cette action après qualification. Ne pas inclure les simples inscrits à l’étape 1 ni importer indistinctement tous les contacts Resend.

L’email E01 remplace le contenu de livraison actuel lors d’un futur branchement ; il ne s’ajoute pas à un second email de remise du même guide. Si la livraison est déjà partie, commencer au prochain message pertinent sans rejouer J0.

La conformité de la collecte et du périmètre de communication devra être vérifiée sur le formulaire réellement publié avant activation. Ce document est éditorial et opérationnel ; il ne conclut pas que le téléchargement autorise à lui seul tous les futurs envois.

## Sorties et priorités

| Événement | Traitement prévu |
|---|---|
| Désinscription, plainte ou adresse invalide | Arrêt immédiat, sans mail de confirmation commercial. |
| Prise de rendez-vous | Pause de cette séquence ; conserver les messages liés au rendez-vous. |
| Réponse à un mail | Suspendre le prochain envoi, traiter la réponse humainement, puis décider de la suite. Ne pas enchaîner une relance standard au milieu d’une conversation. |
| Client / essai actif | Sortie de la prospection ; suivi client séparé. |
| Demande de rappel à une date donnée | Suspendre jusqu’à la date convenue ; reprendre avec contexte, sans empiler les mails manqués. |
| Cabinet hors cible | Sortie de cette séquence commerciale ; pas de promesses inadaptées au projet. |
| Nouvelle demande du même guide | Redonner l’accès si nécessaire, sans recommencer les 12 mois. |
| J365 | Fin du parcours. Le CTA mène au rendez-vous, sans réinscription automatique ni demande de réponse. |

En cas de conflit : désinscription / suppression > client > rendez-vous ou réponse > prochain mail prévu. Une réservation suivie d’une annulation ne réinscrit pas automatiquement le prospect : reprendre selon l’échange réel.

## Suivi de l’intérêt et fatigue

Tous les contacts ne doivent pas recevoir mécaniquement les 32 messages. Prévoir un point de contrôle autour de J90 et J180 : clics fiables, réponses, rendez-vous et préférences déclarées. Un taux d’ouverture isolé ne suffit ni à juger l’intérêt ni à déclencher une relance.

Si aucun signal utile n’apparaît pendant plusieurs mois, suspendre plutôt qu’intensifier les envois. On ne reprend pas après une désinscription. Aucun changement de domaine pour contourner le refus ou la baisse d’intérêt.

Ne pas faire partir une newsletter générale en plus de cette séquence la même semaine. Une édition ponctuelle vraiment pertinente peut remplacer un message, sans déplacer tous les suivants ni doubler la pression.

## Segmentation à partir du formulaire existant

- `metier` : adapter les exemples, voir les variantes ci-dessous. Le titre « architecte » et les missions réglementées ne sont pas attribués automatiquement à un diplômé ou à un autre métier.
- `structure` : préférer « votre cabinet » dans le tronc commun. « Petite équipe » reste la formulation visible.
- `origine_projets` : choisir une introduction pertinente ; ne pas écrire que la personne souffre de son canal actuel.
- `departement` : contexte pour une conversation, pas insertion automatique de recommandations locales inventées.
- Valeur manquante : envoyer le texte commun, sans prénom vide ni faux détail personnel.
- Maître d’œuvre, autre métier, structure de six personnes et plus : remise du guide conservée ; revue du profil avant inscription à ce parcours conçu pour la cible Essort.

Les variantes remplacent un passage du mail ; elles ne créent pas des envois supplémentaires.

## Personnalisation des exemples

La séquence est utilisable comme tronc commun. Pour personnaliser, adapter une mission citée à partir du métier et des informations réellement déclarées : rénovation de maison pour un architecte exerçant cette mission ; réaménagement d’appartement pour un architecte d’intérieur concerné. Ne pas lui attribuer automatiquement le suivi de travaux, un secteur, un portfolio ou un besoin qu’il n’a pas indiqué.

E02 et E04 mènent à la méthode Essort. E08, E13, E20 et E28 invitent à réserver un échange sur les priorités du cabinet. E32 clôture la série avec une invitation à réserver. Aucun mail ne demande de répondre, de transmettre son site par email ou de confirmer la poursuite par retour de mail.

Le texte reste au conditionnel lorsqu’il décrit une situation possible. Les scènes et exemples ne sont pas présentés comme des témoignages clients. E17 compare deux campagnes fictives : même budget, 20 demandes dont 4 pertinentes contre 8 dont 6 pertinentes. Aucun de ces nombres n’est une performance Essort ou une prévision.

## Présentation des mails

Format éditorial Essort : logo officiel, fond blanc, bleu profond, paragraphes courts, image liée au sujet et bouton sobre pour les CTA de clic. Chaque CTA principal utilise un bouton vers une destination existante. Aucun faux transfert « Re: », compteur, ou photographie illustrative présentée comme un résultat client. Voir README-templates.md pour les fichiers HTML, leurs versions texte et les points d’intégration.

L’objet et le texte d’aperçu sont distincts. Salutation « Bonjour [prénom], ». Remplacer la variable par le prénom correctement renseigné et nettoyé ; à défaut, utiliser « Bonjour, ». Dans l’objet E01, retirer « , [prénom] » si le prénom manque. Convertir cette notation vers la syntaxe de l’outil choisi, sans crochets visibles au destinataire. Signature : Loys et Enzo / Essort.

Pour E10, une véritable capture anonymisée de la plateforme peut être ajoutée après validation, avec la mention « Démonstration — données fictives » si elle vient de la démo du guide. Le mail reste compréhensible sans image. Aucune vidéo YouTube non tournée n’est annoncée comme disponible.

Le pied de mail doit expliquer l’origine du message et offrir une désinscription fonctionnelle. Les liens de désinscription et l’identité de l’expéditeur sont des champs à renseigner dans l’outil, jamais des éléments à laisser entre accolades en production.

## Pilotage après lancement

Mesurer par cohorte de remise du guide : emails effectivement remis, réponses utiles, clics vérifiés, rendez-vous réservés puis tenus, propositions et clients. Suivre aussi plaintes, désinscriptions et erreurs de distribution.

Ne pas attribuer toute signature au dernier clic : le rendez-vous peut avoir été pris après plusieurs messages et visites. Les 12 mois donnent une fenêtre d’observation, pas une garantie de conversion.

Premier test recommandé : varier uniquement l’objet de E02 entre « Votre prochain beau projet » et « Quel projet aimeriez-vous attirer ? ». Sur une petite base, les retours qualitatifs peuvent être plus utiles qu’un faux verdict statistique.

Relire les prix, conditions, liens et fonctionnalités avant lancement, puis au moins chaque trimestre. La durée relative des mails évite les saisons fictives et les promesses datées ; une modification d’offre doit mettre à jour tous les envois encore en attente.

## Prolongement : une newsletter vivante

Une newsletter ultérieure pourra être proposée via un parcours d’inscription cliquable distinct, à créer avant utilisation. E32 ne collecte aucune inscription. Pour cette newsletter éventuelle, prévoir au maximum deux lettres par mois au départ :
- une analyse d’une décision concrète de cabinet ;
- un exemple vérifié ou une démonstration, terminé par un CTA explicite qui prolonge le sujet.

Rotation possible : positionnement, messages publicitaires, suivi des demandes, organisation du cabinet. Une vraie évolution de produit ou un cas client documenté peut remplacer un sujet prévu. Le contenu est revu avant chaque édition ; on ne programme pas des « actualités » fictives douze mois à l’avance.

## Sources et limites

- Base locale structurée associée au dépôt [Process-Valere](https://github.com/georgescold/Process-Valere), remote `template` : [emailing](../../base-valere/03-marketing-copy/emailing.md), [structure CEO](../../base-valere/03-marketing-copy/structure-ceo.md), [objets](../../base-valere/07-templates/objets-email.md).
- [Cible Essort](../cible/cible-avatar.md), [marché et cible](../marche/marche-et-cible.md), [offre de référence](../offre/offre-actuelle.md).
- Dernières décisions de cette conversation et FAQ publiée : elles priment sur les formulations historiques (« sinon Essort n’est pas payé », « accompagnement », exclusivité départementale).
- [Guide actuel](../acquisition/leadmagnet/README.md) et [plateforme : vérifications](../crm.md).
- Parcours observé : `site/api/lead.js`, `site/frontend/src/data/ressources.js`.

La recherche Reddit oriente les sujets ; elle ne prouve pas ce que pense chaque cabinet français. Les généralisations, statistiques et formulations dénigrantes du matériau de recherche ne sont pas reprises dans les mails.

## Relecture Valère — version 3

Chaque mail suit une progression courte : un désir ou une situation dans laquelle le lecteur se reconnaît ; une friction précise ; une explication concrète ; le bénéfice pour son cabinet ; un CTA explicite et motivé. L’ouverture peut poser une question, montrer une scène ou partir d’une phrase de propriétaire.

Le rêve ne prend pas la même forme dans tous les messages : temps de conception, mission choisie, valeur comprise, décision plus claire. Les peurs sont réduites par une explication du fonctionnement ; elles ne sont pas amplifiées. L’obstacle reste le flou dans le message ou l’organisation, jamais l’identité du professionnel.

Les onze blocs d’une VSL ne sont pas répétés mécaniquement dans chaque courrier. La progression CEO est condensée pour garder des mails lisibles. L’urgence repose uniquement sur le choix d’une prochaine action ; aucun faux délai n’a été ajouté.

Les objets comptent au maximum 40 caractères dans la source, avec la variable [prénom] le cas échéant. Ils ouvrent une question dont le corps apporte la réponse. Aucun faux « Re: », chiffre spectaculaire ou objet sans rapport avec le contenu.

## Ce qui change dans cette refonte

Le rôle d’Essort est d’apporter un regard sur l’acquisition, pas d’apprendre à l’architecte à mener son métier. Le mail sur la question à poser au propriétaire à propos de son budget est supprimé. Les conseils génériques de rendez-vous ou d’organisation sont remplacés par des mécanismes qui expliquent comment attirer et suivre les projets recherchés.

Chaque mail doit répondre à trois questions : quel mécanisme le lecteur comprend-il mieux ; quel bénéfice cela peut-il apporter à son cabinet ; pourquoi effectuer l’action proposée maintenant ? « Maintenant » désigne une décision pertinente, sans urgence artificielle.

Les sujets couvrent la recommandation et la découverte, les angles publicitaires, la diffusion locale, les formulaires, le coût des demandes pertinentes, les intentions de recherche, les limites d’un simple boost, les priorités du site, le suivi et le périmètre de délégation. Les aspirations restent les missions choisies, la valeur comprise et le temps de conception.

La signature et le CTA ne suffisent pas à rendre un mail commercial : le contenu doit montrer comment le travail d’Essort aide à atteindre cette aspiration. Le bouton prolonge le sujet avec une destination précise. Aucune invitation à répondre par email ; aucun exercice à faire seul n’est compté comme CTA.

## Continuité éditoriale

Chaque mail rappelle brièvement l’idée qui lui sert de point de départ, sans obliger le lecteur à avoir lu les précédents. Les transitions progressent des missions recherchées au message, puis au parcours de découverte, aux critères de qualité et à la délégation. Sur la durée, ces thèmes sont repris avec un nouvel exemple ou une décision différente.

La fin du parcours relie concrètement les sujets : E21 diffusion des contenus → E22 secteur → E23 rôle du site → E24 correction d’une annonce trop large → E25 essai du fonctionnement Essort. E26 précise la différence avec Google, puis E27–E30 développent le périmètre de délégation, le positionnement et les tests de messages. E31–E32 préparent la prochaine décision du cabinet.

E24, « Pourquoi ces demandes ? », remplace l’explication abstraite du suivi par un exemple : des demandes pour une pièce alors que le cabinet cherche des rénovations complètes. Le texte montre l’ajustement de l’annonce et du formulaire, puis ce qu’il faut observer. Aucun résultat n’est promis sur la seule base de cette reformulation.

## Application des quatre réponses

Les variantes décrites dans PERSONNALISATION.md sont désormais opérationnelles dans l’aperçu et l’export local. Elles utilisent les options réelles du formulaire, avec un moteur commun et 52 règles éditoriales. Le métier influe sur les missions et les exemples, la structure sur l’organisation, l’origine des projets sur l’argumentation, et le département sur la discussion du secteur. Les consignes de personnalisation manuelle précédentes sont remplacées par ces règles pour les passages concernés.

Le parcours ne suppose pas qu’une origine de projets indique un échec. Un cabinet qui utilise déjà Google, les réseaux ou la publicité reçoit un discours qui tient compte de cette expérience. Le branchement au site et à l’outil d’envoi n’est pas activé.
