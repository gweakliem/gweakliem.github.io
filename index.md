## About
This is the personal website for Gordon Weakliem. I've owned this domain for about 20 years and I had a weblog from about 2002-2009, first at Radio Userland, then later hosted on this domain.

## Recent Posts

<ul>
  {% for post in site.posts %}
    <li>
        {{ post.date | date: "%b %-d, %Y" }} <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

[Feed](/feed.xml)

## Links
* [GitHub](https://github.com/gweakliem)
* [X](https://x.com/weakliem69467)
* [Bluesky](https://bluesky.app/profile/2hardproblems)
* [LinkedIn](https://linkedin.com/in/gweakliem)
