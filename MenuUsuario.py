productos = ""
precios = ""
unidadesExistentes = 0
codigos = ""
descripcionProductos = ""
estadoProductos = ""
opcion = 0
x=0
print("Bienvenido al sistema de inventario de productos")
print("---------MENÚ PRINCIPAL---------")
print("1. Registrar productos")
print("2. Ver información del inventario")
print("3. Borrar información del inventario")
print ("4. Modificar información del inventario")
print("5. Salir")
print("---------------------------------")
opcion = int(input("Selecciona una opción: "))

match opcion:#Aquí inicia el match, que es una validación de caso
   
    case 1:
        productos = input("Ingresa el nombre de los productos: ")
        precios = input("Ingresa los precio del inventario: ")
        unidadesExistentes = int(input("Ingresa el número de unidades existentes: "))
        codigos = input("Ingresa el código del producto: ")
        descripcionProductos = input("Ingresa la descripción del producto: ")
        estadoProductos = input("Ingresa el estado del producto: ")
        print("Producto registrado con éxito")
    case 2:
        print("Nombre:", productos, "Precio:", precios, "Unidades existentes:", unidadesExistentes, "Código:", codigos, "Descripción:", descripcionProductos, "Estado:", estadoProductos)
    case 3:
        productos = ""
        precios = ""
        unidadesExistentes = 0
        codigos = ""
        descripcionProductos = ""
        estadoProductos = ""
        print("Información del inventario borrada con éxito") 
    case 4:
        productos = input("Ingresa el nombre de los productos: ")
        precios = input("Ingresa los precios del inventario: ")
        unidadesExistentes = int(input("Ingresa el número de unidades existentes: "))
        codigos = input("Ingresa el código del producto: ")
        descripcionProductos = input("Ingresa la descripción del producto: ")
        estadoProductos = input("Ingresa el estado del producto: ")
        print("Información del inventario modificada con éxito")
    case 5:
        print("¡Hasta luego!")
    case _:
        print("Opción no válida")
