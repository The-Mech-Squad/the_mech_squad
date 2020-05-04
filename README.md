# The Mech Squad present:

## Space-Trash

The educational application that visualises satellites and space debris, using machine learning to try and predict the future state of these objects.

### The idea

A long time ago, in a galaxy far far away, a group of Makers decided to create an application. Its mission? To create a predictive model which could help solve the problem of space debris

The initial goal was to use machine learning to predict the optimal orbit for a sweeper that would remove the items that are cluttering up our thermosphere. As a first iteration of this project, Space_Trash 1.0, is currently able to:

* fetch TLE data from space-track.org's API
* import it to a local database
* render the data to a model of the earth, using Cesium.js
* let the user input the predictions they would like our model How2 to make based on objects of their choice.

### To run the application locally

Clone this repository, then run:

```
python manage.py migrate
pythong manage.py runserver
```
Visit localhost and have a look.

### To run the tests

```
python manage.py test
```

To view the test coverage run
```
coverage report
```

### User interaction

As a user on the site, you can tell How2 what he should be predicting and which values he should be using to make his predictions. Not only will you be able to see his expected results but you'll also be able to see how accurate his predictions were.

### Design decisions

To help provide context for the project we opted to have a landing page that would explain the concept and briefly outline the actions that a user could take.

We implemented a postgres database that would be populated by the API once every 24 hours. The goal was to streamline the amount of calls we made to the API since the amount of data being processed could affect the speed of the application.

The visualisation that displays the satellite data to the user requires a great deal of processing power so we decided to limit the number of objects that could be displayed at one time. A user can search for a specific object which can render in another's place.

### Technologies used

• Django • Python • D3 • Tensorflow • Anaconda • Cesium • Travis • Heroku

### Resources

We are indebted to the following services and sources:

* [Tech with Tim and his series on machine learning in python](https://www.youtube.com/playlist?list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr)
* [Cesium](https://cesium.com/)
* [The study from Hao Peng & Xiaoli Bai named: "Comparative evaluation of three machine learning algorithms on improving orbit prediction accuracy"](https://link.springer.com/article/10.1007/s42064-018-0055-4)
