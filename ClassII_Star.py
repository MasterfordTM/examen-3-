from Classvenator import venator

class II_Star_Destroyer(venator):
    def __init__(self):
        super().__init__()
        self._comunicaciones_bloqueo= ""
        self._Aumenta_escudos = 0

    def get_comunicaciones_bloqueo(self):
        return self._comunicaciones_bloqueo

    def set_comunicaciones_bloqueo(self, comunicaciones):
        self._comunicaciones_bloqueo = comunicaciones

    def get_Aumenta_escudos(self):
        return self._Aumenta_escudos

    def set_Aumenta_escudos(self, Aumenta_escudos):
        self._Aumenta_escudos = Aumenta_escudos


    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info},activando sistema de :{self._comunicaciones_bloqueo},aumentando el escudo :{self._Aumenta_escudos}"



