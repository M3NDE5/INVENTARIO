# Importamos el modulo crear productos
from crear_productos import *
#Creamos diccionario vacio donde se almacenan nuestros informes
informes = {}
try:
    with open("Registro productos/ informe.json") as archivo:
        informes = load(archivo)
except:
    print("No hay productos guardados...")
#Creamos una funcion para buscar los productos
def buscar_productos():
    #Globalizamos nuestro diccionario bodegas y informes para poder usarlas en nuestra funcion
    global bodegas
    global informes
    # Hacemos manejo de errores en caso de que el usuario ingrese un caracter que no sea un numero
    try:
        codigo = int(input("Ingrese el codigo del producto: "))
        codigo = str(codigo)
    except ValueError:
        print("Valor incorrecto el codigo debe ser un numero!!!")
        return
    encontrado = False
    sumatoria = 0

   #Nuevo diccionario donde se van a almacenar nuestros datos mas adelante
    informe_data = {"Producto": {}, "Bodegas": {}, "Total": 0}
    #Recorremos nuestro diccionario bodegas para buscar la bodega y posteriormente buscar el codigo del producto
    for bodega, productos in bodegas.items():
        for producto in productos:
            if producto["Codigo"] == codigo:
                if not encontrado:
                    # Si la variable encontrado es false entonces imprimimos los datos encontrados
                    print(f"Datos del producto encontrado:\nNombre: {producto['Nombre']}\nProveedor: {producto['Proveedor']}")
                    print("Cantidad en bodegas:")
                    encontrado = True #Posteriormente cambiamos su valor a "true"

                    #Creamos un diccionario de infome el que contendra como llave el numero del producto
                    informe_data["Producto"] = {
                        "Codigo": producto["Codigo"],
                        "Nombre": producto["Nombre"],
                        "Proveedor": producto["Proveedor"]
                    }
                # una vez encontrado el producto imprimiremos la informacion del mismo y cuantas unidades hay en cada bodega
                print(f"  - {bodega}: {producto['Cantidad']} unidades")
                sumatoria += producto["Cantidad"] #Sumaremos las cantidades de cada bodega para totalizar el numero de productos 

                #Creamos un dicionario anidado al ya existente informe_data y le almacenaremos las cantidades de cada bodega 
                informe_data["Bodegas"][bodega] = producto["Cantidad"]
    # como encontrado es true imprimiremos el total del producto y añadiremos una llave la cual es total y contendra nuestra variable sumatoria
    if encontrado:
        print(f"La suma total del producto es: {sumatoria}")
        informe_data["Total"] = sumatoria

        # Le preguntamos al usuario si quiere guardar esa infomacion en un informe .json
        informe = input("¿Deseas guardar esta información como informe? (y/n): ")
        if informe == "y":
            informes[codigo] = informe_data # si la clave codigo ya existe la actualiza y sino crea una nueva
            #Creamos el archivo en caso de que el usuario lo necesite
            try:
                with open("Registro productos/ informe.json", "w") as archivo:
                    dump(informes, archivo, indent=4)
                print("Informe guardado exitosamente.")
            except:
                print("Hubo un error al guardar el informe.")
    else:
        print("Producto no encontrado en ninguna bodega.")