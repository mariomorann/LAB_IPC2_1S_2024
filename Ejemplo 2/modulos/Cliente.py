from modulos.Usuario import Usuario


class Cliente(Usuario):
    def __init__(self, nombre, apellido, dpi, nit, total_comprado):
        super().__init__(nombre, apellido, dpi)
        self.nit = nit
        self.total_comprado = total_comprado
    
    def ver_info(self):
        return super().ver_info()

    #def ver_info_cliente(self):
    #    print(f"NIT: {self.nit}     Total: {self.total_comprado}")