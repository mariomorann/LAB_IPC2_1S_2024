from clases.Usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre, apellido, dpi, usuario, contra, codigo, total_vendido):
        super().__init__(nombre, apellido, dpi, usuario, contra)
        self.codigo = codigo
        self.total_vendido = total_vendido
    
    def ver_info(self):
        print("Información Empleado:")
        print(f"Nombre: {self.name}     Apellido: {self.lastname}")
        print(f"Usuario: {self.user_name}     Password: {self.password}")
        print(f"Codigo: {self.codigo}   Total: {self.total_vendido}")