#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Controle systematique des fiches video.

    python verifier.py            # toutes les fiches
    python verifier.py 03 07      # seulement ces episodes

Cherche les erreurs connues, les affirmations non sourcees, les ruptures de
posture, les redites et les sections manquantes.

Les regles viennent de connaissance-metier.md. En cas de contradiction entre
une fiche et ce document, c'est la fiche qui a tort.

    ERREUR  -> faux ou interdit, a corriger avant tournage
    doute   -> probablement un probleme, a verifier a l'oeil
"""
import os, re, sys, io

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
FICHES = os.path.join(ROOT, "fiches")

# Une occurrence precedee d'une de ces tournures est une CONSIGNE, pas une faute.
NEGATIONS = re.compile(
    r"(jamais|ne\s+dis\b|ne\s+pas\b|interdit|c'est\s+faux|erreur|proscri|banni|"
    r"surtout\s+pas|eviter|évite|ne\s+concerne\s+pas|ne\s+s'applique\s+pas|a\s+ne\s+plus)",
    re.I,
)

ERREURS = [
    (r"162\s*pages?", "Archigraphie fait 83 pages, pas 162"),
    (r"\b1\s?000\s*(?:€|euros)\s*/?\s*mois", "L'offre est a 999 EUR, jamais 1 000"),
    (r"exclusivit[ée]\s+d[ée]partementale", "Exclusivite departementale : retiree des engagements"),
    (r"je\s+ne\s+fer(?:ai|ais)|j'ai\s+arr[êe]t[ée]\s+de|mon\s+cabinet\b|mes\s+honoraires|quand\s+j'[ée]tais\s+architecte",
     "Posture : Loys n'est pas architecte"),
    (r"nous,?\s+(?:les\s+)?architectes", "Posture : ne jamais dire 'nous, architectes'"),
    (r"\d[\d\s]*\s*architectes?\s+d'int[ée]rieur\s+en\s+France",
     "Le nombre d'architectes d'interieur n'est pas sourcable"),
    (r"paie\s+le\s+double|×\s?2\b", "Aucun multiplicateur d'honoraires n'est sourcable"),
    (r"oblig[ée]\s+de\s+passer\s+par\s+(?:vous|un\s+architecte\s+d'int)",
     "Aucun monopole legal pour l'architecte d'interieur"),
    (r"mieux\s+que\s+moi|je\s+ne\s+suis\s+pas\s+l[ée]gitime|je\s+ne\s+vais\s+pas\s+vous\s+(?:faire\s+un\s+cours|apprendre)|je\s+ne\s+suis\s+qu'un|pardon(?:nez)?\s+si",
     "Posture : ne jamais se placer en dessous de l'architecte"),
    (r"Je\s+ne\s+suis\s+pas\s+architecte\s*[:,]",
     "Posture : la phrase d'autorite commence par « Je fais de l'acquisition pour », pas par une negation"),
]

DOUTES = [
    (r"150\s*m²", "seuil de 150 m2 : ne vaut QUE pour les personnes physiques, "
                  "verifier que la fiche le precise"),
    (r"d[ée]ontologie", "le code de deontologie ne s'applique PAS aux architectes "
                        "d'interieur : verifier l'audience de l'episode"),
    (r"Archigraphie", "verifier que l'annee des donnees est annoncee : "
                      "revenus 2022, effectifs 2023"),
    (r"nos\s+clients\s+ont|un\s+cabinet\s+a\s+(?:obtenu|sign[ée])",
     "aucun resultat client tant qu'il n'est pas documente et autorise"),
]

SECTIONS = [
    ("## LA BIG IDEA", "la big idea, en tete de fiche"),
    ("## LE FIL DE LA DÉMONSTRATION", "la big idea de chaque chapitre"),
    ("## AVANT DE TOURNER", "ce que tu dois savoir hors camera"),
    ("## LE PIÈGE", "le piege ou l'on se fait reprendre"),
    ("## LES OBJECTIONS", "les objections previsibles et leurs reponses"),
    ("## LE DÉROULÉ", "le deroule par chapitre"),
    ("## GARDE-FOUS", "les garde-fous de l'episode"),
]

OBLIGATOIRES = [
    (r"### 1\.", "des chapitres numerotes dans l'ordre"),
    (r"Exemple de formulation", "des exemples de ce qu'il faut dire"),
    (r"BLOC ACQUISITION", "le bloc acquisition, obligatoire dans chaque episode"),
    (r"Ch\.1 · Ouverture", "le fil de la demonstration, qui commence au chapitre 1"),
    (r"L'idée :", "une idee annoncee pour chaque chapitre"),
    (r"En clair :", "l'explication detaillee de chaque idee"),
    (r"### Les mots de cet épisode", "le lexique des termes employes par l'episode"),
    (r"\nLiens? : https?://", "les liens places sous les lignes « A l'ecran »"),
    (r"publicit[ée] en ligne", "la phrase qui designe la publicite en ligne comme levier"),
    (r"essort\.agency/ressources", "le lien vers le document gratuit"),
]

# Nombres qui n'ont pas besoin d'un lien a cote : annees, numeros de formulaire,
# numeros d'article.
NEUTRES = re.compile(r"^(?:19|20)\d\d$|^13824$|^13404$|^431$|^121$|^132$")

SEPARATEUR = re.compile(r"(?<=[.!?])\s+|[\r\n]+")
TIMECODE = re.compile(r"^\d\d:\d\d\s*[—-]", re.M)


def contexte(t, pos, avant=140, apres=90):
    return re.sub(r"\s+", " ", t[max(0, pos - avant):pos + apres])


def chiffres_sans_source(texte):
    """Un chiffre marquant doit avoir un lien dans la meme section."""
    suspects = []
    for s in re.split(r"\n(?=#{2,3}\s)", texte):
        if "http" in s:
            continue
        titre = s.strip().split("\n")[0][:70]
        for m in re.finditer(r"\b\d{1,3}(?:\s\d{3})+\b|\b\d{2,}\s?%", s):
            val = m.group().strip()
            if NEUTRES.match(val.replace(" ", "")):
                continue
            suspects.append((val, titre))
            break
    return suspects


def repetitions(texte):
    """Deux phrases identiques dans la meme fiche = redite a supprimer."""
    corps = re.sub(r"```.*?```", "", texte, flags=re.S)
    vues, doublons = set(), []
    for ph in SEPARATEUR.split(corps):
        ph = re.sub(r"\s+", " ", ph).strip()
        if len(ph) < 60 or ph.startswith("http"):
            continue
        cle = ph.lower()
        if cle in vues:
            doublons.append(ph[:80])
        vues.add(cle)
    return doublons


def verifier(chemin):
    nom = os.path.basename(chemin)
    t = io.open(chemin, encoding="utf-8").read()
    pbs = {"ERREUR": [], "doute": []}

    for motif, message in ERREURS:
        for m in re.finditer(motif, t, re.I):
            ctx = contexte(t, m.start())
            if NEGATIONS.search(ctx):
                continue
            pbs["ERREUR"].append("%s\n              ...%s..." % (message, ctx[:150]))

    for motif, message in DOUTES:
        if re.search(motif, t, re.I):
            pbs["doute"].append(message)

    for marqueur, message in SECTIONS:
        if marqueur not in t:
            pbs["ERREUR"].append("section absente : " + message)

    for motif, message in OBLIGATOIRES:
        if not re.search(motif, t):
            pbs["ERREUR"].append("absent : " + message)

    for val, titre in chiffres_sans_source(t)[:4]:
        pbs["doute"].append("« %s » sans lien dans sa section (%s)" % (val, titre))

    for d in repetitions(t)[:3]:
        pbs["doute"].append("phrase repetee : « %s… »" % d)

    if TIMECODE.search(t):
        pbs["doute"].append("timecodes presents : le format n'en veut plus")

    return nom, pbs


def main():
    args = [a.zfill(2) for a in sys.argv[1:]]
    fichiers = sorted(f for f in os.listdir(FICHES) if f.endswith(".md"))
    if args:
        fichiers = [f for f in fichiers if f[:2] in args]

    n_err = n_dou = n_prets = 0
    print()
    for f in fichiers:
        nom, pbs = verifier(os.path.join(FICHES, f))
        e, d = len(pbs["ERREUR"]), len(pbs["doute"])
        n_err += e
        n_dou += d
        if e == 0 and d == 0:
            n_prets += 1
            print("%-46s pret" % nom)
            continue
        print("%-46s %d erreur(s), %d doute(s)" % (nom, e, d))
        for p in pbs["ERREUR"]:
            print("   ERREUR   %s" % p)
        for p in pbs["doute"]:
            print("   doute    %s" % p)
        print()

    print("%d fiche(s) — %d erreur(s), %d doute(s), %d prete(s)"
          % (len(fichiers), n_err, n_dou, n_prets))
    print("Regles : connaissance-metier.md. Si une fiche le contredit, c'est la")
    print("fiche qui a tort.\n")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
