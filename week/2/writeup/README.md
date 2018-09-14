Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Evan McIntire
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. First, just from doing a simple google search, I found his reddit and twitter (https://www.reddit.com/user/kruegster1990 and https://twitter.com/kruegster1990, respectively). Then, by searching his username using https://www.namechk.com/ I was able to find his Instagram (https://www.instagram.com/kruegster1990/). From there, I learned he's a fan of Pokemon, and that he's flying first class from BWI to SFO this December.

From his twitter profile, I found that he owns http://cornerstoneairlines.co and his email is kruegster@tutanota.com. I also found out he lives in Silver Spring, Maryland.

3. http://142.93.118.186/. I found this by pinging the http://cornerstoneairlines.co IP.

4. Going to http://cornerstoneairlines.co/robots.txt reveals http://cornerstoneairlines.co/secret, and the Flag: CMSC389R-{fly_th3_sk1es_w1th_u5}

5. http://142.93.117.193/ is the admin page, under contruction - found by just following a link.

6. For the IP the admin page, I found it is hosted with DigitalOcean, and physically located in New Jersey (using an IP lookup website).

7. It is running Ubuntu, with the Apache web server - going to any 404 page reveals this.

8. CMSC389R-{h1dden_fl4g_in_s0urce} on the main page

### Part 2 (55 pts)

First, I ran `nmap 142.93.117.193 -p-` and found a couple of open ports; 1337 being the one of interest. `nc 142.93.117.193 1337` confirmed that when I got a login prompt. I grepped the rockyou passwords for 'pokemon' (based on his interests), and decided to try a few of those passwords before brute forcing with the script.

To my surprise, I got in first try with the username `kruegster` and the password `pokemon`

From there, going to `/home/flight_records` and running `cat *.txt` gives a lot of flags - we know the correct one from his airline ticket on instagram!

```
CMSC389R-{c0rn3rstone-air-27670}
```

As for `stub.py`, the approach is simple - go through, one line of `rockyou` at a time, and try it along with the username we found. It stops when it reaches the correct one (a message other than fail). I also added `filter` variable which will only try passwords with that string as a substring
