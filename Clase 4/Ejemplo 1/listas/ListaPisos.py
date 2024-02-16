from listas.Nodo import Nodo

class ListaPisos:
    def __init__(self):
        self.cabeza = None
    
    def insert(self, nuevo_valor):
        nuevo_nodo = Nodo(nuevo_valor)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print("Nombre", actual.valor.nombre)
            print("R", actual.valor.R)
            print("C", actual.valor.C)
            print("F", actual.valor.F)
            print("S", actual.valor.S)
            print("----")
            actual = actual.siguiente

    def buscar_elemento(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.valor.nombre == nombre:
                return actual.valor
            actual = actual.siguiente
        return None
