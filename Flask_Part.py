from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/heart_rate', methods=["POST"])



@app.route('/api/heart_rate/<user_email>', methods=["GET"])


@app.route('/api/heart_rate/average/<user_email>', methods=["GET"])


@app.route('/api/heart_rate/interval_average', methods=["POST"])

