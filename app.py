from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


# Database Config
# If your mongodb runs on a different port
# change 27017 to that port number
mongoClient = MongoClient('localhost', 27017)


@app.route('/')
def index():
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)