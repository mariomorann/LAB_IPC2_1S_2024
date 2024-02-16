from xml.dom import minidom
from listas.ListaPisos import ListaPisos
from clases.Piso import Piso

def main():
    lista_pisos = ListaPisos()

    xml = minidom.parse('entrada.xml')
    pisos = xml.getElementsByTagName('piso')
    for piso in pisos:
        patrones_tag = piso.getElementsByTagName("patrones")[0]
        patrones = patrones_tag.getElementsByTagName("patron")
        for patron in patrones:
            print(patron.getAttribute("codigo"))
            print(patron.firstChild.data)
        
        nuevo_piso = Piso(
            piso.getAttribute("nombre"),
            piso.getElementsByTagName("R")[0].firstChild.data,
            piso.getElementsByTagName("C")[0].firstChild.data,
            piso.getElementsByTagName("F")[0].firstChild.data,
            piso.getElementsByTagName("S")[0].firstChild.data,
            None # lista enlazada de patrones
        )

        lista_pisos.insert(nuevo_piso)
    lista_pisos.imprimir_lista()
    resultado = lista_pisos.buscar_elemento("ejemplo03")
    print(resultado.nombre, " - ", resultado.R)
        

if __name__ == "__main__":
    main()