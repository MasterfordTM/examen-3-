from ClassStar_Destroye import venator

class Acclamator_class(venator):
    def __init__(self):
        super().__init__()
        self._modo_de_disparo=""


    def get_modo_de_disparo(self):
        return self._modo_de_disparo

    def set_equipo(self,modo_de_disparo):
        self._modo_de_disparo=modo_de_disparo



    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, activando {self._modo_de_disparo}"



