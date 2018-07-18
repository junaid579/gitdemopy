git --> version control 
--> repository management system


100 devs-->server-->code(US) --> www.fb.com --> homepage

100 devs -> single source --> to put all code 

--> drive for code

drive --> repository

2 kinds
-------
local repository --> local machine
remote repository --> server

--> git 
	--> technology 
	--> install --> use it 
	--> files / folders(directories)
--> remote repository
	--> git server (own)
	--> third party services
		->public repository --> free
		->private repository --> paid
			- github
			- bitbucket
			- gitlab

--> download git and run (install)

-->install git
-->create a folder (gitDemoPy)
-->initialise the local repository -- git init
-->git status (status of the initialised folder)

--> git architecture 
--------------------

local machine (folder) 
	- working directory --> my folder/files
	- staging area --> files will be hanging 
	- local repository --> store the files


commands 
--------
git init
git status --> red --> file is in working directory
git add <fileName> --> file gets added to staging area
git status --> green --> file is in staging area
git commit -m "<type some message>" --> file gets added to local repository
git status --> tree is clean

working directory == local repository

code --> local machine --> /Users/junaid/Desktop/gitDemoPy/.git/
code --> remote repository -->server -->github -->https://github.com/junaid579/gitdemopy.git

connection 
----------
git remote add origin https://github.com/junaid579/gitdemopy.git

push code from local to remote
-------------------------------
git push origin master







new line

