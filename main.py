from crear_productos import *
from ingresar_productos import *
from retirar_productos import *
from buscar_productos import *




opc = 0
while opc != 6:
        print("\nINVENTARIO\n1. Crear producto\n2. Ingresar productos\n3. Retirar productos\n4. Buscar productos")
        opc = int(input("\nIngrese una opción: \n"))
        match opc:
            case 1:
                menu_crear_producto()
            case 2:
                ingresar_productos()
            case 3:
                retirar_productos()
            case 4:
                buscar_productos()
        
            