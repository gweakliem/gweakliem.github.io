---
title: "But We Were Just Getting Started"
date: 2025-02-12
---

Claude is my daily driver for AI but one thing I dislike about using it for projects is the warning "The chat is getting long. Long chats cause you to reach your usage limits faster."

That's the point, no? When I work on something with any level of complexity, there are long discussions as I refine my thinking. There's debugging sessions. There's side conversations where I try to remember how to accomplish some task in `zsh` or write a litte utility to do some task. Some of that is not really relevant to the project, but all of it went into making the project and should be part of the context. Yet Claude always seems to hit me with that warning at the point where I'm just getting started, and then I have to start all over in a new chat. Or maybe I don't but I do because if I'm getting the warning, I figure there's a reason.

It really seems like these chat histories are an important artifact - this is analogous to all the meeting minutes, design reviews, and Slack chats that normally make up a project's background documentation. My second frustration with Claude is that there's no way to export these logs. I very much like the fact that OpenAI lets you link to a chat and share it with other people. I think that feature would remove both frustrations. 

It's also interesting that Cursor and Windsurf don't run into these limits. I imagine that they're rebuilding the context on every query, so they don't carry around the entire chat context. It's the same problem, though, I don't see a clear way to tie chat logs to a project and make them part of the artifacts.