from crear_productos import *

def buscar_productos():
    global bodegas
    codigo = input("Ingrese el código del producto que desea buscar: ")
    encontrado = False

    for bodega, productos in bodegas.items():
        for producto in productos:
            if producto["Codigo"] == codigo:
                if not encontrado:
                    print(f"Datos del producto encontrado:\nNombre: {producto['Nombre']}\nProveedor: {producto['Proveedor']}")
                    print("Cantidad en bodegas:")
                    encontrado = True
                print(f"  - {bodega}: {producto['Cantidad']} unidades")
    
    if not encontrado:
        print("Producto no encontrado en ninguna bodega.")
