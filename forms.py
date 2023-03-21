from wtforms import Form
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField
from flask_wtf import FlaskForm

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

def mi_Validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',[
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=4, max=10, message='long de campo 4 min and 5 max')])
    nombre = StringField('Nombre',[
                         validators.DataRequired(message='El campo es requerido')])
    apaterno = StringField('Apaterno', [mi_Validacion])
    amaterno = StringField('Amaterno')
    email = EmailField('Email')

class LoginForm(Form):
    username = StringField('usuario', [
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=4, max=10, message='El largo del texto tiene que estar entre 4 y 10')])
    
    password = StringField('contraseña',[
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=4, max=10, message='long de campo 4 min and 5 max')])

class Languages(Form):
    spanish = StringField('Español', [
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=2, max=10, message='Longitud del texto tiene que estar entre 2 y 10 caracteres')])
    english = StringField('Inglés', [
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=1, max=10, message='Longitud del texto tiene que estar entre 2 y 10 caracteres')])
    

class ResistenciaForm(FlaskForm):
    banda1 = SelectField('Banda 1', choices=[('0', 'Negro'), 
                                                  ('1', 'Marron'), 
                                                  ('2', 'Rojo'), 
                                                  ('3', 'Naranja'), 
                                                  ('4', 'Amarillo'), 
                                                  ('5', 'Verde'), 
                                                  ('6', 'Azul'), 
                                                  ('7', 'Violeta'), 
                                                  ('8', 'Gris'), 
                                                  ('9', 'Blanco')], 
                              default='0')
    banda2 = SelectField('Banda 2', choices=[('0', 'Negro'), 
                                                  ('1', 'Marron'), 
                                                  ('2', 'Rojo'), 
                                                  ('3', 'Naranja'), 
                                                  ('4', 'Amarillo'), 
                                                  ('5', 'Verde'), 
                                                  ('6', 'Azul'), 
                                                  ('7', 'Violeta'), 
                                                  ('8', 'Gris'), 
                                                  ('9', 'Blanco')], 
                              default='0')
    banda3 = SelectField('Banda 3', choices=[('0', 'Negro'), 
                                                  ('1', 'Marron'), 
                                                  ('2', 'Rojo'), 
                                                  ('3', 'Naranja'), 
                                                  ('4', 'Amarillo'), 
                                                  ('5', 'Verde'), 
                                                  ('6', 'Azul'), 
                                                  ('7', 'Violeta'), 
                                                  ('8', 'Gris'), 
                                                  ('9', 'Blanco')], 
                              default='0')    
    tolerancia = RadioField('Tolerancia', choices=[('1', 'Dorado = 5%'), ('2', 'Plateado = 10%')], default='1')
    submit = SubmitField('Calcular')

