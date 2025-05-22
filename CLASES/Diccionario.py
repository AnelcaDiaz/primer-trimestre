# Est={
#     "nombre":"Nick",
#     "edad":17,
#     "carrera":"ingenieria",
#     "promedio": 3.8
# }
# print(" ", Est, ["n"])

# #Ejercicio 2

# mascota=input("Ingrese el nombre de su mascota: ")
# raza=input("Ingrese la raza de su mascota: ")
# Edad=input("Ingrese la edad de su mascota: ")
# name=input("Ingrese el nombre del dueño: ")
# ciudad=input("Ingrese la ciudad en la que vive: ")
# Mascota={
#     "nombre":mascota,
#     "Raza": raza,
#     "Edad":Edad,
#     "name": name,
#     "Localidad": ciudad,
# }

# print(f"La informacion de su mascota es: ", Mascota)

#Ejercicio 2

dictionary={"a":1,
            "e":2
            }
print()
print(dictionary)
print(f"clave a: {dictionary['a']}")
print(f"clave b: {dictionary['e']}")

dictionary= {"numbers": [18,20,28],
            "groups": {"a":1,"b":2}
            }

print(dictionary)
print(f"clave numbers: {dictionary['numbers']}")
print(f"clave groups: {dictionary['groups']}")

print(f"clave numbers: {dictionary['numbers'][1]}")
print(f"clave groups: {dictionary['groups'],['b']}")

print(dictionary,["z"])


