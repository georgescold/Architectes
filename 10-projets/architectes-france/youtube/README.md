# Chaîne YouTube « Essort Architectes » — plan de production

## RESTER DANS SON DOMAINE : L'ACQUISITION

Deuxième règle, juste après la première, et elle en découle.

Loys n'est pas architecte et n'a aucune raison de le devenir. Son domaine, c'est
l'acquisition : où sont les clients, ce que coûte une demande, quels leviers existent,
lequel monter en premier, ce qui convertit et ce qui ne convertit pas. C'est là qu'il est
légitime, c'est là qu'il vend, et c'est le seul terrain où il ne peut pas être repris.

Donc on n'explique JAMAIS à un architecte comment faire son métier. Pas de cours sur les
procédures, pas de tutoriel réglementaire, pas de leçon de conception. Le spectateur en
sait plus que nous sur ces sujets, et il le sent en trois phrases.

La règle des proportions, applicable à chaque épisode :

  Le métier sert à poser le constat. Deux minutes maximum, jamais davantage. On ne
  démontre pas, on cite ce qui est public, on donne la source et on passe.

  L'acquisition occupe tout le reste. C'est là qu'on développe, qu'on chiffre, qu'on
  raconte ce qu'on voit passer, qu'on montre des campagnes et des coûts.

Le test à appliquer sur chaque chapitre : est-ce que je parle de leur métier, ou de la
manière dont leurs clients les trouvent ? Si c'est le premier, le chapitre est trop long
ou n'a rien à faire là.

Ce qui reste dans `connaissance-metier.md` sert à tenir la conversation et les
commentaires, pas à alimenter le script. C'est une préparation, pas un contenu.

---

## LA RÈGLE QUI PRIME SUR TOUTES LES AUTRES

Cette chaîne existe pour amener des clients. Pas pour informer, pas pour faire autorité,
pas pour être irréprochable sur le plan factuel — tout cela sert l'objectif, rien de tout
cela ne le remplace.

Le risque de ce dossier est identifié : à force de viser la rigueur et la valeur
pédagogique, on produit un excellent contenu gratuit que personne ne relie à une
entreprise. Un épisode brillamment documenté qui ne convertit pas est un échec.

Conséquence concrète, non négociable dans chaque épisode : le chemin vers le client doit
être complet et développé. La douleur nommée, la publicité en ligne désignée comme le
levier qui la règle, et le document gratuit appelé franchement. C'est le BLOC ACQUISITION,
deux minutes pleines, jamais en fin de vidéo et jamais expédié. Son absence est une erreur
bloquante dans `verifier.py`.

La rigueur factuelle sert cet objectif : on ne raconte pas n'importe quoi parce qu'un
contenu faux détruit la confiance qui fait signer.

---

> **La chaîne part de zéro abonné.** Tout ce qui suit en tient compte : aucun épisode
> ne suppose une audience existante, ne dépend d'un invité, ni d'un résultat client.
> Les 20 épisodes sont tournables seul, avec un écran et un micro.

## Le dossier

```
youtube/
├── README.md              ← ce fichier : calendrier, conventions, checklists
├── liens-utiles.md        ← banque de liens vérifiée, mutualisée
├── build.py               ← génère les PDF (python build.py, ou build.py 03 07)
├── fiches/                ← 20 fiches source, une par épisode
│   └── 01-....md … 20-....md
└── pdf/                   ← les 20 PDF prêts à imprimer / lire au tournage
```

Documents de cadrage : [`offre-actuelle.md`](../strategie/offre-actuelle.md) ·
[`cible-avatar.md`](../strategie/cible-avatar.md) · [`marche-et-cible.md`](../strategie/marche-et-cible.md) ·
[`benchmark-annonceurs.md`](../strategie/benchmark-annonceurs.md) ·
[`titres-et-chapitrages.md`](titres-et-chapitrages.md) (les 20 sujets,
version courte) · [`structure-ceo.md`](../../../03-marketing-copy/structure-ceo.md) ·
[`youtube.md`](../../../02-acquisition/youtube.md).

---

## 1. Le calendrier — alterné, jamais deux fois la même famille

Quatre familles : **CONSTAT** (le chiffre qui pique) · **PREUVE** (démonstration écran) ·
**RÈGLE** (le texte, le droit, l'aide publique) · **SYSTÈME** (la méthode).
Deux audiences : 🅐 architecte DE · 🅑 architecte d'intérieur · 🅐🅑 les deux.

**Aucun épisode ne suit un épisode de la même famille.** Une chaîne qui enchaîne six
constats passe pour une chaîne de plainte ; une chaîne qui enchaîne quatre méthodes
passe pour une chaîne de vente.

| # | Famille | Audience | Titre | Sujet d'origine |
|---|---|---|---|---|
| 01 | SYSTÈME | 🅑 | Le client qui paie le double et que personne ne cible | 16 |
| 02 | CONSTAT | 🅐🅑 | La moitié des architectes gagnent moins que ça | 1 |
| 03 | PREUVE | 🅐🅑 | Comment j'ai trouvé les 2 SEULS architectes de France qui font de la pub depuis un an | 11 |
| 04 | RÈGLE | 🅐 | Le chiffre qui a sorti les architectes du marché de la maison | 8 |
| 05 | PREUVE | 🅑 | Les architectes d'intérieur sont les MIEUX PLACÉS pour la pub | 14 |
| 06 | CONSTAT | 🅐🅑 | Ce n'est pas la crise. C'est un tri. | 3 |
| 07 | RÈGLE | 🅐🅑 | Le CODE DE DÉONTOLOGIE m'a ouvert les yeux sur la PUB des architectes | 7 |
| 08 | SYSTÈME | 🅐🅑 | Les architectes SURCOMPLIQUENT leur communication | 19 |
| 09 | CONSTAT | 🅐🅑 | J'ai lu 3 778 messages d'architectes écrits sous anonymat | 6 |
| 10 | PREUVE | 🅐 | J'ai lu la page d'accueil de 40 cabinets. C'est la même phrase. | 15 |
| 11 | RÈGLE | 🅑 | Le titre d'architecte d'intérieur ne sera pas protégé | 9 |
| 12 | CONSTAT | 🅐 | Ne baissez surtout pas vos honoraires | 2 |
| 13 | PREUVE | 🅐🅑 | J'audite la fiche Google de trois cabinets | 13 |
| 14 | SYSTÈME | 🅐🅑 | L'acquisition d'un cabinet repose sur 4 PILIERS | 18 |
| 15 | RÈGLE | 🅐🅑 | MaPrimeRénov' 2026 : un massacre pour les uns, 3,6 MILLIARDS pour les autres | 5 |
| 16 | CONSTAT | 🅐 | Les architectes construisent 5 % des maisons de ce pays | 4 |
| 17 | SYSTÈME | 🅐🅑 | Ma méthode EXACTE pour lancer un cabinet sur un nouveau département | 12 |
| 18 | CONSTAT | 🅐🅑 | Les architectes en ont marre de racheter leurs propres clients | 10 |
| 19 | SYSTÈME | 🅐🅑 | Combien coûte vraiment une demande de projet (les chiffres) | 17 |
| 20 | CONSTAT | 🅐🅑 | Faut-il ARRÊTER d'attendre le bouche-à-oreille avant qu'il ne soit TROP TARD ? | 20 |

**Rythme conseillé : 1 vidéo par semaine pendant 20 semaines**, le même jour, à la même
heure. Deux par semaine si le montage suit — la régularité compte plus que le volume,
mais le volume compte plus que la perfection.

### Pourquoi cet ordre précis quand on part de zéro

- **L'épisode 01 est le plus facile et le moins risqué.** Sujet d'opportunité pure
  (le B2B en architecture d'intérieur), aucune douleur à remuer, aucune donnée sensible.
  C'est le rodage : tu apprends le cadrage, le son, le rythme sur une vidéo où une
  maladresse ne coûte rien.
- **Les épisodes 02, 03, 04 sont des vidéos de recherche.** Quelqu'un qui tape
  « salaire architecte », « publicité architecte », « architecte obligatoire 150 m² »
  peut les trouver sans être abonné. **C'est le seul trafic disponible à zéro abonné.**
- **Les épisodes qui vendent arrivent tard** : 17 (la méthode) et 19 (le calcul) sont
  des VSL déguisées. Avant 15 épisodes, elles font fuir.
- **L'épisode 07 est le plus rentable de la chaîne** et demande une validation juridique.
  Le placer en semaine 7 laisse six semaines pour l'obtenir.
- **L'épisode 13 demande l'accord écrit de trois cabinets.** En semaine 13, tu auras
  douze vidéos à montrer pour convaincre — pas zéro.

---

## 2. Les règles de production, valables pour les 20

### Le squelette (structure CEO pliée au watch time)

```
00:00  HOOK (5 s)        Un chiffre officiel + sa source. Rien d'autre.
00:20  INTRO (40 s)      Contexte, enjeu, pay-off. Une open loop. Pas de CV.
01:00  ① RÊVE            Une scène concrète, pas une abstraction
02:00  ② EXCUSE          « On ne vous l'a jamais enseigné »
03:30  ③ PEUR            Le coût de l'inaction, chiffré, jamais inventé
05:00  ④ ENNEMI          Plateforme · conception gratuite · CMI · l'école · l'habitude
06:30  ⑤ DOUTE           On dit l'objection avant lui
08:00  ⑥ PREUVE + BIG IDEA
10:00  ⑦ MÉCANISME       3 étapes maximum, une temporalité
12:00  ★ PITCH (aux ⅔)   Le document gratuit, ou l'appel. Jamais à la fin.
13:00  ⑧ ESCALIER        48 h → 7 jours → 30 jours → 90 jours
14:30  OUTRO             Rouvre une tension → renvoie vers une AUTRE vidéo
```

### Le processus de preparation d'un episode

Quatre etapes, dans cet ordre. Aucune ne se saute.

1. Relire `connaissance-metier.md`. C'est la base verifiee : les deux metiers, qui a le
   droit de signer quoi, les chiffres d'Archigraphie, le cadre publicitaire, les
   concurrents, les avatars. Si une fiche contredit ce document, c'est la fiche qui a tort.

2. Verifier chaque affirmation de l'episode a la source, et l'ecrire dans la section
   LES FAITS VERIFIES avec son lien. Ce qui n'y figure pas ne se dit pas devant la camera.

3. Consulter `registre-des-preuves.md`. Une preuve appartient a un seul episode. Si elle
   est deja attribuee ailleurs, on ne la remontre pas.

4. Lancer le controle :

   ```
   python verifier.py 07
   ```

   Il signale les erreurs connues, les ruptures de posture, les chiffres sans source, les
   sections manquantes et les moments Essort absents. Tant qu'il n'affiche pas `pret`,
   l'episode ne se tourne pas.

Et avant de lancer la camera, les trois questions du registre : qu'est-ce que le
spectateur sait a la fin qu'il ne savait pas au debut, quelle est la source et est-elle
affichable, cette preuve a-t-elle deja ete montree ailleurs.

---

### TA POSITION — l'expert acquisition des architectes

Tu n'es pas architecte, et tu n'es pas non plus en dessous d'un architecte. Tu es
l'expert d'un domaine qu'il ne maîtrise pas : l'acquisition. Tu t'adresses à lui d'égal
à égal, chacun sur son terrain.

La phrase qui porte toute l'autorité, à dire une fois par vidéo dans les deux premières
minutes, affirmative et sans préambule :

> « Je fais de l'acquisition pour des cabinets d'architecture. C'est mon métier d'aller
> chercher des clients pour les vôtres. »

Elle se suffit. On ne l'accompagne d'aucune excuse, d'aucun « je ne suis pas
architecte mais », d'aucun « je ne vais pas vous apprendre votre travail ».

| ❌ Jamais | ✅ Toujours |
|---|---|
| « Vous connaissez ça mieux que moi » | « Ce qui m'intéresse, c'est la conséquence commerciale » |
| « Je ne suis pas légitime pour en parler » | « Voilà ce que je vois passer toutes les semaines » |
| « Je ne vais pas vous faire un cours » | « Je passe directement à ce qui vous concerne » |
| « Je ne suis qu'un prestataire » | « C'est mon métier » |
| « Je ne ferais plus que du professionnel » | « Les cabinets qui y vont signent autrement » |
| « Quand je facturais mes honoraires… » | « Quand je regarde les grilles du marché… » |
| « Nous, architectes… » | « Vous, les architectes… » / « votre métier » |
| « Mon cabinet » | « Les cabinets que j'accompagne » |
| Se faire passer pour un pair | Assumer l'expertise d'à côté |

**D'où vient ton autorité, concrètement :**

1. **Tu achètes de l'attention pour vivre.** Tu sais ce que coûte un clic, une demande,
   un rendez-vous — pas en théorie, parce que tu paies la facture.
2. **Tu vois ce qu'un architecte seul ne voit pas :** ce que font les constructeurs, les
   cuisinistes et les plateformes, parce que tu ouvres leurs campagnes toutes les semaines.
3. **Tu as lu ce que personne ne lit** : Archigraphie en entier, le code de déontologie,
   des milliers de messages d'architectes sous anonymat.

**Les deux erreurs symétriques.** Se faire passer pour un architecte te disqualifie en
une phrase. Te placer en dessous d'un architecte te fait perdre l'autorité qui justifie
qu'on t'écoute — et qu'on t'achète. Tu n'es ni au-dessus ni en dessous : tu es à côté,
sur un domaine dont il a besoin.

---

### Les 3 moments Essort — où le lien se fait

L'agence apparaît **trois fois**, à des endroits précis. Jamais plus, jamais ailleurs.

| # | Moment | Où | Durée | Ce que ça fait |
|---|---|---|---|---|
| **①** | **L'ancrage** | 00:20-01:00, dans l'intro | 10-15 s | Dit d'où tu parles. Pas une offre : une position. C'est la phrase de cadrage ci-dessus. |
| **②** | **La preuve d'usage** | Dans ⑥ PREUVE ou ⑦ MÉCANISME | 20-30 s | « Voilà ce qu'on fait quand un cabinet nous arrive avec ce problème. » Le mécanisme devient réel parce que quelqu'un l'opère. Toujours au **nous**, jamais au **je**. |
| **③** | **Le pitch** | Aux ⅔, ~12:00 | 15 s max | Le document gratuit. Jamais l'offre à 999 €, jamais l'appel. |

**L'offre commerciale n'est jamais vendue dans une vidéo.** Elle vit dans la description
et dans la séquence email qui suit le téléchargement du document. Une chaîne à zéro
abonné qui vend un accompagnement à 999 € dans sa sixième vidéo ne fait ni l'un ni l'autre.

⚠️ Le moment ② est celui qu'on rate. Sans lui, la vidéo est un bon contenu gratuit que
personne ne relie à une entreprise. Avec lui, le spectateur comprend **qu'un métier
existe derrière** — et c'est ce qui fait cliquer sur la description trois vidéos plus tard.

---

### AUCUN MOT DE MÉTIER N'EST EMPLOYÉ SANS ÊTRE EXPLIQUÉ

C'est la règle la plus souvent violée, et celle qui coûte le plus cher — parce qu'un mot
que le spectateur ne comprend pas le fait décrocher sans qu'il sache pourquoi.

Elle vaut à deux niveaux :

1. **Dans la fiche**, pour que Loys comprenne complètement ce qu'il va dire. Une fiche qui
   emploie « maître d'ouvrage », « personne morale » ou « quartile » sans les définir est
   une fiche inutilisable. Le niveau de détail attendu est celui-ci :

   > Une personne morale, c'est une société : SARL, SAS, SCI, association. Un restaurant ou
   > une boutique sont presque toujours des sociétés. La distinction compte parce que les
   > dérogations de surface ne valent jamais pour une société.

   Pas : « le maître d'ouvrage est une société avec construction ».

2. **Dans la vidéo**, où le mot se définit à voix haute, sur place, la première fois qu'il
   est prononcé. Jamais « on y reviendra ».

Le lexique complet est dans `connaissance-metier.md`, section 0. Chaque fiche ouvre sa
section AVANT DE TOURNER par « Les mots de cet épisode » : uniquement les termes que cette
fiche-là emploie, définis en français courant.

Le test, quand tu écris : est-ce que quelqu'un qui n'a jamais mis les pieds dans une agence
d'architecture comprend cette phrase du premier coup ? Si la réponse demande une seconde
lecture, la phrase est à réécrire.

⚠️ Ça vaut aussi pour le vocabulaire d'acquisition — créative, enchère, taux de
transformation, ligne de flottaison. Ce sont des mots d'agence, pas du français.


### LE FIL DE LA DÉMONSTRATION — la section qui porte l'épisode

Chaque fiche contient, juste sous la big idea de l'épisode, une idée par chapitre, dans
l'ordre. Lues à la suite, elles donnent le raisonnement complet de la vidéo.

Toujours la même forme, trois lignes :

```
Ch.7 · Le titre du chapitre

L'idée : ce que le spectateur doit avoir compris à la fin du chapitre. Une phrase, en
langage courant.

En clair : la même chose expliquée en détail, pour toi. Pourquoi c'est vrai, d'où ça
vient, ce que ça prépare pour le chapitre suivant.

À l'écran : la capture, le document ou le schéma qui la porte.
```

Quatre règles :

1. **Une idée par chapitre, et une seule.** Si un chapitre en porte deux, on le coupe en
   deux. Le test : retirer un chapitre du fil — si la suite tient quand même, il ne servait
   à rien.
2. **Aucun mot de jargon de production.** Pas de « la bascule de la vidéo », pas de « le
   cœur factuel », pas de « l'ennemi de l'épisode ». Ces mots-là sont vides pour qui lit la
   fiche six mois plus tard.
3. **Le lien est sous la ligne « À l'écran », jamais ailleurs.** Dès qu'un chapitre montre
   un document, une capture ou une recherche, l'adresse est écrite juste en dessous, sur une
   ligne `Lien :`. On ne renvoie pas à une liste de sources en fin de section : au tournage,
   on suit le fil de haut en bas et on doit pouvoir ouvrir la page au moment où on en parle.
   Ça vaut autant pour les textes officiels que pour les relevés publicitaires.
4. **Rien ne se désigne sans se nommer.** Jamais « les trois autres » ou « ce mécanisme » :
   on écrit lesquels, à chaque fois, même si c'est répété.
5. **Toute capture qui contient un chiffre porte la date du relevé à l'image**, et aucun
   cabinet n'est identifiable — les reconstitutions sont fabriquées par toi.


### LE TITRE EST UN HOOK — le cadre à appliquer aux 20

Un titre doit faire deux choses **en même temps**, et manquer l'une des deux le tue :

**1. Dire le sujet en une à deux secondes.** Pas « mon avis sur le marché » — le sujet
exact, tout de suite. Si quelqu'un doit lire deux fois pour savoir de quoi ça parle, il est
déjà parti.

**2. Créer de la curiosité sur ce sujet précis.** Une curiosité hors sujet ne sert à rien :
elle amène des gens qui partent à la trentième seconde, et la vidéo est punie pour ça.

Les quatre fautes qui tuent un titre :

| Faute | Ce qui se passe | Le correctif |
|---|---|---|
| **Retard** | Le sujet n'arrive qu'à la fin du titre | Le sujet dans les 3 premiers mots |
| **Confusion** | Vocabulaire de métier, phrase passive, double idée | Mots simples, voix active, une seule idée |
| **Hors-cible** | Ça ne parle pas de LUI | Dire « vous », « votre » — nommer sa douleur |
| **Indifférence** | Vrai, mais sans enjeu | Poser un contraste : ce qu'il croit vs. la réalité |

**Le moteur, c'est le contraste.** Le spectateur croit A. Le titre annonce B. L'écart entre
les deux est la seule chose qui fait cliquer.

- « La publicité est autorisée aux architectes **depuis 1992** » → il croit que c'est
  interdit (A), le titre dit le contraire (B), et la date rend le contraste indiscutable.
- « Ce n'est **pas** la crise, c'est **un tri** » → contraste énoncé mot pour mot.
- « 130 publicités pour les constructeurs, **2** pour les architectes » → contraste
  implicite : deux chiffres côte à côte, et il comprend seul.

**Les tests avant de valider un titre :**

1. Le sujet est-il compris en 2 secondes par quelqu'un qui ne me connaît pas ?
2. Est-ce qu'un architecte se reconnaît dedans — « vous », « votre », sa douleur à lui ?
3. Quel est le A, quel est le B ? Si je ne peux pas les nommer, il n'y a pas de hook.
4. Est-ce que j'y ai mis un mot que seul un initié comprend ? Si oui, je le retire.
5. Est-ce que ce titre pourrait être celui d'un autre épisode ? Si oui, il est trop vague.

⚠️ Le titre ne promet jamais plus que ce que la vidéo tient. Un titre qui exagère ramène
des clics et fait chuter la rétention, ce qui coûte plus cher que de ne pas être cliqué.
Et aucun chiffre dans un titre qui ne soit pas dans la vidéo, sourcé.

**Trois titres par fiche.** Le principal est celui qu'on publie. Les deux variantes servent
à tester si la vidéo ne décolle pas au bout de 48 heures — on change le titre, pas la
vidéo.


### Titre et miniature

- **Le texte de la miniature ne répète jamais le titre.** L'œil lit la miniature, puis
  le titre : les deux doivent s'additionner, pas se doubler.
- 2 à 4 mots maximum dans la miniature, très gros, clair sur fond sombre.
- 1 à 3 mots en MAJUSCULES dans le titre, pas plus.
- Une parenthèse finale qui ajoute un bénéfice ou une précision : `(les chiffres)`,
  `(même sans une seule photo)`.
- Le visage à gauche ou à droite, jamais centré. Une seule idée visuelle.

### Voix et rythme

Parler **fort**, débit **rapide**, ton d'autorité. Le micro fait paraître faible une voix
normale. Le niveau doit tenir **du début à la fin** : le défaut n°2 après le hook, c'est
l'intro dynamique suivie d'un corps plat. Une open loop toutes les ~3 minutes.

### Ce qu'on ne fait jamais

| Interdit | Pourquoi |
|---|---|
| « On se retrouve dans cette nouvelle vidéo » | Zéro information, zéro tension |
| « Comme je disais dans ma dernière vidéo » | **À zéro abonné, tu disqualifies 100 % des spectateurs** |
| Un CTA vers le site à la fin | Fait sortir de YouTube, coûte du watch time |
| Nommer un confrère négativement, comparer deux cabinets | **Article 17** du code de déontologie (confraternité). ⚠️ Ne vise que les **confrères** : un constructeur de maisons ou une plateforme n'en est pas un |
| Avancer un chiffre ou une promesse qu'on ne peut pas prouver | Pratique commerciale trompeuse, **L. 121-2** du code de la consommation. Peines **L. 132-2** : 5 ans et 750 000 € quand c'est en ligne. C'est la limite la plus sérieuse de toute la chaîne |
| Citer un résultat client non documenté | [`cible-avatar.md`](../strategie/cible-avatar.md) |
| Dire « 1 000 € » | C'est **999 €** — [`offre-actuelle.md`](../strategie/offre-actuelle.md) |
| Promettre l'exclusivité départementale | Retirée des engagements publics |
| Annoncer un nombre d'architectes d'intérieur | Non sourçable |
| Une vanne de type « même avec 60 de QI » | Chez un architecte dont le confrère vient d'être liquidé, ça passe pour de la moquerie |

### Ce qu'on dit toujours quand on parle de l'offre

**999 €/mois · 4 opportunités commerciales garanties par mois, sinon Essort n'est pas
payé · mise en place sous 48 h · premières demandes sous 48 h · 7 jours d'essai gratuit ·
budget publicitaire distinct, y compris pendant l'essai · une opportunité n'est pas un
contrat signé.**

Les deux dernières mentions ne sont pas facultatives : les taire détruit la relation au
premier mois.

---

## 3. Le gabarit de description YouTube

```
[Une phrase qui reprend la promesse du titre, avec le chiffre.]

📄 Le document gratuit : https://essort.agency/plan-acquisition
🔗 L'article complet : https://essort.agency/blog/<slug de l'épisode>

Sources citées dans la vidéo :
• [source 1] — [lien]
• [source 2] — [lien]

CHAPITRES
00:00 [titre du hook]
01:00 ...
...

Essort accompagne les architectes et architectes d'intérieur indépendants ou
en équipe de 1 à 5 personnes sur leur acquisition de projets.
Échanger 30 min : https://cal.com/essort/30min
Instagram : https://instagram.com/essort.architectes
```

Le **premier chapitre doit être `00:00`**, sinon YouTube n'affiche pas les chapitres.

---

## 4. Checklist avant publication

- [ ] Le titre contient 1 à 3 mots en majuscules, pas plus
- [ ] Le texte de la miniature ne répète pas le titre
- [ ] La première phrase contient un chiffre **et** sa source
- [ ] Aucun « comme je disais dans ma dernière vidéo »
- [ ] Le pitch est aux deux tiers, pas à la fin
- [ ] L'outro rouvre une tension et nomme une autre vidéo
- [ ] Chaque chiffre annoncé est dans [`liens-utiles.md`](liens-utiles.md)
- [ ] Aucune photo de projet d'un cabinet sans autorisation écrite
- [ ] Aucun confrère nommé négativement
- [ ] Sous-titres automatiques relus et corrigés
- [ ] Chapitres en description, premier à `00:00`
- [ ] Lien du blog correspondant en premier lien

## 5. Ce qu'on mesure les 10 premières semaines

**Pas les vues.** À zéro abonné, les vues ne disent rien pendant deux mois.

| Métrique | Cible | Où |
|---|---|---|
| Rétention à 30 s | **50-70 %** — sous 50 %, le hook est à refaire | Studio → Rétention absolue |
| Watch time moyen (vidéo de 12-15 min) | 40-60 % | Studio → Vue d'ensemble |
| Taux de clic | à relever, pas de cible avant 10 vidéos | Studio → Impressions |
| Commentaires | le **volume** compte, la tonalité qualifie l'audience | — |

Si une vidéo a un bon taux de clic mais moins de 3 minutes de watch time, le problème
n'est **pas** la miniature : c'est le hook et la voix.

---

## 6. Régénérer les PDF

```bash
cd 10-projets/architectes-france/youtube
python build.py          # les 20
python build.py 07 13    # seulement ces épisodes
```

Nécessite `markdown` (`pip install markdown`) et Google Chrome. Les liens restent
cliquables dans le PDF.
