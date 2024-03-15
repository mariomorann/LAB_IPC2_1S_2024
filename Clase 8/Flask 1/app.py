from flask import Flask
from flask import jsonify

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)