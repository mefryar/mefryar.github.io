---
layout: post
title: Learning to Love the Command Line
---

### What's a gooey?

Like most people, before I started programming, I interacted with my computer by
clicking, dragging, and typing into windows. To open a file, I'd first click on
the Finder (Mac) or Explorer (Windows) icon, then click on folder icons until I
could see the file icon I wanted, then double click on the file icon. To delete
a file, I could just drag it the [trash (Mac) or recycle bin
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
the 1980s is because in a way they were. The black window they were using was a
terminal emulator, that is, something designed to *emulate* the [computer
terminals](https://en.wikipedia.org/wiki/Computer_terminal) like the [DEC
VT100](https://en.wikipedia.org/wiki/VT100), which became popular in the 1980s
as a replacement for [punched
cards](https://en.wikipedia.org/wiki/Computer_programming_in_the_punched_card_era)
and paper tape.

![DEC VT100](/assets/images/DEC_VT100.png "DEC VT100")
*DEC VT100 computer terminal. Although production stopped in 1983, they have
lived on through emulators.*

That still begs the question though, why continue emulating something from the
1980s? Now that operating systems, like macOS Big Sur, come with beautiful
graphic user interfaces why is the terminal emulator still an essential
application for programmers? The answer, I've learned, is that terminal
emulators offer a powerful way to interact with a computer: the command line
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
keyboard?" I felt like I had been asked to navigate a unfamiliar room where
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

For me, most of the power of the command line comes down to speed. At first,
when I felt I was just poking around in the dark, the CLI was much slower than
using a GUI. But, with practice&mdash;lots and lots of practice&mdash;many tasks
are now faster when I use the command line. There are at least three reasons why
the command line is faster.

#### 1. Precision

When I want to open, rename, move, or delete a file, it's now almost always
faster to use the command line because it allows me to specify any file on my
computer by typing out the path where that file is saved rather than clicking
through a series of folders until I get to it. This facilitated by a command
line feature named [tab
completion](https://en.wikipedia.org/wiki/Command-line_completion) which allows
me to just type the first few characters, then hit the `TAB` key to fill in the
rest.

#### 2. Automation (Recursion)

Where the command line really shines is when I need to repeat a task for a
bunch of files or folders. For example, if I had some wedding photos
named `IMG_1.png`, `IMG_2.png`, and so on, with a single command I could
rename them all to `best_day_ever_1.png`, `best_day_ever_2.png`, etc. Even if
you have ten files to rename like that, being able to do so with a single
command is a big time savings compared to doing it manually. Just imagine the
savings when you have a thousand files or more.

#### 3. You can just use the keyboard!

Although it felt limiting at first, the ability to execute a series of tasks all
without having to take my hands off the keyboard really does make things faster.

Finally, even when the benefits are marginal, it feels more fun!

So if you find yourself someday staring at that black window, don't be afraid.
You can figure it out. And you might even learn to love it.  
