# Product Demonstration Report

## Introduction
The solution our team is presenting will be a Web Application implemented using Python Flask. We have created a minimum viable product with some of the base features implemented for a working Student Attendance Managment System.

In this report we will be demonstrating the following features:
- Login system
- Dashboard
    - User
    - Admin
- Attendance system
---
## Demo
When visiting the web application, the following window is shown and it prompts you to login to your account.
![alt text](https://github.com/anthonypoh/Team4/blob/dev/MVP/Reports/Images/ProductDemonstration/base.png)

Clicking the 'log in', you will be taken to another page to enter your credentials.
![alt text](https://github.com/anthonypoh/Team4/blob/dev/MVP/Reports/Images/ProductDemonstration/login.png)

Logging in as a student moves you to your student dashboard. Here you will see the next class that you can attend. Attend button will only be displayed once the current time matches the lesson start time.
![alt text](https://github.com/anthonypoh/Team4/blob/dev/MVP/Reports/Images/ProductDemonstration/student.png)

This next image displays the Attend button.
![alt text](https://github.com/anthonypoh/Team4/blob/dev/MVP/Reports/Images/ProductDemonstration/attend.png)

After clicking the Attend button, the request is sent to the backend which updates the students attendance in the database. An alert is shown and if it exists; the next classes details will be displayed.
![alt text](https://github.com/anthonypoh/Team4/blob/dev/MVP/Reports/Images/ProductDemonstration/marked.png)

The following is the admin dashboard. Currently the management functions of the admin page have not been implemented yet. In the future we will have included all the features and requirements listed in the brief.
![alt text](https://github.com/anthonypoh/Team4/blob/dev/MVP/Reports/Images/ProductDemonstration/admin.png)
