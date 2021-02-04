from flask import Flask, jsonify
from flask_pymongo import PyMongo

import os 

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] \
                            + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
mongo = PyMongo(app)
db = mongo.db

@app.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)