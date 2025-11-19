# Git & GitHub Quick-Reference Toolbox

## 1. Initial Setup (One-time)
- **Configure Git:** `git config --global user.name "Your Name"`, `git config --global user.email "your.email@example.com"`
- **Initialize Repo:** `git init`
- **Connect to GitHub:** `git remote add origin https://github.com/username/repo-name.git`
- **First Push:** `git push -u origin main`

## 2. Daily Workflow
- **Check Status:** `git status`
- **Stage Changes:** `git add .` (all files) or `git add filename.py`
- **Commit:** `git commit -m "Descriptive message"`
- **Push to GitHub:** `git push origin main`
- **Quick Combo:** `git add . && git commit -m "Message" && git push`

## 3. Checking Your Work
- **See Changes:** `git diff` (unstaged), `git diff --staged` (staged)
- **Commit History:** `git log --oneline`, `git log --graph --oneline`
- **Recent Commits:** `git log -5` (last 5 commits)
- **File History:** `git log --follow filename.py`

## 4. Undoing Changes
- **Unstage File:** `git reset filename.py`
- **Discard Changes:** `git checkout -- filename.py`
- **Undo Last Commit:** `git reset --soft HEAD~1` (keeps changes)
- **Hard Reset:** `git reset --hard HEAD~1` (⚠️ destroys changes)

## 5. Branches
- **List Branches:** `git branch`
- **Create Branch:** `git branch feature-name`
- **Switch Branch:** `git checkout feature-name`
- **Create & Switch:** `git checkout -b feature-name`
- **Merge Branch:** `git merge feature-name`
- **Delete Branch:** `git branch -d feature-name`

## 6. Remote Operations
- **Pull Updates:** `git pull origin main`
- **Fetch Info:** `git fetch`
- **Check Remotes:** `git remote -v`
- **Clone Repo:** `git clone https://github.com/username/repo-name.git`

## 7. Good Commit Messages
- **Format:** `"Type: Brief description"`
- **Examples:** 
  - `"Add: Day 3 Python dictionaries practice"`
  - `"Update: Practice log with sets and tuples notes"`
  - `"Fix: Typo in loop example"`
  - `"Refactor: Organize practice files by week"`

## 8. GitHub-Specific
- **Create Repo:** Go to github.com → New repository
- **README:** Add `README.md` for project description
- **Issues:** Track bugs/features on GitHub
- **Releases:** Tag versions with `git tag v1.0`

## 9. File Management
- **Ignore Files:** Create `.gitignore`, add patterns like `*.log`, `__pycache__/`
- **Remove from Git:** `git rm filename.py`
- **Rename File:** `git mv oldname.py newname.py`
- **Track Empty Folders:** Add `.gitkeep` file

## 10. Common Patterns
- **Feature Branch Flow:**
  1. `git checkout -b new-feature`
  2. Make changes & commit
  3. `git checkout main`
  4. `git merge new-feature`
  5. `git branch -d new-feature`

## 11. Troubleshooting
- **Merge Conflicts:** Edit files manually, then `git add .` and `git commit`
- **Forgot to Pull:** `git stash`, `git pull`, `git stash pop`
- **Wrong Commit Message:** `git commit --amend -m "New message"`
- **Check Git Version:** `git --version`

## 12. Daily Practice Workflow
1. **Start Session:** `git status` (check what's changed)
2. **During Practice:** Make your changes and test code
3. **End Session:** 
   - `git add .`
   - `git commit -m "Day X: [what you learned]"`
   - `git push origin main`
4. **Weekly:** Review with `git log --oneline` to see your progress

## 13. GitHub Desktop Alternative
- **Download:** GitHub Desktop app for visual Git management
- **Benefits:** Point-and-click interface, visual diffs, easier conflict resolution
- **Command Line:** Still useful for quick operations and automation

Keep this file handy during your daily practice! Git becomes second nature with consistent use.