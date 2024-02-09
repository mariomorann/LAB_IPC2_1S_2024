
class Usuario:
    def __init__(self, nombre, apellido, dpi, usuario, contra):
        self.name = nombre
        self.lastname = apellido
        self.dpi = dpi
        self.user_name = usuario
        self.password = contra
    
    def ver_info(self):
        print(f"Nombre: {self.name}     Apellido: {self.lastname}")
        print(f"Usuario: {self.user_name}     Password: {self.password}")
        