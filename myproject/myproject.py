from flask import Flask
import sys

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! I'm {} </h1>".format(sys.version)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
