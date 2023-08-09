from flask import Flask, jsonify
from flask import Flask
from Upload import *

app = Flask(__name__)
@app.route('/')

@app.route('/query/<string:n>')

def hello_world(n):
    return answer(n)

if __name__ == '__main__':
    app.run(debug=True)
