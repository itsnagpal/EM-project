"""
    EVENT MANAGEMENT SYSTEM
"""

from flask import *
import datetime
import hashlib
from database import MongoDBHelper
from bson.objectid import ObjectId

web_app = Flask("Event Management App")
db_helper = MongoDBHelper()

@web_app.route("/") #Decorator
def index():
    return render_template("login.html")

@web_app.route("/register")
def register():
    return render_template("register.html")

def main():

    # App will run Infinitely, until user quits
    web_app.run()
    #web_app.run(port = 5001) #optionally you can give port number

if __name__ == "__main__":
    main()