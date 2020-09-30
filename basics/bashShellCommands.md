# Bash Shell Commands

A **shell** means the window where you type commands on a UNIX system.  Bash is the most common one and the easiest to use.  

Both Ubuntu and Mac are based on UNIX.  Windows is not.  It's command shell is called DOS.  You get to that by running the `cmd` commmand on Windows.

The terminal on Ubuntu and Mac is a bash shell.  On Winows it is DOS.  In order to have a UNIX environment on Windows install cygwin.

On MAC you might have to run this command to change from the default shell to the Bash shell:

`chsh -s /bin/bash`

## location

* single dot (.) means here
* double dots (..) means one level above here

## print working directory

this means to show what folder you are in now

`pwd`

## change directory

this means go to your home directory<br/>

`cd`

go up one level and change to the **Downloads** folder<br/>

`cd ..\Downloads`

go to the **Downloads** folder<br/>

`cd Downloads`


## copy file

means copy file a.txt to b.txt<br/>

`cp a.txt b.txt`


## Exercise

go to Documents folder:<br/>

`cd Documents/`

make a directory called **bash**<br/>
`mkdir bash`

go to the bash directory you just made:<br/>

`cd bash`

now print where you are:<br/>

`pwd`

<br/>
/Users/walkerrowe/Documents/bash

Make a directory called **walker**.<br/>

`mkdir walker`

put the text **hello walker** into the file **hello.txt** in the **walker** folder.<br/>

`echo "hello walker" >> walker/hello.txt`

do a long listing (gives all file details) on the file **hello.txt** in the **walker** folder.<br/>

`ls -l walker/hello.txt`

-rw-r--r--  1 walkerrowe  staff  13 Sep 29 16:59 walker/hello.txt<br/>

go to the **walker** folder<br/>

`cd walker`

copy the file **hello.txt** up one level to the directory above it<br/>

`cp hello.txt ../`

list the contents of the folder one level above here you are:<br/>

`ls -l ../`
 
-rw-r--r--  1 walkerrowe  staff  13 Sep 29 17:01 hello.txt<br/>
drwxr-xr-x  3 walkerrowe  staff  96 Sep 29 16:59 walker<br/>
-rw-r--r--  1 walkerrowe  staff  13 Sep 29 16:59 walker/hello.txt


`pwd`

<br/>

/Users/walkerrowe/Documents/bash/walker

`ls .`

hello.txt<br/>

`ls ..`

hello.txt	walker

