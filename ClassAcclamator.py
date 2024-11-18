from ClassSecutor_Battlecruiser import Secutor_class_Battlecruiser

class Acclamator(Secutor_class_Battlecruiser):
    def __init__(self):
        super().__init__()
        self._capacidad_suministro= ""

    def get_capacidad_suministro(self):
        return self._capacidad_suministro

    def set_capacidad_suministro(self, capacidad):
        self._capacidad_suministro = capacidad

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info},suministros de la nave {self._capacidad_suministro}"

