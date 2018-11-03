Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Evan McIntire
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Yes. Based on looking at ICMP records, we can see that a traceroute was done on http://216.58.219.238/, which redriects to Google.

2. laz0rh4x and c0uchpot4doz

3. 104.248.224.85:33794 is laz0rh4x, who is connecting from North Bergen, New Jersey

206.189.113.189:53878 is c0uchpot4doz, who is connecting from London

4. They're using port 2749

5. They mentioned something was happening, but not what. It is happening at "15:00 tomorrow". The message was sent on October 25th, so that means whatever it is, it happened on October 26th.

6. They mentioned that the updated plans were at https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. They're expect to see each other 'tomorrow' (Oct 26th)

[Sections](2018-11-02-170833_640x291_scrot.png)

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. It was generated at Unix Timestamp 1540428007, which is Thursday, October 25, 2018 12:40:07 AM, GMT

2. lax0rh4x is the author.

3. It says it has 9 sections, but we encounter 11 sections.

4. [Sections](2018-11-02-170727_216x989_scrot.png)

5. From the PNG, CMSC389R-{c0rn3rst0n3_airlin3s_to_the_m00n}
From diffing section 6, CMSC389R-{PlaIN_DIfF_FLAG}