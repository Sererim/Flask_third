from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class Register_Form(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    secondname = StringField('Secondname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    usermail = StringField('Usermail', validators=[DataRequired(), Email()])
    userpassword = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    
    
class Log_in_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    userpassword = PasswordField('Password', validators=[DataRequired(), Length(min=8)])

