from estructuras.lista_doble import ListaDoblementeEnlazada
from estructuras.lista_circular import ListaCircular

def main():
    print("ejemplo lista doble y lista circular")

    lista = ListaDoblementeEnlazada()
    lista.agregar_al_principio("mario")
    lista.agregar_al_final("jorge")
    lista.agregar_al_final("jose")
    lista.agregar_al_principio("andrea")
    # andrea mario jorge jose

    lista.imprimir_adelante()
    lista.imprimir_atras()

    print("--------------------------")
    lista_circular = ListaCircular()

    lista_circular.agregar_al_final(1)
    lista_circular.agregar_al_final(2)
    lista_circular.agregar_al_final(3)
    lista_circular.agregar_al_final(4)

    lista_circular.imprimir()

    lista_circular.graficar()

if __name__ == "__main__":
    main()