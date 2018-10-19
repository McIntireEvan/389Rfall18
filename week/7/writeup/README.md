Writeup 7 - Forensics I
======

Name: Evan McIntire
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 7 writeup

### Part 1 (40 pts)

1. The image is a JPEG, as told by the command `file image`

2. Chicago, Illinois. John Hancock Building./

3. `2018:08:22 11:33:24`, so August 22, 2018 at 11:33:24.

4. iPhone 8 back camera.

5. 539.5m Above Sea Level

6. From running `strings image`, we can find the flag `CMSC389R-{look_I_f0und_a_str1ng}`. From running `binwalk image`, there's another flag, hidden in a png in the image, with the flag `CMSC389R-{abr@cadabra}`

### Part 2 (55 pts)

I started by running `strings binary` to see if I could find the flag just in the binary. The only non-garbage string that it fount was the program's output, "Where is your flag?". I figured I would have to dig a little deeper, so I ran `objdump -d -M intel binary` to hopefully get a sense of what was going on under the hood. In the <main> section, I noticed a lot of calls to `mov` with hex values, later followed by `fopen` and `fwrite`. I decided to investigate the hex that was being written.

I got the values 0x74 0x6d 0x70 0x2f 0x2e 0x73 0x74 0x65 0x67 0x6f 0x0, which when converted into text gives tmp/.stego

Lo and behold, there was a file located in /tmp/.stego after I ran the program. I brought it to this directory, and tried running `strings`, but didn't find anything useful. However, `binwalk` revealed that the file contained a jpeg, 1 byte in (looking into a  hex editor shows that the first byte of `.stego` is null, showing that the person who made this file wanted to hide the magic bytes). We can extract it with binwalk (or remove the leading 00 in the hex editor), and when looking at the image, we get a picture of a stegosaurus. Running `strings` reveals nothing, and when I tried to run `steghide` , it gave the error `Unsupported marker type 0x0a`. I took another look in the hex editor, and found that the end magic bytes were wrong (`FF 0A` rather than `FF D9`). Fixing this lets us correctly `steghide` on it, and I guessed the password `stegosaurus`, based on the image itself. From it, we get the flag `CMSC389R-{dropping_files_is_fun}`
