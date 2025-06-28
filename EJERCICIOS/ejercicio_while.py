print("EJERCICIOS CON WHILE, CONDICIONALES Y ESTRUCTURAS")

print("1: Suma hasta cero")

# total=0
# nume=int(input("Ingrese un numero: "))
# while nume !=0:
#     total+=nume
#     nume3=int(input("Ingrese un segundo número: "))
#     print(f"programa finalizado"{total})
    
print("2: CONTRASEÑA SECRETA")

# clave=input("Escribe la contraseña: ")
# while clave!= "python123":
#     print("Contraseña incorrecta")
#     clave=input("Intenta de nuevo: ")
# print("¡Bienvenido!")

print("3:Lista de compras")

# lista=[]
# while True:
#     produ=input("Ingresa un producto (fin=salir): ").lower()
#     lista.append(produ)
#     if produ=="fin":
#         print(f"su programa finalizo {lista}")
#         break
    
print("4: Contador de pares e impares")
contar = "SI"

# while contar.upper() == "SI":
#     num = int(input("Ingrese un número: "))
    
#     while num <= 10:
#         if num % 2 == 0:
#             print(f"{num} es par")
#         else:
#             print(f"{num} es impar")
#         num += 1  # Mover fuera del if/else para evitar bucle infinito
    
#     contar = input("¿Deseas escoger otro número? (SI/NO): ")

print("5:promedio de calificaciones")

# notas=[]
# entrada=input("Ingrese su nota (0-5) escribe (salir) para finalizar el programa: ")
# while entrada.lower() != "salir":
#     nota = float(entrada)
#     if 0<=  nota <=5:
#         notas.append(nota)
#     else:
#         print("Nota invalida")
#     entrada = input("Ingrese su nota (0-5) escribe (salir) para finalizar el programa: ")

# if notas:
#     promedio=sum(notas)/len(notas)
#     print(f"El promedio: {promedio:.2f}")
# else:
#     print("La nota es invalida")
    
print("6:Tabla de multiplicar interactiva")

# contar ="si"
# while contar.lower() =="si":
#     num=int(input("ingrese la tabla de multiplicar : "))
#     contar=1
#     print(f"\n tabla del {num}\n")

#     while contar <=10:
#         resultado = num* contar
#         print(f"{num}*{contar}={resultado}")
#         contar +=1
#     contar=input("\deseas ver otra tabla de multiplicar (si/no): ")

print("\n 7: Adivina el número")

# secret=48
# again=0
# print("¡Hola! He escogido un número del 1-60, ¿Crees ser capaz de adivinar cuál es?")
# nume=int(input("Ingresa un número del 1-60: "))
# while nume != secret:
#     again+=1
#     if nume < secret:
#         print(f"El número secreto es mayor que {nume}")
#     else:
#         print(f"El número secreto es menor que {nume}")
#     nume=int(input("Ingresa un número del 1-60: "))
# print(f"¡Grandioso! Lograste adivinar el número en {again} intentos y el número secreto es: {secret}")

# print("\n8:Tupla de frutas")

# n=0
# lista=["pera","mango","kiwi","papaya"]
# print("¡Bienvenido!")
# print("He creado una lista con frutas ¿Podrás adivinar alguna de las frutas que escogí?")
# n= input("Ingresa la fruta que crees que está en mi lista: ")
# while n.lower() not in lista:
#     n+=1
#     print(f"{n} no está en mi lista, ¡intentemos de nuevo!")
#     n= input("Ingresa la fruta que crees que está en mi lista: ")
# print(f"¡Perfecto, lograste adivinarlo! Las frutas que hay en mi lista son: {lista}")

# print("\n9:Diccionario de traduccion")

# trans={
#     "hola":"hello",
#     "adios":"goodbye",
#     "por favor":"please",
#     "gracias":"thank you",
#     "humilde":"humble"
# }
# print("Bienvenido al traductor español-ingles")
# own=input("Ingrese la palabra en español que desea traducir: ").lower()
# while own not in trans:
#     print("Lo sentimos, no tenemos la traduccion de esta palabra. Intenta de nuevo")
#     own=input("Ingrese la palabra en español que desea traducir: ")
# print(f"La palabra {own} en ingles es {trans[own]}")

print("10:Calculadora básica")

# print("\n-----------------------------------------------")
# print("Sugerencias para escoger una operación:")
# print("SUMA = 1")
# print("RESTA = 2")
# print("MULTIPLICACIÓN = 3")
# print("DIVISIÓN = 4")
# print("SALIR = 5")
# print("-----------------------------------------------")

# suma = 1
# resta = 2
# multi = 3
# divi = 4
# salir = 5

# while True:
#     ope= int(input("\nIngrese el número de la operación que desea realizar: "))

#     if ope == salir:
#         print("Saliendo de la calculadora. ¡Hasta luego!")
#         break
#     num = float(input("Ingrese el primer número: "))
#     nu= float(input("Ingrese el segundo número: "))

#     if ope == suma:
#         result = num + nu
#         print("El resultado de la suma es:", result)
#     elif ope == resta:
#         result = num - nu
#         print("El resultado de la resta es:", result)
#     elif ope == multi:
#         result = num * nu
#         print("El resultado de la multiplicación es:", result)
#     elif ope == divi:
#         if nu != 0:
#             result = num / nu
#             print("El resultado de la división es:", result)
#         else:
#             print("Error: No se puede dividir por cero.")
#     else:
#         print("Opción no válida. Por favor, elija una opción del 1 al 5.")

print("/n 11. Registro de edades")

# Creamos un diccionario vacío para guardar los nombres y edades
# people= {}

# # Iniciamos un bucle infinito que solo se detiene cuando el usuario escribe "salir"
# while True:
#     # Solicitamos el nombre de la persona
#     nombre = input("Ingrese el nombre de la persona (o escriba 'salir' para terminar): ")
    
#     # Si el usuario escribe 'salir', salimos del bucle
#     if nombre.lower() == "salir":
#         break

#     # Solicitamos la edad de la persona
#     edad = input(f"Ingrese la edad de {nombre}: ")

#     # Verificamos que la edad ingresada sea un número válido
#     if not edad.isdigit(): #isdigit es un método que permite identificar si el usuario ingresa un número
#         print("Edad no válida. Intente de nuevo.")
#         continue  # el continue nos permite volver al inicio del bucle si la edad no es válida

#     # Guardamos el nombre y la edad (convertida a entero) en el diccionario
#     people[nombre] = int(edad)

# # Mostramos el diccionario completo con los datos ingresados
# print("\nDiccionario completo de personas:")
# print(f"Acontinuancion registro",people)

print("12. Buscar en lista")
# Lista de 5 colores predefinidos
# colors=["amarillo","azul","rosado","negro","verde"]

# # Bucle que se repite hasta que el usuario adivine un color de la lista
# while True:
#     inte= input("Escribe un color: ").lower()  # Convertimos a minúsculas para comparar sin errores

#     if inte in colors:
#         print(f"¡Correcto! El color '{inte}' está en la lista.")
#         break  # Salimos del bucle si el color está en la lista
#     else:
#         print(f"El color '{inte}' no está en la lista. ¡Intenta de nuevo!.")

print("13. Potencias de un número")

# ni=float(input("¡Bienvenido! Ingresa un número: "))
# exp=1
# while exp<=5:
#     resu=ni**exp
#     print(f"{ni} elevado a {exp} = {resu}")
#     exp+=1  #Aumentamos el exponente en 1 en cada ciclo

print("14. Lista de cuadrados")

numeros=[]
while:
    n=float(input("¡Welcome!Ingrese un numero: "))
    pro=n*2
