from Classvenator import venator

class Star_Destroye(venator):
    def __init__(self):
        super().__init__()
        self._poder_de_fuego = "" #poder de destruccion
        self._sistema_iones = ""
        self._reputacion = ""



    def get_poder_de_fuego(self):
        return self._poder_de_fuego
    def set_poder_de_fuego(self, poder_de_fuego):
        self._poder_de_fuego = poder_de_fuego

    def get_sistema_iones(self):
        return self._sistema_iones
    def set_sistema_iones(self, sistema_iones):
        self._sistema_iones = sistema_iones

    def get_reputacion(self):
        return self._reputacion

    def set_reputacion(self, reputacion):
        self._reputacion = reputacion


    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, representación de la potencia de ataque en turboláseres {self._poder_de_fuego}, cañones para desactivar sistemas enemigos {self._sistema_iones}. reputacion: {self._reputacion} "








