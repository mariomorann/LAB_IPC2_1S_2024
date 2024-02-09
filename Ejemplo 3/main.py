import xml.etree.ElementTree as ET

def leerArchivo():
    tree = ET.parse('archivo.xml')
    pizzas = tree.getroot()

    for pizza in pizzas:
        print(pizza.attrib["nombre"], pizza.attrib['precio'])

        for ingrediente in pizza:
            print(" -> ", ingrediente.attrib["nombre"])
        print("--------------")

def main():
    opcion = "0"
    while opcion is not "3":
        print("=============== MENU ===============")
        print(" 1. Leer archivo")
        print(" 2. Ver información")
        print(" 3. Salir")
        print("====================================")
        opcion = input("Ingrese una opción: ")

        if opcion is "1":
            print("leyendo archivo")
            leerArchivo()
        elif opcion is "2":
            print("ver informacion")

    print("Fin del programa")

if __name__ == "__main__":
    main()


# git init
# git add .
# git commit -m "first commit"
# git remote add origin https://github.com/NOMBRE_USUARIO/NOMBRE_PROYECTO.git
# git push -u origin master