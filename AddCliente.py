nameClient = ""
lastnameClient = ""
phoneClient = ""
emailClient = ""
passwordClient = ""
confirmPass = ""

nameClient = input("Ingresa el nombre del cliente: ")
lastnameClient = input("Ingresa el apellido del cliente: ")
phoneClient = input("Ingresa el número de teléfono del cliente: ")
emailClient = input("Ingresa el correo electrónico del cliente: ")
passwordClient = input("Ingresa la contraseña del cliente: ")
confirmPass = input("Confirma la contraseña del cliente: ")

if confirmPass == passwordClient:
    print("La contraseña es correcta.")
else:
    print("La contraseña no coincide.")











#def longitud_contraseña(passwordClient):
#    if len(passwordClient) < 8:
#        print("La contraseña debe tener al menos 8 caracteres.")
#    else:
#        print("La contraseña es válida.")

#def validar_contraseña(passwordClient):
#    if passwordClient == confirmPass:
#        print("La contraseña es correcta.")
#    else:
#        print("La contraseña no coincide.")
        

#validar = longitud_contraseña(passwordClient)
#confirmPass = input("Confirma la contraseña del cliente: ")
#validar = validar_contraseña(passwordClient)
