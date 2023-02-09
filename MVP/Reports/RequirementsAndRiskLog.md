# Requirements and Risk Log
Our team members & their roles:
Anthony: Scrum Masters
Danny: Product Owner
Megan: Development Team
Jun Yong: Development Team/Stake holders

*In this markdown document, list all of the requirements that you have identified for your product so far.*

# Requirements

*List several user stories (no more than 8) that describe the product requirements. For each user story that you include:*

**User Story 1** - I need a system to track and manage students attendance and allow students/lecturers to access the system so that i can manage the users expectations. 
Issue 1.1 - Create Flask Application Server
Issue 1.2 - Create User Database
Issue 1.3 - Create Class Database
Issue 1.4 - Create MVP UI

**User Story 2** - Clocking in and out, This is an attendance management essential – student should be able to clock in and clock out after the class is complete (Student)
Issue 2.1 -  Create Home page
Issue 2.2 - Select Class (Database) to input attendance
Issue 2.3 -  Input button to input current time 
Issue 2.4 -  Input Condition using face recognization

**User Story 3** - Leave Application, To apply and manage the administrative reasons so that i can ensure my excuses are recieved. (Student)
Issue 3.1 - A Leave Application Page
Issue 3.2 - Apply Leave Form, Files to upload, Leave type and Date
Issue 3.3 - Once Submitted, to have a Overall Status page to show, Pending and History leave form.
Issue 3.4 - Allow (Admin) to approve or reject the application review. 

**User Story 4** - Calender feature, to see a overview of classes users have for the months, with the most recent timetable in effect for the change or replacement class. (Student, Lecturer & Admin)  
Issue 4.1 - Calender System
Issue 4.2 - (Lecturer & Admin) Create / edit, Date, Time, and Cancellation of classes 
Issue 4.3 - Reminder or notification Feature: Users are able to set alarms to be reminded of upcoming classes and submissions. 
Issue 4.4 - Classroom information, physical class or online classes. Can be updated by the (Lecturer or Admin)

**User Story 5** - to be able to view the attendance summary for a lesson across a semester and amend accordingly when required. (Admin)
Issue 5.1 -  Create an attendance page summary
Issue 5.2 -  Create option page for each semester
Issue 5.3 -   Import data from database

**User Story 6** - To view the student name list of the selected class, amend & manage all the students attendances (LECTURER & ADMIN)
Issue 6.1 - Button to select the specific class
Issue 6.2 -  Display Student list, with check box to show student is present or absent
Issue 6.3 - Feature for lecturer to add & edit student list

**User Story 7** - Advanced analytics, I want to to view a summary of a particular lesson as well as the overall attendance for a trimester along with pertinent statistics.  (LECTURER & ADMIN)
Issue 7.1 -  Create a pertinent statistic
Issue 7.2 -  Import data from the attendance summary
Issue 7.3 -  Allow user to download the data in Excel format

**User story 8** - System to automatically give warnings when the percentage attendance fall below the requirement or should a consecutive number of lessons be missed. (Student)
Issue 8.1 -  Create pop-up notification
Issue 8.2 - Able to detect the percentage of attendance
Issue 8.3 - Allow system to send notification 
Issue 8.4 -  Student able to view the notification from system


* *Give details of whether this story has been assigned to someone yet, and whether it is completed yet.*

Anthony, our Scrum Master will be in charged of User Story 1, which is to create a flask server, user and class database and MVP UI. We are currently working on User Story 2. Ruiqi will be doing the user interface while Danny and Jun Yong will assist in project backlog and implementing other added user features for the Final Product.
The other users stories will be assigned in our upcoming scrum meetings, at the moment we are working on our MVP.

* *Include a screenshots of any relevant attachments.*

*In addition to user stories (which is the main thing we are trying to teach for agile), try to include one or two other requirement modelling techniques, e.g. as listed in the lecture.*
We are using class based modelling which identifies classes, attributes and relationships used by the system when pulling data. For example, when the student enters his module ID, the system
will show them their attendance for the related model as the attribute "Module" has been classed into our code database.

We are also using data driven modelling which is quantitative data analysis methods to identify and process user data. For example, the system will remember the lecturer's or student's favourite settings
without them having to set it up everytime they login to our webapp. 

*Try to group the requirements under two sub-headings: functional requirements, and non-functional requirements.*

Functional Requirements:
User can reset password via email if forgot password
User can register an account
User can capture Attendance
User can apply leave
User can set alarms
Display timetable and classroom location info
Facial recognition to confirm attendance

Non-functional requirements:
Home page
Input button
Calender feature
View attendance summary
Download and import attendance records
Notifications
Detect percentage of attendance

*When marking this section we will be looking to see your team has understood the correct way to represent User-Stories and one or more other requirement modelling methods, and the requirements listed are giving as much relevant information for the development team as possible.*

## Risk Log

*In this section list the risks you have identified for your project.  For each Risk identified:*

First we will look at the process risks involved, whereby our team do not understand the needs of our users (customers) and we planned a product that is too complicated for them to use.
Hence, Jun Yong will be going over the functional and non-functional requirements and try his best to simplify the software. Danny, our product owner will also discuss with our users,
to gauge their reactions to our software and update their needs to the development team timely.

Another process risk is ineffective testing where our team missed serious defects or problems with our products, this is why Anthony, our scrum master will be in charge of testing the product
based on the AGILE testing model. He is in charge of the testing phase because he has vast knowledge in software engineering. We will then have a second round of test done by Ruiqi and the last
round of testing done by Danny, our product owner - this process will be carried out in accordance with our KanBan Board schedule. If possible, we would like to bring in real students and lecturers
to BETA test the system before the launch so we can effectively mitigate this risk and ensure that our testing is most effective.

Next, let us look at product risk, which is related to our SAMS system. One of the biggest risk would be poorly defined interfaces in our SAMS systems - for example upon login, the roles of the student,
leturers and admins are not properly defined and it leads to confusion or even error in logging attendance. This is why we hold weekly scrum meetings where Anthony will go over our product interfaces and
test our codes to make sure that all functions and databases are correctly defined. Our product owner, Danny will also work with Jun Yong and Ruiqi to ensure the expectations of our users are correctly conveyed.

Next would be inexperienced personnel which is not capable of doing a certain task or did not complete the task as expected due to inexperience - this is actually a common issue where team members over promise and
cannot deliver. This is why we conduct weekly scrum meetings and Anthony(scrum master) will check on our progresses and reassign tasks if a certain team is underperforming. Ruiqi will also hold a weekly counselling session
for members who needs help with their task. Our scrum master is very approachable for any team members that needed help with their tasks. - he is willing to offer advise and help when we needed it.

We are using the AGILE method to manage risks and it is being tracked and updated in real time. The four step risks control method are: Identifying Risks, Making an Assement, considering responses and Analyzing reviews, where
we apply to our projects and this helps us to mitigate risks effectivley. 

* *Include a URL link to the Jira risk issue.* 
* *Paste in the Risk's Description and Summary from Jira.  Also state the Impact and Likilihood.*
* *Give details of whether this story has been assigned to someone yet, and whether it is completed yet.*
* *Include, from the Jira description / comments, details of what mitigating actions are being taking and by whom.*

*When marking this section we will be looking to see several realistic risks have been noted, and are actively being tracked and mitigated against.*

