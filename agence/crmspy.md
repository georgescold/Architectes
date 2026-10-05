# CRMSpy — l'outil interne de traitement des leads

Dépôt Git séparé : [`Enzdo/crmspy`](https://github.com/Enzdo/crmspy), cloné dans
`agence/crmspy/` et **ignoré** par le dépôt de l'agence (voir `.gitignore` à la racine).
Ses commits se font dans ce dossier, sur son propre remote.

À ne pas confondre avec le CRM Essort ([`crm.md`](crm.md)) : le CRM sert **aux cabinets
clients** pour rappeler leurs leads Meta. CRMSpy sert **à l'agence seule**, pour trier et
contacter ses propres prospects, les architectes repérés par la veille concurrentielle.

## Ce que c'est

L'interface de la base de **veille concurrentielle** : les abonnés et les personnes qui
interagissent avec le concurrent suivi (Instagram, TikTok), ses contenus, ses publicités
Meta, son blog et ses témoignages. Chaque profil devient un lead, noté et classé.

- **Priorités** : `P0 — ultra prioritaire` … `P4 — écarté` (la valeur complète, pas `P0` seul).
- **Segments** : architecte, architecte d'intérieur, maître d'œuvre, designer, étudiant,
  hors cible, incertain.
- **Statut de prospection** modifiable dans le tableau et dans la fiche, écrit en base.

## L'interface

| | |
|---|---|
| **Accueil** | leads par priorité et par segment, statuts, abonnés du concurrent, pubs actives, dernier run de collecte et coût Apify |
| **Un onglet par table** | leads, interactions, pipeline, leads chauds, contenus, publicités, pubs gagnantes, SEO, témoignages, snapshots, runs |
| **Filtres** | plein texte, multi-choix avec effectifs, intervalles de nombres et de dates ; enregistrables (table `veille_vues`) |
| **Fiche lead** | bio, scores, contact et toutes ses interactions ; lien direct vers le profil Instagram |
| **Export CSV** | du résultat filtré, colonnes au choix, lisible par Excel |
| **Suppression** | d'un lead, avec ou sans ses interactions |

## Architecture

Node ≥ 20.6, **aucune dépendance npm**, front sans framework.

```
lib/api.js      cœur : tables, requêtes PostgREST, filtres, CSV, session
server.js       serveur local (statique + /api/*)
api/index.js    le même cœur en fonction serverless Vercel
public/         index.html, app.js, style.css
```

La clé `service_role` reste côté serveur : le navigateur ne parle qu'aux routes `/api/*`.
Pour ajouter une table ou changer les colonnes par défaut : `TABLES` dans `lib/api.js`.

## Où tournent les choses

| Quoi | Où |
|---|---|
| Base | Supabase, projet **`spytool`** (ref `lfudtjgwqzcacaibqhro`), organisation `essort` |
| Secrets en local | `agence/crmspy/.env` — `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `PORT` (ignoré par les deux dépôts) |
| En local | `npm run dev` dans `agence/crmspy/` → http://localhost:5173, sans mot de passe |
| En ligne | https://veille-explorateur.vercel.app, projet Vercel `veille-explorateur`, protégé par `APP_PASSWORD` |
| Collecte | le pipeline de veille (Apify), hors de ce dépôt ; son état est visible dans l'onglet Runs |

⚠️ Le projet Vercel `veille-explorateur` **n'est pas relié à Git** : un push sur
`Enzdo/crmspy` ne déploie rien. La mise en ligne se fait à la main, par l'API avec le token
Vercel (jamais le CLI, voir `agence/site.md`), après accord : `POST /v13/deployments` avec
les fichiers de `git ls-files` en base64 (hors `.env`, `.vercel`, `node_modules`).
**Vérifier que la liste n'est pas vide avant d'envoyer** : le 24 septembre 2026, un envoi
sans fichiers est passé en production et le site a répondu 404 le temps de redéployer.

⚠️ La clé `service_role` contourne toutes les règles d'accès de la base. Elle ne va que
dans `.env` et dans les variables Vercel, jamais dans un fichier versionné, jamais dans le
navigateur.

⚠️ Les leads sont des **données nominatives** (profils Instagram, bios, contacts) : aucun
export ne doit entrer dans le dépôt public de l'agence (règle 1 du `CLAUDE.md`).

## Qualifier les leads sans risque

Vérifié le 24 septembre 2026 (commit `89b4d29`), sur la vraie base :

- **La collecte n'écrase jamais tes qualifications.** Son upsert n'envoie ni
  `statut_prospection` ni `notes` : ces deux colonnes ne bougent qu'à la main.
- **Un lead supprimé peut revenir**, en « Nouveau », s'il réagit encore aux contenus du
  concurrent. Pour ne plus le contacter : statut **Écarté**, pas suppression.
- **Pagination stable** : le tri est départagé par le nom d'utilisateur. Avant, les leads
  à score égal pouvaient sauter ou apparaître deux fois d'une page à l'autre (et dans
  l'export CSV). Contrôle : 1 427 leads parcourus, 0 doublon, 0 manquant.
- **Aucun faux « OK »** : un statut qui ne s'enregistre pas renvoie une erreur, et la fiche
  revient au statut réel.
- **Notes de prospection éditables** dans la fiche (Ctrl + Entrée pour enregistrer).
- Statuts possibles : Nouveau, À qualifier, Contacté, Répondu, RDV, Client, Déjà traité, Écarté.
  La base n'a pas de contrainte : la liste vit dans `STATUTS` (`lib/api.js`).
- **Déjà traité** (depuis le 05/10/2026) : lead pris en charge hors de CRMSpy, par exemple une
  demande de rendez-vous venue des pubs (base Airtable des leads, fiches d'appel). À ne pas
  recontacter. Avec « Écarté », la ligne est estompée dans le tableau. Pour ranger un lead, on
  change son statut : on ne le supprime pas, sinon la collecte peut le recréer en « Nouveau ».
- **Date du dernier changement de statut** : colonne `statut_change_le`, remplie par un
  déclencheur en base à chaque changement de statut (migration dans `crmspy/sql/`). La
  collecte ne la touche pas. Pour les relances : filtre statut « Contacté » + « + Filtre »
  → statut changé le, jusqu'à il y a 3 jours. Les statuts posés avant le 24/09/2026 n'ont
  pas de date (« avant le 24/09 »). `maj_le`, lui, reste la date du dernier passage de la
  collecte.

## Les leads de la prospection sortante

Depuis le 2 octobre 2026, CRMSpy reçoit aussi les cabinets trouvés par la prospection
sortante (voir `prospection/prospection-sortante.md`), pas seulement ceux de la veille :
144 ajoutés ce jour-là, source **« Prospection sortante »** dans la colonne `sources`.

- **Clé** : le compte Instagram quand il existe ; sinon le domaine du site
  (`nom-du-cabinet.fr`), et le bouton profil ouvre le site au lieu d'Instagram.
- **Notes** : canal conseillé, téléphone, email, contrôles Sirene et plateforme, accroche
  et message d'approche. La collecte ne les touche jamais.
- **Priorité** : P0 pub Meta en cours, P1 pub arrêtée ou disponible sur Trouver mon
  Architecte, P2 installation récente ; `score_engagement` à 0 (aucune interaction avec
  le concurrent).
- Avant d'en ajouter d'autres : chercher les doublons par Instagram, email, domaine et nom.
  Un domaine de plateforme (architectes-pour-tous.fr…) ne prouve pas un doublon.

## Interface — 2 octobre 2026

Statut en première colonne, figée au défilement, et en couleur (une teinte par étape) ;
priorité, segment, engagement et scores en couleur. Clic sur un en-tête : trier, filtrer
sur la colonne (dont « vide / renseigné »), masquer. Les effectifs des filtres comptent
désormais tous les leads : ils s'arrêtaient aux 1 000 premiers (limite de Supabase par
requête). Commits `8ce70a8` et `5ad8163`, déployés le même jour.

La collecte remarche : le run du 2 octobre à 8 h 15 est OK sur toutes les sources.

## État au 24 septembre 2026

Testé en local avec le `.env` : 1 427 leads, 1 580 interactions, 25 publicités actives
suivies sur 184 détectées. Le dernier run de collecte (24/09, 08 h 05) est **en échec** :
quota Apify épuisé (5,20 $ sur 5 $), Instagram en HTTP 403, YouTube en HTTP 404. Aucun
nouveau lead n'est collecté tant que ce n'est pas réglé.
