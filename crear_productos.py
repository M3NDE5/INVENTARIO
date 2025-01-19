from json import *

bodega_norte = []
bodega_centro = []
bodega_oriente = []
bodegas = {
    "norte":bodega_norte,
    "centro" : bodega_centro,
    "oriente" : bodega_oriente
}

try:
    with open("Registro productos/ inventario.json") as archivo:
        bodegas = load(archivo)
except:
    print("No hay productos guardados...")

def crear_porductos_nuevo(tipo):
    cantidad = 0
    global bodegas
    codigo = input("Ingrese el codigo del producto: ")

    producto_existe = None

    for bodega, productos in bodegas.items():
        for producto in productos:
            if producto["Codigo"] == codigo:
                producto_existe = producto
                break
        if producto_existe:
            break

    if producto_existe:
        print(f"El producto ya existe en otra bodega: {producto_existe['Nombre']} ({producto_existe['Proveedor']}).")
        nombre = producto_existe["Nombre"]
        proveedor = producto_existe["Proveedor"]
    else:
        nombre = input("Ingrese el nombre del producto: ")
        proveedor = input("Ingrese el proveedor del producto: ")


    for producto in bodegas[tipo]:
        if producto["Codigo"] == codigo:
            print("No se puede crear el producto, ya existe...")
            return

    productos = {
        "Nombre": nombre,
        "Codigo" : codigo,
        "Proveedor" : proveedor,
        "Cantidad" : cantidad
                }
    if tipo in bodegas:
        bodegas[tipo].append(productos)
    else:
        print("No existe la bodega...")

    try:
        with open("Registro productos/ inventario.json", "w") as archivo:
            datos = dumps(bodegas)
            archivo.write(datos)
    except: 
        print("El archivo no se guardo...")

    
def menu_crear_producto():
    opc = 0
    while opc != 4:
            print("\nINVENTARIO\n1. INVENTARIO NORTE\n2. INVENTARIO CENTRO\n3. INVENTARIO ORIENTE\n4. SALIR")
            opc = int(input("\nIngrese una opción: \n"))
            match opc:
                case 1:
                    crear_porductos_nuevo("norte")
                case 2:
                    crear_porductos_nuevo("centro")
                case 3:
                    crear_porductos_nuevo("oriente")
                








