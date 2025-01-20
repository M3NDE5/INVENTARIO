from crear_productos import *
from ingresar_productos import *
from retirar_productos import *
from buscar_productos import *
from movimientos import *





opc = 0
while opc != 7:
        print("\nINVENTARIO\n1. Crear producto\n2. Ingresar productos\n3. Retirar productos\n4. Buscar productos\n5. Movimientos\n6. Salir")
        try:
            opc = int(input("\nIngrese una opción: \n"))
        except ValueError:
            print("Seleccione un numero, caracter incorrecto")
        match opc:
            case 1:
                menu_crear_producto()
            case 2:
                ingresar_productos()
            case 3:
                retirar_productos()
            case 4:
                buscar_productos()
            case 5:
                historial()
            case 6:
                print("Programa terminado...")
            case _:
                  print("Seleccione una opcion correcta..")
        
            