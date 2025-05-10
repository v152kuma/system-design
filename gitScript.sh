!#/bin/bash
echo "# data-engineering" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/v152kuma/data-engineering.git
git push -u origin main
