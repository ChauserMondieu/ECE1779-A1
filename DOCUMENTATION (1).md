# Face Detection #

Welcome to use the documentation of the face detection application. "Face Detection" is a program which allows users to register an account and upload a photo with a human face, feedback an original picture and a detected photo with a rectangle around human faces.

## Introduction ##

The documentation contains **User's Guide** and **Developer's Reference**. User Guide demonstrates how to use the program for implementing face detection function. Developer's Reference explains the working principle to help other programmers understanding and upgrading the program easily.

## User Guide ##

### Login Page ###

Open the browser and enter the dynamic URL**Server's IPv4 address + :5000** to access the login page. As a standard login page, it contains a user's name&password block and a registration block. If the pair of the name and the password is correct, the browser will show the user's personal page. Else, a message will tell you the pair of the user's name and the password is wrong. If you don't have an account, please click the **No account?** so that the browser will show the registration page for you to register.

![](https://i.imgur.com/G85AolN.jpg)
<h6 style="text-align: center;" markdown="1">Login Page</h6>

### Register Page ###

You can access the registration page in two ways. One is by the login page and another is entering the URL **Server's IPv4 address + :5000 + '/api/register'** to access directly. If a name already existed, the browser will tell you that you can not use the name. Moreover, you must enter the password twice to check the password. If the registration process is successful, the page will back to the login page and you can log in and access your personal page.  

![](https://i.imgur.com/kA3N3Kq.jpg)
<h6 style="text-align: center;" markdown="1">Register Page</h6>

### Personal visit page ###

When you access the personal visit page for the first time, the browser will tell you that you have not uploaded the photo. You can click the **Upload picture** to access your upload page for you to upload your photo. In this project, one account can only keep one photo in the server, if you want to detect different photos in the same account, please clear your browser cache and upload another photo, the new photo will replace the old photo. When you upload a photo successfully, the personal visit page will show you your uploaded photo's thumbnail and you can click the thumbnail to access the result page.

![](https://i.imgur.com/MhQA1nz.jpg)
<h6 style="text-align: center;" markdown="1">Personal Visit Page with first login</h6>
![](https://i.imgur.com/RuPvcem.jpg)
<h6 style="text-align: center;" markdown="1">Personal Visit Page with uploading successfully</h6>

### Upload Page ###

If you login your account by the login page, you can upload your photo in your personal upload page. Please note the form of your upload files could only be "XX.png" and "XX.jpg". If you upload the invalid files such as "XX.txt" and "XX.gif", the website will not upload the files until you upload a valid photo. <br>
Moreover, you can also use another way to upload your photo by the URL **Server's IPv4 address + :5000 + '/api/upload'**. If both of the user name and the password is correct and your upload file is valid, you can access your personal visit page.

![](https://i.imgur.com/Rg74dqt.jpg)
<h6 style="text-align: center;" markdown="1">Personal Upload Page</h6>
![](https://i.imgur.com/Mjq6ZDa.jpg)
<h6 style="text-align: center;" markdown="1">Upload Page</h6>

### Result Page ###
When you upload the photo successfully and click the thumbnail, the browser will access the result page and show you your original photo and the detected photo. In the bottom of the result page, you can click **Exit** to exit this account and back to login page.

![](https://i.imgur.com/RGpU47U.jpg)
![](https://i.imgur.com/IhJgyjX.jpg)
<h6 style="text-align: center;" markdown="1">Result Page</h6>

## Deverlopor's Reference ##

### Program development ###

#### Programming environment ####

> Programming language: **Python 3.5** <br>
> Web framework: **Flask 0.11.1** <br>
> Integrated Development Environment: **PyCharm 2018.3.4 x64 bit** <br>
> Database: **Mysql 8.0** <br>
> Server Connector: **cygwin 2.11.2** , **TightVNC 2.8.11** , **FileZilla 3.40.0 x64 bit**<br>
> Browser: **firefox 51.0.1 x64 bit**(server), **google chrome 70.0.3538.110 x64 bit**(developer) <br>

#### Program Structure ####

    FaceDetection                                         # Project directory
    ├ static                                              # Static file directory
    │├ picture                                            # Picture directory
    ││├ raw_picture                                       # Raw picture directory
    ││├ face_detected_picture                             # Detected picture directory
    ││└ thumbnail_picture                                 # Thumbnail directory
    │└
    ├ templates                                           # Web page file directory
    │├ registration_page.html
    │├ result_page.html
    │├ upload_page.html
    │├ uploadF_page.html
    │├ visit_page.html
    │└ welcome_page.html
    ├ venv                                                # Virtual environment directory
    ├ . idea                                              # Support file directory (flask project)
    ├ __pycache__                                         # Support file directory (flask project)
    ├ app.py                                              # Main function
    ├ faceDetection_function.py                           # Customized Module
    └ imageThumbnail_function.py                          # Customized Module


#### Main Program ####

> Open Module: <br>

    flask_sqlalchemy               #Connector that connects the flask and the Mysql
    flask_wtf & wtforms            #Operator that reads the user's input from the web page
    flask_login                    #Operator that protects the user's security in the login permission
    werkzeug                       #Operator that protects the user's security in the data
    os                             #Operator that is used to obtain operating addresses in the system
    jinja2                         #Operator that writes the server's output to the web page
    OpenCV                         #Generator that generates the detected photo

> Customized Module: <br>

    faceDetection_function         #The function can read the original photo and write the detected photo to the aimed address
    imageThumbnail_function        #The function can read the original photo and write the thumbnail to the aimed address

> Customized Class: <br>

    WelcomeForm()                  #Define a WTF form for reading the user's input in the login page
    RegistrationForm()             #Define a WTF form for reading the user's input in the register page
    UploadForm()                   #Define a WTF form for reading the user's input in the personal upload page
    UploadFForm()                  #Define a WTF form for reading the user's input in the upload page
    User()                         #Define a table form in the Mysql database

> Customized Function: <br>

    user_loader()                  #The function can load the user for managing the login permission
    welcome_function()             #The routing function operates the input from the login page
    registration_function()        #The routing function operates the input from the register page
    visit_function()               #The routing function operates the input from the personal visit page
    result_function()              #The routing function operates the input from the personal result page
    upload_function()              #The routing function operates the input from the personal upload page
    uploadF_function()             #The routing function operates the input from the upload page

> Templates: <br>

    Registration_page              #Display the register page
    result_page                    #Display the result page
    upload_page                    #Display the personal upload page
    uploadF_page                   #Display the upload page
    visit_page                     #Display the personal visit page
    welcome_page                   #Display the login page

#### Database ####

> Service Name : **Mysql@localhost:3306** <br>
> Database name: **faced** <br>
> table name   : **user**  <br>

    | Column Name      | Data type    | Characteristic                          | Default |             # The structure of the table 'user'
    ---------------------------------------------------------------------------------------
    | id               | INT(11)      | Primary Key, Not Null, Auto Incremental |         |
    | name             | VARCHAR(100) | Unique Index                            |  NULL   |
    | password         | VARCHAR(100) |                                         |  NULL   |
    | originalAddress  | VARCHAR(100) | Unique Index                            |  NULL   |
    | detectedAddress  | VARCHAR(100) | Unique Index                            |  NULL   |
    | thumbnailAddress | VARCHAR(100) | Unique Index                            |  NULL   |


#### Open Code ####

> The open code is made public at the Github.

[https://github.com/ChauserMondieu/ECE1779-A1](https://github.com/ChauserMondieu/ECE1779-A1)


### AWS Server development ###

#### Create an AWS account ####

This part is intended for those who haven’t set up Amazon AWS accounts, for this project, please skip this section and go directly into the log-in instruction. <br>

> Amazon Web Services (AWS) is a secure cloud services platform, offering compute power, database storage, content delivery and other functionality to help businesses scale and grow. In order to start cloud service in AWS cloud platform, you should come to visit [Amazon official website](https://aws.amazon.com/) and sign up for one regular account. <br>

After signing up for the regular AWS account, log in to it and navigate to the Console interface. Click on the account name on the far-left button of the top navigate bar right next to a small bell icon, then choose “My account” option on the drop-down list. In “My account” interface, select and copy your regular account id under the category “Account Setting”, you may use this series of number linking your regular account to the AWS Educate account during the following processes. <br>

Then, enter the [AWS Educate website](https://aws.amazon.com/education/awseducate/) and apply for one AWS Educate Account, later on paste your regular AWS account id into the input field, this process will automatically link your regular AWS account to the newly created AWS Educate account. After the connection, check your e-mail box for the confirmation mail from AWS team and after the activating procedure you’ll be able to use the AWS Educate account and launch cloud services in Amazon AWS

#### Log into an existing account ####

For the sake of fully accomplishing this project, we have set up one educational account in AWS. Try navigating to the signing-in [website](https://www.awseducate.com/signin/SiteLogin) and log in with the following information:

    Account name: ece1779_std1@cs.toronto.edu
    Password: std1_ece1779_fall9102#

![figure1](https://i.imgur.com/ffychmm.jpg)
<h6 style="text-align: center;" markdown="1"> Login interface for AWS Educate Account</h6>

Once you’re in the navigation webpage of AWS Educate, try clicking on the far-left button **My Classroom** in the upper navigation bar entering the classroom interface, then click on the **Go to classroom** button in the right column of the existing chart.

![figure2](https://i.imgur.com/tNMGA5L.png)
<h6 style="text-align: center;" markdown="1"> Clicking on "My Classroom" button on the top navigation bar</h6>

![figure3](https://i.imgur.com/jKiq60C.jpg)
<h6 style="text-align: center;" markdown="1">Clicking on the “go to classroom” button on the right column</h6>

In Vacareum welcoming interface, click on **AWS console** to navigate to the AWS console

![figure4](https://i.imgur.com/8D2ykvr.jpg)
<h6 style="text-align: center;" markdown="1">Click on the “AWS Console”</h6>

#### Activate the established EC2 instance ####

You are already there. While logging into the AWS Management Console, change the service section to **N.Virginia**, the switch button could be found in the middle of the top navigation bar. The next step for you is to click on the **EC2** services in the **All Service** directory and enter into the EC2 service control panel.

![figure5](https://i.imgur.com/a9xA8JH.jpg)
<h6 style="text-align: center;" markdown="1">Click on the EC2 Service in the “All Service” Directory</h6>

Under the **Resources** section, click on the **Running Instances**, or just click on the **Instances** on the left navigation bar, this move will direct you into the page showing all the instances deploying in this account.

![figure6](https://i.imgur.com/haMlJHz.jpg)
<h6 style="text-align: center;" markdown="1">Click on the “Instances” on the left navigation bar</h6>

 From the control panel of all the instances deploying in this account, we can see one with the name **Project-F** (which is exactly the final Version of our web application project), and that is the one that we deploy our web application on. Now you can see that this instance is currently in stop state. We need to activate it. **Select this instance** and click on the **action** button on the top of the displaying chart, choose **Instance State->Start** in the drop-down list respectively and start the instance. 

![figure7](https://i.imgur.com/DYZR2H1.jpg)
<h6 style="text-align: center;" markdown="1">Activate the selected instance</h6>

As we can see, in the Description panel, the security group of this instance is named **launch-wizard-7**, which is customized to open SSH transmission as well as to open port 5000 in TCP for connection from outside the instance. By activating the instance, it will be automatically dispatched one dynamic public DNS aka IP address, copy this IP address and save it for the further SSH remote connection use. 

#### Connect to the instance via SSH and VNC ####

Now that we have already started the instance, the next step for us is to connect to it via secured data transmission channels. The key pair is named “Li_et_Liu” and is stored in the following directory of this project: 

> directory of the .pem document


in the contraction file. In this case we will use SSH to establish this data-transmitting tunnel. 

First, open your Cygwin Terminal and type in the following command code in order to familiarize your system with the storing directory of the key pair

    % pwd
    % ls -alrth "pem directory path"
    % cp "pem directory path" .
    % chgrp Users "pem document name"
    % ls -alrth "pem document name"

> Notice: substitute the current directory path of private key file “Li_et_Liu” for the sudo code “pem directory path”, and replace “pem document name” with “Li_ _ et_ _ Liu.pem”

Then, with all preparation done, we could start the SSH connection with the code down below:

    % ssh -i key pair doc.pem ubuntu@Public DNS (IPv4) -L port number :localhost: port number

One example could be:

    % ssh -i Li_et_Liu.pem ubuntu@ec2-3-80-135-112.compute-1.amazonaws.com -L 5001:localhost:5901

![figure8](https://i.imgur.com/YZNqxpG.jpg)
<h6 style="text-align: center;" markdown="1">SSH connection command input</h6>

Type **yes** upon the prompting line confirming admission of connection.

![figure9](https://i.imgur.com/eJDqqVY.jpg)
<h6 style="text-align: center;" markdown="1">SSH connection succeed </h6>



> The SSH connection is successfully established.

After connecting with the instance via SSH, we could establish VNC in the instance and start manipulating via GUI. The needed application requirements are deployed in the instance aforehand. All we needed to do is to launch the VNC server in the instance by typing in:
    
    % vncserver

The instance will automatically launch the vnc service pre-deployed in it.

![figure10](https://i.imgur.com/EtJPMZ2.jpg)
<h6 style="text-align: center;" markdown="1">VNC service is launched in the instance</h6>

Next, open **TightVNC**, fill in the inbound port of the instance (in this case is **localhost::5001**),  click on **connect** button, type in the connection password **ece1779pass**, after that you will be successfully log in to the instance with GUI in your PC.

#### Implement the project in the server ####

Now that we have set up our AWS instance and successfully connect to it, the next thing we should do is to deploy our well-developed application to the instance. We strongly recommend that all the applications be implemented off-line and then uploaded onto the cloud server as a project. The sole account for this is that it will save the time as well as the resources required for developing the target applications.

In the former process, we have already set up the SSH connection between your local application-developing host and the AWS EC2 server. In this step, we will upload our project onto the cloud server taking full advantages of this SSH connection. There are two ways of data transmission via established SSH tunnel, the first one is using the **scp** command in the Command Line Interface (CLI), which is somehow tedious to manipulate due to the file managing system. In this documentation, we will go on the second option: using the third-party graphical interface AIDS application, to state one, FileZilla in this project.

Launch **FileZilla** in the local host, create a new file transmission task, then fill in the boxes with information shown as follows:

>1. Choose SFTP-SSH FIle Transfer Potocol in the  __Protocol__ box </br>
>2. Copy the dynamic IP address into the __Host__ box              </br>
>3. Leave the __Port__  box balnk                                  </br>
>4. Choose Normal in the __Logon Type__                            </br>
>5. Fill in "ubuntu" in the __User__ box                           </br>

![Figure 1](https://i.imgur.com/KWb2NgW.jpg)
<h6 style="text-align: center;" markdown="1">Settings of a new SSH file transmission</h6>


In order to meet the security standards of the SSH connection, we also need to assign the connection key pair to the SSH client. Select:

> Edit->Settings->SFTP

![Figure 2](https://i.imgur.com/E8tfStX.jpg)
<h6 style="text-align: center;" markdown="1">Assign the key pair to the transmission task</h6>


Choose the directory location of the key pair **Li _et_ Liu.pem**, then click 

> Add key file

Click **connect**. 

Now, all the settings are done for the file transmission between your local host and the AWS Cloud Server.<br>
![Figure 3](https://i.imgur.com/p73w7XQ.jpg)
<h6 style="text-align: center;" markdown="1">Interface after finishing the settings</h6>

From the interface above, you could just upload or download files to or from your AWS Cloud Server by simply dragging the items to the other side of the interface. Remember to choose the right directory before starting a new file transmission process.

For simplicity, the main file of the web application are uploaded into the 

> /home/ubuntu/Documents

directory,while the boosting file of the application **Start.sh** is uploaded to the Desktop of the instance, whose directory path is 

>/home/ubuntu/Desktop

##### Start the application #####
Open the Command Line Interface of the instance, then type in the following directive:

    $ cd /home/ubuntu/Desktop
    $ ./Start.sh

After a while the application will fully execute in the instance, you could access to this web application outside from the instance as well. The instructions of this process is mentioned in the previous paragraphs.



<hr>@ Copyright 2019, Zhonghao Li & Botao Liu & Qiuchen Wang. Created using Markdownpad 2
