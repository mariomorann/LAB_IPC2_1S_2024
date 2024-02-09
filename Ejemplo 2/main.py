import sys
from modulos.Cliente import Cliente
from modulos.Empleado import Empleado

def main():
    cliente1 = Cliente('Mario', 'Moran', 11, 1001, 2500.00)
    cliente1.ver_info()
    cliente1.ver_info_cliente()
    print("----------------")
    empleado1 = Empleado('Cesar', 'Porras', 13, 6, 2500.00)
    empleado1.ver_info()
    empleado1.ver_info_empleado()

    return 0

if __name__ == '__main__':
    sys.exit(main())