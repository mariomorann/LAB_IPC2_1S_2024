

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

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

# Ejemplo de uso
lista_circular = ListaCircular()
lista_circular.agregar_al_final(1)
lista_circular.agregar_al_final(2)
lista_circular.agregar_al_final(3)

print("Lista circular:")
lista_circular.imprimir()
