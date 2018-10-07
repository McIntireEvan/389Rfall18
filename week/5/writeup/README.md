Writeup 5 - Binaries I
======

Name: Evan McIntire
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 5 Writeup

My first thought on the `my_memset` function was to get the basic functionality down as soon as possible. That is, I wanted to start by just copying the character onto the first memory location, before worrying about the rest.

Based on the information from the slides about parameter registers, I guessed that the three parameters would be in the registers `rdi`, `rsi`, and `rdx`. Using `mov [rdi], rsi`, I was able to see that my guess was correct - I overwrote the "World" string with a single z.

With that done, the next step was to loop. I put another label in the function, set `rcx` to be equal to the `rdx` parameter (strl). Then, I added the loop command, and made sure to increment `rdi` so it would move forward in memory each time.

After these changes, I tested, and it almost worked - `Hello World` became `Hello zzzzz`, which is missing the exclamation point at the end.

After some debugging and reading docs, I realized this was because `rsi` is so big that it overwrites the rest of the string. I found that `sil` is the lower byte of `rsi`, and after changing the instruction to `mov byte [rdi], sil`, we got the expected output!

For strncpy, I could tell I would have to do the same general approach, but instead of reading from `sil`, I'd be reading from the other memory location.

Since we can't do `mov [mem], [mem]`, I load the src char into `r8b`, and then read it into `[rdi]`; the dest char. I then move both forward one, and loop similarly to how I did in `my_memset`.

And with that, it worked! The biggest hurdle here was figuring out register sizes and how to only do a byte. Once that was done, the rest of it was pretty straightforward!