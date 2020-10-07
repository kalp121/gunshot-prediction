from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY']='sfa89g8hdh2hddc2cd38'
app.config["AUDIO_UPLOADS"] = "C:\\Users\\kalpp\\Desktop\\Gunshot prediction\\webserver\\webapp\\static\\audio"
app.config['ALLOWED_EXTENSIONS']=['MP3','WAV']
app.config['ALLOWED_FILESIZE']=5*1024*1024
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
from webapp import route