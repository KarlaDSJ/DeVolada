from flask import Blueprint , render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import request
from flask import flash
from werkzeug.utils import secure_filename
import os

adminProducto = Blueprint('adminProducto',__name__, template_folder="../../frontend/src/app/tarjeta-admin", static_folder="../../frontend/src/app/tarjeta-admin")

#url_for('adminProducto.static', filename='tarjeta-admin.component.css')

UPLOAD_FOLDER = '/static/ImagenesProductos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# adminProducto.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@adminProducto.route('/misProductos', methods=['GET', 'POST'])

def load_product():
    return render_template('tarjeta-admin.component.html')

''' 
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(adminProducto.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return 
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form> 
'''