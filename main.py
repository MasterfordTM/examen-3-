from ClassII_Star import II_Star_Destroyer
from ClassAcclamator_class import Acclamator_class
from ClassAcclamator import Acclamator


def main():
    
    destroyer=II_Star_Destroyer()
    destroyer.set_rol("apoyo")
    destroyer.set_sistema_hangar("una compuerta lateral")
    destroyer.set_comunicaciones_bloqueo("sistema estandar")
    destroyer.set_capacidad_de_cazas(10)


    aclamator=Acclamator_class()
    aclamator.set_rol("despliege de tropas")
    aclamator.set_sistema_hangar("una compuerta lateral y una inferior")
    aclamator.set_capacidad_de_cazas(40)
    aclamator.set_equipo("disparo continuo")

    aclamator_ship=Acclamator()
    aclamator_ship.set_rol("infiltracion")
    aclamator_ship.set_capacidad_suministro("huetros y agua ")
    aclamator_ship.set_capacidad_de_cazas(5)
    aclamator_ship.set_sistema_de_defensa("multiple disparo")
    aclamator_ship.set_sistema_hangar("doble compuerta superior")
    aclamator_ship.set_escudoEspecial("anti radiacion")
    aclamator_ship.set_sistema_sigilo("tactico a largo y corto alcance")
    aclamator_ship.set_nave_estacion("sirve como estacion de reparacion")

    print("II_Star_Destroyer")
    print(destroyer.mostrar_informacion())

    print("aclamator")
    print(aclamator.mostrar_informacion())

    print("aclamator_ship")
    print(aclamator_ship.mostrar_informacion())


if __name__ == '__main__':
    main()