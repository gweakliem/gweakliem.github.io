---
title: "Introducing Yappr"
date: 2025-09-01
published: True
---

I just completed an MVP on something I'm calling [Yappr](https://yappr.site/). This all started about 10 days ago when a friend sent me a link to an article, but I was about to jump into the car. Then, I got to my destination and found that the site was not mobile-friendly and I couldn't read it on my phone. I eventually got to my desktop and read it, but the whole thing got me wishing for an app that would read to me when my eyes were busy elsewhere. 

Initially I thought I'd create a dedicated app for mobile, but this had a few problems: iOS or Android? Did I want to support CarPlay / Android Auto? Did I want to use native or something cross platform, and all the tradeoffs involved there. I also haven't done much mobile development and all this felt like friction, I just wanted to listen to an article!

But we already have apps that will read arbitrary audio: we've had podcasts for about 20 years. These days we have good text-to-speech models that can do a reasonable job with text for not too much money. So the idea refined: how about an app that would convert text articles to MP3s of spoken words, and then organize that into an RSS feed?

So I've unabashedly vibe-coded this thing, although not strictly vibe coded: there were unexpected things that happened and I had to dive in and figure them out. GCP Authentication had to be solved for both my local dev environment and production. I learned about deploying things to Vercel and working with Supabase. There are things that need refinement: my initial choice of voice model is pretty bad, for example it doesn't understand contractions. The raw text could use more preprocessing to help out the voice model and make a nicer presentation. But it works in some minimal sense, and anyone can use it. 

I told myself 2025 was going to be the year of building, but I hit some detours. This feels like I'm getting back on track.