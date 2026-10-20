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