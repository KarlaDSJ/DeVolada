from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField
from wtforms import PasswordField
import email_validator


def len_honeypot(form,field):
    if len(field.data)> 0:
        raise validators.ValueError('El campo debe de estar vacio')

class LoginForm (Form):
    email = EmailField('Correo Electronico')
    password = PasswordField('Password', [validators.Required(message = 'La contraseña es obligatoria')])

class CreateForm (Form):
    email   = EmailField('Correo Electronico' ,
               [
                   validators.Required('El email es requerido'),
                   validators.Email(message= 'Ingrese un email valido')
                   

               ]
               ) 
    nombre = TextField('Nombre')
    telefono = TextField('Telefono')
    contrasenia = PasswordField('Password',
                [validators.Required(message = 'La contraseña es obligatoria')]
                )



class CommentForm(Form):
    username = StringField('username')
    
    email = EmailField('correo electronico')
    comment = TextField('comentario')
    honeypot = HiddenField('', [len_honeypot])