'use strict';
const DATA_PATH = 'data/bars.json';
let allBars = [];
const byId = id => document.getElementById(id);
const make = (tag, className, value) => { const e=document.createElement(tag); if(className)e.className=className;if(value!==undefined)e.textContent=value;return e; };
function readFavs(){try{return JSON.parse(localStorage.getItem('vibing-favs')||'[]')}catch{return []}}
function writeFavs(favs){try{localStorage.setItem('vibing-favs',JSON.stringify(favs))}catch{}}
function createCard(bar){
 const article=make('article','card');
 const art=make('div','card-art',bar.emoji);art.setAttribute('aria-hidden','true');article.append(art);
 const top=make('div','row');top.append(make('span','pill',`${bar.district} · ${bar.vibe}`),make('span','price',`NT$ ${bar.price}`));article.append(top);
 article.append(make('h3','',bar.name),make('p','',bar.description));
 const event=make('p','');event.append(make('strong','', '主題｜'),document.createTextNode(bar.event));article.append(event);
 const tags=make('div','tags');bar.tags.forEach(t=>tags.append(make('span','tag',t)));article.append(tags);
 const bottom=make('div','row');bottom.append(make('small','',`資料編輯：${bar.updated}`));
 const fav=make('button','fav','♡ 收藏');fav.type='button';
 const repaint=()=>{let v=readFavs().includes(bar.id);fav.textContent=v?'♥ 已收藏':'♡ 收藏';fav.setAttribute('aria-pressed',String(v));fav.setAttribute('aria-label',`${v?'取消收藏':'收藏'} ${bar.name}`)};
 fav.addEventListener('click',()=>{const set=new Set(readFavs());set.has(bar.id)?set.delete(bar.id):set.add(bar.id);writeFavs([...set]);repaint();});repaint();bottom.append(fav);article.append(bottom);return article;
}
function render(container,items){container.replaceChildren();items.forEach(x=>container.append(createCard(x)));if(!items.length)container.append(make('div','empty','沒有符合條件的示範酒吧，試試其他搜尋條件。'));}
function filterBars(){
 const query=(byId('search')?.value||'').trim().toLowerCase();const district=byId('district')?.value||'all';const vibe=byId('vibe')?.value||'all';const budget=Number(byId('budget')?.value||0);
 const result=allBars.filter(b=>(district==='all'||b.district===district)&&(vibe==='all'||b.vibe===vibe)&&(!budget||b.price<=budget)&&(!query||[b.name,b.district,b.vibe,b.event,b.description,...b.tags].join(' ').toLowerCase().includes(query)));
 const node=byId('results');if(node)render(node,result);if(byId('result-count'))byId('result-count').textContent=`找到 ${result.length} 間示範酒吧`;
}
async function init(){
 const results=byId('results'),featured=byId('featured');if(!results&&!featured)return;
 try{const res=await fetch(DATA_PATH);if(!res.ok)throw Error('HTTP '+res.status);const data=await res.json();allBars=data.bars;
 if(featured)render(featured,allBars.slice(0,3));
 if(results){['search','district','vibe','budget'].forEach(id=>byId(id)?.addEventListener('input',filterBars));byId('reset')?.addEventListener('click',()=>{byId('search').value='';byId('district').value='all';byId('vibe').value='all';byId('budget').value='';filterBars()});filterBars()}
 }catch(error){const msg=make('div','empty','無法讀取示範資料。請使用本機 HTTP 伺服器或 GitHub Pages 開啟網站。');(results||featured).replaceChildren(msg);console.error(error)}
}
init();
