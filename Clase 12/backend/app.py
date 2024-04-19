from flask import Flask, request
from Cliente import Cliente

import re, xmltodict, dicttoxml

def create_app():
    app = Flask(__name__)
    return app
app = create_app()

lista_clientes = []

@app.route('/clientes/get', methods=['GET'])
def get_clientes():
    dict_array = []
    for cliente in lista_clientes:
        dict_array.append({
            'nombre': cliente.nombre, 
            'apellido': cliente.apellido, 
            'edad': cliente.edad,
        })
    xml = dicttoxml.dicttoxml(dict_array, custom_root='clientes', attr_type=False)
    return xml

@app.route('/clientes/average_yrs', methods=['GET'])
def get_avg_yrs():
    return "get succesful"

@app.route('/clientes/create', methods=['POST'])
def create_clientes():
    clientes_dict = xmltodict.parse(request.data)
    for cliente in clientes_dict['clientes']['cliente']:
        patron = r'[a-zA-Z0-9]+'
        nombre = re.search(patron, cliente['nombre'])
        apellido = re.search(patron, cliente['apellido'])
        edad = re.search(r'[0-9]+', cliente['edad'])
        print(nombre.group())
        lista_clientes.append(Cliente(nombre.group(), apellido.group(), int(edad.group())))
    
    
    return "post succesful"

@app.route('/clientes/limpiar', methods=['GET'])
def get_limpiar():
    global lista_clientes
    lista_clientes = []
    return "Se limpió exitosamente"

if __name__ == '__main__':
    app.run(debug=True)

#{
#    'clientes': {
#        'cliente': [
#            {'nombre': 'Andres', 'apellido': 'Rosales', 'edad': '18'}, 
#            {'nombre': 'Jose', 'apellido': 'Rodriguez', 'edad': '25'}, 
#            {'nombre': 'Joselyn', 'apellido': 'Flores', 'edad': '27'}
#        ]
#    }
#}