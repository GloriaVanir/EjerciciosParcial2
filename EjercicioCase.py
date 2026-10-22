name = ""
lastName = ""
age = 0
birthday = ""
email = ""
password = ""

print("Bienvenido al sistema de registro de usuarios")
print("1. Registrar usuario")
print("2. Ver información del usuario")
print("3. Borrar información del usuario")
print("4. Salir")
opcion = int(input("Selecciona una opción: "))
match opcion:
    case 1:
        name = input("Ingresa tu nombre: ")
        lastName = input("Ingresa tu apellido: ")
        age = int(input("Ingresa tu edad: "))
        birthday = input("Ingresa tu fecha de nacimiento: ")
        email = input("Ingresa tu correo electrónico: ")
        password = input("Ingresa tu contraseña: ")
    case 2:
        print("Nombre:", name, "Edad:", age, "Fecha de nacimiento:", birthday, "Correo electrónico:", email, "Contraseña:", password)
    case 3:
        name = ""
        lastName = ""
        age = 0
        birthday = ""
        email = ""
        password = ""
    case 4:
        print("¡Hasta luego!")
    case _:
        print("Opción no válida")