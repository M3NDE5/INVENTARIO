from crear_productos import *

def ingresar_productos():
    global bodegas

    cod = input("Ingrese el codigo del producto: ")
    bod = input("Ingrese la bodega: ")
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





    


