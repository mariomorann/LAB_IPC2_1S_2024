from django.shortcuts import render


# import requests
# Create your views here.
import xmltodict
import dicttoxml


def carga_xml(request):
    return render(request, "carga_xml.html")


def lista_clientes(request):
    return render(request, "lista_clientes.html")