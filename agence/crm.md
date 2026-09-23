# Le CRM Essort — provenance, démo et limites de vérification

Inspecté le 15 septembre 2026. Dépôt fourni par l'utilisateur : https://github.com/Enzdo/crm.git
Commit cloné : `207f026d4ee1d8b7ce78ee561cacdfb9ff5e3635`.

## Ce que le code confirme

- Next.js 15 / React 19 ; styles et composants Essort existants.
- Interface leads tableau, kanban et « Ma journée », filtre par campagne/statut/urgence.
- Pipeline : nouveau, contacte, qualifie, tres_qualifie, rdv, signe, perdu.
- Fiche : réponses du formulaire, notes, journal d'interactions, nombre de tentatives, délai de premier rappel, date du prochain rappel, montant signé et motif de perte.
- Actions de rappel et historique ; export CSV côté serveur.
- Suivi de campagnes / indicateurs ; dépenses saisies manuellement dans le code actuel (`saveCampaignSpend`).
- Ingestion par webhook et exemple de synchronisation Google Sheets / Apps Script. Ceci ne prouve pas qu'une connexion est configurée en production.
- Accès agence / cabinet avec authentification et isolation SQL. Aucun audit de sécurité complet effectué.
- CLAUDE.md parle d'un CRM privé pour clients Essort, mais il ne prouve pas les conditions commerciales actuelles ; le guide invite à les demander, sans affirmer qu'il est gratuit pour tous.

Fichiers de référence : `components/leads/*`, `lib/queries/leads.ts`, `lib/actions/leads.ts`, `lib/actions/campaigns.ts`, `app/api/export/leads/route.ts`, `scripts/apps-script/essort-sync.gs`.

## Démonstration locale

Clone : `agence/crm/` — dépôt Git séparé (`Enzdo/crm`), ignoré par le dépôt de l'agence. Ses commits se font dans ce dossier, sur son propre remote.
Serveur Next local : `http://127.0.0.1:3199` ; session exec actuelle 30500 (redémarrage après ajustement des polices).

- Tableau : http://127.0.0.1:3199/demo
- Pipeline : http://127.0.0.1:3199/demo?vue=kanban
- Ma journée : http://127.0.0.1:3199/demo?vue=journee
- Fiche latérale : http://127.0.0.1:3199/demo?lead=00000000-0000-4000-8000-000000000003

HTTP 200 vérifié sur tableau, kanban et fiche. Le parent réalise la QA visuelle et les captures via le navigateur autorisé.

La route `/demo` réutilise les composants d'origine avec des fixtures écrites expressément pour le guide. Aucun fichier `.env` récupéré ou créé, aucune connexion à une base, aucun client réel. Les coordonnées utilisent `.invalid`, pas de numéro à appeler. Bandeau de démonstration permanent. Les 12 500 € sont un exemple fictif, jamais une preuve de résultats.

Modifications limitées au clone : nouveaux fichiers `app/demo/*` ; police Google chargée localement dans `app/layout.tsx` (Inter repris des assets du guide, Instrument Serif libre téléchargée du dépôt officiel Google Fonts). Correction d'une variable CSS récursive préexistante (`--font-sans: var(--font-sans)`) dans `app/globals.css` pour que la vraie police Inter s'affiche. Aucun fichier produit original modifié, aucun déploiement.

Les liens internes des composants d'origine restent `/leads` et mènent à la connexion. Utiliser directement les URL `/demo` ci-dessus pour les captures. Éviter les actions d'écriture dans cette démo : il n'y a aucune persistance. Aucun envoi de message, aucun webhook ni synchronisation lancés.

Relance du serveur si besoin : depuis le clone, `node node_modules/next/dist/bin/next dev --turbopack --hostname 127.0.0.1 --port 3199`.

## Wandeed

Sources officielles ouvertes :
- CRM2 : https://www.wandeed.com/architecture/
- CRM3 : https://www.wandeed.com/crm/
- CRM4 : https://www.wandeed.com/fonctionnalites/

Le site présente Wandeed comme ERP/CRM adapté aux architectes : projets, contrats, planification, prévisionnel de facturation, temps, documents, contacts et gestion commerciale. Ces affirmations proviennent de la documentation commerciale de l'éditeur ; le produit n'a pas été testé. Pas de prix repris, pas de recommandation absolue.

Capture à faire sur la page publique architecture ou CRM. Ne pas prétendre avoir essayé un compte Wandeed. Pas d'inscription d'essai déclenchée.

## Intégration guide

`crm.md` propose 4 pages prêtes à intégrer, avec blocs `::capture crm-kanban`, `crm-fiche`, `crm-journee`, `wandeed`. Les légendes disent explicitement « démonstration » et « données fictives ».
Les routines d'onboarding et de collaboration du texte sont une organisation recommandée à confirmer au démarrage ; le dépôt seul ne permet pas de certifier un processus commercial déjà appliqué à tous les cabinets.
