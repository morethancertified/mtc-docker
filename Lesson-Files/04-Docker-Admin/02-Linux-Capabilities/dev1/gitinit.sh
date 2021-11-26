git init &&
git remote add origin https://gitlab.com/mtc-infra/$(echo ${PWD} | awk -F/ '{print $NF}').git &&
git add . && 
git commit -m "initial" &&
git push -u origin master