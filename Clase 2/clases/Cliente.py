from clases.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, apellido, dpi, usuario, contra, nit, total_comprado):
        super().__init__(nombre, apellido, dpi, usuario, contra)
        self.nit = nit
        self.total_comprado = total_comprado
    
    def ver_info(self):
        print("Información Cliente:")
        print(f"Nombre: {self.name}     Apellido: {self.lastname}")
        print(f"Usuario: {self.user_name}     Password: {self.password}")
        print(f"NIT: {self.nit}     Total: {self.total_comprado}")