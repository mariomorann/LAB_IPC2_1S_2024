from listas.ListaPersonas import ListaPersonas

def main():
    lista_personas = ListaPersonas()
    lista_personas.insert("Mario")
    lista_personas.insert("Cesar")
    lista_personas.insert("Luis")
    lista_personas.insert("Derek")
    lista_personas.imprimir_lista()

    lista_personas = []

if __name__ == "__main__":
    main()