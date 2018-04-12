### heart_rate_databases_starter
Starter codebase for BME590 Databases Assignment (which can be found [here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/main.md#mini-projectassignment)). 

# Brief Description
This project is the back-end server for a [React JS application](https://github.com/ps178/doctor-hr-frontend). This server uses docker to store databases in mongodb. In addition, this project uses Flask to set-up the serve. This server has three different routes;

`/api/heart_rate` takes post requests and creates a new user with an associated user_email, user_age,and HR_data (the server attaches a time stamp to the HR data). If the user alreadys exists then the server will find the user via the primary key (user email) and append the new HR data (with time stamp for the new HR data) to the array of HR data for the user.

`api/heart_rate/<user_email>` takes get requests and returns all the HR data (and time stamp) for the specified user. 

`/api/heart_rate/average/<user_email>` takes get requests and returns the average HR of all the HR data available for the specified user.

`/api/heart_rate/interval_average` takes post requests and returns the average HR of the HR data entered into the system after the specified "heart_rate_average_since" for the specified user. 

Overall, this server creates users based on email addresses and uses mongodb to store each user's HR data.


# Set-up Instructions
### Docker
This project uses mongodb to store databases. 
To get mongodb program running simply run;

```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```

either on your local machine (if you have docker installed there) or on a virtual machine you have access to where you can first install docker.

*if you are running your mongodb database on a virtual machine, you need to replace the `connect` URI string in `Flask_Part.py`. Replace `localhost` with a VM address, like so:

```py
connect("mongodb://VM_ADDRESS:27017/heart_rate_app") # open up connection to db
```
### Virtualenv
Once your database is running and your connection string is set, activate your `virtualenv` and install all the dependencies listed in `requirements.txt`. To do this, simply run;

```
virtualenv env  # to create a virtualenv called env
```
```
source env/bin/activate # to activate the env
```
```
pip install -r requirements.txt # to install all the dependencies
```

### Running Flask
After all the dependencies are installed run the flask server by running;

```
FLASK_APP=Flask_Part.py flask run --host=0.0.0.0
```
Now you are ready to send GET and POST requests to the server.

