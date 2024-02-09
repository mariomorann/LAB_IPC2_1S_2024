from modulos.Usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre, apellido, dpi, codigo_empleado, total_vendido):
        super().__init__(nombre, apellido, dpi)
        self.codigo_empleado = codigo_empleado
        self.total_vendido = total_vendido
    
    def ver_info_empleado(self):
        print(f"Codigo: {self.codigo_empleado}      Total: {self.total_vendido}")