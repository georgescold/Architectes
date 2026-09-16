"""Canevas continu pour commenter à l'écran ; aucun cadre de diapositive."""
from pathlib import Path
import json,html,base64,io,hashlib
from PIL import Image,ImageOps,ImageFont
R=Path(__file__).parent; O=R/'01-client-professionnel'; P=R.parent.parent
E=[];F={};n=0;Y=0
BLACK='#18202b';GRAY='#68707c';BLUE='#263653';GREEN='#c3f4ce';RED='#e06e67';GOLD='#e4b350'
def obj(t,x,y,w,h,**kw):
 global n
 n+=1
 d=dict(id=f'board-{n}',type=t,x=x,y=y+Y,width=w,height=h,angle=0,strokeColor=BLACK,backgroundColor='transparent',fillStyle='solid',strokeWidth=3,strokeStyle='solid',roughness=1,opacity=100,groupIds=[],frameId=None,roundness=None,seed=n*701,version=1,versionNonce=n*911,isDeleted=False,boundElements=None,updated=1790000000000,link=None,locked=False)
 d.update(kw);E.append(d);return d
def txt(s,x,y,w,size=56,c=BLACK):
 f=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',size);lines=[]
 for p in s.split('\n'):
  line=''
  for word in p.split(' '):
   trial=(line+' '+word).strip()
   if f.getlength(trial)>w-5 and line:lines.append(line);line=word
   else:line=trial
  lines.append(line)
 s='\n'.join(lines)
 return obj('text',x,y,w,len(lines)*size*1.25,strokeColor=c,fontSize=size,fontFamily=2,text=s,originalText=s,textAlign='left',verticalAlign='top',containerId=None,lineHeight=1.25,autoResize=False)
def box(x,y,w,h,c):return obj('rectangle',x,y,w,h,strokeColor=c,backgroundColor=c,roughness=0,strokeWidth=0)
def arrow(x,y,x2,y2,c=BLACK):return obj('arrow',x,y,abs(x2-x),abs(y2-y),strokeColor=c,strokeWidth=5,points=[[0,0],[x2-x,y2-y]],startBinding=None,endBinding=None,startArrowhead=None,endArrowhead='arrow',elbowed=False)
def line(x,y,x2,y2,c=RED):return obj('line',x,y,abs(x2-x),abs(y2-y),strokeColor=c,strokeWidth=7,points=[[0,0],[x2-x,y2-y]])
def pic(p,x,y,w,h):
 im=ImageOps.fit(Image.open(p).convert('RGB'),(int(w),int(h)));b=io.BytesIO();im.save(b,'JPEG',quality=91);r=b.getvalue();i=hashlib.sha1(r).hexdigest();F[i]=dict(id=i,mimeType='image/jpeg',created=1790000000000,dataURL='data:image/jpeg;base64,'+base64.b64encode(r).decode());return obj('image',x,y,w,h,fileId=i,status='saved',scale=[1,1],crop=None)
def heading(num,s):
 txt(f'{num:02d}',110,20,160,42,GRAY);txt(s,110,110,2140,96)
def aside(s,y):txt(s,140,y,2080,44,GRAY)
restaurant=O/'assets/restaurant.jpg';home=P/'site/frontend/public/cards/solution-realisations-pro-2026.jpg';plans=P/'site/frontend/public/cards/solution-qualification-pro-2026.jpg'
bookmarks=[]
def zone(i,title,height=1450):
 global Y
 Y=sum(b['h']+330 for b in bookmarks)
 bookmarks.append(dict(title=title,x=0,y=Y-30,w=2400,h=height))
 heading(i,title)

zone(1,'Votre prochain client\nn’habite peut-être PAS son projet.',1550)
box(109,238,2040,116,GREEN);txt('n’habite peut-être PAS son projet.',110,230,2140,96)
pic(home,130,455,805,530);pic(restaurant,1240,455,970,660)
txt('Le lieu où l’on vit.',130,1040,850,54);txt('Le lieu qui fait vivre\nune activité.',1240,1160,990,62)
arrow(990,710,1180,710);txt('autre client,\nautre enjeu',975,850,255,32,GRAY)
aside('Architectes d’intérieur · indépendants et petites équipes',1440)

zone(2,'Vous dessinez un lieu.\nVotre client cherche autre chose.',1350)
txt('PARTICULIER',140,415,900,48,GRAY);txt('PROFESSIONNEL',1290,415,990,48,GRAY)
txt('« Je veux me sentir\nbien chez moi. »',140,535,890,74)
txt('« Je dois accueillir\nmes clients ici. »',1290,535,990,74)
line(1135,425,1135,980,'#cfd4da')
txt('Confort\nHabitudes\nIdentité',140,855,880,56)
txt('Accueil\nCirculation\nExploitation',1290,855,990,56)
box(120,1170,2110,95,GREEN);txt('Parlez de l’usage avant de parler de votre style.',144,1175,2040,65)

zone(3,'« Les professionnels »\nest encore une cible trop large.',1500)
txt('RESTAURANT',130,505,700,68);txt('BOUTIQUE',900,505,670,68);txt('CABINET\nDE SOINS',1650,505,650,68)
txt('Circulation de l’équipe\nAccueil des clients',130,737,680,47)
txt('Produits visibles\nParcours dans le lieu',900,737,670,47)
txt('Confidentialité\nAccueil et confort',1650,737,640,47)
obj('ellipse',90,450,750,210,strokeColor=RED,strokeWidth=6)
arrow(450,925,450,1140,RED);txt('Une seule cible pour commencer.',130,1200,2100,74)
aside('Choisir selon vos compétences, vos références et votre zone.',1360)

zone(4,'La question qui change la conversation :\n« Qu’est-ce qui doit être prêt, et quand ? »',1680)
box(120,427,1050,153,GREEN);txt('OUVRIR DANS 3 MOIS',145,450,1020,82)
txt('Souhait du client.\nÀ confronter à la faisabilité.',1320,445,925,49,GRAY)
arrow(420,665,420,815)
txt('Comprendre',130,890,650,65);txt('Vérifier',940,890,650,65);txt('Organiser',1720,890,600,65)
arrow(710,945,880,945);arrow(1450,945,1650,945)
txt('Le local\nLes usages\nL’enveloppe',130,1050,670,52)
txt('La faisabilité\nLes autorisations',940,1050,675,52)
txt('Les choix\nLes travaux\nLe suivi',1720,1050,580,52)
aside('Cas fictif : ce calendrier n’est pas une promesse de délai.',1530)

zone(5,'Votre preuve ≠ une liste d’adjectifs.',1490)
txt('« Passionné. Créatif. Sur mesure. »',135,330,2040,65,GRAY);line(130,377,1360,360)
pic(plans,135,550,950,660)
txt('1. La contrainte',1250,575,1040,67);txt('Ce qui rendait le projet difficile.',1250,675,1020,42,GRAY)
txt('2. Votre décision',1250,855,1040,67);txt('Le choix concret que vous avez fait.',1250,955,1020,42,GRAY)
txt('3. Le résultat observable',1250,1130,1060,61)
aside('Montrez une compétence réelle. Ne vous inventez pas une référence.',1360)

zone(6,'Le même savoir-faire.\nUn message que le client comprend.',1560)
txt('« Des espaces qui vous ressemblent. »',130,405,2110,70,GRAY)
line(130,459,1680,443)
arrow(440,550,440,700)
box(119,764,2110,216,GREEN)
txt('« Vous ouvrez un restaurant à Lyon ? »',145,790,2070,84)
txt('Un lieu accueillant et adapté au service.',145,1050,2110,64)
txt('UNE CIBLE',130,1260,650,57);txt('UNE SITUATION',900,1260,800,57);txt('UN USAGE',1770,1260,520,57)
aside('Exemple fictif de rédaction. La zone doit être celle que vous desservez.',1450)

zone(7,'Un message clair ne suffit pas.\nIl faut organiser la suite.',1730)
txt('Réseau',140,440,680,80);txt('OU',900,455,300,58,GRAY);txt('Publicité locale',1300,440,1000,80)
arrow(440,600,860,785);arrow(1750,600,1200,785)
txt('Message + preuve',690,840,1250,85)
arrow(1150,975,1150,1090)
txt('Projet · zone · calendrier',510,1140,1720,70)
arrow(1150,1265,1150,1370)
box(580,1420,1160,130,GREEN);txt('Une vraie conversation',620,1440,1100,77)
aside('Un formulaire rempli n’est pas encore une mission signée.',1610)

zone(8,'Votre premier test tient en 4 choix.',1300)
for i,(a,b) in enumerate([('1 cible','Un métier, dans votre zone.'),('1 preuve','Une contrainte réellement résolue.'),('1 message','Une situation que le client reconnaît.'),('1 canal','Un moyen de contact, avec un suivi.')]):
 y=355+i*208
 obj('rectangle',135,y+8,70,70,strokeWidth=4)
 txt(a,255,y,690,81);txt(b,1060,y+19,1200,56,GRAY)
aside('Décidez du budget et du suivi avant de lancer.',1190)

zone(9,'Faites-vous choisir\npour un problème précis.',1450)
box(110,235,1635,125,GREEN);txt('pour un problème précis.',110,230,2140,96)
pic(restaurant,1540,495,700,690)
txt('Une question sur votre cible\nou votre acquisition ?',135,550,1270,65)
txt('@essort.architectes',135,840,1320,89,BLUE)
txt('On en parle à partir de vos projets,\nde votre zone et de ce qui bloque.',135,1030,1270,46,GRAY)
aside('Ensuite : votre Instagram plaît… mais reçoit-il des projets ?',1320)

# Native Excalidraw: one continuous board, zero frames.
(O/'01-client-professionnel.excalidraw').write_text(json.dumps(dict(type='excalidraw',version=2,source='https://excalidraw.com',elements=E,files=F,appState={'viewBackgroundColor':'#ffffff','gridSize':None}),ensure_ascii=False),encoding='utf8')
def svg():
 out=[]
 for e in E:
  x,y,w,h=e['x'],e['y'],e['width'],e['height'];c=e['strokeColor'];t=e['type']
  if t=='text':
   s=e['fontSize'];out.append(f'<text font-family="Arial,sans-serif" font-size="{s}" fill="{c}">')
   for j,l in enumerate(e['text'].split('\n')):out.append(f'<tspan x="{x}" y="{y+s*.95+j*s*1.25}">{html.escape(l)}</tspan>')
   out.append('</text>')
  elif t=='image':out.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{F[e["fileId"]]["dataURL"]}"/>')
  elif t=='rectangle':out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{e["backgroundColor"] if e["backgroundColor"]!="transparent" else "none"}" stroke="{c}" stroke-width="{e["strokeWidth"]}"/>')
  elif t=='ellipse':out.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="none" stroke="{c}" stroke-width="6"/>')
  else:
   dx,dy=e['points'][1];marker=' marker-end="url(#arr)"' if t=='arrow' else ''
   out.append(f'<path d="M{x} {y} l{dx} {dy}" fill="none" stroke="{c}" stroke-width="{e["strokeWidth"]}"{marker}/>')
 return ''.join(out)
notes=json.loads((O/'chapitres.json').read_text(encoding='utf8'))
data=json.dumps({'marks':bookmarks,'notes':notes},ensure_ascii=False)
template='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Essort · tableau de tournage EP01</title><style>*{box-sizing:border-box}body{margin:0;background:white;color:#18202b;font:14px Arial}#board{position:fixed;inset:0;width:100%;height:100%;touch-action:none;cursor:grab}#board.pen{cursor:crosshair}#toolbar{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);display:flex;gap:5px;align-items:center;background:#fffefc;padding:8px;border:1px solid #d6d9dd;border-radius:14px;box-shadow:0 8px 35px #0001;white-space:nowrap}button,a{font:inherit;background:white;color:#263653;border:0;padding:9px 12px;border-radius:7px;text-decoration:none;cursor:pointer}button:hover,a:hover{background:#eef1f4}#hint{position:fixed;top:16px;left:20px;color:#7b8188;font-size:12px}#panel{position:fixed;right:16px;top:45px;bottom:85px;overflow:auto;width:390px;background:#fff;padding:24px;box-shadow:0 5px 35px #0002;border:1px solid #ddd;line-height:1.6}#panel[hidden]{display:none}.record #toolbar,.record #hint,.record #panel{display:none!important}#toolbar .active{background:#fce1bc}@media(max-width:800px){#toolbar{max-width:98vw;overflow:auto;left:1vw;transform:none}}</style><svg id="board" xmlns="http://www.w3.org/2000/svg"><defs><marker id="arr" markerWidth="12" markerHeight="12" refX="9" refY="4" orient="auto"><path d="M0,0 L9,4 L0,8" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs>SVG<g id="ink"></g></svg><div id="hint">ESSORT / TABLEAU CONTINU · glisser pour déplacer · molette pour parcourir · Ctrl + molette pour zoomer</div><div id="toolbar"><button onclick="go(index-1)">←</button><button onclick="go(index+1)">→</button><button onclick="chapters()">Repères</button><button onclick="overview()">Vue globale</button><button onclick="zoom(.8)">+</button><button onclick="zoom(1.25)">−</button><button id="pen" onclick="pen()">Stylet D</button><button onclick="undo()">Annuler</button><button onclick="showNotes()">Notes N</button><button onclick="record()">Filmer F</button><a href="01-client-professionnel.excalidraw" download>↓ Excalidraw</a></div><aside id="panel" hidden></aside><script>
const data=DATA,marks=data.marks,board=document.getElementById('board'),panel=document.getElementById('panel');let index=0,v={x:0,y:0,w:2400,h:1500},drawing=false,drag=null,anim=0;const ratio=()=>innerWidth/innerHeight;function set(){board.setAttribute('viewBox',`${v.x} ${v.y} ${v.w} ${v.h}`)}function fit(b){let w=Math.max(b.w,b.h*ratio()),h=w/ratio();return{x:b.x-(w-b.w)/2,y:b.y-(h-b.h)/2,w,h}}function move(to,smooth=true){cancelAnimationFrame(anim);const start={...v},t0=performance.now();function tick(t){let p=Math.min(1,(t-t0)/600);p=1-Math.pow(1-p,3);for(const k of ['x','y','w','h'])v[k]=start[k]+(to[k]-start[k])*p;set();if(p<1)anim=requestAnimationFrame(tick)}if(smooth)anim=requestAnimationFrame(tick);else{v=to;set()}}function go(n){index=Math.max(0,Math.min(8,n));move(fit(marks[index]));panel.hidden=true}function overview(){move(fit({x:0,y:0,w:2400,h:marks[8].y+marks[8].h+90}))}function zoom(f){const w=v.w*f,h=v.h*f;move({x:v.x+(v.w-w)/2,y:v.y+(v.h-h)/2,w,h},false)}function point(e){const r=board.getBoundingClientRect();return{x:v.x+(e.clientX-r.left)*v.w/r.width,y:v.y+(e.clientY-r.top)*v.h/r.height}}function pen(){drawing=!drawing;board.classList.toggle('pen',drawing);document.getElementById('pen').classList.toggle('active',drawing)}function undo(){document.getElementById('ink').lastElementChild?.remove()}function chapters(){panel.hidden=false;panel.innerHTML='<h3>Repères dans le tableau</h3>'+marks.map((b,i)=>`<p><button onclick="go(${i})">${i+1}. ${b.title.replaceAll('\\n',' ')}</button></p>`).join('')}function showNotes(){if(!panel.hidden){panel.hidden=true;return}let mid=v.y+v.h/2;index=marks.reduce((best,b,i)=>Math.abs(b.y+b.h/2-mid)<Math.abs(marks[best].y+marks[best].h/2-mid)?i:best,0);const n=data.notes[index];panel.hidden=false;panel.innerHTML='<h3>'+marks[index].title+'</h3><ul>'+n.notes.map(t=>'<li>'+t+'</li>').join('')+'</ul><p><b>Transition :</b> '+n.transition+'</p>'}async function record(){document.body.classList.toggle('record');if(document.body.classList.contains('record')){panel.hidden=true;try{await document.documentElement.requestFullscreen()}catch{}}else if(document.fullscreenElement)await document.exitFullscreen()}board.addEventListener('wheel',e=>{e.preventDefault();cancelAnimationFrame(anim);if(e.ctrlKey||e.metaKey){const p=point(e),f=Math.exp(e.deltaY*.002);v.x=p.x+(v.x-p.x)*f;v.y=p.y+(v.y-p.y)*f;v.w*=f;v.h*=f}else{v.y+=e.deltaY*v.h/innerHeight;v.x+=e.deltaX*v.w/innerWidth}set()},{passive:false});board.onpointerdown=e=>{cancelAnimationFrame(anim);const p=point(e);board.setPointerCapture(e.pointerId);if(drawing){const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('d',`M${p.x} ${p.y}`);path.setAttribute('fill','none');path.setAttribute('stroke','#d65c51');path.setAttribute('stroke-width',v.w/260);path.setAttribute('stroke-linecap','round');document.getElementById('ink').appendChild(path);drag={path}}else drag={x:e.clientX,y:e.clientY,v:{...v}}};board.onpointermove=e=>{if(!drag)return;if(drag.path){const p=point(e);drag.path.setAttribute('d',drag.path.getAttribute('d')+` L${p.x} ${p.y}`)}else{v.x=drag.v.x-(e.clientX-drag.x)*v.w/innerWidth;v.y=drag.v.y-(e.clientY-drag.y)*v.h/innerHeight;set()}};board.onpointerup=()=>drag=null;board.onpointercancel=()=>drag=null;addEventListener('keydown',e=>{if(e.key==='ArrowRight')go(index+1);else if(e.key==='ArrowLeft')go(index-1);else if(/^[1-9]$/.test(e.key))go(+e.key-1);else if(e.key==='0')overview();else if(e.key.toLowerCase()==='d')pen();else if(e.key.toLowerCase()==='n')showNotes();else if(e.key.toLowerCase()==='f')record();else if(e.key==='Escape'){document.body.classList.remove('record');panel.hidden=true}else if((e.ctrlKey||e.metaKey)&&e.key==='z'){e.preventDefault();undo()}});addEventListener('resize',()=>{v.h=v.w/ratio();set()});document.addEventListener('fullscreenchange',()=>{if(!document.fullscreenElement)document.body.classList.remove('record')});move(fit(marks[0]),false);
</script></html>'''
(O/'presenter.html').write_text(template.replace('SVG',svg()).replace('DATA',data),encoding='utf8')
(O/'tableau-reperes.json').write_text(json.dumps(bookmarks,ensure_ascii=False,indent=2),encoding='utf8')
print(f'{len(E)} objets modifiables, aucun cadre ; {len(bookmarks)} repères dans un tableau continu.')

# Breathing room around the camera area keeps the floating tools off the content.
presenter=(O/'presenter.html').read_text(encoding='utf8')
presenter=presenter.replace('function fit(b){let w=', 'function fit(b){b={...b,y:b.y-65,h:b.h+195};let w=')
(O/'presenter.html').write_text(presenter,encoding='utf8')

# Speaker sheet follows the same continuous board; no slide/reveal directions.
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
pdfmetrics.registerFont(TTFont('Body','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Bold','C:/Windows/Fonts/arialbd.ttf'))
c=canvas.Canvas(str(O/'fiche-tournage.pdf'),pagesize=(595,842));c.setTitle('Essort - EP01 - Notes du tableau continu');page=0
def pt(s,y,size=11,bold=False,color=BLACK):
 font='Bold' if bold else 'Body';c.setFont(font,size);c.setFillColor(HexColor(color))
 for para in s.split('\n'):
  line=''
  for word in para.split():
   trial=(line+' '+word).strip()
   if pdfmetrics.stringWidth(trial,font,size)>511 and line:c.drawString(42,y,line);y-=size*1.4;line=word
   else:line=trial
  c.drawString(42,y,line);y-=size*1.4
 return y
def pg():
 global page
 if page:c.showPage()
 page+=1;pt('ESSORT / EP01 / TABLEAU CONTINU',802,10,True,BLUE);pt(f'Notes de parole · Pilote à valider                                                        {page}',28,9,False,GRAY)
pg();y=pt('Le client professionnel que votre portfolio oublie',735,27,True)
y=pt('9-10 minutes indicatives. Un grand tableau à parcourir librement, avec des mots clés, des images et des schémas pour soutenir votre parole.',y-24,12)
y=pt('Le fil du tournage',y-22,17,True)
for i,b in enumerate(bookmarks):y=pt(f'{i+1:02d}. '+b['title'].replace('\n',' '),y-10,11)
y=pt('Comment le parcourir',y-25,17,True)
y=pt('Molette : faire défiler. Glisser : déplacer le tableau. Ctrl + molette : zoomer. Touches 1 à 9 : rejoindre un repère. D : dessiner ; Ctrl + Z : annuler un trait. N : notes privées. F : masquer les outils pour filmer. Échap : revenir.',y-12,11)
pt('Dans Excalidraw : tous les objets sont modifiables, sans cadres de diapositives. Le lecteur HTML est séparé et ne se met pas à jour après une modification manuelle du fichier Excalidraw.',y-15,10,False,GRAY)
gestures=['Partir du gros titre, descendre vers les deux photos, puis pointer le changement d’usage.', 'Mettre les deux attentes en regard. Souligner « usage » au stylet.', 'Pointer les trois métiers. Entourer le restaurant, choisi ici comme exemple.', 'Zoomer sur « 3 mois », puis suivre les dépendances avec le pointeur.', 'Barrer les adjectifs. Descendre sur les trois éléments de preuve.', 'Montrer la phrase générale, puis descendre sur la phrase précise.', 'Suivre les deux entrées qui rejoignent la même conversation.', 'Cocher les quatre choix au stylet ; laisser le temps de les lire.', 'Revenir au titre de conclusion et formuler l’invitation naturellement.']
md=['# EP01 — Notes du tableau continu','', 'Durée indicative : 9–10 minutes. Les repères servent à naviguer, sans imposer de changement de page.','']
for start in range(0,9,2):
 pg();y=740
 for i in range(start,min(start+2,9)):
  y=pt(f'{i+1:02d} / '+bookmarks[i]['title'].replace('\n',' '),y,17,True)
  for t in notes[i]['notes']:y=pt('• '+t,y-8,10.5)
  y=pt('À montrer : '+gestures[i],y-12,10,False,BLUE)
  y=pt('Transition : '+notes[i]['transition'],y-10,10,False,GRAY)-28
  md += [f'## {i+1:02d}. '+bookmarks[i]['title'].replace('\n',' '),'']+['- '+t for t in notes[i]['notes']]+['','**À montrer :** '+gestures[i],'','**Transition :** '+notes[i]['transition'],'']
 if y<60:raise ValueError(f'PDF overflow {page}')
 if start==8:
  y=pt('Images et vérifications',y-15,14,True)
  y=pt('Photographies réelles : Pexels photo 9685262 ; posters des vidéos 10135086 et 10375427. Licence : https://www.pexels.com/license/. Illustrations, aucun projet présenté comme client Essort.',y-12,10)
  pt('Le délai de trois mois et le message restaurant à Lyon sont des exemples fictifs. Aucun « ×2 », zéro concurrence ou délai de signature promis. Vérifier le lien du guide avant publication.',y-12,10)
c.save();(O/'script.md').write_text('\n'.join(md),encoding='utf8')
(O/'README.md').write_text('''# EP01 — Tableau continu à valider

Le pilote a été repris après la référence YouTube de Louis Appert : un grand support blanc à parcourir, avec gros textes, surlignages, images et flèches. Aucun cadre de diapositive.

- `presenter.html` : canevas continu. Molette pour défiler ; glisser pour déplacer ; Ctrl + molette pour zoomer. Repères 1–9 ; stylet D ; annuler Ctrl + Z ; notes N ; filmer F ; sortie Échap.
- `01-client-professionnel.excalidraw` : tous les objets sont modifiables, photographies intégrées, aucun cadre.
- `fiche-tournage.pdf` et `script.md` : notes orales, transitions et gestes sur le tableau.

Les annotations du lecteur sont temporaires. Le lecteur HTML n’est pas synchronisé avec les modifications manuelles du fichier Excalidraw. Régénérer avec `../build_tableau.py`.

Photographies Pexels : photo 9685262, vidéos 10135086 et 10375427. Licence https://www.pexels.com/license/. Aucune image générée par IA ; images illustratives, pas des clients Essort.

Référence de format consultée : https://www.youtube.com/watch?v=ZBSYIZtMwhg. Ses captures restent dans le dossier interne de vérification et ne sont pas intégrées au support livré.
''',encoding='utf8')
