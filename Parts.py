from pymodm import connect
import models
import datetime
import numpy as np

def add_heart_rate(email, heart_rate, time):
    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    user.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    user.save() # save the user to the database

def create_user(email, age, heart_rate):
    u = models.User(email, age, [], []) # create a new User instance
    u.heart_rate.append(heart_rate) # add initial heart rate
    u.heart_rate_times.append(datetime.datetime.now()) # add initial heart rate time
    u.save() # save the user to the database

def check_user(email):
    user_status = User.objects.raw({"_id": email}).first()

def user_heart_rate(email):
    user = User.objects.raw({"_id": email}).first()
    user_all_heart_rate = user.heart_rate
    return user_all_heart_rate

def user_average_heart_rate(user_all_heart_rate):
    average_heart_rate = np.mean(user_all_heart_rate)
    return average_heart_rate    

def user_heart_rate_time(email):
    user = User.object.raw({"_id": email}).first()
    user_time = user.heart_rate_times
    return user_time

def user_interval_average_heart_rate(time, heart_rate, interval):
    pass
