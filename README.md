## Eighty/Twenty

This is the source for [eighty-twenty.net](https://eighty-twenty.net).

It's built on [Github Pages](https://pages.github.com/) and [Jekyll](https://jekyllrb.com/) and uses the [Hacker](https://github.com/pages-themes/hacker) theme.

`newpost.py` creates new posts. Run `uv run newpost --help` for help. Once you've created a post, commit the new file and run `git push`, Github Actions does the rest.


### Testing Locally

```
bundle install
bundle exec jekyll serve
```

[Drafts](https://jekyllrb.com/docs/posts/#drafts) add the `--drafts` to integrate posts in the `_drafts` folder.
