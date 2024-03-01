
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
    def getValor(self):
        return self.valor
    
    def getSiguiente(self):
        return self.siguiente