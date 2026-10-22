Mon terminal:

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (rudy)
$ git branch -c feature/display-observation-dates-rudy

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (rudy)
$ git switch feature/display-observation-dates-rudy
Switched to branch 'feature/display-observation-dates-rudy'
Your branch is ahead of 'origin/rudy' by 5 commits.
  (use "git push" to publish your local commits)

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (feature/display-observation-dates-rudy)
$ git merge feature/display-observation-dates-rudy/rudy
merge: feature/display-observation-dates-rudy/rudy - not something we can merge

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (feature/display-observation-dates-rudy)
$ git branch -a
* feature/display-observation-dates-rudy
  main
  rudy
  remotes/origin/HEAD -> origin/main
  remotes/origin/Mathis
  remotes/origin/main
  remotes/origin/rudy

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (feature/display-observation-dates-rudy)
$ git merge origin/rudy
Already up to date.

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (feature/display-observation-dates-rudy)
$ git merge origin/feature/display-observation-dates-rudy
merge: origin/feature/display-observation-dates-rudy - not something we can merge

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (feature/display-observation-dates-rudy)
$ git merge origin/main
Updating 9596943..3324864
Fast-forward
 evidence/td4.md | 313 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 src/main.py     |   9 ++
 2 files changed, 322 insertions(+)
 create mode 100644 evidence/td4.md

Admin@LAPTOP-IRNN4PFF UCRT64 ~/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07 (feature/display-observation-dates-rudy)
$ git merge origin/rudy
Already up to date.

PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git add src/main.py
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git commit -m "feat: display first and last observation dates"
On branch feature/display-observation-dates-rudy
Your branch is ahead of 'origin/rudy' by 7 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git status
>> git log --oneline -5
On branch feature/display-observation-dates-rudy
Your branch is ahead of 'origin/rudy' by 7 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
3324864 (HEAD -> feature/display-observation-dates-rudy, origin/main, origin/HEAD, main) td4 rendu
b955bee feat: display first and last observation dates
9596943 (rudy) Add files via upload
f24b71c docs: add simple comments to MarketPulse code
1f7af0b Evidences du td2 et td3
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git switch rudy
Switched to branch 'rudy'
Your branch is ahead of 'origin/rudy' by 5 commits.
  (use "git push" to publish your local commits)
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git merge feature/display-observation-dates-rudy
Updating 9596943..3324864
Fast-forward
 evidence/td4.md | 313 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 src/main.py     |   9 ++
 2 files changed, 322 insertions(+)
 create mode 100644 evidence/td4.md
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> & C:\Users\Admin\AppData\Local\Programs\Python\Python313\python.exe "c:/Users/Admin/OneDrive/Desktop/esilv/A4/Python Git Linux/Projet TD/esilv-marketpulse-g03-t07/src/main.py"
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First date  : 2026-09-01
Last date   : 2026-09-30
First close : 250.00 USD
Last close  : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First date  : 2026-09-01
Last date   : 2026-09-30
First close : 6600.00
Last close  : 6742.00
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git pull origin rudy
From https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07
 * branch            rudy       -> FETCH_HEAD
Already up to date.
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git pull origin rudy
From https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07
 * branch            rudy       -> FETCH_HEAD
Already up to date.
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git switch main  
Switched to branch 'main'
Your branch is behind 'origin/main' by 5 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git pull main origin
fatal: 'main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git pull main rudy
fatal: 'main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git pull HEAD rudy
fatal: 'HEAD' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git switch rudy
Switched to branch 'rudy'
Your branch is up to date with 'origin/rudy'.
PS C:\Users\Admin\OneDrive\Desktop\esilv\A4\Python Git Linux\Projet TD\esilv-marketpulse-g03-t07> git status
>> git log --oneline --graph --decorate --all -10
On branch rudy
Your branch is up to date with 'origin/rudy'.

nothing to commit, working tree clean
* 4abba41 (origin/main, origin/Mathis, origin/HEAD) docs: remove TD4 markdown replaced by notebook
* f05d331 docs: add Mathis TD4 notebook
*   2ac75c1 Merge branch 'main' into Mathis
|\  
| * 3324864 (HEAD -> rudy, origin/rudy, main, feature/display-observation-dates-rudy) td4 rendu
| * b955bee feat: display first and last observation dates
* | 0c580e1 Merge branch 'main' of https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07 into Mathis
|\| 
| * 9596943 Add files via upload
:
* 4abba41 (origin/main, origin/Mathis, origin/HEAD) docs: remove TD4 markdown replaced by notebook
* f05d331 docs: add Mathis TD4 notebook
*   2ac75c1 Merge branch 'main' into Mathis
|\  
| * 3324864 (HEAD -> rudy, origin/rudy, main, feature/display-observation-dates-rudy) td4 rendu
| * b955bee feat: display first and last observation dates
* | 0c580e1 Merge branch 'main' of https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07 into Mathis
|\| 
| * 9596943 Add files via upload
| * f24b71c docs: add simple comments to MarketPulse code
| * 1f7af0b Evidences du td2 et td3
| * 5e49bbd création des fichiers dans evidence
~

~
) docs: remove TD4 markdown replaced by notebook



ure/display-observation-dates-rudy) td4 rendu
on dates
com/Enrique-JaraRon/esilv-marketpulse-g03-t07 into Mathis


se code


~
~
~
* 4abba41 (origin/main, origin/Mathis, origin/HEAD) docs: remove TD4 markdown replaced by notebook
* f05d331 docs: add Mathis TD4 notebook
*   2ac75c1 Merge branch 'main' into Mathis
|\  
| * 3324864 (HEAD -> rudy, origin/rudy, main, feature/display-observation-dates-rudy) td4 rendu
| * b955bee feat: display first and last observation dates
* | 0c580e1 Merge branch 'main' of https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07 into Mathis
|\| 
| * 9596943 Add files via upload
| * f24b71c docs: add simple comments to MarketPulse code
| * 1f7af0b Evidences du td2 et td3
| * 5e49bbd création des fichiers dans evidence
~

$ git branch
git branch --merged
git log --oneline --graph --decorate --all
  feature/display-observation-dates-rudy
* main
  rudy
  feature/display-observation-dates-rudy
* main
  rudy
* 0a52a8b (HEAD -> main) td 4 rendu final rudy
* 28ad24c (origin/main, origin/HEAD) td 4 rendu rudy
| * b382c47 (origin/Mathis) sujet td5
|/  
* 4abba41 docs: remove TD4 markdown replaced by notebook
* f05d331 docs: add Mathis TD4 notebook
*   2ac75c1 Merge branch 'main' into Mathis
|\  
| * 3324864 (origin/rudy, rudy, feature/display-observation-dates-rudy) td4 rendu
| * b955bee feat: display first and last observation dates
* | 0c580e1 Merge branch 'main' of https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07 into Mathis
|\| 
| * 9596943 Add files via upload
: