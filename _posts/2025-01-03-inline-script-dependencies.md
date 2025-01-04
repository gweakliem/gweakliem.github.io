---
title: "Inline Script Dependencies"
date: 2025-01-03
categories: [til]
---

(via [Simon Willison](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/))

TIL about [inline script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) which is something that uv supports - basically if you have a python file that requires some external dependencies you can essentially declare an environment (python version + requirements.txt) and uv will take care of setting it up, so instead of needing separate requirements.txt and all that, you can package it all in one file. 