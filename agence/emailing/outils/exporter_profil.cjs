const fs=require('fs'),path=require('path');
const P=path.resolve(__dirname,'..');const api=require(path.join(P,'personnalisation.js'));
const rules=JSON.parse(fs.readFileSync(path.join(P,'personnalisation-regles.json'),'utf8'));
if(!process.argv[2]){console.error('Usage : node outils/exporter_profil.cjs profil.json');process.exit(1)}
const profile=api.normalize(JSON.parse(fs.readFileSync(path.resolve(process.argv[2]),'utf8').replace(/^\uFEFF/,'')));
const state=api.eligibility(profile,rules);if(['incomplete','generic'].includes(state.status)){console.error(state.reason);process.exit(2)}
const slug=[profile.metier,profile.structure,profile.origine_projets].join('-');const dir=path.join(P,'exports-profils',slug);fs.mkdirSync(dir,{recursive:true});
let mails=JSON.parse(fs.readFileSync(path.join(P,'sequence-12-mois.json'),'utf8'));if(state.status==='review')mails=mails.filter(x=>x.id==='E01');
const manifest=[];
for(const m of mails){let content=fs.readFileSync(path.join(P,'html',m.id+'.html'),'utf8');content=api.adapt(content,m.id,profile,rules,true);fs.writeFileSync(path.join(dir,m.id+'.html'),content,'utf8');
let text=api.adapt(fs.readFileSync(path.join(P,'texte',m.id+'.txt'),'utf8'),m.id,profile,rules,false);fs.writeFileSync(path.join(dir,m.id+'.txt'),text,'utf8');
manifest.push({...m,corps:api.adapt(m.corps,m.id,profile,rules,false),html:m.id+'.html',texte:m.id+'.txt'});}
fs.writeFileSync(path.join(dir,'profil-et-sequence.json'),JSON.stringify({profile,status:state.status,envoi_active:false,mails:manifest},null,2),'utf8');
console.log(JSON.stringify({directory:dir,status:state.status,emails:mails.length,envoi_active:false}));
