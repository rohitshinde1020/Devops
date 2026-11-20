
from flask import Flask, request, render_template
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = pymongo.MongoClient(os.getenv("MONGO_URL"))

db = client["mydatabase"]
users = db["mycollection"]


@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "Username and password are required.", 400

    users.insert_one({
        "username": username,
        "password": password
    })

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
