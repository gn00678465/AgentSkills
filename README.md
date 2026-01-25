# Agent Skills

## Install

### skill install

```
npx skills add https://github.com/gn00678465/AgentSkills.git
```

## Included Skills

### Commit Message

分析 git staged changes 並根據 Conventional Commits 規範自動生成繁體中文 commit message。

**Use Cases:**

適用於需要生成符合規範的 commit 訊息時，例如：

- 「幫我寫 commit message」
- 「產生 commit」
- 「提交變更」

**Usage:**

1. 確保有暫存的變更：`git add <files>`
2. 輸入上述任一指令。
3. 根據回饋建議選擇提交方式（`-m` 或 `-F`）。

### GitHub PR

協助建立或修改 GitHub Pull Request，自動分析分支 commits 並產生繁體中文 PR 標題與描述。

**Use Cases:**

適用於需要建立或修改 Pull Request 時，例如：

- 「建立 PR」
- 「create pull request」
- 「幫我開 PR」
- 「修改 PR 內容」

**Features:**

- **建立 PR**：從當前分支建立 Pull Request 到目標分支
- **修改 PR**：更新現有 PR 的標題或描述
- **分析 commits**：自動彙整分支變更產生 PR 內容

**Usage:**

1. 確保當前分支已推送至遠端：`git push -u origin <branch>`
2. 輸入上述任一指令
3. 若 PR 已存在，會自動進入修改模式
4. 若 PR 不存在，會自動分析 commits 並建立 PR

**Prerequisites:**

- 需安裝並登入 GitHub CLI (`gh auth login`)

### Prompt Optimizer

分析並優化使用者的 prompt，透過系統化解構和框架重建，將模糊或結構不良的 prompt 轉換為高精準、無歧義的版本。

**Use Cases:**

適用於需要改善 prompt 品質時，例如：

- 「優化這個 prompt」
- 「改進這段指令」
- 「重構這個 prompt」
- 「讓這個 prompt 更清楚」

**Features:**

- **解構分析**：識別 prompt 的核心目標、模糊點與任務複雜度
- **框架重建**：根據任務類型選擇最適合的框架（B.R.O.K.E, T.R.A.C.E, C.L.E.A.R 等）
- **驗證檢查**：確保優化後的 prompt 完整、無歧義且符合框架結構

**Usage:**

1. 準備需要優化的 prompt
2. 輸入上述任一指令並提供原始 prompt
3. 獲得優化後的 prompt 及優化理由說明