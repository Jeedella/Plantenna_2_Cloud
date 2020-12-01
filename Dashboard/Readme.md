# Installation and setup of Thingsboard

## AWS setup
First of all, you should have setup an AWS EC2 instance on which Thingsboard will be installed. If not, please refer to this [guide](https://github.com/Jeedella/Plantenna_2_Cloud/blob/master/Cloud/Readme.md)

## Installation of Thingsboard for Ubuntu
Please not that Thingsboard Community Edition is being used. This is an open source and free setup. There is a Professional Edition which will not be used.
To install Thingsboard, follow the steps in this [guide](https://thingsboard.io/docs/user-guide/install/ubuntu/)

## HAPROXY for Ubuntu
If you installed Thingsboard on your local machine with a GUI, you can access Thingsboard with *http://localhost:8080/*
If you installed it on the AWS EC2 instance, you must install HAPROXY to be able to access the website from Chrome or Firefox.
Please refer to [this](https://thingsboard.io/docs/user-guide/install/pe/add-haproxy-ubuntu/) guide for the installation of HAPROXY

When the installation is finished, you can access Thingsboard using the IP address configured for your AWS EC2 instance.
The standard login credential are: 
    - System Administrator: sysadmin@thingsboard.org / sysadmin
    - Tenant Administrator: tenant@thingsboard.org / tenant
    - Customer User: customer@thingsboard.org / customer

## Registering your first device
It is time to register your first device!
Steps to register the device:
    1. On the left pane, go to devices
    2. On the right, there is a '+' sign, click on that, choose *add new device*
    3. A new tab will pop up.
    4. Fill in the name and device type. Optionally enter a description.
    5. Congrats, you just created your first device!

## Retrieving Device Token
You will need the device token to connect to it using MQTT. To retrieve the token:
    1. Click on the device you created.
    2. A tab will open, click on *COPY ACCESS TOKEN*
    3. Paste this token in your script

## Create your first Dashboard
To create your first dashboard, follow the steps:
    1. On the left pane, click on Dashboards
    2. On the right, there is a '+' sign, click on that, choose *Create new dashboard*
    3. Give it a title and optionally a description
    4. Click on your created dashboard, a tab on the left will open. Click on *open dashboard*
    5. The page is empty. On the left bottom there is a orange button, click on that. CLick on the '+' button and then *create new widget*
    6. A tab on the right will open. Choose the widget type you want. 
    7. Add a datasource which can come from you device. It will ask you to create a new alias. Do that.
    8. If you configured everything correctly, the widget will appear and new data will be visible!

For more explanation about this please refer to this [link](https://thingsboard.io/docs/samples/raspberry/temperature/)

