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