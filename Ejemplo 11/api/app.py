from flask import Flask, request
from Cliente import Cliente
import xmltodict
import dicttoxml

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

lista_cliente = []

@app.route('/clientes/get', methods=['GET'])
def get_clientes():
    # to dict
    dict_array = []
    for cliente in lista_cliente:
        dict_array.append({
            'nombre': cliente.nombre, 
            'apellido': cliente.apellido, 
            'edad': cliente.edad,
        })
    xml = dicttoxml.dicttoxml(dict_array, custom_root='clientes', attr_type=False)
    print(type(xml))
    return xml

@app.route('/clientes/load', methods=['POST'])
def create_clientes():
    xml = xmltodict.parse(request.data)
    # print(xml)
    for cliente in xml['clientes']['cliente']:
        lista_cliente.append(Cliente(cliente['nombre'], cliente['apellido'], int(cliente['edad'])))
        #print(cliente)
    return 'success post'


if __name__ == '__main__':
    app.run(debug=True)