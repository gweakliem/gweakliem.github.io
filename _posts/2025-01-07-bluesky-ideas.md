---
title: "Bluesky Ideas"
date: 2025-01-07
---

I've been mulling on doing something with the Bluesky firehose for about a month. The base firehose is kind of daunting, but [Jetstream](https://github.com/bluesky-social/jetstream) is a great deal simpler. One thing we used to do at NewsGator was simple keyword feeds, where you could monitor keywords and we'd synthesize an RSS feed of posts that mentioned those keywords for you. 20 years later you could do some really interesting things. Like what if you built embeddings for the feed and subscribed based on a vibe rather than just keywords?

This hit my bsky feed yesterday:

<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:kft6lu4trxowqmter2b6vg6z/app.bsky.feed.post/3leyztswv5k2q" data-bluesky-cid="bafyreigmldvq4fztukz3ib23nmg4vmjecrxbpjfwhjqzmipfjbnwn2kc7e"><p lang="en">I&#x27;d love to build a custom @bsky.app  feed for myself, but it looks like step one might be to start consuming and storing the ENTIRE firehouse, which is a bit of friction I don&#x27;t particularly want to deal with!</p>&mdash; Simon Willison (<a href="https://bsky.app/profile/did:plc:kft6lu4trxowqmter2b6vg6z?ref_src=embed">@simonwillison.net</a>) <a href="https://bsky.app/profile/did:plc:kft6lu4trxowqmter2b6vg6z/post/3leyztswv5k2q?ref_src=embed">January 5, 2025 at 9:24 AM</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>

Defining the feed logic in custom code is an interesting idea too. 

I started a project that just dumps Jetstream output into Parquet files, which is a data engineer thing to do, but it's not all that interesting by itself. Seems like I should figure out a way to dump all that into a vector db as a next step?