"""Encode small display copies; leave prompt URLs and original media unchanged."""
from pathlib import Path
import argparse,json,subprocess,concurrent.futures,urllib.request
from PIL import Image
p=argparse.ArgumentParser();p.add_argument('--asset-cache',type=Path);a=p.parse_args()
root=Path(__file__).resolve().parents[1];cache=a.asset_cache or root/'work/asset-cache'
data=json.loads((root/'app/library-data.json').read_text(encoding='utf-8'))
out=root/'public/thumbs';out.mkdir(exist_ok=True)
def prepare(asset):
 url=asset['url'];relative=url.split('.here.now/',1)[1]
 if not url.lower().endswith(('.png','.jpg','.jpeg','.webp','.avif','.gif')):return
 source=cache/relative
 if not source.exists():
  source.parent.mkdir(parents=True,exist_ok=True)
  with urllib.request.urlopen(urllib.request.Request(url+'?raw=1',headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:source.write_bytes(r.read())
 name=source.stem+'.webp';dest=out/name
 with Image.open(source) as image:w,h=image.size
 ratio=min(1,960/w,720/h);size=(max(1,int(w*ratio)),max(1,int(h*ratio)))
 if not dest.exists():subprocess.run(['ffmpeg','-v','error','-i',str(source),'-vf',f'scale={size[0]}:{size[1]}','-c:v','libwebp','-quality','82','-compression_level','5','-frames:v','1',str(dest)],check=True)
 asset['thumbnail']='/thumbs/'+name
 return url,asset['thumbnail']
all_assets=[asset for pack in data for asset in pack['assets']]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:mapping=dict(x for x in pool.map(prepare,all_assets) if x)
for pack in data:
 for key in ('primary','secondary'):
  url=pack['cover'].get(key)
  if url in mapping:pack['cover'][key]=mapping[url]
(root/'app/library-data.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'thumbnails':len(mapping),'total_bytes':sum(p.stat().st_size for p in out.glob('*.webp'))}))
