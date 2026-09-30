#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Brochure de proposition + mail d'accompagnement, après le premier appel avec un cabinet.

    python agence/offre/brochure/generer-brochure.py <fiche-client.json>

Deux sources de données, dans le dépôt PRIVÉ (agence/prospection/listes/fiches-appel/propositions/) :
  - _socle-essort.json : tout ce qui est commun à toutes les brochures (prestations, histoire,
    clients références, questions-réponses, réassurance, émetteurs) ;
  - la fiche du cabinet (AAAA-MM-JJ-prenom-nom-proposition-essort.json) : seulement ce qui vient
    de l'appel (nom, zone, seuil de budget, prix annoncé, budget de l'essai, dates…). Elle peut
    aussi remplacer n'importe quel champ du socle (un texte, une question, une prestation).
Modèle vierge : _modele-client.json. Mode d'emploi : README.md de ce dossier.

Les textes peuvent contenir des variables Jinja, remplacées à la génération :
{{ client.prenom }}, {{ zone.nom }}, {{ zone.de }}, {{ zone.villes }}, {{ euros(seuil_travaux) }},
{{ essai.jours }}… Une valeur « À REMPLIR » bloque la génération.

Sorties, à côté de la fiche : le PDF (…-proposition-essort.pdf) et le mail (…-mail.txt).

⚠️ Les fiches, le socle et les PDF nominatifs ne vont JAMAIS dans ce dépôt public.

Chaîne : Jinja2 -> HTML + CSS d'impression -> Chrome headless -> PDF, comme les
conditions de l'essai (../generer-pdf-conditions.py).
"""
import copy, json, math, os, re, subprocess, sys, tempfile
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup
from PIL import Image

ICI = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.normpath(os.path.join(ICI, "..", "..", "site", "frontend", "public"))
LOGO = os.path.normpath(os.path.join(ICI, "..", "..", "site", "frontend", "src", "Group.svg"))
OFFRE = os.path.normpath(os.path.join(ICI, "..", "offre-actuelle.md"))
SOCLE = "_socle-essort.json"
A_REMPLIR = "À REMPLIR"

# Visuels du site (Pexels, usage commercial libre : voir site/frontend/public/cards/README.md).
IMAGES = {
    "couverture": "cards/villa-signature-pro-2026.webp",
    "methode": "cards/interieur-perspective-pro-2026.webp",
    # Portraits avec de l'air au-dessus de la tête : equipe-*.jpg sont recadrées au ras des
    # cheveux, et la brochure leur coupait le haut du crâne (remarque de Loys, 30/09/2026).
    "equipe_loys": "fondateur-portrait.jpg",
    # (fichier, recadrage en fractions gauche, haut, droite, bas) : Enzo resserré pour que
    # son visage ait la même échelle que celui de Loys.
    "equipe_enzo": ("auteur-enzo.jpg", (0.165, 0.2275, 0.835, 1.0)),
}

CHROMES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium",
]


def euros(montant):
    """20000 -> « 20 000 € », avec les espaces insécables de la typographie française."""
    entier = int(round(montant))
    return f"{entier:,}".replace(",", "\u202f") + "\u00a0€"


def euros_mail(montant):
    """Pour le mail en texte brut : des espaces ordinaires, que toutes les messageries affichent."""
    return f"{int(round(montant)):,}".replace(",", " ") + " €"


def mois_couverts(prix_mensuel):
    def rendu(honoraires):
        mois = honoraires / prix_mensuel
        if mois < 1:
            return "moins d'un mois"
        entiers = math.floor(mois)
        return f"{entiers} mois" if mois == entiers else f"plus de {entiers} mois"
    return rendu


def prix_de_l_offre():
    """Le prix mensuel écrit dans offre-actuelle.md, qui fait foi."""
    texte = open(OFFRE, encoding="utf-8").read()
    m = re.search(r"([\d\s\u202f\u00a0]+)\s*€ par mois", texte)
    return int(re.sub(r"\D", "", m.group(1))) if m else None


def fusionner(base, ajout):
    """La fiche du cabinet complète le socle : un dictionnaire se fusionne champ par champ,
    tout le reste (texte, nombre, liste) remplace la valeur du socle."""
    for cle, valeur in ajout.items():
        if isinstance(valeur, dict) and isinstance(base.get(cle), dict):
            fusionner(base[cle], valeur)
        else:
            base[cle] = copy.deepcopy(valeur)
    return base


def rendre_variables(valeur, contexte, env):
    """Remplace les {{ … }} des textes par les valeurs de la fiche."""
    if isinstance(valeur, str):
        return env.from_string(valeur).render(**contexte) if ("{{" in valeur or "{%" in valeur) else valeur
    if isinstance(valeur, list):
        return [rendre_variables(v, contexte, env) for v in valeur]
    if isinstance(valeur, dict):
        return {k: rendre_variables(v, contexte, env) for k, v in valeur.items()}
    return valeur


def a_remplir(valeur, chemin=""):
    """Chemins des champs encore marqués « À REMPLIR »."""
    if isinstance(valeur, str):
        return [chemin] if A_REMPLIR in valeur else []
    if isinstance(valeur, list):
        return [c for i, v in enumerate(valeur) for c in a_remplir(v, f"{chemin}[{i}]")]
    if isinstance(valeur, dict):
        return [c for k, v in valeur.items() for c in a_remplir(v, f"{chemin}.{k}" if chemin else k)]
    return []


def typographie(html):
    """Espaces insécables de la typographie française, dans le TEXTE visible seulement : ni le
    CSS, ni les balises, ni le dessin SVG du logo (ses coordonnées ressemblent à des montants,
    et une première version les a abîmées). Sans ces espaces, un « ? » ou un « : » peut se
    retrouver seul en début de ligne, et « 20 000 € » se couper en deux."""
    tete, _, corps = html.partition("</style>")
    morceaux = re.split(r"(<svg.*?</svg>|<[^>]+>)", corps, flags=re.S)
    for i in range(0, len(morceaux), 2):  # les indices pairs sont du texte, les impairs du balisage
        texte = morceaux[i]
        for avant, apres in ((" ?", "\u202f?"), (" !", "\u202f!"), (" ;", "\u202f;"),
                             (" :", "\u00a0:"), ("« ", "«\u00a0"), (" »", "\u00a0»"),
                             ("e-mail", "e\u2011mail")):
            texte = texte.replace(avant, apres)
        texte = re.sub(r"(\d) (?=\d{3}\b)", lambda m: m.group(1) + "\u202f", texte)
        texte = re.sub(r"(\d) €", lambda m: m.group(1) + "\u00a0€", texte)
        texte = re.sub(r"(\d) (?=h\b)", lambda m: m.group(1) + "\u00a0", texte)  # « 4 h » ne se coupe pas
        morceaux[i] = texte
    return tete + "</style>" + "".join(morceaux)


def uri(chemin):
    return "file:///" + chemin.replace("\\", "/")


def charger(source):
    """Socle + fiche du cabinet, émetteur résolu, variables remplacées, champs vérifiés."""
    dossier = os.path.dirname(source)
    socle_chemin = os.path.join(dossier, SOCLE)
    if not os.path.exists(socle_chemin):
        raise SystemExit(f"Socle introuvable : {socle_chemin}")
    donnees = fusionner(json.load(open(socle_chemin, encoding="utf-8")),
                        json.load(open(source, encoding="utf-8")))
    donnees = {k: v for k, v in donnees.items() if not k.startswith("_")}  # notes et aides

    # L'émetteur est celui qui a mené l'appel : c'est son nom et son SIRET qui figurent en pied
    # de page (Essort est un nom commercial, pas une société).
    emetteurs = donnees.pop("emetteurs", {})
    if isinstance(donnees.get("emetteur"), str):
        cle = donnees["emetteur"]
        if cle not in emetteurs:
            raise SystemExit(f"Émetteur inconnu : {cle!r} (connus : {', '.join(emetteurs)})")
        donnees["emetteur"] = emetteurs[cle]
    donnees["emetteur"].setdefault("role", "Cofondateur")

    manquants = a_remplir(donnees)
    if manquants:
        raise SystemExit("Champs encore « À REMPLIR » :\n  - " + "\n  - ".join(manquants))

    env_texte = Environment()
    env_texte.globals.update(euros=euros)
    for _ in range(2):  # deux passes : une variable peut en contenir une autre
        donnees = rendre_variables(donnees, dict(donnees, euros=euros), env_texte)

    # Logos des références : chemins relatifs au dossier des fiches (dépôt privé).
    for ref in donnees.get("references", []):
        if ref.get("logo"):
            ref["logo"] = uri(os.path.join(dossier, ref["logo"]))
    return donnees


def ecrire_mail(donnees, source, pdf):
    env = Environment(loader=FileSystemLoader(ICI), keep_trailing_newline=True)
    env.globals.update(euros=euros_mail)
    texte = env.get_template("mail.txt.j2").render(**donnees, piece_jointe=os.path.basename(pdf))
    sortie = re.sub(r"-proposition-essort$", "", os.path.splitext(source)[0]) + "-mail.txt"
    open(sortie, "w", encoding="utf-8").write(texte)
    return sortie


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    source = os.path.abspath(sys.argv[1])
    donnees = charger(source)

    # L'offre fait foi pour le prix : un écart avec le prix annoncé au cabinet est signalé.
    reference = prix_de_l_offre()
    if reference and donnees["prix_mensuel"] != reference:
        print(f"⚠️  Prix de la brochure : {donnees['prix_mensuel']} €/mois ; "
              f"offre-actuelle.md : {reference} €/mois. Vérifier que c'est voulu.")

    logo = open(LOGO, encoding="utf-8").read()
    logo = re.sub(r'\s(width|height)="[^"]*"', "", logo, count=2)
    env = Environment(loader=FileSystemLoader(ICI), autoescape=select_autoescape(["html", "j2"]))
    env.globals.update(euros=euros, mois_couverts=mois_couverts(donnees["prix_mensuel"]))
    page = env.get_template("brochure.html.j2").render(
        **donnees,
        logo=Markup(logo),  # le SVG du logo est du HTML sûr : sans Markup, il s'afficherait en texte
        images={cle: uri(os.path.join(PUBLIC, chemin if isinstance(chemin, str) else chemin[0]))
                for cle, chemin in IMAGES.items()},
    )

    sortie = os.path.splitext(source)[0] + ".pdf"
    chrome = next((c for c in CHROMES if os.path.exists(c)), None)
    if not chrome:
        raise SystemExit("Chrome ou Edge introuvable.")
    with tempfile.TemporaryDirectory() as tmp:
        # Photos réduites à leur taille d'impression : en pleine définition, le PDF pesait
        # 9 Mo, trop lourd pour une pièce jointe.
        for cle, chemin in IMAGES.items():
            chemin, cadre = (chemin, None) if isinstance(chemin, str) else chemin
            reduite = os.path.join(tmp, cle + ".jpg")
            im = Image.open(os.path.join(PUBLIC, chemin)).convert("RGB")
            if cadre:
                l, h = im.size
                im = im.crop((int(cadre[0] * l), int(cadre[1] * h), int(cadre[2] * l), int(cadre[3] * h)))
            im.thumbnail((1400, 1400))
            im.save(reduite, "JPEG", quality=82, optimize=True)
            page = page.replace(uri(os.path.join(PUBLIC, chemin)), uri(reduite))
        html = os.path.join(tmp, "brochure.html")
        open(html, "w", encoding="utf-8").write(typographie(page))
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--allow-file-access-from-files", "--virtual-time-budget=20000",
                        f"--print-to-pdf={sortie}", uri(html)],
                       check=True, capture_output=True)
    print("PDF  :", sortie)
    print("Mail :", ecrire_mail(donnees, source, sortie))


if __name__ == "__main__":
    main()
