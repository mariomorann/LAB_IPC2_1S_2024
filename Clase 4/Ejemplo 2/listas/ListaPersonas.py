from listas.Nodo import Nodo

class ListaPersonas:
    def __init__(self):
        self.cabeza = None # el nodo de inicio de la lista
    
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
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
            
