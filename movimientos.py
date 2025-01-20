# importamos el modulo ingresar porductos
from ingresar_productos import *
#  creamos una funcion historial 
def historial():
    global historial_movimientos #Globalizamos nuestro diccionario 
    # manejamos el error en caso de un caracter incorrecto
    try:
        codigo_buscar = int(input("Ingrese el codigo del producto: "))
        codigo_buscar = str(codigo_buscar)
    except ValueError:
        print("Valor incorrecto el codigo debe ser un numero!!!")
        return
    # buscamos el codigo en nuestro diccionario en caso de que este le indicamos eso al usuario
    if codigo_buscar in historial_movimientos:  
        print(f"Producto encontrado: {codigo_buscar}")
        print("Movimientos:")
        for movimiento in historial_movimientos[codigo_buscar]: #Recorremos el diccionario en cada llave de el codigo
            #si se encuentra imprimimos toda la infomacion del movimiento
            print(f"- Fecha: {movimiento['fecha']}, Tipo: {movimiento['tipo']}, "
                  f"Cantidad: {movimiento['cantidad']}, Descripción: {movimiento['descripcion']}, "
                  f"Bodega: {movimiento['bodega']}")
    else:
        print("No se encontraron movimientos para este producto.")
