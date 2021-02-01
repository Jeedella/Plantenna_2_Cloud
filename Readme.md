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
-   [creating a dashboard](https://thingsboard.io/docs/iot-video-tutorials/#dashboard-development-guide-part-1-of-3-visualizing-assets-data-using-maps-and-tables)
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

The new group will not have access to the virtual machine anymore. A new one should be created.
After doing the installations above, follows these steps:
-   Download the backup file and transfer it using SCP to your VM
-   log in to the postgreSQL using the following command: `psql -U postgres -d postgres -h 127.0.0.1 -W`
-   Restore the database using the following command: `psql -U postgres -d postgres -h 127.0.0.1 -f thingsboard.sql.bak`
Now you should see data being restored.






