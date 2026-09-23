# Le site Essort — carte du dépôt

Le site a son **propre dépôt git** : [`Enzdo/essort`](https://github.com/Enzdo/essort).
Il est cloné dans `agence/site/` et **ignoré** par le dépôt de l'agence
(voir `.gitignore` à la racine). Conséquence pratique :

- on lit la base de connaissance et le code du site dans la même session ;
- les commits du site se font **dans** `site/`, sur son remote à lui ;
- un `git add -A` à la racine n'embarque jamais le site.

```bash
cd agence/site && git pull
```

## Ce que c'est

React 19 + Tailwind (CRA via craco), pré-rendu maison au build, déployé sur
**Vercel** (`vercel.json`). API Express séparée (`backend/`) sur **Render**
(`render.yaml`, région Francfort), qui parle à Supabase, Discord et Google Sheets.
Le `README.md` du dépôt parle encore de Strapi : c'est faux, l'API Express l'a
remplacé. PostHog est branché côté front.

| Quoi | Où |
|---|---|
| Domaine servi | `https://essort.agency` — `essort.fr` ne résout pas |
| Rendez-vous | Cal.com, `https://cal.com/essort/30min` |
| Routes | `frontend/src/App.js` |
| Page d'accueil | `frontend/src/pages/HomePage.jsx` |
| Sections de l'accueil | `frontend/src/components/home/` |
| Autres pages | `frontend/src/pages/` — contact, blog, plan-acquisition, légal |
| API | `backend/src/routes/` — `leads`, `blog`, `caseStudies`, `localPages` |

## Les fichiers qu'on modifiera

Tout le texte nominatif et commercial est **centralisé**. On ne réécrit pas une
section pour changer un prix ou un libellé de bouton.

| Besoin | Fichier |
|---|---|
| Nom, promesse, domaine, CTA, fondateur, SEO | `frontend/src/data/brand.js` |
| Les 3 offres : prix, features, visibilité | `frontend/src/data/offers.js` |
| Articles de blog | `frontend/src/data/articles.js` |
| Le document gratuit | `frontend/src/data/planAcquisition.js` |
| Capture de lead (POST) | `backend/src/routes/leads.js` |

`offers.js` porte un drapeau `visible` par offre : le passer à `false` retire
l'offre partout (accueil, pied de page, pré-rendu) sans la supprimer.

## L'état du funnel, à connaître avant de toucher au copy

L'accueil suit déjà la **structure CEO** (`03-marketing-copy/structure-ceo.md`),
dans cet ordre : Hero → Problem → Solution → Mechanism → MethodPromise →
Offers → IsThisYou → Faq → BlogPreview → FinalCta.

Deux choses décidées le 5 septembre 2026 et écrites en commentaire dans
`HomePage.jsx` :

1. **Quatre sections sont retirées de la page, pas du dépôt** — `Proof`,
   `FreePresentation`, `Objective`, `Founder`. Les remonter dans `HomePage.jsx`
   suffit à les rétablir. `Objective` promet un parcours à 90 jours qui déborde
   du périmètre Meta Ads : il ne remonte qu'avec le Système Carnet Plein.
2. **La page ne porte aucune preuve** depuis le retrait de `Proof` : ni
   témoignage, ni chiffre, ni garantie chiffrée, ni urgence réelle. C'est un
   manque, pas un parti pris — et il ne se comble pas par de la formule.
   Il se comble par un premier résultat client.

Seule l'offre **Meta Ads (999 €/mois, installation offerte)** est en ligne ;
le Défi 7 Jours est masqué. La page ne doit donc rien promettre qui déborde de
ce périmètre.

## Ce qui reste à renseigner

`brand.js` porte des `TODO` qui alimentent les mentions légales : `legalName`,
`contact.email`. Les laisser vides est une non-conformité ; les inventer serait
pire. C'est au fondateur de les donner.
