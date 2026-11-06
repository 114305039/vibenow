# VIBING NOW｜網站開發規則

- 專案製作者：政大 114305039 企管二 許筱捷
- GitHub 儲存庫：`114305039/vibenow`
- 網站預計網址：`https://114305039.github.io/vibenow/`（需完成部署）
- 修改網站時，保留作者資訊，不要自行更動學號、系級或姓名。

> 後續要請 AI 新增酒吧、修改功能或做新頁面時，請先閱讀這份規則及 README，再開始修改。網站是可以放上 GitHub Pages 的靜態網站。

## 1. 專案目標與邊界
- 產品：VIBING NOW，協助使用者以「今晚的氣氛」挑選酒吧的展示型探索網站。
- 受眾：成年夜生活探索者及對網站設計有興趣的讀者。
- 現階段：課程用靜態網站；資料均為**虛構示範資料**，不宣稱即時優惠或真實營業資訊。
- 不實作：登入、支付、訂位、個人定位、真實即時人流、酒精購買與年齡驗證機制。
- 未經來源確認，不得將示範活動替換為真實酒吧消息；不得自行捏造評分、特價、地址。

## 2. 技術與部署約束
- 只用 HTML5、CSS3、原生 JavaScript、`data/bars.json`；不需 npm、API key、後端或 CDN。
- 所有頁面皆以**相對路徑**引用素材，例如 `assets/style.css`、`data/bars.json`；不可寫死 `/assets/`，以相容 `username.github.io/repo/`。
- 不使用需要後端的功能；收藏只存使用者瀏覽器 localStorage。
- 檢查：`python3 scripts/check_project.py`；本機啟動：`python3 -m http.server 8000`。

## 3. 檔案架構（不得任意搬移）
```
index.html              首頁與本週主題
explore.html            酒吧資料篩選與收藏
about.html              專案理念與資料揭露
AGENTS.md               AI 規範
README.md               人類使用說明與部署步驟
assets/style.css        所有頁面共用樣式
assets/app.js           全站共用載入、篩選、渲染邏輯
assets/favicon.svg      品牌圖示
data/bars.json          酒吧內容單一資料來源
templates/page.html     新靜態頁面範本
scripts/check_project.py 自動檢查資料與頁面
```

## 4. 視覺設計系統
- 風格：夜間編輯式視覺；深紫黑底、珊瑚粉、奶油白，感覺現代、有質感、不花俏。
- 色票：背景 `#0E0B17`、區塊 `#191525`、主色 `#F6A7BA`、強調色 `#D8C9FF`、文字 `#F7F1ED`、次要文字 `#B9B1C6`。
- 字型：使用作業系統 sans-serif；不載入外部字型。
- 元件：共用 `.container`、`.card`、`.pill`、`.btn`、`.section-heading`。新頁面不可另起一套設計。
- 手機優先，320px 寬度仍可閱讀；行動版導覽可換行；焦點狀態須可見；所有按鈕有文字。

## 5. 資料規格
`data/bars.json` 是一個物件，格式 `{ "bars": [ ... ] }`。每筆必填：
- `id`: 小寫英數與連字號，唯一，例如 `lunar-room`
- `name`: 顯示名稱（字串）
- `district`: 僅用 `信義`、`大安`、`中山`、`其他`
- `vibe`: 僅用 `熱鬧`、`Chill`、`約會`、`音樂`
- `price`: 每人預估費用，正整數（新臺幣）
- `event`: 展示用主題活動名稱，非即時事實
- `description`: 40–100 字左右的簡介
- `tags`: 1–4 個短標籤，陣列字串
- `emoji`: 一個氣氛代表圖示
- `updated`: ISO 日期 `YYYY-MM-DD`，代表示範資料編輯日，不代表真實店家更新
新增或修改資料不得改動欄位語意；避免重複 `id`，不要包含未查證真實店家資訊。

## 6. 新增一筆酒吧資料的標準流程
1. 閱讀本文件與現有 JSON，確定風格與欄位。
2. 在 `data/bars.json` 的 `bars` 陣列新增一筆，使用唯一 `id` 和所有必要欄位。
3. 不要修改 `assets/app.js` 的卡片 HTML 來硬寫新資料；前端會自動渲染。
4. 執行 `python3 scripts/check_project.py`，修正所有錯誤。
5. 在瀏覽器測試探索頁的搜尋、地區、氛圍、價格、收藏，確認新資料出現。

## 7. 新增新頁面的標準流程
1. 複製 `templates/page.html` 為 `kebab-case.html`，例如 `music-guide.html`。
2. 替換 `<title>`、主標題、簡介、區塊內容；保留頁首、頁尾、導覽、無障礙跳至內容連結。
3. 引用共用的 `assets/style.css` 和 `assets/app.js`，不得複製一套 CSS。
4. 若新頁應該從選單進入，同步更新 `index.html`、`explore.html`、`about.html` 和新頁導覽；設定正確 `aria-current="page"`。
5. 連結只用相對路徑，圖片須有 `alt`，表單須有 `label`，動態內容須注意 XSS。
6. 執行驗證腳本並以手機/桌面檢視。

## 8. 修改既有內容或程式的規則
- 原則：先閱讀、最小修改、不破壞既有頁面。不得任意更名 `id`、CSS class 或資料結構。
- 資料顯示使用 DOM `textContent`，不得把 JSON 字串直接插入 `innerHTML`。
- 所有互動要支援鍵盤；空結果要有文字提示，資料讀取失敗要顯示錯誤。
- 收藏 localStorage 出錯時要優雅降級，不影響查詢功能。
- 禁止向使用者暗示資料為「即時真實」；所有頁面保持「示範資料」聲明。
- 新功能需附測試步驟，不可只修改外觀；不能宣稱未測試功能已完成。

## 9. 每次交付前的驗收清單
- [ ] `python3 scripts/check_project.py` 無錯誤。
- [ ] `index.html`、`explore.html`、`about.html` 可開啟。
- [ ] 桌面、手機版不溢出，選單與連結可用。
- [ ] 搜尋、篩選、清除條件、收藏運作。
- [ ] 新增一筆 JSON 資料後，卡片不需改程式即可自動出現。
- [ ] 沒有私密金鑰，也沒有未經查證的即時活動宣稱；作者與 GitHub 連結保持正確。

## 10. 給未來 AI 的範例任務
**任務：**「請新增一間虛構的中山區 Chill 酒吧『雲朵之後』，並新增一個『夜生活禮儀』介紹頁。」
**AI 應執行：**閱讀本檔 → 新增符合 schema 的 JSON → 從 `templates/page.html` 複製新頁 → 更新全站導覽 → 執行驗證 → 告知使用者修改檔案與測試結果。不得憑空宣稱酒吧真的存在。
