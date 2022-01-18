# webapp-master
DfE Cloud Specialism - Final Project
Introduction
This project serves as the culmination of all of the topics you have covered as part of your training. It will involve the following concepts/technologies:

Project Management
Python Fundamentals
Python Testing
Git
Linux
Python Web Development
Databases
Continuous Integration and Deployment (CI/CD)
Cloud Fundamentals
Containerisation
This project is an individual project designed to demonstrate your knowledge.

Overview
Your objective with this project is to achieve the following:

To create a web application that integrates with a database and demonstrates CRUD functionality.
To utilise containers to host and deploy your application.
To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.
Project Management and Version Control
Technologies:

Jira (or equivalent)
Git
GitHub
You must use Jira or similar project tracking software to track your project using Agile Scrum methods. You must make use of:

MoSCoW prioritisation.
Estimations of effort (e.g. story points, T-shirt sizes).
User stories.
You will be using Git as your version control system and hosting your code repository using GitHub. You must make use of a feature branch model to complete your work.

You must also produce a risk assessment to identify and analyse any potential risks to your application and infrastructure. This must be evidenced in your documentation.

Application
Technologies:

Python
Pytest
Flask
Docker/Docker Compose
MySQL
You are tasked to create a basic web application using on the Flask web framework.

It must demonstrate CRUD functionality.

The domain/topic of the application is entirely down to you. It's recommended you choose a hobby of yours to base it on. The app must keep track of two entities that have some kind of relationship with each other.

For example:

A fantasy football application that allows you to create football teams and add players to them.
A DnD character creator that allows you to create characters based on fantasy races.
A recipe book app that keeps track of recipes and ingredients.
This relationship between entities is to be modelled in the database. You must illustrate this relationships using an entity relationship diagram (ERD) in your documentation.

Application
The application is a monolithic Flask application that serves both the frontend and backend of the application.

The frontend aspect of the app will use HTML templates to serve the web pages that allow the user to perform CRUD functionality with information from the database.

The backend aspect of the application will use SQLAlchemy to model and integrate with the database.

Diagram for the application service architecture

This application will be hosted in a container to allow it to be deployed to a Docker Swarm.

Database
The application must interface with a separate database service. You are encouraged to use a MySQL container (documentation) for the sake of simplicity, but you may use a database service such as MySQL Database for Azure if you wish to challenge yourself.

The database must contain two tables with a relationship.

The relationship must at least be one-to-many, but a many-to-many relationship may garner extra marks.

For example, a fantasy football app may have a teams table and a players table. The relationship between these two tables is one-to-many, as a player has one team, but a team has many players.

Testing
Unit tests must be written for the application with the aim of achieving high coverage.

You will use pytest to write and test the application.

CI/CD Pipeline
Technologies:

Jenkins
You are also tasked with creating a CI/CD pipeline that will automate the integration and deployment of new code.

The automation server you must use is Jenkins.

You have freedom to organise the pipeline however you see fit, but the pipeline must achieve the following:

Run unit tests.
Build the Docker images.
Push the Docker images to a registry.
Deploy to a Swarm.
Every time you push new code to your GitHub repository, the pipeline should be triggered. This can be achieved using a GitHub Webhook.

Deployment
Technologies:

Docker Swarm
The application should be deployed to a Docker Swarm hosted in the cloud.

It should consist of at least one manager node and one worker node. Neither of these nodes should be the Jenkins build server.

Deliverable
The final deliverable of this project is a GitHub repository containing all of the code you have written for this project, including the software source code, Jenkins configuration, Docker configuration and any related scripts.

Your GitHub repository should also contain the write-up for your project in the form of a README.md file.

You must also provide video evidence of your application and CI/CD pipeline working.

You are required to deliver this project to complete the course. The deadline will be the final day of your bootcamp. All of your work must be merged into your main branch, ready for submission.

You must provide your trainer with the link to your repository.

Documentation
You are required to create a write-up for this project in the form of a README file on your repository.

As specified in the brief for this project, I will plan, prepare and create a web application that demonstrates CRUD functionality. Integrates with a database and is deployed using Docker containers. The technologies I will be using are Python, Flask, Docker compose, Msql, Pytest, Git-hub, Trello, VsCode.
This project is demonstrated in a virtual machine within my own computer. 
In the planning phase I will use a Trello board to segment my work and keep track during each phase of the development. Initially I will be planning and performing research on how best to achieve this. 
Throughout the entire project I will be using scrum to model where I am and where I am going. This will involve a quick 5 minute recap of my current progress and documenting my daily plan. This will be included in the project documentation.
Using the MosCoW prioritisation method the application:
Must have – CRUD functionality, be deployed in a docker container, integrate with a database
Should have – CI/CD pipelines, unit testing
Could have – Interactive images/functionality
Will not have – social media integration, integration of any other language 

The app itself will be a simple book logging app. As an avid reader I like to log what books I have read and my thoughts on it in the form of a review.
As such the app will present with a simple homepage with links to a registration, login, about and links page. 
Home page
The home page should be simple, clean and easy to navigate. Containing links to all relevant pages.
The background image should be simple and apt to the purpose of the site. 
Registration Page
The registration page again should be simple and clean with the same navigation as the home page. Buttons or menus in the same place. This page should allow a user to easily identify it’s a page for registering their login details to return to the site and keep track of their book logs.
Login Page
The login page will carry much the same formatting of the registration page but without the registration button. Again it should be clean and simple but apt to the purpose of the site.
About page
The about page is where I will have a simple message about the site and its purpose with simplified instruction. On this page there will be the same formatting as others but with the instruction easily visible.


Links page
The links page is where I will continue the format of the other pages but with links to popular book websites. These links will be easily identifiable and simply click to go to that site. 
Book entry page
This page will depart from the standard format on other pages and be very simple, very clean. It will simply have an entry section containing the following entries
First name
Last name
Book title
Book author
Basic review
These will be in the for of entry cells. With clear instructions. Followed by a simple submit button.  
Tying all these pages together is a mysql server using phpMyAdmin. This mysql server will store users registration details and the entered book logs.

THE PROJECT

The final state of my project is short of the stated requirments. This is in part due to the lack of time, lack of consistancy in the knowledge base. 

I have made a web app that is configured to be deployed using docker. The webapp has unit tests and while using jenkins my knowledge of how it actually functions 
is lacking. 


This app is python based, docker deployed.

the web app consists of three pages 

![webpage](/webapp-master/imagesformd/webpage1.png)
![webpage](/webapp-master/imagesformd/webpage2.png)
![webpage](/webapp-master/imagesformd/webpage3.png)

the webapp was run in docker containers

![docker ps run](/webapp-master/imagesformd/docker ps run.png)

using jenkins 

![jenkins run image](/webapp-master/imagesformd/jenkins run image.png)

Video of webapp
There is a video file 

Conclusion

While I had two weeks to plan, design and make this project I have fallen short on some criteria. 

For the future i will look to improve on functionality and add to the code the following.

1. on the book entry page show the current book held in the db

2. link the user to the book entries

3. have a display of the top 10 book available to buy

4. have a recommendations window that takes your stored books and provides recomendations based on your entries


Author

shaun cullen








