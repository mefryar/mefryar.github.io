---
layout: post
title: Migrate to Jekyll in 1,000 Minutes
---

### Migrate to Jekyll

When I [created my first version of my website](/2018/10/22/how-its-made), I
agonized over picking a theme. I ultimately chose one that looked slick but left
me feeling like I had just blindly copied and pasted 4,800 lines of CSS,
JavaScript, and HTML. I never felt the site was truly my own, and it lay
dormant.

Fast forward to early 2021. I'd been learning [Ruby on
Rails](https://rubyonrails.org/) over the past year and so had been mulling the
idea of migrating to [Jekyll](https://jekyllrb.com/) since it's written in Ruby
and is the most popular way to build a blog and host it for free on [GitHub
Pages](https://pages.github.com/). I stumbled across the [Poole
theme](https://getpoole.com/) for Jekyll while going down a rabbit hole about
the history of [Bootstrap](https://getbootstrap.com/)[^fn-mdo]. Poole aims "to
provide a clear and concise foundational setup for any Jekyll site." When I
discovered that [Vicki Boykis' tech blog](https://veekaybee.github.io/), which
had just recently been recommended to me by a friend, is also built on Poole, I
was sold.
 
[^fn-mdo]: Poole was created by [Mark Otto](https://twitter.com/mdo) who also co-created Bootstrap.

### In 1,000 Minutes

The first search result for "create blog jekyll poole" is [Set up a Jekyll Blog
in 5 minutes with
Poole.](https://www.sitepoint.com/set-jekyll-blog-5-minutes-poole/) I don't mean
to single out this particular post, since it is representative of lots of
programming advice and I appreciate the way it encourages newbies to not be
intimidated and just dive in. But I knew it would take me a *lot* longer.

First, I knew that I would get tripped up by lots of small problems that I
didn't anticipate. This is the glass half empty version of programming, captured
hilariously by [this *Dinosaur Comics*
strip](https://www.qwantz.com/index.php?comic=1178).

![Dinosaur Comics 1178](/assets/images/dinosaur_comics_1178.png "Dinosaur Comics 1178")

But the glass half full version is that lots of small problems means lots of
small wins! Here's a list of some of my small wins from this migration:

* Updating Homebrew to [use full clones rather than shallow
  clones](https://github.com/Homebrew/discussions/discussions/226).
* Getting `brew cleanup` to run successfully by [changing
  permissions](https://github.com/Homebrew/homebrew-core/issues/45009#issuecomment-543795948)
  in `/usr/local`.
* Silencing ZSH errors by reversing the permissions change for `usr/local/share/zsh`.
* Debugging why `rbenv install` was failing. (Because my problem seems to have
  been caused by a recent change in macOS Big Sur, I couldn't just fall back on
  the wisdom of the ancients. But this meant that I actually got to
  [contribute](https://github.com/rbenv/ruby-build/issues/1710#issuecomment-774555962)
  to the wisdom.) 

Second, I knew [there's only so much that can be accomplished in such a short
time](https://norvig.com/21-days.html). Even if I hadn't run into any problems
following a quickstart guide, a quickstart is just that&mdash;a start. I wanted
to spelunk through the code to try to understand what each piece was doing.

Switching to Jekyll made this much easier. In addition to [great
documentation](https://jekyllrb.com/docs/step-by-step/01-setup/), Jekyll's use
of templating allows it to be very concise. Compared to my previous site built
with a Pelican theme, my Jekyll site with the Poole theme has 3x fewer lines of
HTML, 5x fewer lines of CSS, and no JavaScript.

Now that I have site that does truly feel like my own, the next step is just to
write.
