# Benchmark — les architectes qui achètent vraiment du trafic

> **Relevé le 16 septembre 2026**, Bibliothèque publicitaire Meta, pays = France.
> Document de travail : ce sont des observations horodatées, pas des engagements ni des
> arguments de vente. Les chiffres ci-dessous ne doivent pas être transformés en
> statistiques de rareté dans le guide (cf. `cible-avatar.md`, § *Manière de parler*).
>
> Complète `marche-et-cible.md` : celui-là décrit la demande (ce que vivent les
> cabinets), celui-ci décrit l'offre publicitaire réellement diffusée sur Meta.

## Méthode — reproductible en 10 minutes

La recherche par mot-clé de la bibliothèque est inutilisable : elle remonte les écoles,
les fournisseurs de LED et les magazines de déco, presque jamais les cabinets.

Le bon levier est le **champ de recherche en mode annonceur** : en tapant « architecte »,
« architecture », « architecte d'intérieur », « design d'intérieur », « maître d'œuvre »,
la liste déroulante renvoie les pages Facebook **avec leur compte Instagram lié et son
nombre d'abonnés**. C'est le seul endroit où l'on obtient les deux d'un coup.

Ensuite, pour l'historique complet d'un annonceur (actif **et** inactif — la seule façon
de voir l'ancienneté réelle) :

```
https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=FR&view_all_page_id=<ID>&search_type=page&media_type=all
```

Les ID de page sont dans le tableau du § 5.

---

## 1. Le classement — ceux qui tournent depuis longtemps

Classés par **continuité de diffusion**, pas par taille.

| # | Annonceur | Métier / zone | Instagram | Ancienneté de diffusion | Volume | Destination du clic |
|---|---|---|---|---|---|---|
| 🥇 | **L.Decor — Laëtitia Le Petit** | Archi d'intérieur + déco, **Morbihan** | [@l.decor_laetitia_lepetit](https://instagram.com/l.decor_laetitia_lepetit) · **34,8 K** | **16 déc 2024 → aujourd'hui, sans trou** | **120 pubs** | Profil Instagram · Messenger |
| 🥈 | **Berkail** | Archi d'intérieur • maîtrise d'œuvre • travaux, **Sud-Est + Lyon** | [@berkail.co](https://instagram.com/berkail.co) · 7,8 K | **17 sep 2025 → 15 sep 2026, sans trou** | **880 diffusions / 12 créatives** | `berkail.co` → formulaire |
| 🥉 | **Hi Architecture Détail** ⚠️ | ~~Cabinet~~ → **produit numérique vendu AUX architectes** | [@hi_architecture_detail](https://instagram.com/hi_architecture_detail) · **87,9 K** | **17 sep 2025 → aujourd'hui**, runs de 3 à 5 mois | **400+ pubs** | `hiarchitecturedetail.com` → *Commander* |
| 4 | **ISTO Architecture & Interior Design** | Studio luxe international, diffuse en FR | [@isto_architecture](https://instagram.com/isto_architecture) · **136,1 K** | **sep 2025 → aujourd'hui**, vagues de 7-30 j | **400+ pubs** | Profil Instagram |
| 5 | **Créaxia** | Maîtrise d'œuvre, **Clermont-Ferrand (63)** | [@creaxia_63](https://instagram.com/creaxia_63) · 2,1 K | 16 déc 2025 → 1er juil 2026 | 13 pubs | `creaxia63.fr` + Messenger |
| 6 | **Amitecte** | Architecte + MOE, **Annecy** | [@amitecte.fr](https://instagram.com/amitecte.fr) · 306 | 28 nov 2025, puis 7 fév → 12 mar 2026 | 3 pubs | **Messenger direct** (`fb.me`) |

**L'observation centrale : sur les dizaines de milliers d'architectes et d'architectes
d'intérieur exerçant en France, deux annonceurs seulement tiennent une diffusion continue
de plus de douze mois.** Tout le reste tient de trois jours à cinq semaines, puis s'arrête.

---

## 2. Les faux amis — grosse audience Instagram, zéro publicité

À vérifier avant de citer qui que ce soit comme exemple :

| Annonceur | Instagram | Réalité publicitaire |
|---|---|---|
| **Samuel Elbilia** (Paris) | @samuelelbilia · **52,6 K** | **12 pubs** en tout, des salves de 2 à 7 heures. 100 % organique. |
| **Reno** | @reno__fr · 9,7 K | **Aucune pub active.** |
| **Tm architecte d'intérieur** | @tm_archinterior · 10,4 K | aucune campagne longue repérée |
| **Antoine Lejeune** | @lejeune_architecte_interieur · 8,3 K | idem |
| **Cabinet BIEC** (Bordeaux) | @cabinetbiec · 3,2 K | **1 pub, 2 jours.** |
| **O-Conception** (Vendée) | @o.conception · 1,2 K | 3 pubs, dont une pour des **portes ouvertes** |

> C'est la situation *« Architecte d'intérieur avec de beaux contenus »* de
> `cible-avatar.md`, vérifiée sur pièces : l'audience existe déjà, elle ne produit pas
> de conversations projet. Samuel Elbilia a 52 600 abonnés et n'a jamais engagé de
> dépense publicitaire suivie.

---

## 3. Les 4 modèles d'acquisition observés

### Modèle A — « Le boost perpétuel vers le profil Instagram » (L.Decor, ISTO)

Pas de site, pas de landing page, pas de formulaire. On sponsorise un **avant/après** et
le CTA est *Voir le profil Instagram* ou *Envoyer un message*.

- **Structure L.Decor** : une créative « evergreen » qui tourne 11 mois d'affilée
  (16 déc 2024 → 5 nov 2025), puis des relais de 2 mois (nov→jan, jan→mar, mar→mai,
  juin→août), **plus un flux permanent de boosts de 7 jours** par-dessus.
- **Le texte est minimaliste**, écrit comme un post, pas comme une publicité :
  > *« Transformation🔥 Nous avons fait cet appartement un lieu accueillant et cosy♥️
  > tu as projet de réno ou déco?? 👉 @l.decor_laetitia_lepetit »*

  Tutoiement, fautes comprises, aucune promesse chiffrée. Ça tourne depuis 21 mois.
- **Coût** : faible. Ce sont des boosts de publication, pas des campagnes structurées.
- **La limite** : pas de pixel exploitable, pas de liste, pas de mesure de coût par
  demande. Tout repose sur les messages privés et sur la personne qui y répond.

### Modèle B — « Le contractant général qui industrialise » (Berkail) ⭐

Le seul dispositif publicitaire réellement construit du relevé, côté français.

- **880 diffusions pour 12 contenus créatifs** → la même vidéo dupliquée 12 à 16 fois.
  C'est une **multiplication par zone et par audience**, pas de la production créative.
- **Diffusion continue sur 12 mois**, par blocs de 2 à 3 mois.
- **Positionnement, mot pour mot** :
  > *« Architecture d'intérieur • Maîtrise d'œuvre • Travaux. L'atelier Berkail réunit
  > tous les ingrédients afin d'allier design et qualité d'exécution, pour votre projet
  > de rénovation. »* — accroche : **« Votre projet, tout-en-un ! »**
- **Le parcours complet** : vidéo de 17 s → `berkail.co` → **formulaire de 3 minutes**
  → étude gratuite à domicile → rendez-vous avec l'architecte d'intérieur → conducteur
  de travaux dédié → livraison. Le bouton *« Je démarre mon projet »* est répété 4 fois.
- **Les preuves affichées sur le site** : 52 biens rénovés · 5/5 sur Google · 2 jours
  d'avance moyenne à la livraison · 3 témoignages avec photos de chantier.
- **Aucun prix affiché.** Devis après visite gratuite.
- **La zone est explicite** : Provence, Var, Alpes-de-Haute-Provence, Côte d'Azur, Lyon.

### Modèle C — « Le Messenger à coût zéro » (Amitecte, Créaxia)

Pas de site dans la publicité : le clic ouvre une conversation Messenger.

> *« Un projet immobilier commence par une bonne estimation. Un architecte vous contacte
> rapidement pour échanger sur votre projet et vous donner une première estimation
> gratuite, sans engagement. »* — CTA : **Obtenir un devis** · *Réponse rapide • Sans engagement*

Créaxia y ajoute la **signature géographique dans le corps du texte** :

> *« Vous l'avez imaginée pièce par pièce. Créaxia, la concrétise étape par étape.
> 📍 Clermont-Ferrand & alentours »*

- **Avantage** : aucune infrastructure, démarrage en vingt minutes.
- **Limite** : ça s'éteint vite. Amitecte a tenu cinq semaines, Créaxia six mois en
  pointillés. Sans personne pour rappeler, le contact Messenger se périme.

### Modèle D — « Le produit numérique vendu aux architectes » (Hi Architecture Détail) ⚠️

**Ce n'est pas un cabinet.** C'est un vendeur de produits numériques dont **la cible, ce
sont les architectes eux-mêmes** — la même audience que celle d'Essort.

- Ce qu'ils vendent : des **bibliothèques de détails CAD 2D prêts à l'emploi**, un
  « technical book », et un **workflow de rendu par IA**.
- Texte des annonces (en anglais, diffusion mondiale dont la France) :
  > *« Create high-end architectural visuals in minutes — without complex rendering tools. »*
  > *« Ready-to-use 2D construction details to integrate directly into your projects,
  > ensuring flawless drawings and zero errors. »*
- CTA : **Commander / Acheter** — achat direct, pas de document gratuit en amont.
- **400+ publicités, des runs de 3 à 5 mois sur la même créative**, 87,9 K abonnés Instagram.

> Leur angle est l'**outil technique** — faire gagner du temps sur la production. Pas
> l'acquisition client. À surveiller : ils ont déjà l'audience s'ils décident d'élargir.

---

## 4. Ce que le relevé apporte au projet

1. **L'affirmation « très peu de cabinets font de la publicité » est vérifiable.**
   Deux annonceurs continus sur tout le marché français. C'est une observation sourçable,
   à manier comme un constat de terrain — pas comme un argument de rareté.
2. **La situation « beaux contenus, peu de conversations » est confirmée sur pièces.**
   52 600 abonnés, 12 publicités. C'est le meilleur exemple concret pour les contenus
   qui parlent de transformer une audience en demandes de projet.
3. **Celui qui tient la distance n'est pas architecte, c'est un contractant général.**
   Berkail ne vend pas de l'architecture : il vend *« tout-en-un »* et *« zéro stress »*,
   un interlocuteur unique et une date de livraison tenue. Le métier se fait prendre les
   projets par ceux qui structurent leur marketing, pas par ceux qui conçoivent moins bien.
4. **La zone géographique est déjà un critère d'achat du marché.** Berkail liste ses
   départements sur son site, Créaxia écrit « 📍 Clermont-Ferrand & alentours » dans le
   corps de l'annonce. ⚠️ Cela documente une pratique observée — **ce n'est pas une
   reprise de l'exclusivité départementale**, qui n'est pas un engagement actuel
   (cf. `offre-actuelle.md`, § *Cohérence des contenus*).
5. **Le modèle A est le premier pas réaliste à expliquer.** L.Decor tourne depuis 21 mois
   avec des publications boostées et un texte de trois lignes. C'est reproductible en une
   semaine par un cabinet qui n'a jamais fait de publicité, et ça produit la première
   demande entrante — avant toute construction de tunnel.

---

## 5. Annuaire brut — annonceurs archi repérés (avec Instagram)

Matière première pour de la veille, du contenu ou des captures d'écran. Tous ont au
moins une publicité dans la bibliothèque.

| Annonceur | Instagram | Abonnés IG | Page ID Meta |
|---|---|---|---|
| ISTO Architecture | @isto_architecture | 136,1 K | `305763869547948` |
| Hi Architecture Détail | @hi_architecture_detail | 87,9 K | `102688471803915` |
| Samuel Elbilia (Paris) | @samuelelbilia | 52,6 K | `439614152775320` |
| L.Decor (Morbihan) | @l.decor_laetitia_lepetit | 34,8 K | `255425574640770` |
| Tm architecte d'intérieur | @tm_archinterior | 10,4 K | `100236101887584` |
| Reno | @reno__fr | 9,7 K | `105512561920272` |
| Antoine Lejeune | @lejeune_architecte_interieur | 8,3 K | `1623542781285075` |
| Berkail | @berkail.co | 7,8 K | `101746778948315` |
| AC Design (33) | @acdesign.33 | 6,8 K | — |
| Audrey Clain — Pinkspace | @pinkspace_deco | 5,9 K | `277351799092819` |
| Coccia Architecture | @coccia.architecture | 3,6 K | `104585748074715` |
| Cabinet BIEC (Bordeaux) | @cabinetbiec | 3,2 K | `175134175949962` |
| Créaxia (63) | @creaxia_63 | 2,1 K | `865373093584092` |
| Carl Tran — CT Création | @carltran_ctcreation | 1,4 K | `146974902032714` |
| O-Conception (Vendée) | @o.conception | 1,2 K | `236795143162992` |
| Guillaume Wacgnere (Dijon) | @guillaumewacgnere | 907 | `104335627635103` |
| Horizon-Intérieurs | @horizon.interieurs | 446 | `986012671436317` |
| Xiléades Architecteurs | @xileades | 313 | `105303971433647` |
| Amitecte (Annecy) | @amitecte.fr | 306 | `215577235305491` |
| Apto | @apto_architecte_interieur | 305 | `805973402607116` |

**Concurrence directe sur la même cible** — à surveiller, à ne pas citer dans un contenu
public : Maxime Architecte Libre — @architecte_libre · **29,5 K** · page `100653691800364`.

---

## 6. Limites du relevé

- Les compteurs « 400 résultats » / « 880 résultats » sont **plafonnés ou agrégés** par
  Meta : une carte « récapitulatif » peut couvrir 12 à 16 diffusions du même contenu.
  Ce sont des ordres de grandeur, pas des comptages exacts.
- **ISTO et Hi Architecture Détail ne sont pas des cabinets français.** Ils diffusent en
  France, leurs annonces sont en anglais. À ne pas présenter comme des confrères locaux.
- Les dates sont celles affichées par Meta le 16 septembre 2026. Les publicités bougent :
  **tout revérifier avant publication ou tournage**, capture datée et URL visible.
