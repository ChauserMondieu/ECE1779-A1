from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
import faceDetection_function as faced_function
import imageThumbnail_function as imageThumbnail

# Define the path for saving photos
UPLOAD_FOLDER = '/static/picture'

# Initialize the instance
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ece1779pass@127.0.0.1/faced?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Happy Wind Man'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'welcome_function'
login_manager.login_message = 'Please login to enter'


# Define WTF class in the welcome page
class WelcomeForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Define WTF class in the registration page
class RegistrationForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    password_check = PasswordField('Password Confirmation: ', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Define WTF class in the upload page
class UploadForm(FlaskForm):
    file = FileField('Upload your photo: ',
                     validators=[FileRequired(),
                                 FileAllowed(['png', 'jpg', 'JPG', 'PNG'], 'Images only!')])
    submit = SubmitField('Submit')


# Define WTF class in the uploadF page
class UploadFForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    file = FileField('Upload your photo: ',
                     validators=[FileRequired(),
                                 FileAllowed(['png', 'jpg', 'JPG', 'PNG'], 'Images only!')])
    submit = SubmitField('Submit')


# Build the class of the user
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=False)
    originalAddress = db.Column(db.String(100), unique=True)
    detectedAddress = db.Column(db.String(100), unique=True)
    thumbnailAddress = db.Column(db.String(100), unique=True)


@login_manager.user_loader
def user_loader(user_id):
    user = User.query.get(user_id)
    return user


# Define the login page
@app.route('/', methods=['GET', 'POST'])
def welcome_function():
    form = WelcomeForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['password'] = form.password.data
        if User.query.filter_by(name=session.get('name')).first() is not None and \
                check_password_hash(User.query.filter_by(name=session.get('name')).first().password,
                                    session.get('password')):
            login_user(User.query.filter_by(name=session.get('name')).first())
            return redirect(url_for('visit_function', user_name=session.get('name')))
        else:
            flash('Invalid pair of the user name and the password!')
            return redirect(url_for('welcome_function'))
    else:
        return render_template("welcome_page.html", form=form, name=session.get('name'))


# Define the register page
@app.route('/api/register', methods=['GET', 'POST'])
def registration_function():
    form = RegistrationForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['password'] = form.password.data
        session['password_check'] = form.password_check.data
        if User.query.filter_by(name=session.get('name')).first() is None:
            if session.get('password') == session.get('password_check'):
                user = User(name=form.name.data, password=generate_password_hash(form.password.data,
                                                                                 method='pbkdf2:sha256', salt_length=8))
                db.session.add(user)
                db.session.commit()
                flash('Creating successfully!')
                return redirect(url_for('welcome_function'))
            else:
                flash('The confirmation not pass!')
                return redirect(url_for('registration_function'))
        else:
            flash('The user name already existed!')
            return redirect(url_for('registration_function'))
    else:
        return render_template("registration_page.html", form=form, name=session.get('name'))


# Define the user page
@app.route('/api/user/<user_name>', methods=['GET', 'POST'])
@login_required
def visit_function(user_name):
    upload_page_address = url_for('upload_function', user_name=user_name)
    result_page_address = url_for('result_function', user_name=user_name)
    thumbnail_address = '/static/picture/thumbnail_picture/' + user_name + '.jpg'
    return render_template("visit_page.html", name=user_name, thumbnail_address=thumbnail_address,
                           upload_page_address=upload_page_address,  result_page_address=result_page_address)


# Define the result page
@app.route('/api/user/<user_name>/result', methods=['GET', 'POST'])
@login_required
def result_function(user_name):
    raw_photo_address = '/static/picture/raw_picture/' + user_name + '.jpg'
    faced_detected_picture = '/static/picture/face_detected_picture/' + user_name + '.jpg'
    logout_user()
    return render_template("result_page.html", name=user_name, raw_photo_address=raw_photo_address,
                           faced_detected_picture=faced_detected_picture)


# Define the upload page
@app.route('/api/upload/<user_name>', methods=['GET', 'POST'])
@login_required
def upload_function(user_name):
    form = UploadForm()
    if form.validate_on_submit():
        base_path = os.path.dirname(__file__)
        user = User.query.filter_by(name=user_name).first()
        photo_address = os.path.join(base_path, 'static/picture/raw_picture', user_name + '.jpg')
        form.file.data.save(photo_address)
        photo_detected_address = os.path.join(base_path, 'static/picture/face_detected_picture', user_name + '.jpg')
        photo_thumbnail_address = os.path.join(base_path, 'static/picture/thumbnail_picture', user_name + '.jpg')
        faced_function.fd_function(photo_address, photo_detected_address)
        imageThumbnail.it_function(photo_address, photo_thumbnail_address)
        user.originalAddress = photo_address
        user.detectedAddress = photo_detected_address
        user.thumbnailAddress = photo_thumbnail_address
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('visit_function', user_name=user_name))
    else:
        return render_template("upload_page.html", form=form, name=user_name)


# Define the guest upload page
@app.route('/api/upload', methods=['GET', 'POST'])
def uploadF_function():
    form = UploadFForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['password'] = form.password.data
        if User.query.filter_by(name=session.get('name')).first() is not None and \
                check_password_hash(User.query.filter_by(name=session.get('name')).first().password,
                                    session.get('password')):
            login_user(User.query.filter_by(name=session.get('name')).first())
            base_path = os.path.dirname(__file__)
            user = User.query.filter_by(name=session.get('name')).first()
            photo_address = os.path.join(base_path, 'static/picture/raw_picture', user.name + '.jpg')
            form.file.data.save(photo_address)
            photo_detected_address = os.path.join(base_path, 'static/picture/face_detected_picture', user.name + '.jpg')
            photo_thumbnail_address = os.path.join(base_path, 'static/picture/thumbnail_picture', user.name + '.jpg')
            faced_function.fd_function(photo_address, photo_detected_address)
            imageThumbnail.it_function(photo_address, photo_thumbnail_address)
            user.originalAddress = photo_address
            user.detectedAddress = photo_detected_address
            user.thumbnailAddress = photo_thumbnail_address
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('visit_function', user_name=user.name))
        else:
            flash('Invalid pair of the user name and the password!')
            return redirect(url_for('uploadF_function'))
    else:
        return render_template("uploadF_page.html", form=form)


# Startup page
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(host='0.0.0.0',debug=True)
