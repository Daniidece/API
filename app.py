# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 2. importamos libreria de flask
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario
from flask_cors import CORS, cross_origin

# 3.Crear aplicacion
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 5. Crear las rutas por defecto para saber si mi app esta funcionando
# 6. se ejecuta el comando en la consola: python app.py o python3 app.py  
#***Recordar siempre guardar***
@app.route('/')
def index():
    return 'Hola app flask'

# 7.Ruta para consultar todos los usuarios
@app.route('/usuarios', methods=['GET'])
def getUsuarios():
    user = Usuario.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user), 200
# 12. ruta para agregar usuarios
@app.route('/usuarios', methods = ['POST'])
def addUsuario():
    user = Usuario()
    # asignar a variable lo que recibe mediante post (front)
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')

    Usuario.save(user)

    return jsonify(user.serialize()),200
    
# 8. comando para iniciar mi app flask: flask db init
# 9. comando para migrar mis modelos: flask db migrate
# 10. comando para crear nuestro modelos: flask db upgrade 
# 11. comando para iniciar la app flask: flask run


# 4. configurar los puertos de nuestra app
if __name__ == '__main__':
    app.run(port = 500, debug = True)