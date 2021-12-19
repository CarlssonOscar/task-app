# Introduction

Task App enables users to add tasks, mark tasks as finsihed, remove finished tasks and clear all list items.  

[Link to site](task-app007.herokuapp.com)

 ***  

 ## Index – Table of Contents   


* [User Stories](#User-Experience)  

* [Features](#Features)  

* [Technologies](#Technologies)  

* [Testing](#Testing)  

* [Deployment](#Deployment)    

* [Acknowledgements](#Acknowledgements)  

***  

# User Stories

As a user I want:

* To be able to use the app on all devices.
* The app to be responive on all devices.
* To create an account.
* To have clear intructions for how to use the app.
* To have a user specific task list.
* To be able to add tasks to the list.
* To be able to mark tasks as finsihed.
* To be able to remove finished tasks from the list.
* To be able to remove all tasks from the list.

# Features

* Users can create an account.
* App works on all tested devices.
* App is responive.
* Instructions for how the app works.
* Users has their own list.
* Users can add tasks.
* Users can mark tasks as finished.
* Users can remove finished tasks from the list.
* Users can remove all tasks from the list.

## Future Features

* Enable users to have mulitple lists.
* Enable users to get notifications abouts task deadlines.
* Enable users to share lists with other users.

# Technologys

## Languages
* HTML
* CSS 
* JavaScript
* Python

## Libraries
* Bootstrap 
* Django 
* Google Fonts

## Tools:
* Heroku - for deployment.
* Github - hosts the repository.
* Cloudinary - storage of static files. 
* Allauth - Enables the creation and hosting of users.
* Google Chrome DevTools - for testing and debugging.
* W3 html validator - test html code.
* W3 css validator - test css code.
* PEP8 - test Python code.

# Testing

The testing can be found [here](test.md).

# Deployment 

## Heroku

After one is logged in to Heroku.
* Click on "New" in the right corner and the on "Create new app".
* Choose a app name.
* Select the region closest to where you are.

Under the settings tab:
* Click reveal Config Vars.
* DATABASE_URL, CLOUDINARY_URL, DISABLE_COLLECTSTATIS and SECRET_KEY was added.
 - These variables is part of env.py and are loaded in settings.py.

Under the deploy tab.
* Click on deploy method choose Github and then connect the relevant repository.
* In the automatic deploys section click deploy.


# Acknowledgements

* Stack overflow - provided excellent information on different topics.
* 

I want to thank:
* My mentor Tim Nelson for providing excellent guidance.
* Code Insitutes patient tutors.


