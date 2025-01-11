---
title: "Jekyll Archives and GitHub Pages"
date: 2025-01-11
categories: [til]
---

Edit: It turns out this is all wrong, jekyll will build locally but the GitHub actions to build pages will not render the archives. It's a [known issue](https://github.com/github/pages-gem/pull/106) and they won't fix it, so this attempt was a failure, at least for GitHub pages. TIL also that you don't declare victory until CI/CD completes :)

I've been building out this site iteratively, working in small chunks. Stood up a basic site, picked a theme, tweaks to the layout, install a [syndication feed](/feed.xml). The one major thing I've wanted was to set up archives. It seems like Jekyll has enough to do it myself, but I ran into this post by David Sleight on [grouping by year](https://stuntbox.com/blog/jekyll-archives-group-posts-by-year/) and David talks about using [jekyll-archives](https://github.com/jekyll/jekyll-archives/tree/master) as part of his solution, so I figured that would save me some work. However, I couldn't get it to work and while debugging I ran into some things suggesting that `jekyll-archives` doesn't work with GitHub pages. I went to bed and came back with some fresh eyes and noticed something interesting in my Gemfile:

```
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end
# other stuff ...
gem 'jekyll-archives'
```

`jekyll-archives` installation instructions just said to "Add gem 'jekyll-archives' to your site's Gemfile" and put the plugin in the `plugins:` section of `_config.yml`, but it wasn't rendering any archive pages - I'm setup to run the site locally and I can see that `_site/` doesn't have any index pages where they should be. It's one of the nice things about these static page sites, it's easy to see what's being served.

In any case, the answer is to structure the Gemfile like this:

```
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem 'jekyll-archives'
end
```

As soon as I did that and ran `bundle exec jekyll serve`, bam, index pages appear. Then it's just a matter of building some layouts. 

One other trick I learned was that if you want to modify the layout a plugin installed, there's a handy way to get your starting template. You can look at what layouts are installed using `ls "$(bundle info --path hacker)/_layouts/"`, and then create your own copy using a command like `cp "$(bundle info --path hacker)/_layouts/post.html" ./_layouts` in the project root for your site. Really that's just allowing you to introspect on bundles you've installed, but it's a handy way to modify templates too. I had wanted "next" and "previous" navigation on individual posts, so I added that while I'm at it.

I also learned a little about [jekyll variables](https://jekyllrb.com/docs/variables/), there's a ton of things you can do with those but that's a project for another day.