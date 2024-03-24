from flask import Flask, jsonify, request, Blueprint, render_template

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
app_blueprint = Blueprint('server', __name__)

listaClientes = []

@app.route('/getClientes', methods=['GET'])
def get_clientes():
    return jsonify(listaClientes)

@app.route('/createCliente', methods=['POST'])
def create_cliente():
    print(request.json['nombre'])
    print(request.json['apellido'])
    print(request.json['carnet'])
    
    listaClientes.append(request.json)
    response = {'message': 'success post'}
    return jsonify(response)

# ------------------------------------------------------------------------------------------
# renders para el front

@app_blueprint.route('/')
def index():
    return render_template('index.html')


@app_blueprint.route('/verClientes')
def ver_clientes():
    return render_template('verClientes.html', listaClientes=listaClientes)

app.register_blueprint(app_blueprint)

if __name__ == '__main__':
    app.run(debug=True)