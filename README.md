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

You need to include:

An explanation of your app and how it fulfils the brief.
A technical description of how the application works.
A technical description of how the pipeline works.
A report on the success and code coverage of your unit tests.
Any future improvements you would make.
You must use diagrams to illustrate your work as much as possible and opt for a succinct writing style. Examples of diagrams to include are:

Entity Relationship Diagram (ERD).
A full CI/CD pipeline diagram.
An infrastructure diagram, illustrating the cloud resources and how they network together.
A component-level diagram, illustrating how the application interfaces with the database.
You are welcome to combine diagrams if you so wish, such as the CI/CD pipeline with the infrastructure pipeline.

Video
You should also record a brief video (between 2-5mins) demonstrating:

The CRUD functionality of your app.
Your CI/CD pipeline in action, show how after a new push to your GitHub repository your changes should be automatically reflected on the deployed application without manual configuration.
Consult the following links for guidance on recording your screen:

Recording your screen on Windows
Recording your screen on MacOS
If you are struggling to record your screen, please ask your trainer for support.


This video should be hosted on a file sharing site (Google Drive, Dropbox, etc.) and linked in your README file. Make sure that the link is public so whoever is marking it can view it.

Marking Scheme
Below are the skills that we will be evaluating for this
assessment. These skills are as described in the SFIA 7 framework;
please see below if you wish to have more information:

https://www.sfia-online.org/en/framework

The skills this assessment will discuss are the following:

Programming/software development
Systems integration and build
Software Design
Release and Deployment
Programming & Software Development
Designs, codes, verifies, tests, documents, amends and refactors simple
programs/scripts. Applies agreed standards and tools, to achieve a
well-engineered result. Reviews own work.
Below is the list of criteria that will be assessed from your
deliverable:

I have created a very basic web app.
This app will take a new user and register there username and password
they will then be able to login
once logged in the user can enter the details of the book they have read


This app is python based, docker deployed.

the web app consists of three pages 

![webpage](/webapp-master/imagesformd/webpage1.png)
![webpage](/webapp-master/imagesformd/webpage2.png)
![webpage](/webapp-master/imagesformd/webpage3.png)

the webapp was run in docker containers

![docker ps run](/webapp-master/imagesformd/docker ps run.png)

using jenkins 

![jenkins run image](/webapp-master/imagesformd/jenkins run image.png)

Conclusion

While I had two weeks to plan, design and make this project I have fallen short on some criteria. 

For the future i will look to improve on functionality and add to the code the following.

1. on the book entry page show the current book held in the db

2. link the user to the book entries

3. have a display of the top 10 book available to buy

4. have a recommendations window that takes your stored books and provides recomendations based on your entries


Author

shaun cullen








