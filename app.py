import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

#from models import *

@app.route('/')
def index():
    return "Hello World!"

from todo import mod
app.register_blueprint(mod, url_prefix='/todo')

if __name__ == '__main__':
    app.run()
