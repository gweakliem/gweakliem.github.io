---
title: "TIL llm configuration"
categories: [til]
date: 2025-07-14
published: True
---

I saw Simon's [article on using Kimi](https://simonwillison.net/2025/Jul/11/kimi-k2/#atom-everything) with his great [llm](https://llm.datasette.io/en/stable/index.html) tool. The one mysterious thing was editing the `extra-openai-models.yaml` file, I couldn't figure out where that was located. It turns out the answer (on OSX) is:

```
dirname  "$(llm logs path)"
```

but basically, the parent of whatever `llm logs path` returns. Combine that with `extra-openai-models.yaml` and that's the path!