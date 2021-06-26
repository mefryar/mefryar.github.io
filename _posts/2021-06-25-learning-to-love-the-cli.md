---
layout: post
title: Learning to Love the Command Line
---

### What's a gooey?

Like most people, before I started programming, I interacted with my computer by
clicking, dragging, and typing into windows. To open a file, I'd first click on
the Finder (Mac) or Explorer (Windows) icon, then click on folder icons until I
could see the file icon I wanted, then double click on the file icon. To delete
a file, I could just drag it to the [trash (Mac) or recycle bin
(Windows)](https://ux.stackexchange.com/a/55967) icon. To edit a document, I'd
open Microsoft Word or Google Docs.

All of this was remarkably easy, even intuitive in the best cases. I later
learned that these visual representations of files and programs that can be
controlled through clicking are known as [graphical user
interfaces](https://www.britannica.com/technology/graphical-user-interface), or
GUIs (sometimes pronounced 'gooey'). Like the [fish that doesn't know what water
is](https://lifehacker.com/fish-dont-know-theyre-in-water-5821126), I didn't
even know they had a name because I didn't know there was any other way to
interact with a computer.

### What's that black window the nerds are using?

When I interned with [Juntos](https://juntosglobal.com/about/) in the summer of
2013, I got a glimpse at another way to interact with computers. The two weeks I
spent in the Mountain View office before I headed to Bogotá and Mexico City were
the first time that I got to see software engineers in the wild. I remember
being struck by the fact that, whenever I peeked at their screens, they often
had open a black window with text in a retro-looking font. Why, I wondered, were
the people who knew the most about computers using something that looked like it
was straight out of the 1980s?

I now know that the reason their screens looked like something straight out of
the 1980s is because, in a way, they were. The black window they were using was a
terminal emulator; that is, something designed to *emulate* the [computer
terminals](https://en.wikipedia.org/wiki/Computer_terminal) like the [DEC
VT100](https://en.wikipedia.org/wiki/VT100), which became popular in the 1980s
as a replacement for [punched
cards](https://en.wikipedia.org/wiki/Computer_programming_in_the_punched_card_era)
and paper tape.

![DEC VT100](/assets/images/DEC_VT100.png "DEC VT100")
*DEC VT100 computer terminal. Although production stopped in 1983, they have
lived on through emulators.*

That still begs the question though, why continue emulating something from the
1980s? Now that operating systems like macOS Big Sur come with beautiful
graphic user interfaces, why is the terminal emulator still an essential
application for programmers? The answer, I've learned, is that terminal
emulators offer a powerful way to interact with a computer: the command-line
interface.

![macOS Big Sur](/assets/images/macOS_BigSur.jpeg "macOS Big Sur")
*macOS Big Sur. Although focused on graphic user interfaces, it still includes
a [terminal emulator](https://en.wikipedia.org/wiki/Terminal_(macOS)).*

### You can just use the keyboard

A [command line
interface](https://launchschool.com/books/command_line/read/introduction), or
CLI, allows you to interact with the files and programs on a computer by
typing out commands from a keyboard. Unlike a *graphic* user interface, the
command line is *text* based, meaning you can just use the keyboard.

The first time I used the command line, I wanted to cry, "I can *just* use the
keyboard?" I felt like I had been asked to navigate an unfamiliar room where
someone had just turned out the lights. Instead of a window with a menu of
commands and icons I could click on, I just sat staring at that black window.

![Blank Command Line](/assets/images/blank_cli.png "Blank Command Line")
*A blank command line.*

The learning curve seemed steep and intimidating. Because there were no menus, I
had to learn commands through a combination of observing mentors and lots of
searches like "how to delete a file using command line" and "how to search a
file using command line".

The lack of menus meant that I also had to memorize the commands that I learned.
This was made more challenging by the fact that most commands were either terse
abbreviations, like `rm` to delete or "remove" a file, or entirely non-mnemonic,
such as [`grep`](https://en.wikipedia.org/wiki/Grep) to search a file.

However, all the effort to move up that learning curve now feels like time well
spent since it has allowed me to leverage the power of the command line.

### The power of the command line

In my first draft of this post, I wrote that, for me, much of the power of the
command line comes down to speed. However, a segment of an episode of the
[Cognicast](https://www.cognitect.com/cognicast/160)[^fn-cognicast] that I was
listening to this morning made me realize that speed wasn't what I wanted to
emphasize.

[^fn-cognicast]: The segment, which is from 8:00 to 9:30 discusses the quote, attributed to Rich Hickey that "Programming is not about typing, it's about thinking."

What I care about is not speed but productivity. I care less about the time it
takes me to accomplish a given task than about the tasks I can accomplish in a
given time.

Learning how to use the command line has made me more productive because it has
helped me to become more intentional. If I am not intentional when typing out a
command, it either won't execute, or worse, it will do something other than what
I intended.[^fn-grep]

[^fn-grep]: Like the multiple times I have entered `grep -r 'some pattern'` and left off the directory.

This means that I'm almost always *slower* whenever I'm first trying to learn
how to use the CLI to do a task for which I previously used a GUI. The
productivity gains only come after I invest the time to think about exactly what
it is that I want to do and how to translate that into a precise command.

### Three scenarios where I've come to use the CLI

To offer some examples, (though not an exhaustive list), here are three
scenarios where I've come to use the command line rather than a graphic user
interface.

#### 1. Using the CLI makes me more productive because it allows me to automate something repetitive

Sometimes the productivity gains from using the CLI to complete a task do
primarily come down to speed. This is often the case when what I want to do is
simple conceptually but repetitive. For example, let's say that I have some
wedding photos named `IMG_1.png`, `IMG_2.png`, and so on, that I want to rename
to `best_day_ever_1.png`, `best_day_ever_2.png`, etc. This would be
time-consuming to do via a GUI even if I only have 10 photos but a single
command can do this type of renaming for thousands of files.

#### 2. Using the CLI makes me more productive because it forces me to understand what I'm trying to do

For other tasks, using the CLI might only be marginally faster. However, it
makes me more productive over time because the requirement to be precise forces
me to gain a better understanding of what I'm trying to do. One example of this
is navigating project codebases. Especially at first, it was easier to open a
file by searching for it by name without having to know where it was located in
the project's nested folder structure. Although it is possible to search for a
file by name from the CLI, to open it from the CLI I have to specify the full
path. Opening files from the CLI in this way has helped me gain a grasp of why
those project folders are structured the way they are. As a result, I can now
learn something about a file even before I open it just by looking at where it's
located.

#### 3. Using the CLI may or may not be more productive but it feels more fun!

Finally, even when the productivity gains of using the CLI for a particular task
are doubtful, sometimes it just feels more fun! It makes me feel closer to the
metal, which I gather is a large part of why car enthusiasts prefer to use a
stick shift. There's also an element of initiation, the sense that I'm learning
the magic incantations of the ancients. It has helped a lot in my journey that
I've been able to go at my own pace, choosing to explore when it feels fun
without being compelled to do things any particular way.

### Don't fear the learning curve

Picking the right problem to work on matters far more than the tools you use.
But learning how to use the command line has added a tool to my belt that I
didn't even know existed before.

So if you find yourself someday staring at that black window, don't be afraid.
You can figure it out. It could make you more productive. And you might even
learn to love it.
