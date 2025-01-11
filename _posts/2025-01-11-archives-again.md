---
title: "Archives, again"
date: 2025-01-11
---


https://github.com/github/pages-gem/pull/106

[Aneejian](https://aneejian.com/automated-jekyll-archives-github-pages/) posted a solution but I didn't like this - it involves adding a page to generate archive links, then building a docker container and running a python script from GitHub actions. It adds a lot of build overhead and then I wasn't sure how customizable it was. `jekyll-archives` does exactly what I want out of the box. 

[This defunct site](https://web.archive.org/web/20180905102746/https://www.drinkingcaffeine.com/deploying-jekyll-to-github-pages-without-using-githubs-jekyll/) describes an approach with similar problems - you generate the archive offline and upload it. It's possible since I edit locally and I could add a step to run jekyll before committing, but I was hoping for something a bit more automatic for me.

[This is the solution](https://github.com/hzhangxyz/hzhangxyz.github.io/tree/master) that I ultimately copied. It dynamically generates the archives, it probably won't scale that well over many blog posts but it'll do for a while. I also think that I could extend it using the techniques shown at [Stuntbox](https://stuntbox.com/blog/jekyll-archives-group-posts-by-year/), but that's enough messing with jekyll for the weekend.