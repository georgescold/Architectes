#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Construit un PDF par fiche vidéo.

    python build.py            # toutes les fiches
    python build.py 03 07      # seulement ces épisodes

Chaîne : fiches/*.md  ->  (markdown)  ->  HTML + CSS print  ->  Chrome headless  ->  pdf/*.pdf
Les liens restent cliquables dans le PDF.
"""
import os, re, sys, subprocess, tempfile, shutil
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
FICHES = os.path.join(ROOT, "fiches")
OUT = os.path.join(ROOT, "pdf")

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium",
]

CSS = """
@page { size: A4; margin: 15mm 14mm 16mm 14mm; }
* { box-sizing: border-box; }
body {
  font-family: "Segoe UI", -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-size: 10.2pt; line-height: 1.5; color: #14181d; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
h1 {
  font-size: 19pt; line-height: 1.2; margin: 0 0 2mm; color: #0d1117;
  border-bottom: 2.5px solid #d4622a; padding-bottom: 3mm; letter-spacing: -0.2px;
}
h2 {
  font-size: 12.5pt; margin: 8mm 0 3mm; color: #0d1117;
  border-left: 3.5px solid #d4622a; padding-left: 3mm; page-break-after: avoid;
}
h3 { font-size: 10.8pt; margin: 5mm 0 2mm; color: #33404d; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
ul, ol { padding-left: 5mm; margin: 2mm 0; }
li { margin: 0.8mm 0; }
a { color: #1a5fb4; text-decoration: none; word-break: break-word; }
strong { color: #0d1117; }
code {
  font-family: "Cascadia Mono", Consolas, monospace; font-size: 8.8pt;
  background: #f1f3f5; padding: 0.4mm 1.2mm; border-radius: 2px; color: #b23a10;
}
pre {
  background: #f7f8fa; border: 1px solid #e3e6ea; border-left: 3px solid #8b97a3;
  padding: 3mm; border-radius: 3px; font-size: 8.5pt; line-height: 1.45;
  overflow-wrap: break-word; white-space: pre-wrap; page-break-inside: avoid;
}
pre code { background: none; padding: 0; color: #2b3138; }
blockquote {
  margin: 3mm 0; padding: 2.5mm 4mm; background: #fdf6f2;
  border-left: 3px solid #d4622a; color: #3d2b22; font-size: 9.6pt;
}
blockquote p { margin: 1mm 0; }
table {
  border-collapse: collapse; width: 100%; margin: 3mm 0; font-size: 9.1pt;
  page-break-inside: auto;
}
th {
  background: #eef1f4; text-align: left; font-weight: 600; color: #0d1117;
  border: 1px solid #d3d9df; padding: 1.6mm 2.2mm;
}
td { border: 1px solid #e1e6ea; padding: 1.6mm 2.2mm; vertical-align: top; }
tr { page-break-inside: avoid; }
tbody tr:nth-child(even) { background: #fafbfc; }
hr { border: none; border-top: 1px solid #e1e6ea; margin: 6mm 0; }
/* 1re colonne des tableaux de chapitrage : timecodes */
table td:first-child { white-space: nowrap; font-variant-numeric: tabular-nums; }
.footer {
  margin-top: 9mm; padding-top: 2.5mm; border-top: 1px solid #e1e6ea;
  font-size: 7.8pt; color: #7a848e;
}
"""

HTML = """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>{title}</title><style>{css}</style></head>
<body>{body}
<div class="footer">Essort Architectes — fiche de production vidéo · document interne ·
source&nbsp;: <code>{src}</code></div>
</body></html>"""


def find_chrome():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    w = shutil.which("chrome") or shutil.which("chromium") or shutil.which("google-chrome")
    if w:
        return w
    raise SystemExit("Chrome introuvable : ajoute son chemin dans CHROME_CANDIDATES.")


def to_pdf(md_path, chrome):
    name = os.path.splitext(os.path.basename(md_path))[0]
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"^#\s+(.+)$", text, re.M)
    title = m.group(1).strip() if m else name
    body = markdown.markdown(
        text, extensions=["tables", "fenced_code", "sane_lists", "attr_list"]
    )
    html = HTML.format(title=title, css=CSS, body=body, src=os.path.basename(md_path))

    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(tempfile.gettempdir(), f"essort_{name}.html")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(html)

    pdf = os.path.join(OUT, name + ".pdf")
    subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-sandbox",
         "--no-pdf-header-footer", "--print-to-pdf-no-header",
         f"--print-to-pdf={pdf}", "file:///" + tmp.replace("\\", "/")],
        capture_output=True, timeout=120,
    )
    os.remove(tmp)
    if not os.path.exists(pdf):
        return None
    return pdf


def main():
    chrome = find_chrome()
    wanted = sys.argv[1:]
    files = sorted(f for f in os.listdir(FICHES) if f.endswith(".md"))
    if wanted:
        files = [f for f in files if any(f.startswith(w) for w in wanted)]
    if not files:
        raise SystemExit("Aucune fiche trouvee dans " + FICHES)
    ok = 0
    for f in files:
        p = to_pdf(os.path.join(FICHES, f), chrome)
        if p:
            ok += 1
            print(f"OK   {os.path.basename(p)}  ({os.path.getsize(p)//1024} Ko)")
        else:
            print(f"FAIL {f}")
    print(f"\n{ok}/{len(files)} PDF generes dans {OUT}")


if __name__ == "__main__":
    main()
