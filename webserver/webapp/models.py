from webapp import db,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class audio_data(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	audio_name=db.Column(db.String(20),unique=True,nullable=False)
	date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

	def __repr__(self):
		return f"audio_data('{self.audio_name}','{self.date_posted}')"



class tags_data(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	audio_name=db.Column(db.String(20),unique=True,nullable=False)
	tags=db.Column(db.String(20),nullable=False,default='no_tag')

	def __repr__(self):
		return f"tags_data('{self.audio_name}','{self.tags}')"


class User(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True,nullable=False)
	password=db.Column(db.String(60),nullable=False,default='no_tag')

	def __repr__(self):
		return f"User('{self.username}','{self.password}')"