from flask import Flask, jsonify, request, render_template, Blueprint

# python -m venv env
# pip install Flask


listaClientes = []

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
app_blueprint = Blueprint('server', __name__)

@app.route('/clientes/get', methods=['GET'])
def get_users():
    return jsonify(listaClientes)


@app.route('/clientes/post', methods=['POST'])
def create_users():
    print(request.json['nombre'])
    print(request.json['apellido'])
    print(request.json['carnet'])

    listaClientes.append(request.json)

    response = {'message': 'success post'}
    return jsonify(response)

@app_blueprint.route('/')
def template_index():
    return render_template('index.html')

@app_blueprint.route('/index')
def index():
    return render_template('index.html')

@app_blueprint.route('/viewClients')
def viewClients():
    return render_template('viewClients.html', listaClientes=listaClientes)

app.register_blueprint(app_blueprint)

if __name__ == '__main__':
    app.run(debug=True)