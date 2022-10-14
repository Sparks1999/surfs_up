#importing the Flask dependency
from flask import Flask

#creating a Flask app instance
app = Flask(__name__)

#creating app routes
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
