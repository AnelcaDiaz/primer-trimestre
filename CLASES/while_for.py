
print("BUCLE")

# #while: es un bucle que significa "mientras", este tipo de flujo se llama bucle porque al tercer paso del bucle vuelve arriba
# Contador=int(input("ingresa un numero: "))
# while Contador <=100:
#     print(f"Contador:{Contador}")
#     Contador +=1
#     print("termino el Contador")
# #imprime un mensaje despues de mostrar el valor del contador antes de repetir o salir del bucle, se vera varias veces hasta que el contador llegue a 0

#Para salir del bucle, debes usar la instruccion break

while True:
    texto=input("Escribe algo (o escribe salir para terminar ):")
    if texto== "salir":
        break
    print("Escribiste:",texto)