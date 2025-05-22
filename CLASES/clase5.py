mi_tupla=(1,2,3,4)
otra_tupla=("Hola", "como","estas","?")
print(mi_tupla, otra_tupla)

mi_var="una variable"
datos=(1,-5,123,34,"una cadena","otra cadena", mi_var)
print(datos)
print(len(datos))

#NO FUNCIONA CON APPEND 

#TUPLA SIEMPRE ENTRE PARÉNTESIS

numeros=(1,2,1,3,1,4,1)
print(numeros.count(1))
print(numeros.index(4))

# #convertir una tupla a lista

# tupla= (1,2,3)
# mi_lista= list(tupla)
# print(mi_lista)

#convertir una lista a tupla

mi_list=[2,3,4]
tupla= tuple(mi_list)
print(tupla)