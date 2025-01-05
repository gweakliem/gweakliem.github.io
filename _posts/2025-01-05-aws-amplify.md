---
title: "AWS Amplify"
categories: [til]
date: 2025-01-05
---

TIL about [AWS Amplify](https://aws.amazon.com/amplify/) as an option for hosting static sites. I had been working on this [web-utils](https://github.com/gweakliem/web-utils) project, but it existed only locally. I probably could have deployed it on GitHub pages, but I had the domain https://meggie.be/ hanging around basically unused. 

Amplify was extremely easy to set up through the AWS console. I had a thought in the back of my mind "clickops bad, must use Terraform" but part of the point is to just get to done, and if the definition of done is some professional irresponsibility, so be it. Anyway, Amplify makes it easy to hook up to Route 53 (which owns meggie.be) and set up an SSL cert in the bargain. However, my first attempt timed out, and this morning I took a look at Route 53 and it seemed like none of the DNS records updated. I deleted all but the `NS` and `SOA` records, then had Amplify retry the custom domain activation and it worked like a charm.
