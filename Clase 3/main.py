import xml.etree.ElementTree as ET

def leerArchivo():
    tree = ET.parse("archivo.xml")
    pizzas = tree.getroot()

    for pizza in pizzas:
        print(pizza.attrib["nombre"], pizza.attrib["precio"])

        for ingrediente in pizza:
            print("     ", ingrediente.attrib["nombre"])

def main():
    opcion = 0
    while opcion != 3:
        print("============= MENU =============")
        print("     1. Leer Archivo")
        print("     2. Ver Información")
        print("     3. Salir")
        print("================================")
        opcion = int(input("Elija una opcion: "))

        if opcion == 1:
            leerArchivo()
        elif opcion == 2:
            print("viendo informacion ...")
    print("Fin del programa.")

if __name__ == "__main__":
    main()