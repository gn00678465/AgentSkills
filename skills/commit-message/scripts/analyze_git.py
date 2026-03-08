import subprocess
import os
import sys
import re

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
        return result.stdout.strip()
    except Exception:
        return ""

def analyze():
    # 1. 檢查分支
    current_branch = run_command("git branch --show-current")
    is_main = current_branch in ["main", "master"]

    # 2. 取得統計數據
    stats_raw = run_command("git diff --staged --stat")
    if not stats_raw:
        print("Error: No staged changes found.")
        sys.exit(0)

    # 解析統計資料 (e.g. " 5 files changed, 20 insertions(+), 10 deletions(-)")
    files_changed = 0
    insertions = 0
    deletions = 0
    
    stats_lines = stats_raw.splitlines()
    if stats_lines:
        last_line = stats_lines[-1]
        files_match = re.search(r'(\d+) file', last_line)
        ins_match = re.search(r'(\d+) insertion', last_line)
        del_match = re.search(r'(\d+) deletion', last_line)
        
        if files_match: files_changed = int(files_match.group(1))
        if ins_match: insertions = int(ins_match.group(1))
        if del_match: deletions = int(del_match.group(1))
    
    total_lines = insertions + deletions

    # 3. 取得變更檔案清單
    files_list_raw = run_command("git diff --staged --name-only")
    files_list = files_list_raw.splitlines() if files_list_raw else []

    # 4. 計算分數
    score = 0
    risk_factors = []

    if total_lines > 200:
        score += 3
        risk_factors.append(f"大量變更 ({total_lines} 行)")
    if files_changed > 5:
        score += 2
        risk_factors.append(f"變更檔案過多 ({files_changed} 個)")

    # 高風險檔案檢查
    lock_files = [
        "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "bun-lock.json",
        "Cargo.lock", "go.sum", "poetry.lock", "Gemfile.lock", "composer.lock"
    ]
    found_locks = [f for f in files_list if os.path.basename(f) in lock_files]
    if found_locks:
        score += 5
        risk_factors.append(f"包含 Lock 檔案: {', '.join(found_locks)}")

    # 安全與資料庫檢查
    has_auth = any(re.search(r'auth|security|permission|login', f, re.I) for f in files_list)
    has_db = any(re.search(r'migration|schema|database|db', f, re.I) for f in files_list)
    
    if has_auth:
        score += 3
        risk_factors.append("涉及認證或安全邏輯")
    if has_db:
        score += 3
        risk_factors.append("涉及資料庫變更")

    # 5. 建議分支名稱邏輯
    suggested_branches = []
    # 判斷主要類型
    primary_type = "feat"
    if any(re.search(r'fix|bug|patch', f, re.I) for f in files_list):
        primary_type = "fix"
    elif any(re.search(r'refactor', f, re.I) for f in files_list):
        primary_type = "refactor"
    elif any(re.search(r'build|ci|chore', f, re.I) for f in files_list):
        primary_type = "build"
        
    # 根據檔案名稱提取關鍵詞
    keywords = []
    for f in files_list:
        name = os.path.basename(f).split('.')[0]
        if name and name not in ["index", "main", "app", "file1", "file2", "SKILL"]: # 過濾無意義名稱
            keywords.append(name)
    
    top_keyword = keywords[0] if keywords else "work"
    suggested_branches.append(f"{primary_type}/{top_keyword}")
    if has_auth: suggested_branches.append(f"{primary_type}/auth-logic")
    if has_db: suggested_branches.append(f"{primary_type}/db-migration")

    # 輸出結果
    print(f"Branch: {current_branch}")
    print(f"IsMain: {str(is_main).lower()}")
    print(f"Score: {score}")
    print(f"RiskFactors: {', '.join(risk_factors) if risk_factors else 'None'}")
    print(f"FilesChanged: {files_changed}")
    print(f"TotalLines: {total_lines}")
    print(f"SuggestedBranches: {', '.join(suggested_branches)}")
    print("-" * 20)
    print(stats_raw)

if __name__ == "__main__":
    analyze()
