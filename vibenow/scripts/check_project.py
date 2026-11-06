#!/usr/bin/env python3
"""用 Python 標準函式庫檢查 VIBING NOW 的專案結構、內容與連結。"""
from pathlib import Path
from html.parser import HTMLParser
from datetime import date
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
required=['AGENTS.md','README.md','index.html','explore.html','about.html','assets/style.css','assets/app.js','data/bars.json','templates/page.html']
for path in required:
    if not (ROOT/path).is_file():errors.append(f'缺少檔案：{path}')
try: data=json.loads((ROOT/'data/bars.json').read_text(encoding='utf-8'))
except (OSError,json.JSONDecodeError) as e:errors.append(f'JSON 無法讀取：{e}');data={'bars':[]}
bars=data.get('bars',[])
if not isinstance(bars,list) or not bars:errors.append('bars 必須是非空陣列');bars=[]
ids=set()
for index,b in enumerate(bars,1):
    if not isinstance(b,dict):errors.append(f'第 {index} 筆不是物件');continue
    fields=['id','name','district','vibe','price','event','description','tags','emoji','updated']
    for field in fields:
        if field not in b:errors.append(f'第 {index} 筆缺少欄位 {field}')
    id=b.get('id','')
    if not isinstance(id,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',id):errors.append(f'第 {index} 筆 id 無效')
    if id in ids:errors.append(f'重複 id：{id}')
    ids.add(id)
    for field in ['name','event','description','emoji']:
        if not isinstance(b.get(field),str) or not b[field].strip():errors.append(f'{id}：{field} 必須是非空字串')
    if b.get('district') not in ['信義','大安','中山','其他']:errors.append(f'{id}：district 不合法')
    if b.get('vibe') not in ['熱鬧','Chill','約會','音樂']:errors.append(f'{id}：vibe 不合法')
    if type(b.get('price')) is not int or b['price']<=0:errors.append(f'{id}：price 必須是正整數')
    if not isinstance(b.get('tags'),list) or not 1<=len(b['tags'])<=4 or not all(isinstance(t,str) and t.strip() for t in b['tags']):errors.append(f'{id}：tags 須為 1 至 4 個字串')
    try:date.fromisoformat(b['updated'])
    except (KeyError,TypeError,ValueError):errors.append(f'{id}：updated 須為 YYYY-MM-DD')
class Parser(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.main=False;self.title=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in ['a','link','script']:self.links.extend([a[k] for k in ['href','src'] if k in a])
        if tag=='main' and a.get('id')=='main':self.main=True
        if tag=='title':self.title=True
for file in [*ROOT.glob('*.html'),*ROOT.glob('templates/*.html')]:
    parser=Parser();parser.feed(file.read_text(encoding='utf-8'))
    if not parser.main or not parser.title:errors.append(f'{file.name} 缺少 main#main 或 title')
    for href in parser.links:
        if href.startswith(('https:','http:','mailto:','#','data:')):continue
        target=(file.parent/href.split('#')[0]).resolve()
        if not target.is_file():errors.append(f'{file.name} 連結檔案不存在：{href}')
if errors:
    print('❌ 驗證失敗：');print('\n'.join(' - '+e for e in errors));sys.exit(1)
print(f'✅ 驗證通過：{len(bars)} 筆酒吧資料、{len(list(ROOT.glob("*.html")))} 個正式網頁、模板與連結檢查完成。')
