from flask import Flask, jsonify, request
from pymodm import connect
from pymodm import MongoModel, fields
import models
import datetime
import numpy as np
import Parts

connect("mongodb://vcm-3584.vm.duke.edu:27017/HR_Info")

app = Flask(__name__)

@app.route('/api/heart_rate', methods=["POST"])
def heart_rate():
    R = request.get_json()
    
    try:
        Parts.add_heart_rate(R["user_email"], R["user_age"], R["heart_rate"])
    except:
         Parts.create_user(R["user_email"], R["user_age"], R["heart_rate"])
    
    return jsonify(R)

@app.route('/api/heart_rate/<user_email>', methods=["GET"])
def heart_rate_all(user_email):
    user_all_heart_rate = Parts.user_heart_rate(user_email) 
    return jsonify(user_all_heart_rate)

#@app.route('/api/heart_rate/average/<user_email>', methods=["GET"])
#def average_heart_rate():
#    user_all_heart_rate = Parts.user_heart_rate(user_email)
#    average_heart_rate = Parts.user_average_heart_rate(user_all_heart_rate)
#    return jsonify(average_heart_rate)

#@app.route('/api/heart_rate/interval_average', methods=["POST"])
#def interval_average_heart_rate():
#    R = request.get_json()
 
#    interval_heart_rate = Parts.user_interval_average_heart_rate(R["user_email"], R["heart_rate_average_since"])
    
#    return jsonify(interval_heart_rate)

#if __name__ == "__main__":
#    app.run(host="0.0.0.0")
