# The Mech Squad present:

## Space-Trash

The educational application that visualises satellites and space debris, using machine learning to try and predict the future state of these object's properties.

### The idea

A long time ago, in a galaxy far far away, a group of Makers decided to create an application. Its mission? To create a predictive model which could help solve the problem of space debris

The initial goal was to use machine learning to predict the optimal orbit for a sweeper that would remove items that are cluttering up our thermosphere. As a first iteration of this project, Space_Trash 1.0, is currently able to:

* fetch TLE data from space-track.org's API
* import it to a local database
* render the data to a model of the earth, using cesium.js
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

As a user on the site you can tell How2 what he should be predicting and which values he should be using to make his predictions. Not only will you be able to see his expected results but you'll also be able to see how accurate his predictions were.

### Technologies used

• Django • Python • D3 • Tensorflow • Anaconda • Cesium • Travis • Heroku


### Resources

We are indebted to the following services and sources which helped use formulate the idea and the ideation for this project.

*
*
*
*
*
