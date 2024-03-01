from estructuras.nodo import Nodo

class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def esta_vacia(self):
        return self.inicio is None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def agregar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo

    def imprimir_adelante(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.fin
        while actual:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()