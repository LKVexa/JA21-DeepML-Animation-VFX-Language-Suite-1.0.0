#!/usr/bin/env python3
from pathlib import Path
import gzip,json,csv,hashlib,sys,re
root=Path(__file__).resolve().parents[1]
errors=[]
master=root/'corpus/technical/deepml_vfx_technical_corpus_10000.jsonl.gz'
count=0; ids=set()
with gzip.open(master,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line); count+=1; ids.add(r['id'])
        if r['language']!='deepml.vfx': errors.append(f"bad language {r['id']}")
if count!=10000: errors.append(f"technical corpus count={count}")
if len(ids)!=10000: errors.append(f"technical corpus unique ids={len(ids)}")
scripts=list((root/'script_pack_1000').rglob('*.deepml'))
if len(scripts)!=1000: errors.append(f"script count={len(scripts)}")
for p in scripts:
    s=p.read_text(encoding='utf-8')
    if not s.startswith('deepml vfx 0.3'): errors.append(f"bad header {p}")
    if 'module ' not in s: errors.append(f"missing module {p}")
    if 'policy deterministic' not in s or 'policy no_network' not in s: errors.append(f"missing policy {p}")
    if s.count('{')!=s.count('}'): errors.append(f"brace imbalance {p}")
cat=list(csv.DictReader(open(root/'script_pack_1000/catalog.csv',encoding='utf-8')))
if len(cat)!=1000: errors.append(f"catalog count={len(cat)}")
print(json.dumps({'status':'PASS' if not errors else 'FAIL','technical_records':count,'scripts':len(scripts),'catalog_rows':len(cat),'errors':errors[:50]},indent=2))
sys.exit(1 if errors else 0)
