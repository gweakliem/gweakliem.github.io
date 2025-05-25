---
title: Nifty Databricks Tricks
date: 2025-05-24
categories:
  - spark
tags:
  - spark
  - databricks
---

Some nifty Databricks tricks I've learned over the last couple of years:

## Convert any .py file to a notebook

Do this by by putting this comment at the first line:
```
# Databricks notebook source
```
Then you divide the notebook into cells with this marker:
```
# COMMAND ----------
```
This is really powerful when you need to debug a file in place. I generally have a separate file with all the transformations: DataFrame(s) in, DataFrame out. You can open the file in Databricks as a notebook and run your code in place. I generally have a `COMMAND` section at the end with some commented out test code to load up a sample DataFrame.

## Dataflint

I discovered [Dataflint](https://github.com/dataflint/spark) while debugging a slow job. I suspected a skew problem but I was mostly trying random things. Dataflint is fantastic - it pinpointed my skew problem but also gave some good suggestions on executor memory and cluster size. It's a pretty new project so hopefully it will get even better over time.

## Editor Tricks

Possibly the biggest lifehack here is the fact that Databricks' worksheet editor is based on the Monaco engine, which is the same engine that powers VS Code. What that means is that many of the same keyboard accelerators work! CMD+D selects words, CMD+Shift+Arrow does multiselect, etc. I haven't documented how much of the VS Code keymap is availible, but there are definitely some editing improvements available.