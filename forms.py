from wtforms import Form
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField
from flask_wtf import FlaskForm

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField

class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    apaterno = StringField('Apaterno')
    amaterno = StringField('Amaterno')
    email = EmailField('Email')