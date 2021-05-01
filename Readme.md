# Smart Plant Monitoring System -- Cloud System
This document contains all the necessary information about the cloud system. How it is setup, and how to use it.

## Summary
-   Microsoft Azure Virtual Machine: This VM is used to host the cloud system on
-   Thingsboard IoT Platform: This is the platform on which the data will be presented 
-   AWS Route53: This is the Amazon service on which the current DNS name is purchased

## Microsoft Azure
NOTE: THIS PROJECT WAS FIRST WORKING ON AWS. DUE TO CHANGES, THIS PROJECT HAS BEEN MIGRATED TO AZURE

Microsoft Azure is comparable to AWS, but less complex. It is much more user friendly. A bonus is that each student has a 100 dollar to spend free on Azure. 

### Choosing a Virtual Machine
First of all, two things have to be considered when choosing a VM: The operating system and size.
-   Operating system: For the operating system, Ubuntu 18.04-LTS is required. 
-   For the size: This is a difficult one, because it depends on the budget. a 100 dollar budget is not enough to run a good sized VM for long. When we created the VM, a B1ms size was chosen. But after some time, this size was not enough due to lagging. So an upgrade has been made to B2ms. This is a better size, but still not enough for this system. 

### Accessing the Virtual Machine
To access the VM, an SSH connection is needed. For this, use your Windows/MAC terminal or an app like Visual Studio Code.
Make sure the Keypair is saved somewhere safe!

## Installation of Thingsboard for Ubuntu
Now the Virtual Machine is running, follow these guides to install Thingsboard
How to install Thingsboard on Ubuntu: https://thingsboard.io/docs/user-guide/install/ubuntu/

To check whether the Thingsboard instance is running, use the following command: `sudo service thingsboard status`

### Installation of Haproxy
How to install and setup openSSL: https://thingsboard.io/docs/user-guide/install/pe/add-haproxy-ubuntu/
You can skip step 1, 9 and 10

To check whether the Haproxy service is running, use the following command: `sudo service haproxy status`

If everything went well, you should be able to access your Thingsboard instance. This can be done with the IP address allocated by Azure

### Creating your first dashboard
Thingsboard has excellent guides on how to use their platform. The following links are very useful to learn how to register a device, and how to build your very own dashboard.
-   [Creating a dashboard](https://thingsboard.io/docs/iot-video-tutorials/#dashboard-development-guide-part-1-of-3-visualizing-assets-data-using-maps-and-tables)
-   [How to use MQTT to publish](https://thingsboard.io/docs/samples/raspberry/temperature/)
-   [How to use MQTT to subscribe](https://thingsboard.io/docs/samples/raspberry/gpio/)

## Setup a domain in Route53
Because the project started in AWS, a DNS has been acquired there. This has been done using AWS Route53. 

To setup a domain and link it to EC2 follow this guide: https://www.cloudbooklet.com/how-to-setup-route-53-for-your-domain-in-aws/\

The registered domain is plantenna.nl

# IMPORTANT: BACKUP OF POSTGRESQL
In this repository, a backup file is added named thingsboard.sql.bak
## !!!DO NOT REMOVE THIS FILE!!!
This file contains the backup of the database, which should be used if restoring is needed.

This backup file has been generated in Thingsboard version 3.2.1. This version uses OpenJDK 8.

The new group will not have access to the virtual machine anymore. A new one should be created.

## How to restore the database ##
1. Download the backup file and transfer it using SCP or Filezilla to your VM
2. Download OpenJDK 8
3. Download Thingsboard version 3.2.1
4. Download postgresql and set the password according to what is noted in "login_credentials_SPMS.xlsx"
5. Create database named 'thingsboard'
6. restore the database using the following command `psql -U postgres -d thingsboard -h 127.0.0.1 -f thingsboard.sql.bak`
7. Run the install script for thingsboard. Note that this will gives errors because there are already things excisting. This is normal. 
8. Start Thingsboard
Now if everything went well, the database should be restored.

If wanted, upgrading to newer versions of Thingsboard is now possible. Note that the newer update of thingsboard used OpenJDK 11. An upgrade to it is needed for the installation. 

--DISCLAIMER--
The restoring could be done using another method, with different installation steps. But the method explained here is verified to work. 
Just keep in mind, as long as the backup file is available, you won't lose anything. 








