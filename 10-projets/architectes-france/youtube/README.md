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

### ⚠️ Ta position — tu n'es PAS architecte

**La règle la plus importante du dossier.** Tu es prestataire en acquisition marketing.
Tu ne dessines pas, tu n'as jamais déposé un permis, tu n'as pas de cabinet. Ta
légitimité ne vient pas de l'expérience du métier : elle vient d'**ailleurs**, et c'est
précisément ce qui la rend utile.

| ❌ Jamais | ✅ Toujours |
|---|---|
| « Je ne ferais plus que du professionnel » | « Les cabinets qui y vont signent autrement » |
| « Quand je facturais mes honoraires… » | « Quand je regarde les grilles d'honoraires du marché… » |
| « Nous, architectes… » | « Vous, les architectes… » / « votre métier » |
| « J'ai arrêté de faire ça » | « Ce que je vois passer, c'est… » |
| « Mon cabinet » | « Les cabinets que j'accompagne » |
| Se faire passer pour un pair | Assumer le regard extérieur |

**D'où vient ton autorité, concrètement :**

1. **Tu achètes de l'attention pour vivre.** Tu sais ce que coûte un clic, une demande,
   un rendez-vous — pas en théorie, parce que tu paies la facture.
2. **Tu vois ce qu'un architecte seul ne voit pas :** ce que font les constructeurs, les
   cuisinistes et les plateformes, parce que tu ouvres leurs campagnes toutes les semaines.
3. **Tu as lu ce que personne ne lit** : Archigraphie en entier, le code de déontologie,
   3 778 messages d'architectes sous anonymat.

La phrase de cadrage, à dire une fois par vidéo, dans les deux premières minutes :

> « Je ne suis pas architecte. Je fais de l'acquisition pour des cabinets d'architecture
> — c'est mon métier d'aller chercher des clients pour les vôtres. Et de là où je suis,
> il y a des choses qui sautent aux yeux. »

**Ne jamais s'en excuser.** Un regard extérieur qui s'excuse d'être extérieur perd les
deux : il n'est ni pair, ni expert.

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
