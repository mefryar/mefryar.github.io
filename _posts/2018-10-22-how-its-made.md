---
layout: post
title: How It's Made
---

**Note**: This post describes how I built the first version of my site using Pelican. I
have since [migrated to Jekyll]({% post_url 2021-04-25-migrate-to-jekyll %})

![How It's Made: Pencils](http://i.imgur.com/788bA.gif)

### Static Sites vs. Dynamic Sites: GitHub Pages vs. WordPress
My purpose in starting a blog is to create a space where I can learn out loud
about new tools I discover. So, as a meta point, I chose to host my site through
[GitHub Pages](https://pages.github.com) since it allows me to look under the
hood and understand how my website is made. This is because sites hosted via
GitHub Pages are static sites, meaning are mostly made up of HTML files. They
are static in the sense that each page displays the same information to all
visitors. The opposite of static sites are dynamic sites which build each page
at the moment it is visited. (David Walsh has a great [intuitive
metaphor](https://davidwalsh.name/introduction-static-site-generators) to
explain the difference between dynamic and static sites.)

Creating a static site through GitHub Pages rather than a dynamic site through
WordPress also offers a number of additional advantages. First, security. As
[Aaron Autrand
explains](https://www.netlify.com/blog/2016/05/18/9-reasons-your-site-should-be-static/),

> "With a static site, you don’t have to worry about malicious code being
> injected into your site when users visit it... No build process means standard
> hacking attacks like scripting or database security exploits just don’t work."

Second, speed. Your pages load much faster when they are being written on the
fly. Third, scalability. With a static site, if you, say, wake up to discover
you've won a Nobel Prize for studying technological innovation, you're much less
likely to have to [spend that morning rebooting your website's
server](https://twitter.com/paulmromer/status/1049256472423682051). Fourth,
since static sites are just a collection of files, GitHub can afford to host
them for free, without ads. And, finally, because it's GitHub, you get version
control.

The major disadvantage of static sites is that you have to figure out a way to
create all those HTML files. This is where Pelican swoops in the save the day.

### Static Site Generators: Pelican
Pelican is an example of a static site generator, a tool that does the hard work
of converting plain text documents to HTML. In the early days of the Internet,
all websites were static sites. Around the turn of the millennium, however,
dynamic sites took off in popularity. This was in part because, thanks to
Content Management Systems like WordPress, they made it possible to quickly
create a basic website without knowing any HTML.  Static site generators solve
the problem of having to know HTML in order to build a static site, allowing you
to write your blog posts in an easy-to-use language like Markdown.

The most popular static site generator is Jekyll, which was created and is
supported by GitHub. But thanks to [Angela Ambroz's
blog](http://angelaambroz.com/blog/index.html), which was my original
inspiration for starting a blog, I knew that Pelican was an alternative written
in Python rather than Ruby. [Pelican's Quickstart
guide](http://docs.getpelican.com/en/stable/quickstart.html) was in fact quick
to follow and pretty soon I was previewing my site. Now that the skeleton was
built, the next step was fleshing it out and customizing its appearance.

### Picking a Theme: Premium-Blog
The aspect that I agonized over the longest was picking a theme. I wanted
something that was minimalist but more distinctive than the default. There are
[more than 100 Pelican themes available](http://www.pelicanthemes.com) but very
few caught my eye. One that did was the [nice-blog
theme](https://github.com/guilherme-toti/nice-blog) by Guilherme Toti. When I
went to [Guilherme's website](http://guilhermetoti.com/) to see it in action,
however, I noticed that he was using a new theme he created called premium-blog,
which I liked even better. I reached out to Guilherme to ask if I could use it
for my own website and he responded almost immediately with a gracious and
enthusiastic green light. A couple tweaks to the theme configuration files and,
just like that, I had a website!

### Next Steps
Of course, nothing is ever done. I'd still like to figure out how to add
Atom/RSS feeds and Google Analytics. But those can be the subjects of future
posts.
