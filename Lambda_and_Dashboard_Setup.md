# Lambda functions and Dashboard Setup
## Lambda Functions
Lambda functions are the main "protocol" AWS to interconnet its different services to work together. Hence, it is importat to know how to set them up and make them work correctly.\
The first and most important Lambda function that needs to be setup is the one enabling the comunication between the Greengrass Core and the Iot Platform from AWS.
## Lambda function for the Greengrass Core communication
Before writting any code, the Software Development Kit (SDK) needs to be downloaded. To do so, please enter to the next link: https://github.com/aws/aws-greengrass-core-sdk-python/ and download all the files.\
Within the folder, there is another one named "greengrasssdk" which contains all the libraries to create a successfull connection with AWS and the Greengrass Core. More on that topic will be covered in the following steps.
### Step 1.- Prepare the documents
From the files downloaded, you will need to create a new zip file. Go to the folder and select the next files:

-greengrassHelloWorld.py

-greengrasssdk folder

With these 2 files, create a new zip folder named *"hello_world_python_lambda.zip"*. Make sure that the zip file only contains these two files, otherwise it wont work.
### Step 2.- Creating the Lambda function
Go to the AWS Managment Console and search for the option **Lambda** under the section **Compute** and click on the **Create Function** option on the top rigth corner. In the next screen, you will be able to see 3 options. For this case, we will select the *Author from Scratch* option and you will name the function as *"Greengrass_HelloWorld"* and select *"Python 3.7"* as runtime option and click on the **"Create function"** button.\
In the next screen, scroll down until the *"Function code"* section appears. In the top rigth corner of that section, click on dropdown menu with the header *Actions* and select the *"Upload a .zip file"* option.\
Select the zip file created in step 2 (*"hello_world_python_lambda.zip"*) and upload it.\
Go to the section called *"Basic settings"* and click on edit. Make sure the **runtime** is selected as *"Python 3.7"*. Search for the **handler** option and define it as ***greengrassHelloWorld.function_handler***. Save the function.\
To publish the function, click on the **Actions** --> **Publish New Version** and click on the *Publish* button.\
After that, click on **Actions** --> **Create alias** and click on the **Create** button.
### Step 3.- Linking Lambda function to IoT Core
Although the Lambda function is already uploaded, it still needs to be linked to the IoT Core.\
To do so, go to the IoT Core service in AWS, click on *Greengrass* and chose the group you created. In the group page, navigate to the *Lambdas* tab and click on the **Add Lambda** button.\
In the next screen, select the *"Use an existing Lambda function"* option. Select the Lambda function previously created and click on the **Finish** button.\
Once the Lambda fuction is displayed, click on the "..." button and select *"Edit configuration"*.\
In the new screen, scroll down and chang the **Timeout** to 25 seconds. Then change the **Lifecycle** to *"Make this function long-lived..."* and click on the **Update** button.\
### Step 4.- Subscribing to the Lambda function
In the group screen, select the tab **Subscriptions** and click on the **Add first subscription button**.\
In the next screen, on the option *"Select a source"* select the Lambda fuction previously created. On the option *"Select a target"* select the **IoT Cloud** option and then click on the **Next** button. The new screen will display a *"Topic filter"* option. Click on it and type *"hello/world"*. Click on the **Next** button and then on the **Finish** button. 
### Step 5.- Deploying the group
Once all the steps are done, you will need to deploy the group with the new configurations. To do so, go to *"Greengrass"* --> *"Groups"*. In the group, select the **Actions** dropdown menu on the top right and click on the **Deploy** option. The deployment process will take a little while (not more than 2 minutes).
### Step 6.- Testing the functionality. 
To test the connectivity and functionality of the whole group, go to the *"Test"* tab on the **IoT Cloud** dashboard. On the new screen, fill the *Subscription topic* with **hello/world**. For the *"Quality of service"* select the option **0** and for the *"MQTT payload display"* select **Desplay payload as string** and click on the *"Subscribe to topic"* button.\
If everything is working fine, you should see an incoming message *"hello world!..."*.
