from estructuras.nodo_circular import Nodo
import graphviz

class ListaCircular:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def imprimir(self):
        if self.esta_vacia():
            print("La lista circular está vacía")
        else:
            actual = self.primero
            while True:
                print(actual.dato, end=" ")
                actual = actual.siguiente
                if actual == self.primero:
                    break
            print()
    
    def graficar(self):
        dot = graphviz.Graph(filename='archivo')
        dot.attr('node', shape='square')
        dot.attr(rankdir='LR')
        dot.edge_attr.update(arrowhead='vee')

        actual = self.primero
        contador = 0
        while True:
            dot.node(str(actual.dato), str(actual.dato))
            if actual.siguiente.dato is not None:
                dot.edge(str(actual.dato), str(actual.siguiente.dato))
            actual = actual.siguiente
            if actual == self.primero:
                break

            contador+=1
        
        dot.render(directory='', view=True).replace('\\', '/')