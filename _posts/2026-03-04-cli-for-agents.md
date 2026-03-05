---
title: "CLI for AI Agents"
date: 2026-03-04
published: True
---

[Justin Poehnelt](https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/) just published "You Need to Rewrite Your CLI for AI Agents". I think he makes a number of points worth thinking about:

1. It's a lot easier for an agent to communicate with JSON. It's a pain for humans but no problem for an AI.
2. Write documentation! I'd say it as "write it for an idiot".
3. That extends into "write it for an ambitious idiot". Harden your inputs against things like trying control characters, because it seemed like a good idea. Something only a malicious human would do, an AI might try because it's out of real ideas and it's in the training data somewhere.
4. Being disciplined with both offering filter options and pagination
5. Offer a `--dry-run` option, hopefully the user prompts the agent to use it.

I think it's a great idea to think about making your services CLI friendly, but also agent friendly.
