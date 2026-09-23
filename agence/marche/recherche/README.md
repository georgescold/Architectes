# Données brutes de la recherche marché — 16/09/2026

Corpus collecté pour [`marche-et-cible.md`](../marche-et-cible.md).
**Ce sont des sources brutes, pas la base de connaissance.** On n'y répond jamais
directement : on cite le document d'analyse, qui est vérifié et sourcé.

| Fichier | Contenu |
|---|---|
| `corpus-reddit-3778.jsonl` | 3 778 posts et commentaires Reddit dédupliqués (Apify, `trudax/reddit-scraper-lite`). Champs conservés : id, titre, url, auteur, upvotes, date, corps, subreddit |
| `verbatims-par-theme.txt` | Top extraits par thème : clients/leads, prix/honoraires, client pénible, concurrence, burnout, argent, solo, **hiérarchie/statut**, **vérités dures**, **jugement** |
| `verbatims-hierarchie-statut.txt` | 71 extraits sur le mépris inter-métiers (DE ↔ archi d'intérieur ↔ dessinateur ↔ décorateur) |
| `verbatims-francophones.txt` | 107 extraits en français (rares — Reddit est anglophone sur ce métier) |

**Sous-reddits couverts :** r/Architects (148 posts), r/architecture (28),
r/InteriorDesign (22), r/smallbusiness, r/Entrepreneur, r/france, r/AntiTaff,
r/etudiants, r/conseiljuridique, r/autoentrepreneurs.

**Trous connus** (crédits Apify épuisés — 3 comptes × 5 $) :
- r/InteriorDesignPro et les communautés de **professionnels** du design d'intérieur
  (r/InteriorDesign est dominé par des particuliers)
- les groupes Facebook FR
- les commentaires YouTube des chaînes listées au § 13 du document d'analyse

**Encodage :** les apostrophes typographiques de Reddit sont arrivées corrompues
(`�`) et ont été normalisées en `'` dans les fichiers `verbatims-*`. Le JSONL
conserve la forme brute.
