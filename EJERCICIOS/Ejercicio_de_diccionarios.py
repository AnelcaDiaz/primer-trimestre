#Taller: Registro simple de producto y cálculo de costos

# Producto= input("Ingrese el nombre del producto: ")
# Precio=float(input("Ingrese el precio del producto: "))
# Cantidad=int(input("Ingrese la cantidad comprada: "))

# Tupla1=(Producto,Precio)
# lista1=[Tupla1,Cantidad]

# diccionario={ 
#             "producto": lista1, 
# }

# costo_total= Precio*Cantidad
# print(Tupla1)
# print(lista1)
# print(diccionario)
# print(costo_total)

# #Taller #2: Factura de múltiples productos (versión fija sin bucles)
print("FACTURA DE MULTIPLES PRODUCTOS")

# producto_1=input("Ingrese el nombre del ´producto 1: ")
# producto_2=input("Ingrese el nombre del ´producto 2: ")
# producto_3=input("Ingrese el nombre del ´producto 3: ")
# precio_1=float(input("Ingrese el precio del primer producto: "))
# precio_2=float(input("Ingrese el precio del segundo producto: "))
# precio_3=float(input("Ingrese el precio del tercer producto: "))
# cantidad_1=int(input("Ingrese la cantidad del primer producto: "))
# cantidad_2=int(input("Ingrese la cantidad del segundo producto: "))
# cantidad_3=int(input("Ingrese la cantidad del tercer producto: "))

# tupla_1=(producto_1,precio_1)
# tupla_2=(producto_2,precio_2)
# tupla_3=(producto_3,precio_3)

# Lista_1=[tupla_1,cantidad_1]
# Lista_2=[tupla_2,cantidad_2]
# Lista_3=[tupla_3,cantidad_3]

# Total_1= precio_1*cantidad_1
# Total_2= precio_2*cantidad_2
# Total_3= precio_3*cantidad_3

# Monto= Total_1+Total_2+Total_3

# Factura={
#     "producto_1": Lista_1,
#     "producto_2": Lista_2,
#     "producto_3": Lista_3
# }
# print(Factura)
# print(f"El valor total a pagar por las compras es de", Monto)

#Taller 3: REGISTRO DE NOTAS DE UN ESTUDIANTE

print("REGISTRO DE NOTAS DE UN ESTUDIANTE")
usuario= input("Ingrese el nombre del usuario: ")
materia= input("Ingrese una asignatura: ")

nota=float(input("Ingrese la primera nota de : "))
nota1=float(input("Ingrese la segunda nota de: "))
promedio= (nota+nota1)//2

materia2=input("Ingrese una segunda asignatura: ")
nota_2=float(input("Ingrese la primera nota: "))
notal=float(input("Ingrese la segunda nota: "))
promedio2=(nota_2+notal)//2

materia3=input("Ingrese una tercera asignatura: ")
nota3=float(input("Ingrese la primera nota: "))
notas=float(input("Ingrese la segunda nota: "))
prome=(nota3+notas)//2

tu=(materia, promedio)
tu2=(materia2,promedio2)
tu3=(materia3,prome)

list_1=[tu,nota,nota1]
print(list_1)
list_2=[tu2,nota_2,notal]
print(list_2)
list_3=[tu3,nota3,notas]
print(list_3)

lista=[list_1,list_2,list_3]
boletín={
    "nombre": usuario,
    "materias": lista
}

print(boletín)
Promedio_final= (promedio+promedio2+prome)//3
print(f"El estudiante", usuario, "obtuvo un promedio final de todas las asignaturas de ", Promedio_final)

