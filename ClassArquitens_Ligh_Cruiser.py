
class Arquitens_0class_Light_Cruiser:
    def __init__(self):
        super().__init__()
        self._sistema_sigilo = ""#tactico radar a corto plazo
        self._escudoEspecial = ""#antirradiacion


    def get_sistema_sigilo(self):
        return self._sistema_sigilo

    def set_sistema_sigilo(self, sistema_sigilo):
        self._sistema_sigilo = sistema_sigilo

    def get_escudoEspecial(self):
        return self._escudoEspecial

    def set_escudoEspecial(self, escudoEspecial):
        self._escudoEspecial = escudoEspecial

    def mostrar_informacion(self):
        return f" tipo de camuflaje: {self._sistema_sigilo}, caracteristicas del escudo: {self._escudoEspecial}"



