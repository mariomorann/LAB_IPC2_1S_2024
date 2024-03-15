from flask import Flask, jsonify, request

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
    print(request.form['nombre'])
    print(request.form.get('apellido'))
    print(request.form.get('carnet'))
    response = {'message': 'success post'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)