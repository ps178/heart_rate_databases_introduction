from pymodm import connect
import models
import datetime
import numpy as np
import sphinx

def add_heart_rate(email, heart_rate):
    """ Function uses the models.py class to add a new heart rate data to an existing user 

    :param email: the email adress used to identify each user
    :heart rate: the heart rate value to be added to the specified user

    """
    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    user.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(datetime.datetime.now()) # append the current time to the user's list of heart rate times
    user.save() # save the user to the database

def create_user(email, age, heart_rate):
    """ Function creates a new user based on the user's emails.

    :param email: the new user is created and identified using the user email.
    :param age: the user class has an age attribute for the user
    :param heart rate: the heart rate value to be added as an attribute of the user

    """
    u = models.User(email, age, [], []) # create a new User instance
    u.heart_rate.append(heart_rate) # add initial heart rate
    u.heart_rate_times.append(datetime.datetime.now()) # add initial heart rate time
    u.save() # save the user to the database


def user_heart_rate(email):
    """ Function collects all the heart rate values for a specific user

    :param email: The email is used to find/specify the user
    :returns heart rate values: all of the heart rate values of that user is returned

    """
    user = models.User.objects.raw({"_id": email}).first()
    user_all_heart_rate = user.heart_rate
    return user_all_heart_rate

def user_average_heart_rate(user_all_heart_rate):
    """ Function calculates the average HR of a specific user based on all the HR data for that user
 
    :param user_all_heart_rate: All the heart rate values for a specific user provided by the user_heart_rate function.
    :return average_heart_rate: the average HR for the user

    """
    average_heart_rate = np.mean(user_all_heart_rate)
    return average_heart_rate    

def user_interval_average_heart_rate(email, interval):
    """ Function calculates the user's HR over a specific interval
  
    :param email: The specific user's email
    :param interval: The interval for which the HR will be calculated
    :return interval_heart_rate: The average HR of the user over the specified interval

    """
    pass
    user_info = models.User.object.raw({"_id": email}).first()
    time_line = user_info.object.raw({"heart_rate_time" > interval})
    size = len(time_line)
    heart_rate = user_info.heart_rate
    interval_heart_rate = heart_rate

def validate_input_interval(user_email, heart_rate_average_since):
    """ Function validates that the inputs are in correct type

    :param email: In string format
    :param heart_rate_avergae_since: In string format

    """
    if isinstance(user_email, str) and isinstance(heart_rate_average_since, str): 
        indicator = True
    else:
        indicator = False
    return indicator


def validate_input_user(user_email, user_age, heart_rate):
    """ Function validates that the inputs are in correct type

    :param email: string format
    :param heart_rate:int format
    :param user_age: int format

    """
    if isinstance(user_email, str) and isinstance(user_age, int) and isinstance(heart_rate, int):
        indicator = True
    else:
        indicator = False
    return indicator





