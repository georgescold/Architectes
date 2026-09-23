(function(root){
'use strict';
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#x27;');
function normalize(q={}){return {metier:String(q.metier||''),structure:String(q.structure||''),origine_projets:String(q.origine_projets||''),departement:String(q.departement||'').trim().replace(/[\u0000-\u001f]/g,'').slice(0,100)}}
function eligibility(input,rules){const q=normalize(input);if(Object.values(q).every(x=>!x))return {status:'generic',reason:'Version commune — sélectionner un profil pour comparer les adaptations.'};
if(!Object.entries(rules.questions).every(([key,choices])=>choices.includes(q[key]))||!q.departement)return {status:'incomplete',reason:'Les quatre réponses sont nécessaires. Aucune entrée automatique dans la séquence.'};
if(!['architecte-de','architecte-interieur'].includes(q.metier)||q.structure==='6-plus')return {status:'review',reason:'Profil à examiner : remise du guide prévue, séquence commerciale suspendue jusqu’à validation de son adéquation.'};
return {status:'eligible',reason:'Parcours '+(q.metier==='architecte-de'?'architecte DE / DPLG':'architecte d’intérieur')+' · '+(q.structure==='seul'?'indépendant':'petite équipe')};}
function adapt(text,id,input,rules,html=false){const q=normalize(input);const state=eligibility(q,rules);let out=text;
if(state.status!=='eligible')return out;
for(const r of rules.rules){if(!(r.ids.includes('*')||r.ids.includes(id)))continue;if(r.value!=='*'&&q[r.field]!==r.value)continue;if(r.field==='departement'&&!q.departement)continue;
const old=r.old.replace(/&amp;/g,'&');let value=r.new.replace(/&amp;/g,'&').replace('{departement}',q.departement);
// Texte brut et texte HTML partagent les mêmes règles, sans interpolation non échappée.
out=out.split(html?esc(old):old).join(html?esc(value):value);}
if(html&&id==='E30'&&q.metier==='architecte-interieur')out=out.replace(/\/angles\.png/g,'/angles-interieur.png');
return out;}
const api={normalize,eligibility,adapt,escapeHtml:esc};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.EssortQualification=api;
})(typeof window!=='undefined'?window:globalThis);
