---
title: "Learning UV"
tags: 
    - python
    - aicoding
date: 2025-01-04
---

I'm getting used to working inside Jekyll and Github pages. One thing I immediately saw that I needed was a better way to create new posts. I was already spending a lot of energy remembering all the Jekyll template attributes and all the little command line things that I needed to do to create a post. 

Trying out [Simon Willison's one-shot python idea](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/), I created a project using the same prompt Simon did and then used this prompt:

```
Write a command line application to create new posts for Github Pages and Jekyll. 

## Use Cases
Create new Post

title:
date: (implied by current date)
filename: from date and title, title turned to slug by replacing all non-alphanumeric characters with dashes, truncated at 60 char, .md extension
categories: (optional separated by commas - no spaces, turn spaces into _)

display all this to the user ask for confirmation (-y flag to skip)
do a git add on the new filename so that it's staged 

## TILs

same as posts, but add til to categories

## Links
Title: optional, read from link if not provided
categories: [links + other categories]

<a href="link to post">author</a> - (optional link to where I got this link from with "via" as the text)
eg <a href="https://simonwillison.net/2024/Dec/22/link-blog/">Simon Willison</a> <small>(<a href="https://daringfireball.net/">via</a>)</small>

## Command Line

uv run newpost <title> [-y] [-t] [-[-l link] [-a author] [-v via]] [-c category1,category2]
```

The result is [newpost.py](https://github.com/gweakliem/gweakliem.github.io/blob/main/newpost.py). The only thing I changed was the `--author` flag to be `--attrib` because I felt like "author" confused me as the author of the post vs who I'm trying to attribute the link to. 

This is the new world. Back when I started out, Microsoft used to create wizards to guide you through new Windows applications, and there was so much chatter about 4GL and 5GL hypothetical languages that would let analysts and non-technical people write code. The biggest danger so far is that I haven't really taken a look at what Claude wrote. It seems to work well enough, and I achieved in 15 minutes something that would have taken an hour without it.