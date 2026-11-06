# VIBING NOW ✦

**製作者：政大 114305039 企管二 許筱捷**

**專案 Repository：** https://github.com/114305039/vibenow

**Tonight’s vibe, before you arrive.** 一個以「今晚想要的氣氛」為主題的多頁靜態探索網站。這是課堂的網站練習，所有酒吧、活動與費用均為虛構示範資料。

## 已完成的網站成果
- 首頁：品牌定位、精選示範酒吧與網站目的。
- 探索酒吧：關鍵字、地區、氛圍、預算多條件篩選；收藏功能（localStorage）。
- 關於專案：說明如何依照 AGENTS.md 重複新增內容。
- 一套共用樣式、資料 schema、頁面模板及自動驗證腳本。

## 本機開啟
1. 解壓縮專案，在資料夾內開啟終端機。
2. 執行 `python3 -m http.server 8000`。
3. 在瀏覽器輸入 `http://localhost:8000/`。請勿直接雙擊 HTML，因為部分瀏覽器會阻止本機 `fetch` JSON。
4. 可先執行 `python3 scripts/check_project.py` 驗證。

## 上傳 GitHub 與發布 GitHub Pages
1. 登入 GitHub，按 **New repository**，名稱為 `vibenow`，選 **Public**。
2. 在空白 repo 使用 **uploading an existing file**，上傳此專案內所有檔案與資料夾；務必保留 `AGENTS.md` 以及 `data/`、`assets/`、`templates/`、`scripts/` 結構。
3. 在儲存庫 **Settings → Pages → Build and deployment**，Source 選 **Deploy from a branch**，Branch 選 `main`、資料夾選 `/(root)` 並 Save。
4. 網址通常為 `https://114305039.github.io/vibenow/`；請等 GitHub Pages 顯示發布成功後實際點開確認。
5. 提交作業時附上 repo 與實際可開啟的網頁連結，勿提交未建立的示例網址。

## 如何用 AGENTS.md 讓 AI 擴充
直接對 AI 說：
> 請先閱讀根目錄的 AGENTS.md，照其中 schema 在 data/bars.json 新增一間虛構酒吧，並執行 scripts/check_project.py，不要改變既有風格。

新頁面可用：
> 請先閱讀 AGENTS.md，再利用 templates/page.html 新增一個「夜晚音樂風格」頁面，沿用共用 CSS，更新導覽與驗證頁面連結。

## 教學重點
這次作業的核心不是單一頁面的完成，而是設計出 AI 能照著反覆操作的規範，讓新增資料與新增頁面不必每次重新開始。
