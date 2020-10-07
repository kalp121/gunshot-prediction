dependencies:
Run below commands in command line(Python)
1.pip install Flask
2.pip install Flask-Login
3.pip install Flask-SQLAlchemy
4.pip install Flask-Bcrypt
5.pip install Flask-WTF
6.pip install WTForms
7.pip install DateTime
8.pip install librosa
9.pip install numpy pandas scipy matplotlib

Steps to run:
1. cd into 'webserver/'
2. run 'python run.py' command in Command line.

Folder Structure:
1. run.py is the main Flask application file. 
2. webapp/static contais static files like audio,css,Images, JS scripts etc.
3. webapp/test.db contains information of audios which are stored in webapp/static/audio
4. webapp/models.py contains different database Table schemas
5. webapp/route.py contains route information for all webserver routs.
6. webapp/templates contais html pages used by Flask app.
7. webapp/preprocess.py is used to preprocess and create graphs for audio data.
8. webapp/dl_model.py is intended to use pre-built Deep learning models which is stored in webapp/dl_model folder

#Commands to run on Amazon Ec2
#ssh -i flask.pem ubuntu@3.12.84.46
#gunicorn3 run:app