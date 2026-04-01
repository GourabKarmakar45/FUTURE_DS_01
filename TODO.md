# Git Setup and Push to GitHub Repo (FUTURE_DS_01)

## Steps:
- [x] 1. `git init` - Initialize Git repository.
- [x] 2. `git add .` - Stage all files.
- [x] 3. `git commit -m "Initial commit: complete sales analysis project with Python analysis, PowerBI dashboard, charts, and report."` - Commit staged files.
- [x] 4. `git remote add origin https://github.com/GourabKarmakar45/FUTURE_DS_01.git` - Add remote.
- [x] 5. `git branch -M main` - Rename branch to main.
- [x] 6. `git push -u origin main --force` - Force push to overwrite empty remote repo.
- [x] 7. Clean up: Remove cloned dir `Remove-Item -Recurse -Force FUTURE_DS_01` (PowerShell).
- [x] 8. Verify: `git status` and `git remote -v`.

**Notes:** Uses --force-with-lease for safety. Repo will now contain the full current project.
