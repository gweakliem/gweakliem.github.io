---
title: "Is MCP Necessary?"
date: 2025-04-27
tags:
  - mcp
  - ai
---

Tim Kellogg has a post [MCP is Unnecessary](https://timkellogg.me/blog/2025/04/27/mcp-is-unnecessary) and I found myself agreeing, but after reading it and considering his point, I realized something: he's assuming that everything is described by an OpenAPI definition. I posted that on Bluesky, but I wanted to expand. 

There are a number of very useful things that aren't described by OpenAPI. I find the postgres and Databricks extensions useful, especially when running the MCP server locally. I have less worry about credential and information leakage and the response time is generally better. I find that in interactions with Claude, if I give it specific table and column names, it sees the tool advertised in MCP and tries to do its research directly on the database, rather than making me do it. 

There are also a number of web APIs that aren't described by OpenAPI. There are legacy services, services that simply aren't maintained well anymore. There are services, especially those offered by governments and non-profits, where they simply don't have the budge to add support. And then there are useful services not under our control where the owner simply isn't interested in offering the OpenAPI definition. There are also cases where the OpenAPI definition exists, but lacks definitions for things like authentication. Yes, those could be fixed, but in the real world, the won't necessarily be.

That said, there should be a meta service where you can give MCP an OpenAPI definition and the LLM understands it enough to build its own client and use the service. I don't think that's something Claude or ChatGPT can do now - I'm sure they could generate the client code but I don't think they could necessarily execute it. Is there a meta-MCP that can do that, take an OpenAPI definition, dynamically create a client and expose all the endpoints? 