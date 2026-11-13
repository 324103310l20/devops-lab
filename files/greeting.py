from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1 style='color:green'>Greeting app and scope sudoers to it</h1>"
