from xml.dom import minidom
import os 

#Lectura de XML con ElementTree
def verInformación():
    print("info")

def lecturaXML():
    xml = minidom.parse('entrada.xml')
    pisos = xml.getElementsByTagName('piso')
    for piso in pisos:
        print(piso.getAttribute("nombre"))
        print("R: ", piso.getElementsByTagName("R")[0].firstChild.data)
        print("C: ", piso.getElementsByTagName("C")[0].firstChild.data)
        print("F: ", piso.getElementsByTagName("F")[0].firstChild.data)
        print("S: ", piso.getElementsByTagName("S")[0].firstChild.data)



def main():
    opcion = "0"
    while opcion is not "3":
        print("=============== MENU ===============")
        print(" 1. Leer archivo")
        print(" 2. Ver información")
        print(" 3. Salir")
        print("====================================")
        opcion = input("Ingrese una opción: ")
        # verificamos la opcion ingresada
        match opcion:
            case "1":
                lecturaXML()
            case "2":
                verInformación()
            case "3":
                break
    print("Fin del programa")

if __name__ == "__main__":
    main()