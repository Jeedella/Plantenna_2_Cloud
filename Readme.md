# Project Plant Sensing System -- Amazon Web Services Cloud (AWS)
This Readme file will contain a basic and very over the top setup guide for the AWS services needed to connect and deploy the system.
A list of further developments can be found at the end of this file. 

## The goal
The goal of the cloud part is to receive data from the gateway, and visualize it in a dashboard. This dashboard should also be able to send commands back to the gateway. For this an MQTT connection is needed. MQTT supports bi-directional traffic. 
There are a lot of dashboard available. Two dashboard that are open-source are Thingsboard (https://thingsboard.io/) and Thinger (https://thinger.io/). Both support multiple platform and are made to be installed on a server. For this project Thingsboard is chosen. 

## Signing up to AWS
To use the services provided by AWS, an account is needed. Go to (https://aws.amazon.com/) and setup an account. 
Although at the end of the setup process a credit card is needed, all the services used in this project are within the free tier services. 
For more information about the free tier, please fo to (https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)
A more detailed file with the instructions and screenshots will be included in this repo.

## Services available in AWS
AWS is a big cloud computing service with almost 175 different services. All those services can interact with each other. Keep in mind, AWS is not easy, but very complex. One wrong switch and the complete system is screwed. Be aware of that.
The services relevant for Smart Plant Monitoring System are:
    - IoT Core
    - EC2
    - Route53

IoT Core is a platform which has different types of services. Each of those can be used to send data to the cloud. Within IoT Core you can register things, which can be a Raspberry Pi, ESP32 or similar. Those things are your microcontrollers from which you are going to send data from. Each thing can be configured separately to do its job correctly. For more about this check the follow link: https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html
Another service within IoT Core is Greengrass. This is a service which makes it possible to deploy a server on the thing itself. This is called a greengrass core. Benefits of this system is you can integrate lambda functions on the core itself. And if the connection is lost, the data is saved in a temporarily place until reconnection, which then pushes the data to the cloud again. More about Greengrass: https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html
The service that will be used here is EC2 in combination with Route53. EC2 is an AWS service where you can create an instance in form of controller. You can access this controller by SSH to use it like a regular command line. On this EC2, a server will be installed which basically represents the dashboard needed to visualize the data. Example of a dashboard is Thingsboard or Thinger.io . Those dashboards support MQTT which is beneficial when bi-directional traffic is needed. More about EC2: https://aws.amazon.com/ec2/getting-started/
Route53 is used to generate a domain for this instance. Here you can purchase a domain and configure it to route your traffic to your EC2 instance. More about this: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html

## Setup of an EC2 instance
To setup an EC2 instance which is compatible with Thingsboard, follow this guide: https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html

## Associate an Elastic IP to your EC2 instance
Follow this guide: https://www.cloudbooklet.com/how-to-assign-an-elastic-ip-address-to-your-ec2-instance-in-aws/

## Setup of a domain in Route53
To setup a domain and link it to EC2 follow this guide: https://www.cloudbooklet.com/how-to-setup-route-53-for-your-domain-in-aws/\

## Installation of Thingsboard for Ubuntu
You should have created an EC2 instance for Ubuntu in AWS. Connect to this instance through SSH. 
When connected, follow this guide to install Thingsboard: https://thingsboard.io/docs/user-guide/install/ubuntu/

You have finished the installation and should be ready to start sending data to your dashboard!


