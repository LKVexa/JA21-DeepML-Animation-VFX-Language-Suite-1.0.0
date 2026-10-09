#!/usr/bin/env python3
import gzip,json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
q=(sys.argv[1] if len(sys.argv)>1 else '').lower()
path=root/'corpus/technical/deepml_vfx_technical_corpus_10000.jsonl.gz'
shown=0
with gzip.open(path,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line)
        hay=' '.join([r['id'],r.get('topic',''),r.get('class',''),r.get('technical_explanation','')]).lower()
        if q in hay:
            print(json.dumps(r,indent=2,ensure_ascii=False)); shown+=1
            if shown>=5: break
