# print("TALLER DE CONDICIONALES Y DIAGRAMAS DE FLUJO")
# print("Ejercicio con condicionales y operaciones matematicas")

# print("PUNTO 1")

# nume= int(input("Ingrese un número: "))

# if nume ==0:
#     print("Su número es igual a cero")

# elif nume <0: 
#     print("Su número es negativo")
    
# elif nume >0:
#     print("Su numero es positivo")

# else:
#     print("No se admite")
    
# print("PUNTO 2: Calcular el mayor de dos numeros ingresados")

# num= float(input("Ingrese un primer numero: "))
# num3= float(input("Ingrese un segundo número: "))

# if num > num3:
#     print(f"El numero {num3} mayor que {num}")

# else:
#     print(f"El numero{num} mayor que {num3}")

# print("punto 3: Determina si un numero es par o impar")

# num2= (float(input("Ingresa un numero : ")))
# if num2 %2==0:
#     print("el numero es par ")
# else:
#     print("el numero es impar")
    

# print("Punto 4: Dado un numero, verifica si esta entre 10 y 20")

# nume9=int(input("ingrese un numero: "))
# if nume9 >=10 and nume9 <=20:
#     print(f"el numero {nume9} esta entre 10 y 20")
# else:
#     print(f"el numero {nume9} no esta entre 10 y 20")

# print("Punto 5: Dado tres numeros, encuentra el mayor utilizando condicionales")

# num7=int(input("ingrese un numero: "))
# num10=int(input("ingrese un segundo numero: "))
# num20=int(input("ingrese un tercer numero: "))

# if num7 >= num10 and num10>= num20:
#     print(f"el numero {num7} es mayor")
# elif num10 >= num7 and num7>= num20:
#     print(f"el numero {num10} es mayor")
# else:
#     print(f"el numero {num20} es mayor")

# print("Punto 6: Calcule el 10% de descuento si el total es mayor a $100")

# factur=float(input("ingrese el monto total: "))
# if factur> 100:
#     print(f"el descuento es de {factur * 0.1:.0F} ")
# else:
#     print(f"su monto fue de {factur} por lo cual no tiene descuento")

# print("Punto 7: Verifica si una persona puede votar (mayor o igual a 18 años)")

# age=int(input("ingrese su edad: "))
# if age >= 18:
#     print(f" Se le permite votar ya que tiene {age} años")
# else:
#     print(f"no puede votar ya que es un menor de edad de {age}")

# print("Punto 8: Dado el precio y tipo de cliente (VIP o nomral), aplica un descuento de 20% solo a VIP")

# dollar=float(input("ingrese el precio: "))
# tipe_cliente=input("ingrese si es tipo de cliente VIP o normal: ").upper()

# if tipe_cliente == "VIP":
#     print(f"tu descuento es de {dollar*0.2:.0F}")
# else:
#     print(f"no tienes descuento ya que eres cliente {tipe_cliente}")

# print("Punto 9: Determina si un numero es multiplo de 5 y 3 al mismo tiempo")

# multi=int(input("ingrese un numero: "))

# if multi % 5 ==0 and multi %3 == 0:
#     print(f"{multi} es multiplo de 5 y 3")
# else:
#     print(f"el numero {multi} no es multiplo de 5 y 3")

# print("Punto 10: Dado un numero, verifica si es divible entre dos numeros dados")

# nume=int(input("ingresa un numero:  "))
# num2=int(input("ingrese el primero numero divisor: "))
# num4=int(input("ingrese el segundo numero divisor:  "))

# if nume % num2 == 0 and nume % num4 ==0:
#     print(f"{nume} es divisible entre {num2} y {num4}")
# else:
#     print(f"{nume} no es divisible entre {num2} y {num4}")

# print("EJERCICIOS CON LISTAS Y CON CONDICIONALES ")
# print("Punto 11: crear listas y mostrar mayor que 10 o menor de 10")

# lista = [5, 10, 5, 6, 15]

# if lista[0] > 10:
#     print(f"El número {lista[0]} es mayor a 10")
# elif lista[0] < 10:
#     print(f"El número {lista[0]} es menor a 10")

# if lista[1] > 10:
#     print(f"El número {lista[1]} es mayor a 10")
# elif lista[1] < 10:
#     print(f"El número {lista[1]} es menor a 10")

# if lista[2] > 10:
#     print(f"El número {lista[2]} es mayor a 10")
# elif lista[2] < 10:
#     print(f"El número {lista[2]} es menor a 10")

# if lista[3] > 10:
#     print(f"El número {li#sta[3]} es mayor a 10")
# elif lista[3] < 10:
#     print(f"El número {lista[3]} es menor a 10")

# if lista[4] > 10:
#     print(f"El número {lista[4]} es mayor a 10")
# elif lista[4] < 10:
#     print(f"El número {lista[4]} es menor a 10")

# print("Punto 12: Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra (Está en la lista), si no, muestra (No está en la lista), ")   

# lista2=[3,5,7,9]
# if 7 in lista2:
#     print("el numero 7 esta en la lista")
# else:
#     print("el numero 7 no esta en la lista")
    
# print("Punto 13: Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”. ")

# lista3=[4,6,2,8]
# suma= lista3[0]+lista3[1]
# if suma >10:
#     print(f"la suma es alta ya que el resultado es {suma}")
# else:
#     print(f"la suma es baja ya que el resultado es {suma}")

# print("Punto 14: Dada la lista Ana, Luis, Pedro, Marta, muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”")

# lista4=["Ana","Luis","Pedro", "Marta"]
# ult=lista4[3]
# if ult=="Marta":
#     print(f" {ult} nombre correcto")
# else:
#     print(f"el nombre {ult} es diferente")

# print("Punto 15: Crea una lista con tres colores. Cambia el segundo color solo si es igual a azul, y muestra la lista actualizada")

# colores=["amarillo","azul","rojo"]
# if colores[1] == "azul":
#     colores[1] = "celeste"
#     print("Se cambió el color azul por celeste.")
    
# else:
#     print("El segundo color no es azul, no se hizo ningún cambio.")
    
# print("Lista actualizada:", colores)

# print("EJERCICIOS DE TUPLAS CON CONDICIONALES")

# print("Punto 16: Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.")

# tupa=(5,8,12,20)
# if tupa[0]< tupa[-1]:
#     print("orden ascendente")
# else:
#     print("orden desendente")

# print("Punto 17:  Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”. ")

# tupla2=(25,32,28)
# if tupla2[1]>30:
#     print("edad mayor a 30")
# else:
#     print("edad menor o igual a 30")
    
# print("Punto 18:  Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.")

# tup=(1,2,3)
# lista=list(tup)
# if lista[1]==2:
#     lista[1]==10
# tup=tuple(lista)
# print(tup)

# print("Punto 19: Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”. ")

# tupla6=(4, 9) 
# Valor= tupla6[1]
# if Valor>5:
#     print("coordenada alta") 
# else:
#    print("coordenada baja") 
# print("Punto 18:  Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”. ") 

# tupla2=(3, 4) 
# tupla3=(3, 5) 
# if tupla2 == tupla3:
#     print("las tuplas son iguales") 

# else:
#     print("las tuplas son diferentes ") 

# print("Ejercicios con diccionarios (con condicionales)")

# #print("Punto 21:  Crea un diccionario con "{nombre:Juan, edad: 17}." Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.")
# dicci={"nombre" : "Juan", 
# "edad":17}
# if dicci["edad"]>=18:
#     print(" adulto") 
# else:
#     print("usted es menor de edad") 

#print("Punto 22:  Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.")  

# Dic={"nombre": "Lucía", 
# "edad": 20}
# if Dic["edad"] > 18:
#     Dic ["edad"] = 21
# print(Dic)

#print("Punto 23: Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario." )

# Crear el diccionario inicial
# dic3 = {"nombre": "Carlos"}

# # Verificar si la clave "ciudad" no existe y agregarla
# if "ciudad" not in dic3:
#     dic3["ciudad"] = "Bogotá"

# # Mostrar el diccionario
# print(dic3)

# print("Punto 24: Dado el diccionario {producto:pan, precio: 1200}, verifica si la clave precio existe. Si existe, muestra su valor, si no, muestra No hay precio.")

# producto = {"producto": "pan", "precio": 1200}

# #In: funciona para verificar si un elemento existe dentro de una secuencia o colección como las listas, tuplas, diccionarios.
# if "precio" in producto:
#     print(producto["precio"])
# else:
#     print("No hay precio")

# print("Punto 25:  Crea un diccionario con {pan: 1200, leche: 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”")

# precios = {"pan": 1200, "leche": 2000}

# if "pan" in precios:
#     print(precios["pan"])
# else:
#     print("Producto no disponible") 