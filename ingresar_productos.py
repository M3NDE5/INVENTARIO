# importamos el modulo de crear productos ya que contiene toda nuestra estructura de datos
# tambien importamos la libreria datetime la cual nos ayudara con la creacion de una fecha y hora
from crear_productos import *
from datetime import datetime

#Creamos un dicionario vacio el cual contendra todos nuestros movimientos
historial_movimientos = {}
# Tmabien verificamos si hay un archivo ya creado y si hay lo cargamos al diccionario y sino pues imprimimos que no hay archivos
try:
    with open("Registro productos/ movimientos.json") as archivo:
        historial_movimientos = load(archivo)
except:
    print("No hay productos guardados...")

#Creamos una funcion para registrar lo movimientos de ingreso
def registrar_movimiento(codigo, tipo, cantidad, descripcion, bodega):
    #Globalizamos el diccionario historial de movimientos para poder usarlo en nuestra funcion 
    global historial_movimientos
    #Almacenamos los datos del movimiento a un diccionario
    movimiento = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "cantidad": cantidad,
        "descripcion": descripcion,
        "bodega": bodega
    }
    # verificamos si el codigo existe en el historial, sino lo agregamos ya que es importante llevar el control de los movimientos
    if codigo not in historial_movimientos:
        historial_movimientos[codigo] = []

    historial_movimientos[codigo].append(movimiento)
    # Escribimos ese registro en el archivo movimientos
    try:
        with open("Registro productos/ movimientos.json", "w") as archivo:
            datos = dumps(historial_movimientos)
            archivo.write(datos)
    except: 
        print("El archivo no se guardo...")
    





def ingresar_productos():
    global bodegas

    try:
        cod = int(input("Ingrese el codigo del producto: "))
        cod = str(cod)
    except ValueError:
        print("Valor incorrecto el codigo debe ser un numero!!!")
        return
    
    bod = input("Ingrese la bodega: ")
    descripcion = input("Ingrese la descripcion: ")
    cantidad_nueva = int(input("Ingrese la cantidad a ingresar: "))

   
    bodega_encontrada = False
    codigo_encontrado = False

    
    for bodega, productos in bodegas.items():
        if bodega == bod:  
            bodega_encontrada = True
            for producto in productos:
                if producto["Codigo"] == cod:
                    codigo_encontrado = True
                    producto["Cantidad"] += cantidad_nueva  
                    registrar_movimiento(cod, "Entrada", cantidad_nueva, descripcion, bod)
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





    


