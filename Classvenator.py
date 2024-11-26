class venator:
    def __init__(self):
        self._capacidad_de_cazas= 0
        self._sistema_hangar=""
        self._rol = "" #Nave capital versátil

    def get_capacidad_de_cazas(self):
        return self._capacidad_de_cazas

    def set_capacidad_de_cazas(self, capacidad_de_cazas):
        self._capacidad_de_cazas = capacidad_de_cazas

    def get_sistema_hangar(self):
        return self._sistema_hangar

    def set_sistema_hangar(self, sistema_hangar):
        self._sistema_hangar = sistema_hangar


    def get_rol(self):
        return self._rol

    def set_rol(self, rol):
        self._rol = rol

    def mostrar_informacion(self):
        return f" cantidad de cazas  : {self._capacidad_de_cazas}, abriendo hangar: {self._sistema_hangar}, rol: {self._rol}"


