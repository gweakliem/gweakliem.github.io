---
title: "How I Program With LLMs"
date: 2025-01-08
---

<a href="https://crawshaw.ioablog/programming-with-llms">How I program with LLMs</a> <small>(<a href="https://news.ycombinator.com/item?id=42617645">via</a>)</small> mirrors a lot of what I've experienced. The second paragraph struck me, last spring I was going around telling people that this felt like 1995. My story was sitting in my rented room in Dallas, on my couch with my newly-issued work laptop, fumbling around to configure a SLIP dialer and Trumpet Winsock, then finally ending up online, coming up for air a couple hours later. In a way, I never came up for air, the Internet is the sea I've swum in since then. 

Some other points he makes:

>Sometimes the LLM is wrong. So are people.

That's my instant retort to the "AI is useless" trope. [Metacrap](https://people.well.com/user/doctorow/metacrap.htm) is one of my favorite essays about tech, because the truths still hold outside of Doctrow's original subject: people lie, people are lazy, people are stupid, self-awareness is hard, biases are inherent, metrics influence results, and there's more than one way to describe something. There have been numerous times where people have asked me questions and I've given bad or incorrect advice. There have been numerous times where I've received bad or incorrect advice. But we all still go around trying to learn in the face of all these failures.

>I reach a point in the day when I know what needs to be written, I can describe it, but I don’t have the energy...

I too am a morning person. One thing that I find is that on days where I've been leaning heavily on an LLM, I start to feel the way I did when I was working in a pair programming environment: it's _tiring_. Having a partner makes me work harder. I think one thing Windsurf or Cursor should do is say "how about a game of ping pong?" at some points. 

>Chat-based LLMs do best with exam-style questions

I wouldn't put it as "Exam Style Questions" but I find that I tend to want to micromanage the LLM, and that's not a productive way to use it. I do much better with iterating on smaller chunks of work. In some ways, it's like working with a very enthusiastic intern, maybe very knowledgeable but sometimes a little off base and needing a lot of guidance. One thing is that LLMs are universally bad at saying "I don't know" or "that's not possible". Many of the hallucinations I've run into come from me asking it for something that's just not possible.

>The goal is not a “Web IDE” but rather to challenge the notion that chat-based programming even belongs in what is traditionally called an IDE.

I actually am having much better luck using the LLM inside of the IDE (comparing Continue.dev to Cursor to Windsurf is a whole other post or three), but I do feel like you could be really productive stitching together tools like [llm](https://github.com/simonw/llm) and command line tools. One thing I was experimenting with yesterday was a crude "LLM as a judge" setup, where I took a coding question and gave it to one LLM in LMStudio, then opened a separate session and asked a different LLM for an opinion on the first one's solution. It actually found and corrected some bugs! That kind of thing might be productive - crudely stated, `llm chat -m llm1 "solve problem X" | llm chat -m llm2 "evaluate this solution to problem X"`. I want to play with this more, but it's late, and I'm not a night owl.