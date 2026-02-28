# Agent Skills

## Install

### skill install

```
npx skills add https://github.com/gn00678465/AgentSkills.git
```

## Included Skills

### Commit Message (v0.2.1)

分析 git staged changes 並根據 Conventional Commits 規範自動生成**繁體中文 commit message** 與**語意化分支名稱**。

**Use Cases:**

- 「幫我寫 commit message」
- 「取個分支名並產生 commit」
- 「提交變更」
- 「主分支誤改，幫我切分支並提交」

**Features:**

- **自動化分析**：透過 `analyze_git.py` 自動計算變更複雜度與識別高風險檔案（如 Lock 檔案）。
- **語意化分支建議**：根據變更內容（feat, fix, refactor）自動產生建議的分支名稱。
- **主分支保護**：偵測到在 `main`/`master` 分支時，主動阻止提交並引導切換。
- **原子化提交引導**：針對高複雜度變更，提供具體的 `git reset` 與 `git add` 指令協助拆分提交。

**Usage:**

1. 確保有暫存的變更：`git add <files>`
2. 輸入上述任一指令。
3. 依據模型回饋選擇執行對應的 Git 指令。

### GitHub PR (v0.1.1)

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
- **防止轉義**：強制使用 `--body-file` 避免換行符被轉義為 `\n` 字串。

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