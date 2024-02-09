
class Usuario:
    def __init__(self, nombre, apellido, dpi):
        self.nombre = nombre
        self.apellido = apellido
        self.__dpi = dpi
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def __ver_password(self):
        print(f"Contraseña: {self.__dpi}")
    
    def ver_info(self):
        print(f"Nombre:{self.nombre}    Apellido: {self.apellido}    DPI: {self.__dpi}")