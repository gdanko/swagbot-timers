Last login: Fri Mar  9 10:12:34 on ttys004
[gdanko@SDGL141bb265b ~]$ cd git
[gdanko@SDGL141bb265b git]$ cd python-s3pypi/
[gdanko@SDGL141bb265b python-s3pypi]$ ./foo.py 
Traceback (most recent call last):
  File "./foo.py", line 8, in <module>
    import s3pypi.utils as utils
ModuleNotFoundError: No module named 's3pypi.utils'
[gdanko@SDGL141bb265b python-s3pypi]$ ll
total 16
-rwxr-xr-x@ 1 gdanko  CORP\Domain Users  2054 Mar  9 10:22 foo.py
drwxr-xr-x@ 5 gdanko  CORP\Domain Users   160 Mar  9 10:16 s3pypi
drwxr-xr-x@ 3 gdanko  CORP\Domain Users    96 Mar  9 10:04 scripts
-rw-r--r--@ 1 gdanko  CORP\Domain Users  1195 Mar  9 09:52 setup.py
[gdanko@SDGL141bb265b python-s3pypi]$ ll s3pypi
total 16
-rw-r--r--@ 1 gdanko  CORP\Domain Users  3257 Mar  9 09:48 exception.py
-rw-r--r--@ 1 gdanko  CORP\Domain Users     0 Mar  9 10:16 repo.py
-rw-r--r--@ 1 gdanko  CORP\Domain Users  3261 Mar  9 10:21 utils.py
[gdanko@SDGL141bb265b python-s3pypi]$ ll s3pypi
total 16
-rw-r--r--@ 1 gdanko  CORP\Domain Users  3257 Mar  9 09:48 exception.py
-rw-r--r--@ 1 gdanko  CORP\Domain Users     0 Mar  9 10:16 repo.py
-rw-r--r--@ 1 gdanko  CORP\Domain Users  3261 Mar  9 10:21 utils.py
[gdanko@SDGL141bb265b python-s3pypi]$ ./foo.py 
  File "./foo.py", line 13
    if executable:
    ^
IndentationError: unexpected indent
[gdanko@SDGL141bb265b python-s3pypi]$ ./foo.py 
/usr/local/bin/pip
[gdanko@SDGL141bb265b python-s3pypi]$ 
