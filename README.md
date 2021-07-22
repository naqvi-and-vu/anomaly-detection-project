# Anomaly Detection Project
By: Mariam Naqvi and Anna Vu

<br>
<br>

Have we ever wondered if there was some abnormalities with Codeup's cohorts and their use of the online curriculum? 
Have we ever wondered what lessons are the most popular to students, even post graduation?
Were there students who didn't use the curriculum much...?

Can't say it was our main thought of the day, but we're still out to find the answers! 

<br>

In this anomaly detection project, we will be exploring Codeup's curriculum access log based off this following email.
<br>


*Email to analyst:*


*Hello,*


*I have some questions for you that I need to be answered before the board meeting Thursday afternoon. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.*

### Table of Contents
--- 

1.   [Project Description          ](#1-project-description)
2.   [Project Deliverables         ](#2-project-deliverables)
3.   [Project Questions            ](#3-project-questions)
4.   [Findings                     ](#4-findings)
5.   [Data Dictionary              ](#5-data-dictionary)


### 1. Project Description

We are going to manipulating data in order to find trends and abnormalities in the Codeup Curriculum Access Log. 
Some features we will be able to look into are date, endpoint, user ID, cohort, IP address, and more!
<br>
<br>

### 2. Project Deliverables

As stated in the email, we will need to create a single slide to document our finds similar to an executive summary. We will also be creating a final notebook for review, and of course, reply to the email with our discoveries. 

<br>
<br>

### 3.) Project Questions
 - 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
 - 2. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
 - 3. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
 - 4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
 - 5. Which lessons are least accessed?
 
<br>
<br>

### 4.) Findings

<br>

**Lesson With Most Traffic by Program:**
- Web Development: Javascript I
- Data Science: Classification Overview 
- Full Stack PHP: Javascript I
- Front End: HTML/CSS 
<br>

**Inactive Students?**
- There are 36 students who accessed the curriculum less than 50 times while they were active. 
- Half of those students have not graduated yet (the data stopped recording at 4/21/21, they graduate later)
- Marco, Neptune, and Oberon had not graduated at the time this dataset was made.
- Only between web development and data science students
- Most of these inactive students accessed the curriculum up until ~ 3 days after their start date. Possible they left.
<br>

**Suspicious Activity**
- User 341 has a very high number of page views, 272 pages accessed on 03-03-2019 and 104 pages accessed 04-21-2020
- Access the pages in a very short time span, over a wide variety of subjects
- They graduated 6-04-2019
- Have multiple IP addresses
<br>


**Post-Grad Lessons**

These are the top 3 lessons for each program accessed post-graduation
- Web development: JavaScript-I, Spring, HTML-CSS
- Data Science: SQL, Classification Overview (our first machine learning!), Classification Scaling
- Full Stack PHP: Jacascript-I, HTML-CSS, Spring
- Front End: content html-css, favicon, and introduction (expected for staff)
<br>

**Least Accessed Lessons**
- Assuming least accessed pages were accessed at least once
- There were 458 pages accessed only once from the time of creation to 04/21/2021
- Most of these were professional development, some were curriculum lessons.
- Examples include: conditionals, editing with vim, control statements and loops.

<br>
<br>

 

### 5.) Data Dictionary
| Column Name    | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| accessed_after | 1 if page accessed after student's graduation date, 0 if page was accessed as a current student |
| cohort         | cohort name                                                                                     |
| created_at     | date and time curriculum was created                                                            |
| date           | date of access                                                                                  |
| end_date       | student's graduation date (end of class)                                                        |
| endpoint       | path within curriculum page                                                                     |
| ip             | IP address that accessed the curriculum page                                                    |
| program_id     | 1 for PHP, 2 for web development, 3 for data science, 4 for front end                           |
| program_name   | course that the student was enrolled in                                                         |
| start_date     | date of student's first day of class                                                            |
| time           | time that the page was accessed                                                                 |
| user_count     | the number of times that student accessed the curriculum                                        |
| user_id        | the student's identification number                                                             |
| user_proba     | probability of an access being that particular student                                          |


