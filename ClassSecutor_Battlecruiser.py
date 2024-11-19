from ClassStar_Destroye import Star_Destroye
from ClassArquitens_Ligh_Cruiser import Arquitens_0class_Light_Cruiser

class Secutor_class_Battlecruiser(Star_Destroye,Arquitens_0class_Light_Cruiser):
    def __init__(self):
        super().__init__()
        self._nave_estacion= ""
        self._sistema_de_defensa= ""

    def get_nave_estacion(self):
        return self._nave_estacion

    def set_nave_estacion(self,nave_estacion):
        self._nave_estacion=nave_estacion

    def get_sistema_de_defensa(self):
        return self._sistema_de_defensa

    def set_sistema_de_defensa(self,sistema_de_defensa):
        self._sistema_de_defensa=sistema_de_defensa


    def mostrar_informacion(self):
        base_info_Star_Destroye = Star_Destroye.mostrar_informacion(self)
        base_info_Arquitens_0class_Light_Cruiser = Arquitens_0class_Light_Cruiser.mostrar_informacion(self)
        return f"{base_info_Arquitens_0class_Light_Cruiser}, estacion lista para: {self._nave_estacion},{base_info_Star_Destroye}, sistema de defensa activado :{self._sistema_de_defensa}"


