---
layout: post
title: Learning Clojure &mdash; Interactive Programming and Deliberate Practice
---

## Why Learn Clojure?

This month, I have started a new chapter since [Juntos has been acquired by
Nubank](https://juntosglobal.com/a-personal-letter-from-our-ceo/)! Among the
many, many things I find exciting about Nubank is that their tech stack is
primarily [built on top of
Clojure](https://building.nubank.com.br/welcoming-cognitect-nubank/). To try to
hit the ground running, I spent much of the past month trying to learn
[Clojure](https://clojure.org/).

The goal of this post is to share some of the strategies that I found helpful in
my learning journey in the hope that it might be of use to others who also
decide to learn Clojure. In particular, I focus on how embracing Clojure's
interactive programming flow, REPL-Driven Development, accelerated my
learning by enabling deliberate practice.

The rest of this post is organized as follows:
* [Overview of resources for getting started with
  Clojure](#resources-for-getting-started-with-clojure)
* [Brief definition of REPL-Driven Development](#repl-driven-development)
* [Overview of how to combine resources with REPL-Driven Development to
  enable Clojure deliberate practice](#clojure-deliberate-practice)
* [Appendix: Local setup for Excercism + REPL-Driven Development in
  Vim](#appendix-local-setup-for-excercism--repl-driven-development-in-vim)

## Resources for getting started with Clojure

Since the time that I began trying to learn Clojure, Peter Strömberg has created
a new [Getting Started with Clojure
guide](https://calva.io/get-started-with-clojure/) that I would recommend over
the resources that I used. It leverages Gitpod and Calva to allow for
REPL-Driven Development right from your browser with zero installation. In the
next section, I'll define REPL-Driven Development, but first I'll briefly
describe the resources I used just to give a sense of what else is out there.

When I started my learning journey, I began by reading the official [Learn
Clojure](https://clojure.org/guides/learn/syntax) guide, which provides a
concise overview of syntax, functions, and data structures. For my first
hands-on-keyboard practice, I then turned to the elementary exercises on
4Clojure.com. As it turned out, I was one of the last to get to learn on
4Clojure.com since it was [shut
down](https://groups.google.com/g/clojure/c/ZWmDEzvn-Js?pli=1) at the end of
July 2021. However, Peter Strömberg has also created a new version named [Rich
4Clojure](https://calva.io/get-started-with-clojure/#learn-and-practice-clojure-using-rich-4clojure)
that, like the Getting Started guide and unlike the original 4Clojure, allows
for REPL-Driven Development with zero installation. Another nice addition is
that Rich 4Clojure allows you to see the tests used to check your solution. And
while Rich 4Clojure is working to build up a new history of community solutions,
[4ever-clojure](https://4clojure.oxal.org/), another copy of the original
4Clojure, allows you to view the solutions archive from the original site.

Since the original 4Clojure didn't allow for REPL-Driven Development within the
browser, when I decided to try to learn via REPL-Driven Development I turned to
[Exercism.io](https://exercism.io/). I first learned about Exercism when my
friend Angela [blogged their
praises](https://www.angelaambroz.com/blog/posts/2021/Apr/01/in_praise_of_exercismio/).
Getting set up for REPL-Driven Development via Exercism on your machine *does*
include installation, which is why I now recommend Peter Strömberg's Getting
Started with Clojure guide instead. For those who do want to try Excercism with
Vim, I've listed the setup steps
[at the end of this post](#appendix-local-setup-for-excercism--repl-driven-development-in-vim).

## REPL-Driven Development

In lurking on the very friendly [Clojurians
Slack](https://github.com/clojurians/community-development), one of the
questions that caught my eye was a request for advice about what to practice as
a beginner who wants to become a more productive Clojure programmer. The first
answer from [Sean Corfield](https://github.com/seancorfield) was to learn how to
leverage the Clojure interactive programming workflow known as REPL-Driven
Development.

The [REPL](https://clojure.org/guides/repl/introduction) (short for "Read, Eval,
Print, Loop") enables *interactive programming* in Clojure by allowing for
expressions to be evaluated one at a time. In Sean's pithy summary, REPL-Driven
Development involves adherence to two maxims:
1. Always work in your editor, never type into the REPL.
2. Always evaluate every change you make as you make it.

## Clojure Deliberate Practice

Using REPL-Driven Development to solve problems, like those from 4Clojure and
Exercism, accelerated my learning because it enabled deliberate practice. The
term deliberate practice comes from the research of psychologist K. Anders
Ericsson who studied people achieve expertise. Ericsson argued that the key to
achieving expertise in any domain is "deliberate practice," which ["entails
considerable, specific, and sustained efforts to do something you can’t do
well—or even at all."](https://hbr.org/2007/07/the-making-of-an-expert) More
than just exerting effort on a challenging task, Ericsson
[defined](https://graphics8.nytimes.com/images/blogs/freakonomics/pdf/DeliberatePractice(PsychologicalReview).pdf)
deliberate practice as requiring that:

1. "The design of the task should take into account the preexisting knowledge of
   the learners."
2. "[Learners] should receive immediate informative feedback and knowledge of
   results of their performance."

Ericsson's research has received some fair
critiques,[^fn-deliberate-practice-critics] but I have nonetheless found it a
useful framework for explaining why I have found that solving problems like
those from 4Clojure and Excercism with a REPL-Driven Development workflow has
been effective for learning Clojure. 

[^fn-deliberate-practice-critics]: This [blog post](https://improvingteaching.co.uk/2018/10/28/critiquing-deliberate-practice-is-it-useful-in-teacher-education/) has a concise but nuanced summary of the criticisms of Ericsson's research. For an academic summary see [Hambrick et al. (2020)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7461852/).

In particular, this combination facilitated deliberate practice for me in five
ways:

1. The problems on 4Clojure and Excercism are specifically targeted at beginners
   and designed to help them incrementally learn the fundamentals of Clojure so
   that I was always stretching just beyond my comfort zone.

2. Working inside an interactive development environment, like Gitpod + Calva in
   your browser or any of the number of options for local IDEs (IntelliJ +
   Cursive, Emacs + CIDER, Vim + vim-fireplace, Neovim + Conjure), helped to
   build my knowledge by making it easy to look up the documentation for
   functions as I encountered them for the first time.

3. Using a REPL-Driven Development workflow allowed for immediate informative
   feedback since I could evaluate each incremental code change.

4. The fact that Rich 4Clojure and Excercism allowed me to see the tests provided
   feedback on edge-cases that I should consider and helped me to learn to write
   good tests in Clojure.

5. The ability to view community solutions on 4ever-clojure and Exercism.io gave
   me feedback about how to make my solutions more idiomatic, allowing me to
   learn from the accumulated expertise of the entire Clojure community.

I'm still far from an expert and, even after I've had a chance to practice a lot
more, there will always be more to learn. But I've come a long way from where I
started and I'm excited to continue the journey.

## Appendix: Local setup for Excercism + REPL-Driven Development in Vim

Before I began, I was intimidated by the prospect of setting up my local
development environment for REPL-Driven Development. Partly, I feared it would
be time-consuming and confusing. Partly, I hesitated because I was unsure
whether I should switch from [Vim](https://opensource.com/resources/what-vim) to
[Spacemacs](https://www.spacemacs.org/) so that I could use the popular
[CIDER](https://cider.mx/) interactive development environment.[^fn-vim]

[^fn-vim]: I switched from Sublime Text to Vim around the beginning of 2021 and had been getting a lot of joy out of learning Vim. However, I learned from the [State of Clojure 2021 Survey](https://www.surveymonkey.com/results/SM-S2L8NR6K9/) that Vim is a distant fourth in the ranking of the most popular editors for Clojurians (at 8.66% of respondents), with Emacs + CIDER (44%) and IntelliJ + Cursive (31%) being the two most popular.

While I hesitated, I spent a lot of time typing into the REPL.

Ultimately, I chose to just stick with Vim and set up
[vim-fireplace](https://github.com/tpope/vim-fireplace) to connect to a REPL
from my editor and I'm very glad I did! I plan to try out Neovim + Conjure in
the future but I'm glad that I chose to start with vim-fireplace since it
allowed me to just focus on learning Clojure but at a much faster rate (which is
what
[multiple](https://www.reddit.com/r/Clojure/comments/cleuqn/beginning_clojure_should_i_switch_to_spacemacs_or/evv5e9r?utm_source=share&utm_medium=web2x&context=3)
[Redditors](https://www.reddit.com/r/Clojure/comments/cleuqn/beginning_clojure_should_i_switch_to_spacemacs_or/evvcrhs?utm_source=share&utm_medium=web2x&context=3)
[recommended](https://www.reddit.com/r/Clojure/comments/cleuqn/beginning_clojure_should_i_switch_to_spacemacs_or/evv9d6y?utm_source=share&utm_medium=web2x&context=3)).

In case it helps inspire others to take the leap, below is an outline of how I
set up my local development environment for learning Clojure with Exercism and
Vim. It's not intended to be a step-by-step walk-through since specific
instructions might go stale.[^fn-exercismv3] Instead, the goal is to list the
basic steps in the hope of reinforcing that it really isn't that complicated.

[^fn-exercismv3]: In fact, as I write this on August 28, 2021, we are days away from the launch of Exercism v3 which will introduce a new online editor that enables solving exercises directly in the browser without setting up anything locally, though the CLI tool will remain.

### Installing Exercism

This was really easy thanks to Exercism's excellent
[walkthrough](https://exercism.io/cli-walkthrough).

### Install Clojure

Following [Exercism's advice](https://exercism.io/tracks/clojure/installation),
I set up Clojure by installing
[Leiningen](https://github.com/technomancy/leiningen) via Homebrew. (Leiningen is a build
tool that allows you to run Clojure code and, importantly, provides access to a
REPL.)

### Install cider-nrepl

This step was a bit confusing at first but would up being simple. All I had to
do was create a `~/.lein/profiles.clj` and then paste the
[suggested](https://docs.cider.mx/cider-nrepl/usage.html#via-leiningen) minimal
`profiles.clj`. ([CIDER nREPL](https://github.com/clojure-emacs/cider-nrepl) is
a "collection of [network REPL](https://github.com/nrepl/nrepl) middleware" that
enhances vim-fireplace.)

### Install vim-fireplace

Also, a little bit confusing since the README for
[vim-fireplace](https://github.com/tpope/vim-fireplace) simply says "Install
Fireplace using your favorite package manager, or use Vim's built-in package
support," and then gives step-by-step instructions for the latter but no
instructions for the former.  However, again, it was simple in the end, since I
just had to [add a
line](https://github.com/mefryar/dotfiles/commit/11862f63e0367ab44a7e765cb4b17aa5560a6198)
to the plugins section of my `.vimrc`.[^fn-vim-plug] (vim-fireplace is what
allows Vim to talk to the nREPL so that you can evaluate Clojure code without
having to leave Vim.)

[^fn-vim-plug]: I initially agonized over which Vim plugin manager to use. (Astute readers might be noticing a pattern.) I have been happy with my choice of [vim-plug](https://github.com/junegunn/vim-plug) but think [Vundle or Pathogen](https://vi.stackexchange.com/q/388/33828) would have been fine too.

### Install clj-kondo for linting

I love code linters. I learned more about how to write idiomatic Python and Ruby
from [flake8](https://flake8.pycqa.org/en/latest/) and
[RuboCop](https://rubocop.org/), respectively, than from any other single
source. I chose [clj-kondo](https://github.com/clj-kondo/clj-kondo) since I'm
using the Vim plugin ALE and clj-kondo is one of two linters that [ALE supports
for
Clojure](https://github.com/dense-analysis/ale/blob/master/doc/ale-clojure.txt).

I used Homebrew to [install
clj-kondo](https://github.com/clj-kondo/clj-kondo/blob/master/doc/install.md#brew-macos-and-linux)
and then
[added](https://github.com/mefryar/dotfiles/commit/4ff32b8f470bdaaae54c2dca8596c0ed5840d32f)
`clj-kondo` to the list of ALE linters in my `.vimrc`

### Hello Excercism + vim-fireplace 

Now that your setup is complete, here's a short example using Exercism's [Hello
World exercise for
Clojure](https://exercism.io/tracks/clojure/exercises/hello-world) to illustrate
how a REPL-Driven Development workflow facilitated by vim-fireplace can be used
to solve Exercism problems and get the kind of feedback that is central to
deliberate practice.

First, start a terminal session and download the exercise via the Exercism CLI
tool. (When viewing the exercism on Exercism.io, there is a helpful button to
copy this code.) 

```
$ exercism download --exercise=hello-world --track=clojure
```

Second, start another terminal session (either in a new window or a new tab if
using an emulator like
[iTerm2](https://iterm2.com/documentation-general-usage.html)), change to the
directory containing the Leiningen project for the exercise, and begin a REPL.

```
$ cd ~/Exercism/clojure/hello-world
$ lein repl
```

Next, return to your first terminal session and use Vim to open up the file
where you'll encode your solution.

```
$ cd ~/Exercism/clojure/hello-world
$ vim src/hello_world.clj
```

You should now see a file that looks like this:

```
(ns hello-world)

(defn hello [] ;; <- arglist goes here
  ;; your code goes here
)
```

#### 1. Getting Feedback From Documentation

My own first attempt at this solution looked like this:

```
(ns hello-world)

(defn hello [] (println "Hello, World!"))
```

Before I even try to evaluate this function, vim-fireplace allows me to get
feedback by looking up documentation without having to leave my editor. The
author of vim-fireplace, Tim Pope, [was brand new to
Clojure](https://github.com/tpope/vim-fireplace#navigating-and-comprehending)
when he starting working on the plugin so it includes the following mappings for
understanding code:
* `K` is mapped to look up the symbol under the cursor with `doc`
* `[d` is mapped to look up the symbol under the cursor with `source`

If I place my cursor at the beginning of `println` and hit `K` in normal mode, I
can read the documentation for `println` to see if it is what I want. The
output, in the bottom left-hand corner of my screen will say:

```
-------------------------
clojure.core/println
([& more])
  Same as print followed by (newline)
```

I thought that was what I wanted so the next step was to evaluate the function
itself.

#### 2. Getting Feedback From Evaluating Functions In Your Solution

Before I was set up for REPL-Driven Development, I would evaluate functions by
copying and pasting them into the REPL running in the other terminal. However,
with REPL-driven development, there's an even better way. With my cursor inside
`(println "Hello, World!")`, from normal mode if I type `cpp`, vim-fireplace
evaluates the code and shows me the result in the bottom left-hand corner. In
this case, the result is:

```
Hello, World!
nil
```

This is clearly more efficient! But I was initially confused by the result. Then
I remembered that `println` returns `nil` and I want a function that *returns*
`"Hello, World!"` rather than printing it. Using this learning, I re-wrote my
function to look like this:

```
(ns hello-world)

(defn hello [] "Hello, World!")
```

To test this with vim-fireplace, I can execute `cpp` inside my `defn` to define
the `hello` function and then execute `cpp` inside `(hello)` to see what's
returned. Now all I see returned is `"Hello, World!"`. Looking better!

I can then use the vim-fireplace normal mode command `:Last` to open the
result in the preview window so that I can yank (copy) and then put (paste) the
result below the function into a section named "REPL Experiments" that leverages
Clojure's [rich comment
blocks](https://betweentwoparens.com/blog/rich-comment-blocks/#rich-comment).

```
(ns hello-world)

(defn hello [] "Hello, World!")

;; * REPL Experiments *

(comment
  ;; Check the return value of `hello` function
  (hello)
  )
```

I've found this practice of documenting REPL experiments helpful when
iteratively working to solve multi-part problems. My
[solution](https://exercism.io/tracks/clojure/exercises/run-length-encoding/solutions/808e90ad3256460bb72dd01017fcfb72)
to the Run Length Encoding problem includes an example of this.

### 3. Getting Feedback From Evaluating Functions In The Tests

To confirm that is what the test is expecting, I can open the test file
(`:e test/hello_world_test.clj`) which looks like this:

```
(ns hello-world-test
  (:require [clojure.test :refer [deftest is]]
            hello-world))

(deftest hello-world-test
  (is (= "Hello, World!" (hello-world/hello))))
```

The fact that Exercism allows me to see the test helps make the exercise more
targeted since it tells me exactly what my objective is. Given that I had never
written a test before in Clojure, seeing examples of how to write concise but
comprehensive tests is also a learning in and of itself.  Additionally, as the
problems get more complex, the tests have helped me think about edge cases that
I wouldn't have considered.

Using the same trick as before, I can evaluate the test without leaving my
editor by adding a line that calls the test function (`(hello-world-test)`) and
executing it by typing `cpp`. It returns `nil`, which means it passed! To
double-check, I can now exit my editor and run the test with `lein test` which
will output:

```
lein test hello-world-test

Ran 1 tests containing 1 assertions.
0 failures, 0 errors.
```

### 4. Getting Feedback From The Community

Now, I'm ready to submit my solution:

```
$ exercism submit src/hello_world.clj
```

This will return a link to an Exercism page where I can view my solution and,
more importantly, also get to see community solutions. Seeing others' solutions
has been a great way for me to learn about alternate approaches that I hadn't
considered and get a sense of whether my solution could be made more idiomatic.
