Writeup 3 - OSINT II, OpSec and RE
======

Name: Evan McIntire
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Evan McIntire

## Assignment 3 Writeup

### Part 1 (100 pts)

There were a few big security issues - here are 3 of them, and some steps to address them.

1. Bad password

The password was very simple, easy to associate with personal data, and included in a password data breach.

The best way to rectify this would be to use a password generator/manager to create a unique, strong password. https://www.lastpass.com/ is a popular choice, but there are many other similar tools out there.

Password managers are recommended by both news outlets (https://www.theverge.com/2017/7/24/15921282/best-password-manager-1password-lastpass-dashlane-how-to), and are used widely in businesses. The point of having a password manager is that you can have many very complex, unguessable and hard to brute force passwords, while only having to remember the master password. They also help to avoid password re-use, and some will warn you if your password is in a known data breach.

2. Poor login configuration

In addition to the poor password, the login on the server was insecure. There was no lockout for wrong attempts, so a brute-force script was trivial to use. 

There are a few things that could be done here. One option is logging into the server using a ssh key (https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server), which also addresses the problem of having a poor password while ensuring that only you have access to the server. Another possible step is to set up a service like fail2ban (https://www.fail2ban.org), which will restrict IP addresses from connecting after suspicious behavior (i.e. many failed login attempts). This would hinder anyone trying to brute force their way in, and when combined with #1, would deter a lot of attackers.

3. Open ports

There were a lot of extraneous open ports on the server, which were all potential attack vectors.

Generally, only the standard ports should be open, so that internal software that can be exploited is not exposed.

There are a lot of things that can be done in this area, here are a few: 
- For web traffic and applications, use a (reverse proxy)[https://en.wikipedia.org/wiki/Reverse_proxy] to route to web apps that should run on a port. This means that the extra ports don't have to be opened, and you avoid the risk of some application using that port.
- Close extra ports using `iptables` or `ufw`. As previously mentioned, this reduces the surface area for attacks.
- Detect `nmap` and block ips with it, using `fail2ban`, as mentioned earlier. If an attacker gets blocked while nmapping, they might just give up there, and if not, it hinders them.