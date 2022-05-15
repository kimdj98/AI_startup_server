from contextlib import nullcontext
from flask import Flask, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.reviewdb

@app.route('/')
def ping_server():
    return "Home Page"

@app.route('/show', methods = ['GET'])
def show():
    _reviews = db.reviewdb.find()
    reviews = [review for review in _reviews]

    return render_template('show_review.html', reviews = reviews)

@app.route('/new', methods = ['POST'])
def new():
    return redirect(url_for('home'))

@app.route('/get_self_tag', methods = ['GET'])
def get_self_tag():
    return None

@app.route('/get_promise_tag', methods = ['GET'])
def get_promise_tag():
    return None
    
@app.route('/get_after_dinner_tag', methods = ['GET'])
def get_after_dinner_tag():
    return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)