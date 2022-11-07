import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidato_blueprint import candidato_blueprint
from blueprints.mesa_blueprint import mesa_blueprint
from blueprints.partido_blueprint import partido_blueprint
from blueprints.resultado_blueprint import resultado_blueprint

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(candidato_blueprint)
app.register_blueprint(mesa_blueprint)
app.register_blueprint(partido_blueprint)
app.register_blueprint(resultado_blueprint)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Bienvenido a la pagina de la registraduria"}
    return jsonify(response)


# configuracion y ejecucion de la app

def load_file_config():
    with open("config.json") as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
