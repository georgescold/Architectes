(async function(){
const rules=await fetch('personnalisation-regles.json').then(r=>r.json());
const form=document.createElement('section');form.className='profile-panel';form.innerHTML=`<details open><summary>Adapter les mails au profil du cabinet</summary><div class="profile-fields"><label>Métier<select id="q-metier"><option value="">Version commune</option><option value="architecte-de">Architecte DE / DPLG</option><option value="architecte-interieur">Architecte d’intérieur</option><option value="maitre-oeuvre">Maître d’œuvre</option><option value="autre">Autre métier</option></select></label><label>Structure<select id="q-structure"><option value="">Non renseignée</option><option value="seul">Travaille seul</option><option value="2-5">Petite équipe (2 à 5)</option><option value="6-plus">6 personnes ou plus</option></select></label><label>Origine des projets<select id="q-origine"><option value="">Non renseignée</option><option value="bouche-a-oreille">Recommandations</option><option value="plateformes">Plateformes</option><option value="reseaux">Réseaux sociaux</option><option value="recherche">Google / fiche établissement</option><option value="publicite">Publicité payante</option></select></label><label>Département<input id="q-departement" maxlength="100" placeholder="Ex. 56 ou Morbihan"></label></div><p id="profile-status" role="status"></p><button id="profile-reset" type="button">Revenir à la version commune</button></details>`;
document.querySelector('.envelope').before(form);
const style=document.createElement('style');style.textContent='.profile-panel{max-width:664px;margin:0 auto 14px;background:#fff;border:1px solid #dbe1e9;border-radius:10px;padding:18px 22px}.profile-panel summary{cursor:pointer;font-weight:bold}.profile-fields{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px}.profile-fields label{font-size:11px;color:#657188}.profile-fields select,.profile-fields input{display:block;width:100%;margin-top:6px;padding:10px;border:1px solid #dbe1e9;border-radius:5px;background:white;color:#273554;box-sizing:border-box;font:13px Arial}.profile-panel p{font-size:12px;line-height:1.6}.profile-panel button{background:none;border:0;color:#273554;text-decoration:underline;padding:0;cursor:pointer;font-size:12px}@media(max-width:800px){.profile-panel{margin:0 12px 12px}.profile-fields{grid-template-columns:1fr}}';document.head.appendChild(style);
const keys={metier:'q-metier',structure:'q-structure',origine_projets:'q-origine',departement:'q-departement'};let q={},generation=0,exportBlob=null;
function read(){return Object.fromEntries(Object.entries(keys).map(([k,id])=>[k,document.getElementById(id).value]));}
const initial=new URLSearchParams(location.search);
for(const [k,id] of Object.entries(keys)){if(initial.has(k))document.getElementById(id).value=initial.get(k)}
q=read();
async function render(){const version=++generation;const state=EssortQualification.eligibility(q,rules);document.getElementById('profile-status').textContent=state.reason;const id=mails[current].id;
const blocked=(state.status==='review'||state.status==='incomplete')&&id!=='E01';
const dl=document.getElementById('download');if(exportBlob){URL.revokeObjectURL(exportBlob);exportBlob=null;}
if(blocked){f.removeAttribute('src');f.srcdoc='<html lang="fr"><body style="margin:0;padding:32px;background:white;color:#273554;font:16px/1.7 Arial"><h2>Séquence en attente</h2><p>'+EssortQualification.escapeHtml(state.reason)+'</p><p>Le guide reste accessible après qualification complète. Sélectionnez E01 pour prévisualiser sa remise, ou choisissez un profil dans la cible.</p></body></html>';dl.removeAttribute('href');dl.textContent='Export suspendu';return;}
let source=await fetch('html/'+id+'.html').then(r=>r.text());if(version!==generation)return;
let adapted=EssortQualification.adapt(source,id,q,rules,true);
exportBlob=URL.createObjectURL(new Blob([adapted],{type:'text/html;charset=utf-8'}));dl.href=exportBlob;dl.download=id+'-'+(q.metier||'commun')+'.html';dl.textContent='Télécharger ce HTML';
let preview=adapted.replaceAll('{{assets_url}}',new URL('visuels',location.href).href).replaceAll('{{identite_expediteur}}','Aperçu de travail · aucun envoi activé').replace('href="{{lien_desinscription}}"','href="#" onclick="return false" aria-disabled="true"').replace('>Se désinscrire<','>Désinscription à raccorder avant envoi<');
f.removeAttribute('src');f.srcdoc=preview;
}
const original=window.selectMail;window.selectMail=function(n){f.removeAttribute('srcdoc');original(n);render();};
for(const id of Object.values(keys)){document.getElementById(id).addEventListener(id==='q-departement'?'input':'change',()=>{q=read();render()})}
document.getElementById('profile-reset').onclick=()=>{for(const id of Object.values(keys))document.getElementById(id).value='';q=read();render()};
window.previewQualification={render,get:()=>q};await render();
})();
