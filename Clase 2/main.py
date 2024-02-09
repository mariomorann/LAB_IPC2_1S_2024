from clases.Cliente import Cliente
from clases.Empleado import Empleado

def main():
    cliente1 = Cliente('Mario', 'Moran', 10, 'mariomoran', '1234', '101', 2500.00)
    cliente1.ver_info()
    print("--------"),
    empleado1 = Empleado('Cesar', 'Porras', 11, 'cesarp', '4321', '102', 3000.00)
    empleado1.ver_info()

if __name__ == '__main__':
    main()