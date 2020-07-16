# Project Plant Sensing System -- Amazon Web Services Cloud (AWS)
This Readme file will contain a basic and very over the top setup guide for the AWS services needed to connect and deploy the system.
A list of further developments can be found at the end of this file. 

## Signing up to AWS
To use the services provided by AWS, an account is needed. Go to (https://aws.amazon.com/) and setup an account. 
Although at the end of the setup process a credit card is needed, all the services used in this project are within the free tier services. 
For more information about the free tier, please fo to (https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)
A more detailed file with the instructions and screenshots will be included in this repo.

## Setting up AWS environment
### Greengrass group: 
To set up the Greengrass group go to AWS Managment Console and click on Iot 
Once in the IoT dashboard, on the left panel select **Greengrass** --> **Group** 
Click on the **Create Group** --> **Default group creation**\
A *Grant permission* page might appear. If this is the case, grant permission and continue with the last step you made.\
Give a name to your group and to your core. Consider that the recomendation is to avoid sensitive information. Once you have given a name to both, click on the *Create Group and Core*\
The next screen will show a table with 4 security files. Click on the *"Download the resources as tar.gz"*. **ONCE YOU HAVE DOWNLOADED THE FILES**, click on the *"Finish button"* .
## Setting up the Greengrass core Device (Raspberry Pi):
Before continuing with the setup process, please make sure that your Raspberry Pi is connected to internet.\
Go to the terminal of the Raspberry Pi and run the following commands:\

```
sudo adduser --system ggc_user
sudo addgroup --system ggc_group
```
These command lines will create the name of the user and group that will be connected to AWS.\

### Improving security:
To improve the connection security over the Raspberry Pi with AWS, the ****98-rpi.conf**** file must be modified. Go to the directory where the file is located by running the following command: 

```
cd /etc/sysctl.d
```
Once in the correct directory, follow the next command to open the text and modify it: 

```
sudo nano 98-rpi.conf
```
Add the following lines: 
```
fs.protected_hardlinks=1
fs.protected_symlinks=1
```
Once the lines are added, save and close the file. Reboot the Pi.\
You will also need to modify the ****cmdline.txt**** file. In the terminal enter the following command: 
```
cd /boot/
``` 
To open and modify the file: 
```
sudo nano cmdline.txt
```
Once in the file, go to the end of the first line and enter the following text: 
```
cgroup_enable=memory cgroup_memory=1
```
**Make sure that the added text is at the end of the first line, not in a new one**\
Save and close the file. Reboot the Pi.

### Updating the Pi. 
The final step for getting the Pi ready for hosting the Greengrass Group, is to update it. Although all the latest versions are included when you download the OS, some of them might not be updated. Another important software that needs to be installed before continuing is Java 8. To do so, run the next command:
```
sudo apt update 
sudo apt install openjdk-8-jdk
```
### Downloading the Greengrass software
To succesfully connect the Pi as a core for the greengrass group, special software needs to be installed.\
Go to (https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html#gg-core-download-tab) and search for the architecture and distribution you are using.\
In the case of installing the software in a **Raspberry Pi** using the **Raspberry Pi OS**, download the option for the **architecture** *Armv7l*, **distribution** *Raspbian* and **OS** *Linux*.\
Download the file.\
From here, there are two was in which the installation can be done. If you are using the headless aproach, please follow the next steps. If the process is being done directly in the Pi, please download and install the software as you will normaly do. 
### Headless installation
Locate the folder in which the download was made. Enter the command line and change the directory to where the folder is.\
In this step, two files will be transfered to the Pi: The Greengrass Core software and the downloaded file, containing the security credentials. This file was donwloaded in the **Setting up AWS environment** section.\
When using **Windows** enter the following commands to transfer the files to the Pi:
```
pscp -pw PI-PASSWORD greengrass-OS-ARCHITECTURE-1.10.2.tar.gz pi@IP-ADDRESS:/home/pi
pscp -pw PI-PASSWORD HASH-setup.tar.gz pi@IP-ADDRESS:/home/pi
```
When using **Mac** enter the following commands to transfer the files to the Pi:
```
scp greengrass-OS-ARCHITECTURE-1.10.2.tar.gz pi@IP-ADDRESS:/home/pi
scp HASH-setup.tar.gz pi@IP-ADDRESS:/home/pi
``` 
**MAKE SURE YOU CHANGE THE WORD IN CAPITALS WITH THE CORRECT NAMES**\
Once the files have been transfered, go to the command line in the Pi and enter the following lines to unzip and install the files. Make sure you are in the **home/pi** directory.
```
sudo tar -xzvf greengrass-OS-ARCHITECTURE-1.10.2.tar.gz -C /
sudo tar -xzvf HASH-setup.tar.gz -C /greengrass
```
**Once more, make sure you change the words in capitals to the correct values**\
There is one last file that must be downloaded to the Pi before starting the connection. To do so, in the command line of the Pi go to:
```
cd /greengrass/certs/
```
Once in the directory enter the following: 
```
sudo wget -O root.ca.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
```
When the file is downloaded, the software setup in the Pi is finished and ready to make the connection with AWS. Please enter the following: 
```
cd /greengrass/ggc/core/
sudo ./greengrassd start
```
This last command will make the connection with AWS and should be run **every time** the Pi is rebooted.
