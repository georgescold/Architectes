#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Controle systematique des fiches video.

    python verifier.py            # toutes les fiches
    python verifier.py 03 07      # seulement ces episodes

Cherche les erreurs connues, les affirmations non sourcees, les ruptures de
posture et les sections manquantes. Ne remplace pas la relecture : signale ce
qui merite un coup d'oeil.

Les regles viennent de connaissance-metier.md. En cas de contradiction entre
une fiche et ce document, c'est la fiche qui a tort.

Deux niveaux :
    ERREUR  -> faux ou interdit, a corriger avant tournage
    DOUTE   -> probablement un probleme, a verifier a l'oeil
"""
import os, re, sys, io

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
FICHES = os.path.join(ROOT, "fiches")

# Une occurrence precedee d'une de ces tournures est une CONSIGNE, pas une faute.
NEGATIONS = re.compile(
    r"(jamais|ne\s+dis\b|ne\s+pas\b|interdit|c'est\s+faux|ne\s+jamais|"
    r"erreur|proscri|banni|surtout\s+pas|eviter|évite|ne\s+concerne\s+pas|"
    r"ne\s+s'applique\s+pas|a\s+ne\s+plus)",
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
]

DOUTES = [
    (r"150\s*m²", "seuil de 150 m2 : ne vaut QUE pour les personnes physiques, "
                  "verifier que la fiche le precise"),
    (r"d[ée]ontologie", "le code de deontologie ne s'applique PAS aux architectes "
                        "d'interieur : verifier l'audience de l'episode"),
    (r"Archigraphie", "verifier que l'annee des donnees est annoncee : "
                      "revenus 2022, effectifs 2023"),
    (r"nos\s+clients\s+ont|un\s+cabinet\s+a\s+(?:obtenu|sign[ée])|résultats?\s+obtenus?",
     "aucun resultat client tant qu'il n'est pas documente et autorise"),
]

SECTIONS = [
    ("## CE QUE LE SPECTATEUR APPREND", "ce que le spectateur apprend"),
    ("## LES FAITS VÉRIFIÉS", "la liste des faits verifies avec sources"),
    ("## ORDRE CHRONOLOGIQUE", "le deroule chronologique"),
    ("## GARDE-FOUS", "les garde-fous de l'episode"),
]

MOMENTS = [
    (r"ANCRAGE ESSORT", "moment Essort 1, l'ancrage dans l'intro"),
    (r"PREUVE D'USAGE ESSORT|preuve d'usage Essort", "moment Essort 2, la preuve d'usage"),
    (r"LE PITCH", "moment Essort 3, le pitch aux deux tiers"),
]

# Nombres qui n'ont pas besoin d'etre sources a cote : annees, numeros de
# formulaire, numeros d'article, timecodes, seuils ERP deja documentes.
NEUTRES = re.compile(
    r"^(?:19|20)\d\d$|^13824$|^13404$|^431$|^121$|^132$|^10$|^17$|^19$|^13$|^32$"
)


def contexte(t, pos, avant=140, apres=90):
    return re.sub(r"\s+", " ", t[max(0, pos - avant):pos + apres])


def chiffres_sans_source(texte):
    """Un chiffre marquant doit avoir un lien dans la meme section."""
    suspects = []
    sections = re.split(r"\n(?=#{2,3}\s|\d\d:\d\d\s—)", texte)
    for s in sections:
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


def verifier(chemin):
    nom = os.path.basename(chemin)
    t = io.open(chemin, encoding="utf-8").read()
    pbs = {"ERREUR": [], "DOUTE": []}

    for motif, message in ERREURS:
        for m in re.finditer(motif, t, re.I):
            ctx = contexte(t, m.start())
            if NEGATIONS.search(ctx):
                continue  # c'est une consigne, pas une faute
            pbs["ERREUR"].append("%s\n              ...%s..." % (message, ctx[:150]))

    for motif, message in DOUTES:
        if re.search(motif, t, re.I):
            pbs["DOUTE"].append(message)

    for marqueur, message in SECTIONS:
        if marqueur not in t:
            pbs["ERREUR"].append("section absente : " + message)

    for motif, message in MOMENTS:
        if not re.search(motif, t):
            pbs["DOUTE"].append("absent : " + message)

    for val, titre in chiffres_sans_source(t)[:4]:
        pbs["DOUTE"].append("« %s » sans lien dans sa section (%s)" % (val, titre))

    m = re.search(r"Dur[ée]e\s+(\d+)[-–](\d+)\s*min", t)
    if m and int(m.group(1)) < 10:
        pbs["DOUTE"].append("duree annoncee sous 10 min, la cible est 10-15")

    return nom, pbs


def main():
    args = [a.zfill(2) for a in sys.argv[1:]]
    fichiers = sorted(f for f in os.listdir(FICHES) if f.endswith(".md"))
    if args:
        fichiers = [f for f in fichiers if f[:2] in args]

    n_err = n_dou = 0
    prets = []
    print()
    for f in fichiers:
        nom, pbs = verifier(os.path.join(FICHES, f))
        e, d = len(pbs["ERREUR"]), len(pbs["DOUTE"])
        n_err += e
        n_dou += d
        if e == 0 and d == 0:
            prets.append(nom)
            print("%-46s pret" % nom)
            continue
        print("%-46s %d erreur(s), %d doute(s)" % (nom, e, d))
        for p in pbs["ERREUR"]:
            print("   ERREUR   %s" % p)
        for p in pbs["DOUTE"]:
            print("   doute    %s" % p)
        print()

    print("%d fiche(s) — %d erreur(s), %d doute(s), %d prete(s)"
          % (len(fichiers), n_err, n_dou, len(prets)))
    print("Regles : connaissance-metier.md. Si une fiche le contredit, c'est la fiche")
    print("qui a tort.\n")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
