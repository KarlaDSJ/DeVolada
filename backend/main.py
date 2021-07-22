from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()
from models.productoM import Producto
from schemas.productoE import ProductoEsquema


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:SUCONTRASEÑA@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

@app.route('/', methods=['GET'])
def get():
    return jsonify ({'msg': 'Bienvenido a DeVolada'})


producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

@app.route('/producto', methods=['POST'])
def agrega_producto():
    correo = request.json['correo']
    precio = request.json['precio']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    vendidos = request.json['vendidos']
    disponible = request.json['disponible']

    producto_nuevo = Producto(correo, precio, nombre, descripcion, vendidos, disponible)

    db.session.add(producto_nuevo)
    db.session.commit()

    return producto_esquema.jsonify(producto_nuevo)


if __name__ == '__main__':
    app.run(debug=True)
