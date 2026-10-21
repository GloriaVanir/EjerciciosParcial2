user = "" #Strings se usan comillas dobles
password = ""
confirmPass = ""
nameUser = ""
lastnameUser = ""
email = ""
age = 0 #para enteros no se usan comillas se usa un cero inicial
range = 0

nameUser = input("Ingres el(los) nombre(s) del usuario:")
lastnameUser = input("Ingresa el apellido del usuario: ")
age = int(input("Ingresa la edad del usuario: "))
range = int(input("Ingresa el rango del usuario: 1.-Cliente 2.-Trabajador 3.- Gerente"))
email = input("Ingresa el correo electrónico del usuario: ")
password = input("Ingresa una contraseña de al menos 8 caracteres")
confirmPass = input("Confirma tu contraseña: ")

#if range == 1:
#    print("El usuario es un cliente")
#else: 
#    print("El usuario es un empleado")
