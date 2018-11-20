Writeup 10 - Crypto II
=====

Name: Evan McIntire
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 10 Writeup

### Part 1 (70 Pts)

There was a lot of trail and error involved in the making of the script this week!

To start, I used `nc` manually to get a feel for the tool and how it worked, what sort of output to expect, etc.

I realized I would have to use the script to get the full picture, so I quickly dove in and started writing.

To begin, I started with section 1. Overall, it was fairly straightforward: Talk with the server, send our message to get signed, and get that hash.

The real trouble began with part 2.

At first, I didn't fully understand how the padding was supposed to be constructed. I didn't add the length in at all, and was adding '0x00' instead of '\x00', leading to really lengthy payloads that then messed with the `sock.recv` calls, leading to messages being split between different secret length attempts.

Looking back at the lecture slides, after awhile I realized my mistakes and started over. Before tackling padding, I first dealt with the message length. I knew I had to store it in a little endian way, and I figured the structs package we used before would be useful. A quick google search shows that was correct, and I had the message length portion done.

With that out of the way, I was able to correctly reason about the maximum amount of space padding could take up, and create a string accordingly. I originally had a for loop what did the string concatination, but I wondered if there was a better way. Sure enough, we can just multiply a string by a number. Gotta love python!

Now that I was able to correctly construct the payload, I tinkered around with the sends and recvs to get them right, and tested. After making sure all responses were where I expected, I removed a lot of the output, and added a check that would look for `Hmm...`, which is in the string we get when we fail. Running it again, one of the attempts (secret length 10) responded positively, giving the flag `CMSC389R-{i_still_put_the_M_between_the_DV}`

Answer in hand, I cleaned up and commented the code, and I was finished!

### Part 2 (30 Pts)


