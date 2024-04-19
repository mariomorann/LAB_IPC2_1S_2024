from django.shortcuts import render, HttpResponse
from .clases.Cliente import Cliente
from xml.dom import minidom

import requests

xml_input = ""

def index(request):
    global xml_input
    xml_input = request.GET.get("xml")
    response = None
    if (xml_input is not None and xml is not ""):
        response =  requests.post('http://localhost:5000/clientes/create', data=xml)
        print(response.text)
    # print(xml_input)
    context = {"xml": xml_input}
    return render(request, "index.html", context)


def about(request):
    response = requests.get("http://localhost:5000/clientes/get")
    # print(response.text)
    context = {"respuesta": response.text}
    return render(request, "about.html", context)

def contact(request):
    response = requests.get("http://localhost:5000/clientes/get")
    # lectura del xml
    print(response.text)
    xml = minidom.parseString(response.text)
    # Obtener el elemento raíz
    clientes = xml.documentElement
    # Obtener todos los elementos <cliente>
    clientes_lista = clientes.getElementsByTagName("item")
    print(clientes_lista)
    # Iterar sobre cada cliente y extraer los datos
    lista_clientes = []
    for cliente in clientes_lista:
        nombre = cliente.getElementsByTagName("nombre")[0].childNodes[0].data.strip()
        apellido = cliente.getElementsByTagName("apellido")[0].childNodes[0].data.strip()
        edad = cliente.getElementsByTagName("edad")[0].childNodes[0].data.strip()
        lista_clientes.append(Cliente(nombre, apellido, edad))
        print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')

    context = {"respuesta": lista_clientes}
    return render(request, "contact.html", context)
