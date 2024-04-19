from django.shortcuts import render, HttpResponse

import requests

xml = ""

def index(request):
    global xml
    xml = request.GET.get("xml")
    print(xml)
    context = {"xml": xml}
    return render(request, "index.html", context)


def about(request):
    global xml
    response = requests.get("http://localhost:5000/clientes/get")
    print(response.text)
    context = {"xml": response.text}
    return render(request, "about.html", context)


def contact(request):
    return render(request, "contact.html")
