# GitHub CLI PR 指令參考

完整的 `gh pr` 相關指令參考。

## 目錄

- [建立 PR](#建立-pr)
- [查看 PR](#查看-pr)
- [編輯 PR](#編輯-pr)
- [審核 PR](#審核-pr)
- [合併 PR](#合併-pr)
- [其他操作](#其他操作)

## 建立 PR

### gh pr create

建立新的 Pull Request。

```bash
gh pr create [flags]
```

**常用選項：**

| 選項 | 說明 | 範例 |
|------|------|------|
| `--base <branch>` | 目標分支 | `--base main` |
| `--head <branch>` | 來源分支 | `--head feature/login` |
| `--title <string>` | PR 標題 | `--title "feat: 新增功能"` |
| `--body <string>` | PR 描述 | `--body "## 變更內容..."` |
| `--body-file <file>` | 從檔案讀取描述 | `--body-file pr-body.md` |
| `--draft` | 建立草稿 PR | `--draft` |
| `--reviewer <users>` | 指定審核者 | `--reviewer user1,user2` |
| `--assignee <users>` | 指定負責人 | `--assignee @me` |
| `--label <labels>` | 新增標籤 | `--label bug,urgent` |
| `--milestone <name>` | 設定里程碑 | `--milestone "v1.0"` |
| `--project <name>` | 加入專案 | `--project "Sprint 1"` |
| `--web` | 在瀏覽器中開啟 | `--web` |
| `--fill` | 自動填入標題和描述 | `--fill` |
| `--fill-first` | 使用第一個 commit 填入 | `--fill-first` |

**範例：**

```bash
# 基本建立
gh pr create --base main --title "feat: 新增登入功能" --body "實作 OAuth 登入"

# 建立草稿 PR 並指定審核者
gh pr create --draft --reviewer team-lead --label "WIP"

# 從檔案讀取描述
gh pr create --title "重大更新" --body-file CHANGELOG.md

# 自動填入（使用 commit 訊息）
gh pr create --fill
```

## 查看 PR

### gh pr list

列出 Pull Requests。

```bash
gh pr list [flags]
```

**常用選項：**

| 選項 | 說明 | 範例 |
|------|------|------|
| `--state <state>` | 狀態篩選 (open/closed/merged/all) | `--state open` |
| `--author <user>` | 作者篩選 | `--author @me` |
| `--assignee <user>` | 負責人篩選 | `--assignee user1` |
| `--label <labels>` | 標籤篩選 | `--label bug` |
| `--base <branch>` | 目標分支篩選 | `--base main` |
| `--head <branch>` | 來源分支篩選 | `--head feature/*` |
| `--limit <int>` | 限制數量 | `--limit 10` |
| `--json <fields>` | JSON 輸出 | `--json number,title,state` |

**範例：**

```bash
# 列出所有開啟的 PR
gh pr list

# 列出我建立的 PR
gh pr list --author @me

# 列出待審核的 PR
gh pr list --state open --reviewer @me

# JSON 格式輸出
gh pr list --json number,title,author --limit 5
```

### gh pr view

查看 PR 詳情。

```bash
gh pr view [<number> | <url> | <branch>] [flags]
```

**常用選項：**

| 選項 | 說明 |
|------|------|
| `--web` | 在瀏覽器開啟 |
| `--comments` | 顯示評論 |
| `--json <fields>` | JSON 輸出 |

**範例：**

```bash
# 查看當前分支的 PR
gh pr view

# 查看指定 PR
gh pr view 42

# 在瀏覽器開啟
gh pr view 42 --web

# 顯示評論
gh pr view 42 --comments
```

### gh pr diff

查看 PR 的差異。

```bash
gh pr diff [<number> | <url> | <branch>] [flags]
```

**範例：**

```bash
# 查看當前 PR 差異
gh pr diff

# 查看指定 PR 差異
gh pr diff 42

# 只顯示檔案名稱
gh pr diff 42 --name-only
```

### gh pr checks

查看 PR 的 CI 檢查狀態。

```bash
gh pr checks [<number> | <url> | <branch>] [flags]
```

**範例：**

```bash
# 查看檢查狀態
gh pr checks 42

# 等待檢查完成
gh pr checks 42 --watch
```

## 編輯 PR

### gh pr edit

編輯 Pull Request。

```bash
gh pr edit [<number> | <url> | <branch>] [flags]
```

**常用選項：**

| 選項 | 說明 | 範例 |
|------|------|------|
| `--title <string>` | 修改標題 | `--title "新標題"` |
| `--body <string>` | 修改描述 | `--body "新描述"` |
| `--body-file <file>` | 從檔案讀取描述 | `--body-file body.md` |
| `--base <branch>` | 變更目標分支 | `--base develop` |
| `--add-reviewer <users>` | 新增審核者 | `--add-reviewer user1` |
| `--remove-reviewer <users>` | 移除審核者 | `--remove-reviewer user1` |
| `--add-assignee <users>` | 新增負責人 | `--add-assignee @me` |
| `--remove-assignee <users>` | 移除負責人 | `--remove-assignee user1` |
| `--add-label <labels>` | 新增標籤 | `--add-label bug` |
| `--remove-label <labels>` | 移除標籤 | `--remove-label WIP` |
| `--milestone <name>` | 設定里程碑 | `--milestone "v2.0"` |

**範例：**

```bash
# 修改標題
gh pr edit 42 --title "fix: 修正登入錯誤"

# 修改描述
gh pr edit 42 --body "## 變更說明\n- 修正 bug"

# 新增審核者和標籤
gh pr edit 42 --add-reviewer team-lead --add-label "needs-review"

# 變更目標分支
gh pr edit 42 --base develop
```

## 審核 PR

### gh pr review

審核 Pull Request。

```bash
gh pr review [<number> | <url> | <branch>] [flags]
```

**選項：**

| 選項 | 說明 |
|------|------|
| `--approve` | 核准 PR |
| `--request-changes` | 要求修改 |
| `--comment` | 只留言（不核准或拒絕） |
| `--body <string>` | 審核訊息 |
| `--body-file <file>` | 從檔案讀取審核訊息 |

**範例：**

```bash
# 核准 PR
gh pr review 42 --approve --body "LGTM!"

# 要求修改
gh pr review 42 --request-changes --body "請修正第 15 行的錯誤"

# 只留言
gh pr review 42 --comment --body "這個方法很不錯"
```

## 合併 PR

### gh pr merge

合併 Pull Request。

```bash
gh pr merge [<number> | <url> | <branch>] [flags]
```

**常用選項：**

| 選項 | 說明 |
|------|------|
| `--merge` | 使用 merge commit |
| `--squash` | 壓縮成單一 commit |
| `--rebase` | 使用 rebase |
| `--auto` | 自動合併（等待檢查通過） |
| `--delete-branch` | 合併後刪除分支 |
| `--subject <string>` | 自訂 commit 訊息標題 |
| `--body <string>` | 自訂 commit 訊息內容 |

**範例：**

```bash
# 使用 squash 合併並刪除分支
gh pr merge 42 --squash --delete-branch

# 自動合併（等待 CI 通過）
gh pr merge 42 --auto --merge

# 自訂 commit 訊息
gh pr merge 42 --squash --subject "feat: 新增登入功能 (#42)"
```

## 其他操作

### gh pr close

關閉 PR（不合併）。

```bash
gh pr close [<number> | <url> | <branch>] [flags]
```

**範例：**

```bash
# 關閉 PR
gh pr close 42

# 關閉並刪除分支
gh pr close 42 --delete-branch

# 留言說明原因
gh pr close 42 --comment "此 PR 已由 #43 取代"
```

### gh pr reopen

重新開啟已關閉的 PR。

```bash
gh pr reopen [<number> | <url> | <branch>]
```

### gh pr ready

將草稿 PR 標記為準備審核。

```bash
gh pr ready [<number> | <url> | <branch>]
```

### gh pr comment

在 PR 上留言。

```bash
gh pr comment [<number> | <url> | <branch>] [flags]
```

**範例：**

```bash
# 留言
gh pr comment 42 --body "已完成修改，請再次審核"

# 從檔案讀取留言
gh pr comment 42 --body-file comment.md
```

### gh pr checkout

切換到 PR 的分支。

```bash
gh pr checkout [<number> | <url> | <branch>]
```

**範例：**

```bash
# 切換到 PR #42 的分支
gh pr checkout 42

# 切換並建立本地分支
gh pr checkout 42 --branch local-branch-name
```
