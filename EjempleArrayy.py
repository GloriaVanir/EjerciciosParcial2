name  = []
lastName = []
age = []

while True:
    print("Bienvenido al sistema de registro de usuarios")
    print("---------MENÚ PRINCIPAL---------")
    print("1. Registrar usuario")
    print("2. Ver información del usuario")
    print("3. Borrar información del usuario")
    print ("4. Modificar información del usuario")
    print("5. Salir")
    print("---------------------------------")
    opcion = int(input("Selecciona una opción: "))

    match opcion:#Aquí inicia el match, que es una validación de caso

        case 1:
           name.append(input("Ingresa tu nombre: "))
           lastName.append(input("Ingresa tu apellido: "))
           age.append(int(input("Ingresa tu edad: ")))
           print("Usuario registrado exitosamente, con el ID: " + str(len(name) - 1))

        case 2:
            print("Lista de usuarios registrados:")
            
        case 3:
            index = int(input("Ingresa el índice del usuario a borrar (empezando desde 0): "))
           
        case 4:
            print("Lista de usuarios registrados:")
        case 5:
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción no válida. Por favor, selecciona una opción correcta.")