# Brochure de proposition — après le premier appel

Après chaque premier appel avec un cabinet, on lui envoie une brochure de 4 à 5 pages et un
mail. Ce dossier contient le **moteur**, c'est-à-dire la mise en page, le mail et le générateur.
Le **contenu** vit dans le dépôt privé des fiches.

| Fichier | Rôle |
|---|---|
| `brochure.html.j2` | La mise en page de la brochure, aux couleurs d'Essort |
| `mail.txt.j2` | Le mail qui accompagne la brochure, signé par celui qui a mené l'appel |
| `generer-brochure.py` | Fusionne le socle et la fiche du cabinet, puis produit le PDF et le mail |

## Le contenu : dépôt privé, jamais ici

Dans `agence/prospection/listes/fiches-appel/propositions/`, qui est le dépôt privé
`georgescold/essort-veille-leads` :

| Fichier | Contenu |
|---|---|
| `_socle-essort.json` | Ce qui est commun à toutes les brochures : prestations, histoire d'Essort, clients références et leurs résultats, questions-réponses, réassurance, émetteurs (nom, téléphone, SIRET) |
| `_modele-client.json` | La fiche vierge à copier pour chaque nouveau cabinet |
| `AAAA-MM-JJ-prenom-nom-proposition-essort.json` | La fiche d'un cabinet : seulement ce qui vient de l'appel |
| `…-proposition-essort.pdf` · `…-mail.txt` | Ce qui part chez le cabinet |
| `logos/` | Les logos des clients références |

⚠️ Le socle contient des noms de clients et leurs chiffres, et les fiches des données
nominatives : **rien de tout cela n'entre dans ce dépôt public** (règle n°1 du `CLAUDE.md`).

## Produire une brochure

```bash
python agence/offre/brochure/generer-brochure.py agence/prospection/listes/fiches-appel/propositions/AAAA-MM-JJ-prenom-nom-proposition-essort.json
```

Le script :
1. **fusionne** le socle et la fiche. La fiche complète le socle, et peut en remplacer n'importe
   quel champ : un texte, une question, l'ordre des clients.
2. **remplace les variables** des textes : `{{ client.prenom }}`, `{{ zone.nom }}`, `{{ zone.de }}`,
   `{{ zone.villes }}`, `{{ euros(seuil_travaux) }}`, `{{ essai.jours }}`…
3. **refuse** une fiche où il reste un « À REMPLIR », en listant les champs. Il refuse aussi un
   émetteur sans SIRET.
4. **signale** un prix différent de celui de `../offre-actuelle.md`, qui fait foi.
5. écrit le **PDF** et le **mail** à côté de la fiche.

## Ce que la brochure doit respecter

Ce sont les consignes de Loys du 30/09/2026, lors de la première brochure :

- **Mise en forme très simple** : fond blanc, filets fins, pas d'ombres ni de grands aplats.
  Couverture « Essort × Prénom Nom ». 4 à 5 pages au plus.
- **Le ton** : on parle directement au cabinet, naturellement, pour le rassurer.
  - Le « nous » est réservé aux phrases (« ce que nous mettons en place »).
  - Les listes sont nominales (« Création de… », « Suivi des résultats… »). Jamais « nous faisons ceci, nous faisons cela ».
  - Pas de texte « vendeur » plaqué.
- **La structure CEO par petites touches**, une phrase par section :
  - le rêve en couverture ;
  - l'échec excusé et l'ennemi en page 2 ;
  - la peur et le doute, puis la garantie, en page 3.
- **Pas de HT/TTC** dans le texte : la mention légale de TVA reste seulement en pied de page.
- **Pied de page** : nom de l'émetteur, EI, SIRET, TVA non applicable. **Aucun nom commercial.**
- **Aucune redite** entre les questions-réponses et les pages précédentes, ni à l'intérieur
  d'une carte client.
- **Ce qui est vrai de l'offre** :
  - le cabinet rappelle lui-même ses demandes ;
  - pendant l'essai, les demandes arrivent dans un dossier en ligne partagé, avec une alerte par e-mail ;
  - pendant l'essai, on ne fait que des publicités en images : des vidéos seulement après validation d'un angle ;
  - les identifiants Instagram ne servent qu'aux publicités, comme le disent les conditions d'essai (§ 2) ;
  - on répond sous 4 h, hors week-end ;
  - le paiement se fait en fin de mois, par virement ;
  - un mois d'engagement, puis 7 jours de préavis ;
  - prorata le premier mois ;
  - tout est au nom du client.
- **Après chaque génération**, vérifier chaque page en image :
  - pas de débordement, pied de page présent ;
  - montants et durées non coupés ;
  - logos et portraits entiers.
