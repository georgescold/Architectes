from pathlib import Path
import json, base64, html, io, re, hashlib
from PIL import Image, ImageOps, ImageFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).parent
OUT = ROOT / '01-client-professionnel'
OUT.mkdir(exist_ok=True)
PROJECT = ROOT.parent.parent
NAVY='#263653'; INK='#142039'; MUTED='#65718A'; GOLD='#EBAE48'; LIGHT='#F1F4F8'; GREEN='#237864'; RED='#B44D46'
FONT='C:/Windows/Fonts/arial.ttf'; BOLD='C:/Windows/Fonts/arialbd.ttf'
pdfmetrics.registerFont(TTFont('Arial',FONT)); pdfmetrics.registerFont(TTFont('ArialBold',BOLD))
elements=[]; files={}; slides=[]; serial=0; current=None

def base(kind,x,y,w,h,step=0,**kw):
    global serial
    serial+=1
    d=dict(id=f'ep01-{serial}',type=kind,x=x,y=y,width=w,height=h,angle=0,strokeColor=INK,backgroundColor='transparent',fillStyle='solid',strokeWidth=2,strokeStyle='solid',roughness=0,opacity=100,groupIds=[],frameId=current['id'] if current else None,roundness=None,seed=serial*977,version=1,versionNonce=serial*13,isDeleted=False,boundElements=None,updated=1790000000000,link=None,locked=False,customData={'reveal':step})
    d.update(kw)
    current['objects'].append(d)
    return d

def rect(x,y,w,h,color=LIGHT,step=0,stroke=None):
    return base('rectangle',x,y,w,h,step,backgroundColor=color,strokeColor=stroke or color,roundness={'type':3})

def text(value,x,y,w,size=30,color=INK,step=0):
    font=ImageFont.truetype(FONT,size)
    lines=[]
    for para in value.split('\n'):
        line=''
        for word in para.split(' '):
            cand=(line+' '+word).strip()
            if font.getlength(cand)>w-8 and line:
                lines.append(line);line=word
            else:line=cand
        lines.append(line)
    s='\n'.join(lines)
    h=len(lines)*size*1.22
    return base('text',x,y,w,h,step,strokeColor=color,fontSize=size,fontFamily=2,text=s,originalText=s,textAlign='left',verticalAlign='top',containerId=None,lineHeight=1.22,autoResize=False)

def arrow(x,y,x2,y2,step=0,color=GOLD):
    return base('arrow',x,y,abs(x2-x),abs(y2-y),step,strokeColor=color,strokeWidth=4,points=[[0,0],[x2-x,y2-y]],startBinding=None,endBinding=None,startArrowhead=None,endArrowhead='arrow',elbowed=False)

def photo(path,x,y,w,h,step=0):
    im=ImageOps.fit(Image.open(path).convert('RGB'),(int(w*1.6),int(h*1.6)))
    b=io.BytesIO();im.save(b,format='JPEG',quality=90)
    raw=b.getvalue(); fid=hashlib.sha1(raw).hexdigest()
    files[fid]={'id':fid,'mimeType':'image/jpeg','dataURL':'data:image/jpeg;base64,'+base64.b64encode(raw).decode(),'created':1790000000000,'lastRetrieved':1790000000000}
    return base('image',x,y,w,h,step,fileId=fid,status='saved',scale=[1,1],crop=None)

def scene(title,time,notes,gesture,transition,tag='DÉMONSTRATION',source='Exemple pédagogique · Essort'):
    global current
    i=len(slides)
    current={'id':f'frame-{i+1}','title':title,'time':time,'notes':notes,'gesture':gesture,'transition':transition,'objects':[]}
    slides.append(current)
    rect(0,0,1440,810,'#FFFFFF')
    text('ESSORT / ARCHITECTES',60,32,700,18,NAVY)
    text(f'01   /   {i+1:02d}',1260,32,140,18,MUTED)
    text(tag.upper(),60,100,1260,17,MUTED)
    text(title,60,138,1300,44)
    rect(60,756,1320,2,'#E0E5ED')
    text(source,60,772,1120,14,MUTED)
    text(f'{i+1:02d} / 09',1300,772,100,14,MUTED)

def card(x,y,w,h,num,title,body,step=1,color=LIGHT):
    rect(x,y,w,h,color,step)
    text(num,x+26,y+25,w-52,20,GREEN,step)
    text(title,x+26,y+74,w-52,32,INK,step)
    text(body,x+26,y+h-114,w-52,24,MUTED,step)

restaurant=OUT/'assets/restaurant.jpg'
home=PROJECT/'site/frontend/public/cards/solution-realisations-pro-2026.jpg'
plans=PROJECT/'site/frontend/public/cards/solution-qualification-pro-2026.jpg'

scene('Votre prochain client n’habite peut-être pas son projet.', '00:00 - 00:45',
    ['Un restaurateur qui veut ouvrir dans trois mois et un particulier qui refait son salon peuvent chercher le même talent. Mais ils ne prennent pas leur décision pour les mêmes raisons.',
     'Si vous êtes architecte d’intérieur, seul ou en petite équipe, et que votre communication montre surtout du résidentiel, cette piste mérite d’être regardée.',
     'On va voir quelle cible choisir, comment rendre votre valeur évidente et comment tester sans refaire tout votre cabinet.'],
    'Commencer face caméra. Afficher la photo, puis révéler « UNE DATE À TENIR ». Marquer une pause.',
    'La différence n’est pas seulement le type de bâtiment. C’est la raison pour laquelle le client agit.',tag='LE CLIENT PROFESSIONNEL',source='Photographie réelle : Pexels 9685262 · Illustration, pas un projet client Essort')
photo(restaurant,855,254,525,458)
text('Un restaurant.\nUne ouverture.\nDes décisions à prendre.',60,280,740,50)
rect(60,510,715,114,NAVY,1);text('UNE DATE À TENIR',88,538,660,43,'#FFFFFF',1)
text('Une autre façon de présenter votre valeur.',60,658,750,26,MUTED,2)

scene('Même métier. Deux raisons de vous appeler.', '00:45 - 01:50',
    ['Chez un particulier : une façon de vivre, du confort, un lieu dans lequel se reconnaître. Ce sont de vrais enjeux.',
     'Pour un professionnel : recevoir des clients, organiser le travail, exploiter un espace. Le lieu sert aussi une activité.',
     'Ce n’est pas forcément un client plus riche ou plus rapide. L’idée utile : parler de l’usage du lieu avant de parler de votre style.'],
    'Révéler le particulier, puis le professionnel. Pointer « vivre » et « exercer ».',
    'Mais « les professionnels » est encore beaucoup trop large. Il faut choisir qui vous comprenez le mieux.')
photo(home,60,250,625,230,1);photo(restaurant,755,250,625,230,2)
text('MIEUX VIVRE CHEZ SOI',60,510,610,30,INK,1);text('FAIRE FONCTIONNER SON ACTIVITÉ',755,510,610,28,INK,2)
text('Confort · habitudes · identité',60,569,620,26,MUTED,1);text('Accueil · circulation · exploitation',755,569,620,26,MUTED,2)
rect(60,650,1320,65,LIGHT,3);text('Votre message commence par le problème que le lieu doit résoudre.',83,667,1280,27,NAVY,3)

scene('Choisissez un métier avant de choisir une publicité.', '01:50 - 03:00',
    ['Un restaurateur peut se demander comment faire circuler l’équipe et accueillir les clients. Une boutique pense présentation et parcours. Un cabinet de soins pense accueil et confidentialité.',
     'Choisissez une cible dont vous connaissez les contraintes, accessible dans votre zone et compatible avec vos compétences.',
     'Exemple : vous avez une expérience pertinente en commerces de proximité. Commencez par cette piste, plutôt que de parler à tout le monde.',
     'Certains locaux reçoivent du public : sécurité, accessibilité et autorisations demandent une compétence adaptée. Un beau portfolio résidentiel ne suffit pas à prouver cette maîtrise.'],
    'Faire apparaître les trois cartes. Entourer RESTAURANT au stylet comme choix d’exemple.',
    'Une fois la cible choisie, cherchez la question qui fait vraiment avancer son projet.')
card(60,268,416,306,'01','Restaurant','Circulation de l’équipe\nAccueil des clients',1)
card(512,268,416,306,'02','Boutique','Présentation des produits\nParcours dans le lieu',2)
card(964,268,416,306,'03','Cabinet de soins','Confidentialité\nAccueil et confort',3)
rect(60,622,1320,83,NAVY,4);text('Votre premier filtre : compétences + références + zone accessible.',87,649,1260,27,'#FFFFFF',4)

scene('Une date donne du sens aux décisions.', '03:00 - 04:05',
    ['Prenons un cas fictif : un restaurateur vise une ouverture dans trois mois. Ce délai est un souhait à étudier, pas une promesse que vous pouvez reprendre sans vérification.',
     'Votre rôle est de rendre visibles les dépendances : état du local, autorisations, choix, coordination et travaux.',
     'La question de départ devient : qu’est-ce qui doit être décidé, par qui, et dans quel ordre pour construire un calendrier réaliste ?',
     'L’esthétique reste importante. Vous montrez simplement que votre travail aide aussi à prendre de meilleures décisions.'],
    'Afficher la date, puis les trois étapes de gauche à droite. Pointer le point de blocage « autorisations ».',
    'Et si vous n’avez jamais livré un restaurant ? Voici ce que vous pouvez montrer honnêtement.',source='Cas fictif · Le délai de 3 mois illustre un souhait client, pas une durée garantie')
rect(60,260,315,378,NAVY,1);text('OBJECTIF CLIENT',87,292,260,20,'#FFFFFF',1);text('OUVRIR\nDANS\n3 MOIS',87,360,260,51,'#FFFFFF',1)
for i,(a,b) in enumerate([('Comprendre','Local · usages · enveloppe'),('Vérifier','Faisabilité · autorisations'),('Organiser','Choix · travaux · suivi')]):
    x=436+i*321
    card(x,325,302,272,f'0{i+1}',a,b,i+2)
    if i<2:arrow(x+302,459,x+320,459,i+3)
text('La date souhaitée se confronte à la faisabilité du projet.',435,656,900,28,MUTED,4)

scene('Pas de référence identique ? Montrez la preuve utile.', '04:05 - 05:10',
    ['Ne faites pas passer un appartement pour une référence de restaurant. Cherchez les compétences réellement transférables : circulation, matériaux, coordination, contraintes de chantier.',
     'Expliquez un cas avec trois éléments : la contrainte, ce que vous avez décidé et le résultat observable. Utilisez uniquement des images que vous avez le droit de montrer.',
     'Pour les compétences spécifiques qui vous manquent, identifiez un partenaire qualifié ou une formation. La communication rend une compétence visible ; elle ne la crée pas.',
     'C’est plus rassurant qu’une longue liste d’adjectifs comme “passionné”, “créatif”, “sur mesure”.'],
    'Révéler les trois blocs. Ajouter oralement un cas réel du cabinet, sans inventer de résultat client.',
    'Maintenant, mettons cette preuve dans un message que le professionnel comprend immédiatement.')
photo(plans,60,258,514,455)
for i,(a,b) in enumerate([('La contrainte','Ce qui rendait le projet difficile.'),('Votre décision','Le choix concret que vous avez fait.'),('Le résultat observable','Ce qui a changé dans le lieu.')]):
    y=266+i*148;rect(628,y,752,124,LIGHT,i+1);text(a,653,y+15,696,28,INK,i+1);text(b,653,y+64,696,24,MUTED,i+1)

scene('Passez du beau discours à une situation précise.', '05:10 - 06:15',
    ['“Des espaces qui vous ressemblent” peut être sincère, mais ne dit ni à qui vous parlez ni quel problème vous résolvez.',
     '“Vous ouvrez un restaurant à Lyon ? Pensons un lieu accueillant et adapté au service.” On comprend la personne, la situation et l’usage. Lyon n’est qu’un exemple.',
     'Sous cette phrase : une réalisation autorisée, la contrainte résolue, votre mission et une façon simple de parler du projet.',
     'Évitez les dates garanties, la hausse de chiffre d’affaires promise ou les compétences que vous ne possédez pas. La précision est déjà persuasive.'],
    'Garder le message précis masqué. Demander « Qui est concerné ? ». Révéler la deuxième carte et les trois repères.',
    'Une bonne phrase ne trouve pas les clients toute seule. Il lui faut une porte d’entrée.',source='Exemples de rédaction fictifs · Ni campagne diffusée, ni résultat client')
rect(60,267,580,314,LIGHT,1);text('TROP GÉNÉRAL',88,295,520,19,MUTED,1);text('« Des espaces qui\nvous ressemblent. »',88,366,515,39,INK,1)
arrow(666,420,742,420,2)
rect(780,267,600,314,NAVY,2);text('LE CLIENT SE RECONNAÎT',808,295,540,19,'#BCCDDF',2);text('« Vous ouvrez un\nrestaurant à Lyon ? »',808,352,540,38,'#FFFFFF',2);text('Un lieu accueillant et adapté au service.',808,477,536,25,'#FFFFFF',2)
text('UNE CIBLE',90,650,310,27,GREEN,3);text('UNE SITUATION',527,650,340,27,GREEN,3);text('UN USAGE',1005,650,310,27,GREEN,3)

scene('Reliez votre message à une vraie conversation.', '06:15 - 07:35',
    ['Premier chemin : votre réseau. Identifiez les personnes qui rencontrent déjà ces porteurs de projet : agents de locaux commerciaux, partenaires, contacts professionnels. Une relation se construit ; elle n’est pas garantie.',
     'Autre option : une publicité locale sur Facebook ou Instagram, avec un message et des images qui parlent à la cible. Le ciblage ne garantit pas de toucher uniquement des dirigeants ou des projets prêts à démarrer.',
     'La personne arrive sur une page claire ou sur un formulaire intégré à la publicité. On lui demande la nature du projet, la zone, le calendrier et une enveloppe indicative, puis on échange.',
     'Le chiffre à suivre, ce sont les conversations pertinentes puis les missions signées. Un formulaire rempli ne suffit pas.',
     'Si c’est la partie qui vous semble difficile à relier, envoyez-nous votre type de projet et votre zone sur Instagram. On pourra regarder avec vous par quoi commencer.'],
    'Révéler chaque étape. Tracer le parcours avec le pointeur. Le CTA se dit une seule fois, sans interrompre l’explication.',
    'Pour éviter de lancer cinq chantiers marketing à la fois, voici le premier test à préparer.')
for i,(a,b) in enumerate([('Se faire voir','Réseau OU publicité locale'),('Rassurer','Message + preuve pertinente'),('Qualifier','Projet · zone · calendrier'),('Échanger','Faisabilité + prochaine étape')]):
    x=60+i*338;card(x,286,306,290,f'0{i+1}',a,b,i+1)
    if i<3:arrow(x+307,430,x+332,430,i+2)
rect(60,640,1320,71,LIGHT,5);text('Mesurez : conversations pertinentes → propositions → missions signées.',85,661,1260,27,NAVY,5)

scene('Préparez un test. Pas une refonte complète.', '07:35 - 08:40',
    ['Première décision : une cible précise dans une zone que vous pouvez servir. Deuxième : un cas ou une preuve de compétence que vous pouvez présenter honnêtement.',
     'Troisième : une page ou un profil dont le message et la prise de contact sont clairs. Quatrième : un canal que vous avez les moyens de suivre.',
     'Avant de dépenser, définissez ce qu’est une demande pertinente et qui la rappelle. Fixez votre budget, une période d’observation et votre critère de poursuite.',
     'Vous cherchez à apprendre : est-ce que le message attire les bons projets ? Si rien n’est qualifié, revenez au message, à la diffusion et au traitement des demandes avant d’augmenter le budget.'],
    'Révéler les quatre choix et les cocher au stylet. Laisser quelques secondes pour une capture.',
    'Le but n’est pas de changer de métier. C’est de rendre une partie de votre valeur visible aux bonnes personnes.')
for i,(a,b) in enumerate([('1 cible','Restaurant de proximité dans votre zone'),('1 preuve','Une contrainte réellement résolue'),('1 message','La situation + l’usage du lieu'),('1 canal','Réseau ou publicité, avec suivi')]):
    x=60+(i%2)*677;y=267+(i//2)*202
    rect(x,y,643,174,LIGHT,i+1);text(a,x+27,y+22,580,35,INK,i+1);text(b,x+27,y+90,580,25,MUTED,i+1)

scene('Faites-vous choisir pour un problème précis.', '08:40 - 09:20',
    ['Le client professionnel n’est pas une solution magique. Mais il peut devenir une piste cohérente si vous connaissez son activité, prouvez votre compétence et organisez la prise de contact.',
     'Le guide gratuit rassemble les autres leviers d’acquisition : il est indiqué en description, une fois le lien de téléchargement vérifié.',
     'Si vous voulez regarder votre situation avec nous, écrivez-nous sur @essort.architectes. On parlera de vos projets recherchés, de votre zone et de ce qui bloque aujourd’hui.',
     'Et si votre compte Instagram montre déjà de beaux projets mais ne déclenche pas de messages, c’est exactement le sujet de l’épisode 05.'],
    'Revenir face caméra pour l’invitation. Garder le dernier écran 8 à 12 secondes au montage.',
    'Fin. Ajouter le lien de l’épisode 05 à l’écran de fin seulement lorsqu’il est publié.',tag='À VOUS DE JOUER',source='Essort · Architectes et architectes d’intérieur indépendants / équipes de 1 à 5')
rect(60,269,850,255,NAVY,1);text('Vous savez concevoir le lieu.\nMontrez pourquoi votre client\na besoin de vous.',92,305,790,40,'#FFFFFF',1)
photo(restaurant,968,269,412,439)
text('Une question sur votre cible ou votre acquisition ?',60,566,865,27,INK,2)
text('@essort.architectes',60,616,850,42,GREEN,2)
text('Ensuite : votre Instagram plaît… mais reçoit-il des projets ?',60,700,1270,24,MUTED,3)

# Native editable Excalidraw scene, with numbered frames and embedded photographs.
for i,s in enumerate(slides):
    ox=(i%3)*1600;oy=(i//3)*970
    for o in s['objects']:
        q=dict(o);q['x']+=ox;q['y']+=oy;elements.append(q)
    elements.append(dict(id=s['id'],type='frame',name=f"{i+1:02d} · {s['title']}",x=ox,y=oy,width=1440,height=810,angle=0,strokeColor='#CED4DF',backgroundColor='transparent',fillStyle='solid',strokeWidth=1,strokeStyle='solid',roughness=0,opacity=100,groupIds=[],frameId=None,roundness=None,seed=901+i,version=1,versionNonce=99+i,isDeleted=False,boundElements=None,updated=1790000000000,link=None,locked=False))
scene_file={'type':'excalidraw','version':2,'source':'https://excalidraw.com','elements':elements,'appState':{'viewBackgroundColor':'#E9EDF3','gridSize':None},'files':files}
(OUT/'01-client-professionnel.excalidraw').write_text(json.dumps(scene_file,ensure_ascii=False),encoding='utf8')

def svg(s):
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 810" aria-label="'+html.escape(s['title'],quote=True)+'">']
    for o in s['objects']:
        x,y,w,h=o['x'],o['y'],o['width'],o['height'];c=o['strokeColor'];step=o['customData']['reveal']
        out.append(f'<g data-step="{step}">')
        if o['type']=='rectangle':out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{o["backgroundColor"]}"/>')
        elif o['type']=='text':
            size=o['fontSize']
            out.append(f'<text fill="{c}" font-family="Arial, sans-serif" font-size="{size}">')
            for j,line in enumerate(o['text'].split('\n')):out.append(f'<tspan x="{x}" y="{y+size*.94+j*size*1.22}">{html.escape(line)}</tspan>')
            out.append('</text>')
        elif o['type']=='image':out.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{files[o["fileId"]]["dataURL"]}"/>')
        elif o['type']=='arrow':
            dx,dy=o['points'][1];out.append(f'<path d="M{x} {y} l{dx} {dy} m-12 -8 l12 8 l-12 8" fill="none" stroke="{c}" stroke-width="4"/>')
        out.append('</g>')
    return ''.join(out)+ '</svg>'

svgs=[svg(s) for s in slides]
payload=json.dumps([dict(title=s['title'],time=s['time'],svg=v,notes=s['notes'],gesture=s['gesture'],transition=s['transition']) for s,v in zip(slides,svgs)],ensure_ascii=False).replace('</',r'<\/')
template='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Essort — EP01 · Validation du pilote</title><style>
*{box-sizing:border-box}body{margin:0;background:#e9edf3;color:#142039;font:16px Arial,sans-serif}header{padding:18px 28px;display:flex;align-items:center;justify-content:space-between;gap:18px;background:white;border-bottom:1px solid #dce1e9}header b{letter-spacing:.14em}a{color:#263653}button,.link{border:1px solid #cdd5df;border-radius:8px;background:white;padding:10px 14px;color:#263653;font:inherit;cursor:pointer;text-decoration:none}button:hover,.link:hover{background:#eef2f6}main{max-width:1440px;margin:20px auto;padding:0 24px}#stage{position:relative;box-shadow:0 12px 45px #26365318;background:white;overflow:hidden}svg{width:100%;display:block}svg g{transition:opacity .22s}svg g.hidden{opacity:0;pointer-events:none}nav{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:16px 0}.muted{color:#65718a;font-size:14px}#notes{background:white;padding:24px 32px;border-radius:12px;line-height:1.6}#notes[hidden],#overview[hidden]{display:none}#overview{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:22px 0}#overview button{padding:10px;text-align:left;overflow:hidden}#overview svg{margin-bottom:10px}#overview small{font-size:13px}#counter{font-weight:bold}.record header,.record nav,.record #notes,.record #overview,.record .help{display:none!important}.record main{padding:0;margin:0;max-width:none;height:100vh;display:flex;align-items:center;justify-content:center;background:#111}.record #stage{width:min(100vw,177.7778vh)}#ink{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;touch-action:none}.drawing #ink{pointer-events:auto;cursor:crosshair}.drawing #draw{background:#f7dc9f}.help{line-height:1.6;margin:20px 0 30px}.primary{background:#263653;color:white}@media(max-width:800px){header{flex-wrap:wrap}#overview{grid-template-columns:1fr 1fr}main{padding:0 12px}nav{flex-wrap:wrap}}
</style><header><div><b>ESSORT</b> <span class="muted"> / EP01 · PILOTE À VALIDER</span></div><div><a class="link" href="01-client-professionnel.excalidraw" download>Excalidraw modifiable</a> <a class="link" href="fiche-tournage.pdf">Fiche de tournage</a></div></header><main><div id="stage"></div><nav><div><button onclick="prev()">← Retour</button> <button class="primary" onclick="next()">Révéler / avancer →</button></div><span id="counter"></span><div><button id="draw" onclick="toggleDraw()">Stylet D</button> <button onclick="clearInk()">Effacer C</button> <button onclick="all()">Tout afficher A</button> <button onclick="overview()">Chapitres O</button> <button onclick="notes()">Notes N</button> <button onclick="record()">Tourner F</button></div></nav><section id="overview" hidden></section><section id="notes" hidden></section><p class="muted help">Espace / → : révélation suivante · ← : retour · A : tout afficher · O : chapitrage · N : notes privées · D : dessiner · C : effacer · F : mode tournage · Échap : quitter.<br>Le tableau Excalidraw reste entièrement modifiable. Cette visionneuse séparée ajoute les révélations pour filmer. Les annotations au stylet sont temporaires. Durée visée : 9–10 minutes, à ajuster après répétition.</p></main><script>
const slides=PAYLOAD;let i=0,step=0,drawing=false;const stage=document.getElementById('stage');const max=()=>Math.max(...Array.from(stage.querySelectorAll('[data-step]'),e=>+e.dataset.step));function render(){stage.innerHTML=slides[i].svg+'<canvas id="ink" width="1440" height="810"></canvas>';stage.querySelectorAll('[data-step]').forEach(e=>e.classList.toggle('hidden',+e.dataset.step>step));document.getElementById('counter').textContent=`${i+1} / ${slides.length} · ${slides[i].time} · ${step}/${max()}`;document.getElementById('notes').innerHTML='<b>'+slides[i].title+'</b><ul>'+slides[i].notes.map(t=>'<li>'+t+'</li>').join('')+'</ul><p><b>À l’écran :</b> '+slides[i].gesture+'</p><p><b>Transition :</b> '+slides[i].transition+'</p>';setupInk()};function next(){if(step<max())step++;else if(i<slides.length-1){i++;step=0}render()}function prev(){if(step>0)step--;else if(i>0){i--;step=99}render()}function all(){step=max();render()}function jump(n){i=n;step=0;document.getElementById('overview').hidden=true;render()}function overview(){const o=document.getElementById('overview');o.hidden=!o.hidden;o.innerHTML=slides.map((s,n)=>'<button onclick="jump('+n+')">'+s.svg+'<small>'+String(n+1).padStart(2,'0')+' · '+s.time+'<br>'+s.title+'</small></button>').join('')}function notes(){const n=document.getElementById('notes');n.hidden=!n.hidden}async function record(){document.body.classList.toggle('record');if(document.body.classList.contains('record')){try{await document.documentElement.requestFullscreen()}catch(e){}}else if(document.fullscreenElement){await document.exitFullscreen()}}function toggleDraw(){drawing=!drawing;document.body.classList.toggle('drawing',drawing)}function clearInk(){const c=document.getElementById('ink');c.getContext('2d').clearRect(0,0,1440,810)}function setupInk(){const c=document.getElementById('ink'),ctx=c.getContext('2d');let down=false;ctx.strokeStyle='#d39726';ctx.lineWidth=4;ctx.lineCap='round';function point(e){const r=c.getBoundingClientRect();return[(e.clientX-r.left)*1440/r.width,(e.clientY-r.top)*810/r.height]}c.onpointerdown=e=>{down=true;c.setPointerCapture(e.pointerId);ctx.beginPath();ctx.moveTo(...point(e))};c.onpointermove=e=>{if(down){ctx.lineTo(...point(e));ctx.stroke()}};c.onpointerup=()=>down=false;c.onpointercancel=()=>down=false}document.addEventListener('keydown',e=>{if(e.key===' '||e.key==='ArrowRight'){e.preventDefault();next()}else if(e.key==='ArrowLeft')prev();else if(e.key.toLowerCase()==='a')all();else if(e.key.toLowerCase()==='n')notes();else if(e.key.toLowerCase()==='o')overview();else if(e.key.toLowerCase()==='f')record();else if(e.key.toLowerCase()==='d')toggleDraw();else if(e.key.toLowerCase()==='c')clearInk();else if(e.key==='Escape')document.body.classList.remove('record')});document.addEventListener('fullscreenchange',()=>{if(!document.fullscreenElement)document.body.classList.remove('record')});render();
</script></html>'''
(OUT/'presenter.html').write_text(template.replace('PAYLOAD',payload),encoding='utf8')
(OUT/'chapitres.json').write_text(json.dumps([{k:v for k,v in s.items() if k!='objects'} for s in slides],ensure_ascii=False,indent=2),encoding='utf8')

# Companion PDF: deliberately separate from the on-screen visuals.
c=canvas.Canvas(str(OUT/'fiche-tournage.pdf'),pagesize=(595.28,841.89));c.setTitle('Essort - EP01 - Fiche de tournage');page=0
def pdftext(t,x,y,w,size=11,color=INK,bold=False):
    font='ArialBold' if bold else 'Arial';c.setFont(font,size);c.setFillColor(HexColor(color));lines=[]
    for para in t.split('\n'):
        line=''
        for word in para.split():
            trial=(line+' '+word).strip()
            if pdfmetrics.stringWidth(trial,font,size)>w and line:lines.append(line);line=word
            else:line=trial
        lines.append(line)
    for line in lines:c.drawString(x,y,line);y-=size*1.45
    return y
def newpage(label):
    global page
    if page:c.showPage()
    page+=1
    pdftext('ESSORT / FICHE DE TOURNAGE',42,803,500,10,NAVY,True)
    pdftext(label,42,775,500,10,MUTED)
    c.setStrokeColor(HexColor('#DAE0E8'));c.line(42,47,553,47)
    pdftext(f'EP01 · Document de travail · Pilote à valider                                      {page:02d}',42,30,515,9,MUTED)

newpage('LE CLIENT PROFESSIONNEL / 9-10 MINUTES')
y=pdftext('Votre prochain client n’habite peut-être pas son projet.',42,719,510,27,INK,True)
y=pdftext('Pour architectes d’intérieur indépendants et équipes de 1 à 5 personnes.',42,y-15,510,12,MUTED)
y=pdftext('LA PROMESSE DE LA VIDÉO',42,y-25,510,10,GREEN,True)
y=pdftext('Choisir une cible professionnelle cohérente, expliquer sa valeur et préparer un premier test d’acquisition. Le contenu défend une piste à explorer, pas un marché miraculeux.',42,y-10,510,12)
y=pdftext('3 TITRES À TESTER',42,y-24,510,10,GREEN,True)
for t in ['Architectes d’intérieur : le client professionnel que votre portfolio oublie','Vous montrez des salons. Vos prochains clients ouvrent peut-être un restaurant.','Comment attirer des clients professionnels en architecture d’intérieur ?']:
    y=pdftext('• '+t,42,y-9,510,12)
y=pdftext('3 PISTES DE MINIATURE',42,y-23,510,10,GREEN,True)
for t in ['UNE DATE À TENIR — restaurant + repère de calendrier.', 'UN AUTRE CLIENT — intérieur résidentiel / restaurant en contraste.', 'AU-DELÀ DU SALON — photo de restaurant + visage, sans faux chiffre.']:
    y=pdftext('• '+t,42,y-7,510,11)
pdftext('Rythme : une idée par écran. Révéler les blocs au fil de la parole. Les notes donnent le fond ; ne pas les réciter mot à mot.',42,y-20,510,11,MUTED)

newpage('CHAPITRAGE / RÉPÉTITION')
y=pdftext('Le fil de la vidéo',42,723,510,24,INK,True)
for i,s in enumerate(slides):
    y=pdftext(f'{i+1:02d}  /  {s["time"]}',42,y-17,510,10,GREEN,True)
    y=pdftext(s['title'],42,y-5,510,13)
pdftext('Timecodes indicatifs, à remplacer par ceux du montage. Une hésitation ? Reprendre au début de l’écran : chaque séquence peut être montée séparément.',42,y-20,510,10,MUTED)

for j in range(0,len(slides),2):
    newpage('NOTES ORALES / '+str(j+1).zfill(2)+' ET '+str(min(j+2,9)).zfill(2))
    y=735
    for k in range(j,min(j+2,len(slides))):
        s=slides[k]
        y=pdftext(f'{k+1:02d} · {s["time"]}',42,y,510,10,GREEN,True)
        y=pdftext(s['title'],42,y-6,510,17,INK,True)
        for t in s['notes']:y=pdftext('• '+t,42,y-7,510,10.5)
        y=pdftext('À l’écran : '+s['gesture'],42,y-10,510,10,GREEN)
        y=pdftext('Transition : « '+s['transition']+' »',42,y-9,510,10,MUTED)
        y-=28
        if y<55:raise ValueError(f'PDF overflow on page {page}: {y}')

newpage('PRÉPARATION / SOURCES / PUBLICATION')
y=pdftext('Avant d’enregistrer',42,723,510,24,INK,True)
checks=['Ouvrir presenter.html. Espace avance, A montre tous les blocs, D active le stylet, F masque l’interface pour filmer. Les notes N restent privées et sont masquées en mode tournage.',
'Pour modifier : ouvrir le fichier .excalidraw dans Excalidraw via Ouvrir. Les textes, cartes, flèches et photographies sont des objets distincts. Neuf cadres numérotés donnent l’ordre.',
'Prévoir un cas réel que vous avez le droit de raconter pour la séquence 05. À défaut, garder l’exemple pédagogique et le nommer ainsi.',
'Vérifier le lien du guide avant de le mettre en description. Aucun lien de téléchargement non vérifié n’est proposé dans cette version.',
'Le lecteur HTML est un outil séparé : une modification du tableau Excalidraw ne s’y reporte pas automatiquement. Les annotations dessinées dans le lecteur sont temporaires.']
for t in checks:y=pdftext('• '+t,42,y-10,510,11)
y=pdftext('Ce qui a changé par rapport au brief initial',42,y-22,510,15,INK,True)
y=pdftext('Retrait de « ×2 », « zéro concurrence », de coûts publicitaires inférieurs et de délais de signature non documentés. Le cas d’ouverture à trois mois est fictif. Le raisonnement porte sur les usages et les décisions du client.',42,y-9,510,11)
y=pdftext('Images et liens',42,y-22,510,15,INK,True)
for t in ['Restaurant : https://www.pexels.com/photo/tables-and-chairs-in-a-restaurant-9685262/',
'Intérieur : Pexels vidéo 10135086, Abdullah | 4K. Plans : Pexels vidéo 10375427, RDNE Stock project. Posters déjà utilisés dans le site Essort.',
'Licence : https://www.pexels.com/license/ — photographies et captures vidéo réelles. Aucun visuel généré par IA. Images illustratives, aucun résultat client attribué.',
'Contact : https://instagram.com/essort.architectes · https://cal.com/essort/30min']:
    y=pdftext(t,42,y-8,510,9,MUTED)
if y<55:raise ValueError('Last PDF page overflow')
c.save()

md=['# EP01 — Fiche de tournage','', '**Statut : pilote à valider avant de décliner les 19 autres.**','', 'Durée indicative : 9–10 minutes. Les timecodes sont des repères de répétition.','']
for i,s in enumerate(slides):
    md += [f'## {i+1:02d}. {s["title"]}',s['time'],''] + ['- '+p for p in s['notes']] + ['', '**À l’écran :** '+s['gesture'],'','**Transition :** '+s['transition'],'']
(OUT/'script.md').write_text('\n'.join(md),encoding='utf8')
(OUT/'README.md').write_text('''# EP01 · Pilote à valider

- `presenter.html` : ouvrir dans un navigateur. Révélations à la flèche droite ou à la barre espace ; chapitrage avec O ; notes privées avec N ; stylet D ; mode tournage F.
- `01-client-professionnel.excalidraw` : tableau natif modifiable, neuf cadres numérotés. Ouvrir dans Excalidraw avec son menu Ouvrir. Photos intégrées : aucun fichier externe nécessaire.
- `fiche-tournage.pdf` : préparation, chapitrage, notes orales et sources.
- `script.md` : les notes dans un format facilement modifiable.

Les révélations et le stylet appartiennent au lecteur HTML, pas à une fonctionnalité native d’Excalidraw. Le HTML et le fichier Excalidraw sont générés depuis `../build_pilote.py` ; les modifications manuelles de l’un ne mettent pas à jour l’autre.

Les photographies sont illustratives et proviennent de Pexels (restaurant 9685262 ; vidéos 10135086 et 10375427). Licence : https://www.pexels.com/license/. Aucune image générée par IA. Aucun projet photographié n’est présenté comme un client Essort. Les fichiers ne doivent pas être revendus comme photographies brutes.

Les exemples ne sont pas des résultats clients. Le brief initial reste dans `../../fiches` pour traçabilité ; ce pilote corrige les affirmations non démontrées sur le doublement des honoraires, l’absence de concurrence et les délais de signature.
''',encoding='utf8')
print(json.dumps({'frames':len(slides),'elements':len(elements),'embedded_images':len(files),'pdf_pages':page,'directory':str(OUT)},ensure_ascii=False))
