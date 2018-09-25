Writeup 3 - Pentesting I
======

Name: Evan McIntire
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag is `CMSC389R-{p1ng_as_a_$erv1c3}`. I got it by entering `localhost && cat /home/key.txt` as the input to the prompt. When thinking about how to approach this, the obvious vector to attack from was input to the uptime script. I played around with it, and after a short time realized that if you added more commands afterwords using &&, it would execute them, with the script probably doing something like `ping $input`, allowing me to add commands afterwards to explore and find the flag. (After going back and finding the script in /opt/container_startup.sh, I confirmed that it acted this way.) From there, the data we want would probably be in the home directory, so I went there, and got the key.

Fred could do a few things to secure his uptime tool. First, he should do some sort of input sanitization/filtering. Allowing arbritary input to be run by the script is a very bad idea, and is vulnerable to command injections (like we did here). Having the script ensure the input looks like an IP, or escaping the input in such a way that it is only passed as an input to `ping` would be a huge step up. Another thing he should do is reduce the permissions of the user running the uptime script. Allowing the user to see files and directories that it doesn't need for this script means that even if the command injection is fixed, another exploit getting access to the user is still possible and could be very dangerous. In addition, Fred could look into installing tools on the server that would alert him of repeated connections like this, so he could investigate and detect if any sort of intrusion is taking place. This is less likely to be useful compared to the other two forms of protection, though.

### Part 2 (55 pts)
My approach to implemeting the shell was pretty much an automated version of what I was doing to find the flag. I keep track of the current working directory locally, and then for each command, before executing the command I attempt to `cd` to that directory. Another thing of note is that because we can do any shell input, I route the response from the ping to `/dev/null` so that we don't have to try and hide any of that on the local side. For the `pull` command, I just run `cat <remote-file>`, get the response, and write it to a `local-file`. Right now it probably can't handle large files, but an improvement could be made where it first runs a command to find the size of the file, and then during the `cat` command, reads enough to get the whole file. Another possible improvement would be to get and display errors from the remote server, as right now it displays nothing. Buiilding off of that, we could check the validity of `cd` commands, instead of just assuming they'll work. The overall file could be somewhat cleaner too, but due to Python's scoping issues it's a bit hard, but overall not a big deal, because not every server would be exploitable in this way, so it'd be hard to just take this script and apply it to other servers.