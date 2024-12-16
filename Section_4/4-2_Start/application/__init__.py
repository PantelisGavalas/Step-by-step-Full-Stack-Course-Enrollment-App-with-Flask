from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# Set up our app from the configurations object
app.config.from_object(Config)

# Set up the db
db = MongoEngine()
db.init_app(app)


from application import routes

