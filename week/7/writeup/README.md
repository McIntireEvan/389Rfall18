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

I started by running `strings binary` to see what I could find. The only useful info I got was the output of the program "Where is your flag?". I moved on and ran `objdump -d -M intel binary` to hopefully get a sense of what was going on. In the <main> section, I noticed a lot of calls to `mov`, later followed by `fopen` and `fwrite`. I decided to investigate the hex that was being written.

I got the values 0x74 0x6d 0x70 0x2f 0x2e 0x73 0x74 0x65 0x67 0x6f 0x0, which convert to tmp/.stego

Lo and behold, there was a file there. I brought it to this directory, and was met only with garbage when running `strings`. However, `binwalk` revealed it contained a jpeg, 1 byte in - a look in a hex editor shows that the first byte of `stego` is null. We can extract it with binwalk, and we get a picture of a stegosaurus. Running `strings` gives nothing, and running `steghide` gives the error `Unsupported marker type 0x0a`. Looking at the end of the file, the end bytes were wrong (`FF 0A` rather than `FF D9`). Fixing this lets us correctly `steghide` on it, and with the password `stegosaurus`, we get the flag `CMSC389R-{dropping_files_is_fun}`

