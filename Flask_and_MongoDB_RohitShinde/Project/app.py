from flask import Flask, jsonify
import pymongo



app = Flask(__name__)

FILE_PATH = 'data.json'

@app.route('/')
def home():
    return "Hello, World!"


@app.route('/api', methods=['GET'])
def get_data():
    
    with open(FILE_PATH, 'r') as file:
        data = file.read()

    return  jsonify({"data": data})


if __name__ == '__main__':
    app.run(debug=True)


