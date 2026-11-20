"""Refresh public working packs from a Scroll Site Studio installation."""
from pathlib import Path
import argparse,json,zipfile,math,shutil
p=argparse.ArgumentParser();p.add_argument('--skill-root',type=Path,required=True);p.add_argument('--pack',help='Refresh one pack and the combined download');a=p.parse_args()
root=Path(__file__).resolve().parents[1];skill=a.skill_root.resolve()
catalog=json.loads((skill/'catalog.json').read_text(encoding='utf-8'))
examples=json.loads((root/'app/site-examples.json').read_text(encoding='utf-8'))
meta={
'architectural-landscape':('Architecture','Layered landscapes. Exceptional perspectives.',['Parallax','Layered hero','Property'],'warm residence cutout','warm sunset sky',None),
'coffee-product-carousel':('Commerce','A considered product experience, down to the last detail.',['Product selector','Commerce','Editorial'],'01-caramel-cloud','hero-background-4k',None),
'clothes-rack-showroom':('Commerce','A 3D clothing showroom with two racks, a responsive camera and interactive product browsing.',['Three.js','3D showroom','Product browsing'],'approved showroom preview',None,None),
'orbital-portals':('Interactive','A cinematic portal to somewhere completely different.',['Canvas','Video transitions','Space'],'mercury',None,'mars bg'),
'alpine-editorial':('Architecture','An editorial escape with room to breathe.',['Hospitality','Editorial','Gallery'],'hero',None,None),
'electric-vehicle-explorer':('Interactive','Explore a product through motion, details and material.',['Hotspots','Product explorer','Video'],'exterior-polished',None,'hood-hover-forward'),
'tower-room-tours':('Architecture','From a floor in the sky to a room of your own.',['Floor selector','Room tours','Real estate'],'tower dawn plate',None,'mist loop'),
'cinematic-site-workflow':('Workflows','Turn a business brief into a connected visual story.',['Art direction','Scene planning','Replicate'],'small transparent product reference',None,None),
'desktop-mobile-workflow':('Workflows','One coherent experience. Every screen considered.',['Visual story','Responsive','Mobile direction'],'method reference image',None,None),
'lake-cabin-retreat':('Architecture','A cinematic architectural website built with Codex from a YouTube video reference.',['Codex','YouTube reference','Architecture'],'site screenshot',None,None),
'private-aviation-journey':('Interactive','Five deliberate camera moves. A quieter way to travel.',['Three.js','Camera stages','Aviation'],'charter poster',None,'charter loop'),
'racing-driver-profile':('Interactive','A driver story in depth, motion and racing detail.',['Depth portrait','Liquid reveal','Timeline'],'portrait color',None,None),
'cinematic-wipe-studio':('Interactive','One film. Three layers. Every transition considered.',['Video scrub','Geometric wipes','Film studio'],None,None,'continuous banner film'),
'point-cloud-companion':('Interactive','A character made of light. A product story in motion.',['Point cloud','Glass interface','Scroll choreography'],'reference preview poster',None,'reference preview loop'),
'curved-film-archive':('Interactive','Stories on a shelf, with a little depth.',['3D shelf','Sprite sheets','Film archive'],'cover sprite sheet (1744x2336)',None,None),
'rainy-harbour-penthouse':('Architecture','Black lacquer doors open onto a rain-lit harbour and a layered penthouse view.',['Cinematic intro','Layered typography','Real estate'],'mid','back',None),
'bird-species-atlas':('Interactive','An open stage for a closer look at the natural world.',['Three.js','Field guide','Specimen explorer'],'kingfisher illustration',None,None)}
existing_path=root/'app/library-data.json'
prior={item['id']:item for item in json.loads(existing_path.read_text(encoding='utf-8'))} if a.pack else {}
if a.pack and a.pack not in {item['id'] for item in catalog['reference_packs']}:p.error('Unknown pack')
packs=[]
for entry in sorted(catalog['reference_packs'],key=lambda p:list(meta).index(p['id']) if p['id'] in meta else 100):
 if a.pack and entry['id']!=a.pack:
  if entry['id'] in prior:packs.append(prior[entry['id']])
  continue
 if not entry.get('asset_manifest'):continue
 assets=json.loads((skill/entry['asset_manifest']).read_text(encoding='utf-8'))['assets']
 category,description,tags,primary,secondary,video=meta.get(entry['id'],('Other',entry['description'],[],assets[0]['role'] if assets else None,None,None))
 def find(role):return next((a['url'] for a in assets if a['role']==role),None) if role else None
 if primary and not find(primary):raise ValueError('Missing cover: '+entry['id']+'/'+primary)
 prompt=(skill/entry['index']).read_text(encoding='utf-8')
 references=examples.get(entry['id'],[])
 if references and not all(e['url'] in prompt for e in references):
  prompt=prompt.rstrip()+'\n\n## Live website reference\n\n'+'\n\n'.join('['+e['label']+']('+e['url']+')'+('\n\n'+e['note'] if e.get('note') else '') for e in references)+'\n'
 record={'id':entry['id'],'title':entry['title'],'description':description,'category':category,'tags':tags,'kind':'Workflow' if category=='Workflows' else 'Website','assets':assets,'prompt':prompt,'cover':{'primary':find(primary),'secondary':find(secondary),'video':find(video)},'readingMinutes':max(1,math.ceil(len(prompt.split())/200)),'imageCount':sum(a.get('type','').startswith('image/') or a['url'].lower().endswith(('.png','.jpg','.jpeg','.webp','.svg','.avif','.gif')) for a in assets),'videoCount':sum(a['url'].endswith('.mp4') for a in assets),'hasNotices':bool(entry.get('license_notice')) or entry['id']=='electric-vehicle-explorer'}
 record['noticePath']='/licenses/'+entry.get('license_notice','licenses/electric-vehicle-explorer.txt').rsplit('/',1)[1] if record['hasNotices'] else None
 record['noticeSource']=entry.get('license_notice','licenses/electric-vehicle-explorer.txt') if record['hasNotices'] else None
 record['youtubeVideos']=[{'label':s.get('label','Watch on YouTube'),'url':s['url']} for s in entry['sources'] if s.get('type')=='youtube']
 record['examples']=references
 record['fileCount']=len(assets)-record['imageCount']-record['videoCount']
 record['mediaStatus']=entry.get('media_status')
 packs.append(record)
 for folder,text,name in [('prompts',prompt,entry['id']+'.md'),('manifests',json.dumps({'title':entry['title'],'assets':assets},indent=2),entry['id']+'.json')]:
  dest=root/'public'/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text,encoding='utf-8',newline='\n')
 dest=root/'public/downloads'/(entry['id']+'.zip');dest.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
  z.writestr('prompt.md',prompt);z.writestr('assets.json',json.dumps({'title':entry['title'],'assets':assets},indent=2))
  z.writestr('README.txt','Working prompt and linked asset map. Media files are hosted separately at the URLs in assets.json. Hosted copies do not grant new rights. Use the prompt as written, adapt it, or combine selected ideas. Replicate is the default for new media. Review new media in chat before publication. WordPress is optional.\n')
  if record['hasNotices']:z.write(skill/record['noticeSource'],'LICENSE-NOTICES.txt')
 if record['hasNotices']:
  notice=root/'public'/record['noticePath'].lstrip('/');notice.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(skill/record['noticeSource'],notice)
(root/'app/library-data.json').write_text(json.dumps(packs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
notice=root/'public/licenses/electric-vehicle-explorer.txt';notice.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(skill/'licenses/electric-vehicle-explorer.txt',notice)
with zipfile.ZipFile(root/'public/downloads/studio-library-prompts.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in packs:
  z.write(root/'public/prompts'/(p['id']+'.md'),p['id']+'/prompt.md');z.write(root/'public/manifests'/(p['id']+'.json'),p['id']+'/assets.json')
 for p in packs:
  if p['hasNotices']:z.write(root/'public'/p['noticePath'].lstrip('/'),p['id']+'/LICENSE-NOTICES.txt')
 z.writestr('README.txt',f'Designer Site Studio\n\n{len(packs)} public working prompt packs and their linked asset maps. The {sum(len(p["assets"]) for p in packs)} media and support files remain hosted separately; this bundle contains their direct URLs, sizes and SHA-256 hashes. Private backup documents are excluded. Required notices accompany the relevant packs. No new rights to third-party media are granted.\n\nUse with Codex, Claude or your coding agent. Reuse prompts as written, adapt them or combine ideas. WordPress is optional; Replicate is the default for new media. Review new media in chat before publication.\n')
print(json.dumps({'packs':len(packs),'assets':sum(len(p['assets']) for p in packs)}))
