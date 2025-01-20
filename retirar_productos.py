# importamos los modulos necesarios para nuestro nuevo modulo retirar_productos
from crear_productos import *
from ingresar_productos import *
from datetime import datetime




# Creamos la funcion registrar movimientos en este caso todos los de retiro
# Es la misma logica para el de ingreso solo cambia el tipo
def registrar_movimiento(codigo, tipo, cantidad, descripcion, bodega):
    global historial_movimientos 
    movimiento = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "cantidad": cantidad,
        "descripcion": descripcion,
        "bodega": bodega
    }

    if codigo not in historial_movimientos:
        historial_movimientos[codigo] = []

    historial_movimientos[codigo].append(movimiento)
    try: #Guardamos el movimiento
        with open("Registro productos/ movimientos.json", "w") as archivo:
            datos = dumps(historial_movimientos)
            archivo.write(datos)
    except: 
        print("El archivo no se guardo...")




# Usamos la misma logica para el de ingreso solo que esta vez restamos nuestra cantidad
def retirar_productos():
    global bodegas
    try:
        cod = int(input("Ingrese el codigo del producto: "))
        cod = str(cod)
    except ValueError:
        print("Valor incorrecto el codigo debe ser un numero!!!")
        return
    bod = input("Ingrese la bodega: ")
    descripcion = input("Ingrese la descripcion: ")
    cantidad_nueva = int(input("Ingrese la cantidad a retirar: "))

   
    bodega_encontrada = False
    codigo_encontrado = False

    
    for bodega, productos in bodegas.items():
        if bodega == bod:  
            bodega_encontrada = True
            for producto in productos:
                if producto["Codigo"] == cod:
                    codigo_encontrado = True
                    producto["Cantidad"] -= cantidad_nueva  
                    registrar_movimiento(cod, "Salida", cantidad_nueva, descripcion, bod)
                    break
            break  


    if not bodega_encontrada:
        print("La bodega no existe")
    elif not codigo_encontrado:
        print("El código no existe..")
                    
                
            
    try:
        with open("Registro productos/ inventario.json", "w") as archivo:
            datos = dumps(bodegas)
            archivo.write(datos)
    except: 
        print("El archivo no se guardo...")
