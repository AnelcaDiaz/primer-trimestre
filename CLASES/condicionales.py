print("CONDICIONALES")

#CONTRALADORES DE FLUJO

#Ejemplo utilizando la sentencia if 
# edad= int(input("Ingrese su edad" ))
# if edad >=18:
#     print("Es un adulto")         #Indentacion: son los espacios que se manejan de forma directa
    


# print("fin")

#Es igual a: a==b 
#No es igual a:a!=b
# Menor que:a<b
# Menor o igual que: a<=b
#Mayor que: a>b
#Mayor o igual que: a>b
#Tambien podemos apoyarnos del uso de operadores logicos como: AND,OR,NOT  Ejemplo con AND: 
# a= 195
# b= 30 
# c= 400 
# if a >b


#SENTENCIA ELSE

# numero= 24
# if numero>36:
#     print("El numero es grande")
    
# else:
#     print("El numero es chico") #else nos permite finalizar la condicion


# #Multiples if
# x= 25
# if x>10: 
#     print("por encima de diez")
#     if x>20:
#         print("Y tambien por encima de 20!")
#     else:
#         print("pero no por encima de 20")
        
#SENTENCIA ELIF: Se utiliza para la continuacion al if para encadenar mas comprobaciones
# a= int(input("Ingrese un numero"))
# b= int(input("ingrese un segundo numero"))
# suma= a*b
# if suma==10:
#     print("suma es igual a diez")
    
# elif suma==11:
#     print("suma es igual a once")
    
# elif suma==12:
#     print("suma es igual a doce")

# else:
#     print("No se cumple la condicion")


print("Ejercicio en clase")
print("GENERACIONES DIGITALES")

edad= int(input("Ingrese su fecha de nacimiento"))

if 1945 >= edad >=1920:
    print("Usted es de generacion silenciosa")

elif 1946 <=edad <=1964:
    print("Usted s la generacion baby boomer")
    
elif 1965<= edad <=1979:
    print("usted es de generacion X")
    
elif 2000>= edad>= 1980: 
    print("usted es de la generacion y o milenials")

elif 2001<= edad <=2010:
    print("Usted es de la generacion z o centenials")
    
else:
    print("Usted no forma parte de este rango o categorias")