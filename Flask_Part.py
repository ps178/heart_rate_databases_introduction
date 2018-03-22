from flask import Flask, jsonify, request
from pymodm import connect
import models
import datetime
import numpy as np
import Parts

app = Flask(__name__)

connect("mongodb://vcm-3584.vm.duke.edu:27017/heart_rate_app")


@app.route('/api/heart_rate', methods=["POST"])
    R = request.get_json()
    create_user(R["user_email"], R["user_age"], R["heart_rate"])
    return jsonify("done")

@app.route('/api/heart_rate/<user_email>', methods=["GET"])
    user_all_heart_rate = user_heart_rate(user_email) 
    return jsonify(user_all_heart_rate)

@app.route('/api/heart_rate/average/<user_email>', methods=["GET"])
    user_all_heart_rate = user_heart_rate(user_email)
    average_heart_rate = user_average_heart_rate(user_all_heart_rate)
    return jsonify(average_heart_rate)

@app.route('/api/heart_rate/interval_average', methods=["POST"])
    R = request.get_json()
    
    user_all_heart_rate = user_heart_rate(R["user_email"]):
    user_time = user_heart_rate_time(R["user_email"]):
    interval_heart_rate = user_interval_average_heart_rate(user_time, user_all_heart_rate, R["heart_rate_average_since"]):
    
    return jsonify(interval_heart_rate)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
