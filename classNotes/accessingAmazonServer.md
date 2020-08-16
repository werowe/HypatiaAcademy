
Here is how to logon to Amazon virtual machine and start Jupyter and enable virtual environment.  You need to shutdown and restart Jupyter to add packages with pip.  Other than that Jupyter will run forever so you dont need to restart it to use it.  

```bash
source py35/bin/activate
```

Run this to upload your key to Amazon.  Get the instace-id from Walker.  You must use this key within 60 seconds or reupload it.  That's an Amazon security feature.

```bash

aws ec2-instance-connect send-ssh-public-key \
  --instance-id xxxxxxxxx
  --availability-zone eu-west-3c \
  --instance-os-user george \
  --ssh-public-key file://george.pub
```

Then logon like this

```bash   
 ssh -i ./yourname.pem yourname@walkercodetutorials.com
```
 
 At this point you can run **python** in order to start Python or start a Jupyter notebook.
 
 
 # Start Jupyter Notebook
 Start jupyter notebook like this. It will use port 8888 for first student and 8899 for the second.
 
 ```bash
 nohup jupyter notebook --ip=parisx&
 ````
 Type `more nohup.out` and look for **
 
 http://parisx:8888/?token=xxxxxxxxxxxxxxx
 
 change parisx to walkercodetutorials.com
 
 Type **quit** at top right of screen to shut it down to shut it down
