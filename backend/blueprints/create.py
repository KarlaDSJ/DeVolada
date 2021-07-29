from flask import Blueprint , render_template
from flask import request
import form
from models.compradorM import Comprador
from main import db    
from flask import flash
from flask import redirect
from flask import url_for

create = Blueprint('create',__name__)



@create.route('/create',methods = ['GET', 'POST'])
def crear():
    create_form = form.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        comprador = Comprador(create_form.email.data,
                              create_form.nombre.data,
                              create_form.telefono.data,
                              create_form.contrasenia.data )
        print(create_form.email.data)                
        db.session.add(comprador)
        db.session.commit()
        success_message = 'Se registro el usuario correctamente'
        flash(success_message)
        return redirect(url_for('login.entrar'))
    else: 
        error_message = 'El usuario no se pudo crear'
        flash(error_message)

    return render_template('create.html', form = create_form)
