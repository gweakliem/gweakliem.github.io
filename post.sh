title=$1
filename=$(echo "$title" | tr '[:upper:]' '[:lower:]' | tr -c '[:alnum:]' '-' | tr -s '-' | cut -c1-60)
path="_posts/$(date +%Y-%m-%d)-${filename}.md"
cat <<EOF >> $path
---
layout: default
title: "$title"
date: $(date +%Y-%m-%d)
---
EOF
git add $path
echo $path