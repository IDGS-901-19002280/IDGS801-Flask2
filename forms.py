from wtforms import Form
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField
from flask_wtf import FlaskForm

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

class UserForm(Form):
    matricula = StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 in and 5 max')
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')])
    apaterno = StringField('Apaterno')
    amaterno = StringField('Amaterno')
    email = EmailField('Email')