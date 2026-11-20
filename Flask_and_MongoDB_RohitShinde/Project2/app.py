from flask import Flask, request, render_template, redirect, url_for
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = pymongo.MongoClient(os.getenv("MONGO_URL"))

db = client["mydatabase"]
users = db["mycollection"]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    username = request.form.get('username')
    password = request.form.get('password')

    try:
        

        user_data = {
            "username": username,
            "password": password
        }

        users.insert_one(user_data)

        # Redirect only when data is successfully inserted
        return redirect(url_for('success'))

    except Exception:
        return render_template(
            'index.html',
            error="Something went wrong while submitting your data. Please try again."
        )


@app.route('/success')
def success():
    return "Data submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)