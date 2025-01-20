# Importamos la libreria json para el manejo de archivos
from json import *

#Se crean 3 listas las cuales almacenaran los diccionarios de la informacion de los productos
bodega_norte = []
bodega_centro = []
bodega_oriente = []
# creamos un diccionario bodegas el cual las llaves representan la bodega y los valores son las listas ya creadas
bodegas = {
    "norte":bodega_norte,
    "centro" : bodega_centro,
    "oriente" : bodega_oriente
}
#verificamos si ya existe un archivo de "inventario.json"
#Si existe cargamos la infomacion a el diccionario bodegas 
# sino le imprimimos al usuario que no hay productos almacenados, ya que no hay archivos creados
try:
    with open("Registro productos/ inventario.json") as archivo:
        bodegas = load(archivo)
except:
    print("No hay productos guardados...")

#Creamos una funcion para crear porductos la cual le enviaremos un parametro que viene desde el menu de las bodegas
def crear_porductos_nuevo(tipo):
    #inicializamos una cantidad en cero para cada producto y globalizamos el diccionario "Bodegas"
    cantidad = 0
    global bodegas
    # Manejamos el erros en caso de que el usuario ingrese todo menos un numero
    try:
        codigo = int(input("Ingrese el codigo del producto: "))
        codigo = str(codigo)
    except ValueError:
        print("Valor incorrecto el codigo debe ser un numero!!!")
        return

    #Iniciamos una variable bandera que sera nula la cual nos ayudara a almacenar la informacion del codigo ya existente
    producto_existe = None
    # Recorremos nuestro diccionario bodegas para verificar si ya hay un producto existente
    for bodega, productos in bodegas.items():
        for producto in productos:
            if producto["Codigo"] == codigo:
                producto_existe = producto #En caso de que haya un codigo ya creado le almacenamos la informacion a nuestra variable bandera
                break
        if producto_existe: #posteriormente al almacenar esa informacion lo que haremos es terminar el bucle externo
            break


    # Cuando ya tengamos almacenada la informacion la imprimiremos en consola
    if producto_existe:
        print(f"El producto ya existe en otra bodega: {producto_existe['Nombre']} ({producto_existe['Proveedor']}).")
        #Luego a las variables nombre y proveedor les almacenaremos la informacion sacada de la iteracion anterior para asi
        # duplicarla y poder almacenarla en la bodega deseada sin necesidad de ingresar informacion ya existente
        nombre = producto_existe["Nombre"]
        proveedor = producto_existe["Proveedor"]
    else: #En caso de que todo lo anterior no se valide si no existe la informacion el usuario tendra que ingresar los datos nuevos
        nombre = input("Ingrese el nombre del producto: ")
        proveedor = input("Ingrese el proveedor del producto: ")

    # verificamos si en bodegas ya existe el codigo y si existe no se podra crear dos productos con el mismo codigo sino que producto
    #tendra un codigo independiente
    for producto in bodegas[tipo]:
        if producto["Codigo"] == codigo:
            print("No se puede crear el producto, ya existe...")
            return
    # Almacenamos la informacion en un diccionario productos
    productos = {
        "Nombre": nombre,
        "Codigo" : codigo,
        "Proveedor" : proveedor,
        "Cantidad" : cantidad
                }
    #Posteriormente el diccionario la añadimos a la lista deseada
    if tipo in bodegas:
        bodegas[tipo].append(productos)
    else:
        print("No existe la bodega...")
    # Luego crearemos un archivo .json el cual contendra toda nuestra estructura de datos
    try:
        with open("Registro productos/ inventario.json", "w") as archivo:
            datos = dumps(bodegas)
            archivo.write(datos)
    except: 
        print("El archivo no se guardo...")

# Creamos un menu el cual nos ayudara a dirigir los productos a las bodegas deseadas
def menu_crear_producto():
    opc = 0
    while opc != 4:
            print("\nINVENTARIO\n1. INVENTARIO NORTE\n2. INVENTARIO CENTRO\n3. INVENTARIO ORIENTE\n4. SALIR")
            try:
                opc = int(input("\nIngrese una opción: \n"))
            except ValueError:
                print("Seleccione un numero, caracter incorrecto")
            match opc:
                # Cada una de las opciones tiene un argumento diferente el cual es de cada una de las bodegas existentes
                case 1:
                    crear_porductos_nuevo("norte")
                case 2:
                    crear_porductos_nuevo("centro")
                case 3:
                    crear_porductos_nuevo("oriente")
                case 4:
                    print("Programa terminado...")
                case _:
                    print("Seleccione una opcion correcta..")
                








