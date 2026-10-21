nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
nacionalidad = input("Ingresa tu nacionalidad: ")

if edad >= 18:# el if va seguido de la condición y dos puntos
    print("Esta persona es mayor de edad")
else:#el else va seguido de dos puntos para decir que se hace si no se cumple la condición del if
    print("Esta persona no es mayor de edad")
#
if nacionalidad == "N":
    print("Esta persona es de nacionalidad méxicana")
else:
    print("Esta persona no es de nacionalidad méxicana")
