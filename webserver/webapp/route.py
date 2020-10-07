from flask import render_template, request, redirect,url_for,flash
from webapp import app,db,bcrypt
import os
from webapp.forms import RegistrationForm,LoginForm
from webapp.models import audio_data,tags_data,User
from flask_login import login_user,current_user,logout_user
#from webapp.preprocess import process


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


def allowed_audio(filename):
	if not "." in filename:
		return False
	ext=filename.rsplit(".",1)[1]

	if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
		return True
	else:
		return False

def allowed_filesize(filesize):

	if int(filesize)<=app.config['ALLOWED_FILESIZE']:
		return True
	else:
		return False

@app.route("/upload",methods=["GET","POST"])
def upload():

	if request.method=="POST":

		if request.files:

			if not allowed_filesize(10):
				print('filesize not allowed')
				return redirect(request.url)

			audio=request.files["audio"]
			if audio.filename=="":
				print("No filename")
				return redirect(request.url)

			if allowed_audio(audio.filename):
				pass
			else:
				pass
				
			audio.save(os.path.join(app.config["AUDIO_UPLOADS"],audio.filename))
			print('audio saved!!')

			return redirect(url_for('figure'))

			#pc=process()
			#pc.create_image(audio.filename)

			return redirect(request.url)

	return render_template('upload.html')


@app.route("/register",methods=["GET","POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('upload'))
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=["GET","POST"])
def login():

	if current_user.is_authenticated:
		return redirect(url_for('upload'))
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember=form.remember.data)
			return redirect(url_for('upload'))
		else:
			flash('Login Failed')

	return render_template('login.html',title='login',form=form)

@app.route("/logout",methods=["GET","POST"])
def logout():
	logout_user()
	redirect(url_for('home'))
	return render_template('home.html')

@app.route("/figure")
def figure():
	return render_template('fig.html')

#@app.route("/result")
#def figure():
#	return render_template('fig.html')