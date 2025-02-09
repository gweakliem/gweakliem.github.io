---
title: "Bluesky Progress"
date: 2025-02-09
---

I've been fooling around with the Bluesky Firehose for about a month now. My initial interest is in [building a keyword feed](https://github.com/gweakliem/expert-palm-tree) and that much is done. It's pretty easy using Jetstream, which is very stripped down from the full AT Protocol but fine for my purposes.

When I was at NewsGator 20 years ago, we had keyword feeds. They'd simply scan over the database and collect any hits on keywords, using MS SQL Server full-text search. It worked pretty well but we would talk about something more loose, like a "concept feed". At the time we had no idea how to do this and really didn't have the right tech stack, and the technology to do it was really in its infancy. These days it's not only possible, it's possible to do on my off hours on the weekends.

A few notes about Bluesky and Jetstream:
1. Duplicates are a problem. I haven't tracked down the exact source, I'm guessing that it may be related to restarting on disconnect, but it might be that the feed is at-least-once delivery. In any case, after collecting about 100 GB of data, I found over 50,000 posts that had duplicates, some as many as 50 times, so it's a problem you need to account for. In my case, it's just a merge insert into the database.
2. Text can appear in a variety of places in the payload: as `record.text`, as an external `embed` either as `description` or `title` (the last being probably super-low utility), alt text in `images`, and `text` under `video`. There's also `bridgyOriginalText` but this contains markup that I would want to sanitize and the external description seems to generally be present and is mostly pre-scrubbed.
3. Character encoding is unreliable. Strings containing ASCII NUL (`\x00`) are fairly common, and this frequently seems to be the result of Japanese text incorrectly tagged as English, although there are also a number of posts that I haven't figured out what the encoding is supposed to be.
