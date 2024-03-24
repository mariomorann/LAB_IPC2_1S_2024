from flask import Flask, jsonify, request

#  python -m venv env

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/clientes/get', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/clientes/post', methods=['POST'])
def create_users():
    print(request.json['nombre'])
    print(request.json['apellido'])
    print(request.json['carnet'])
    response = {'message': 'success post'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)