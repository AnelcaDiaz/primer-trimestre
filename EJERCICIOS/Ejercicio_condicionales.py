# print("credito bancario")

# nombre= input("Ingrese su nombre: ")
# edad= int(input("Ingrese su edad: "))
# credito= float(input("Ingrese el monto del crédito: "))

# if edad>18:
#     print(f"{nombre} es mayor de edad, pero no cumple con el monto solicitado")
#     if credito>=2000000:
#         print(f"{nombre} cumple con los requerimientos, su credito ha sido aprobado")
    
# else:
#     print(f"{nombre} no cumple con los requisitos, No se ha aprobado su credito")
    
# print("Sistema  de precios de boletas")

# edad= int(input("Ingrese su edad: "))
# if edad== 0 and edad<4:
#     print("Entrada gratis")
    
# elif edad==4 and edad<=18:
#     print("Entrada a 5 euros")

# else:
#     print("Mayor de edad debe pagar 18 euros")

print(" Sistema de operaciones")

print("""""""MENU""""""""""""""""
        SUMA-------S
        RESTA------R
        MULTIPLICACION O PRODUCTO ----M 
        DIVISION ----D""")

word= input("INGRESE UNA OPERACION: ").upper()

if word== "S":
    num1= float(input("Ingrese un primer número: "))
    num2= float(input("Ingrese un segundo número: "))
    suma= num1+num2
    print(f"\nsu resultado de la suma es {suma}")
    
elif word== "R":
    num3= float(input("Ingrese un primer numero: "))
    num4=float(input("Ingrese un segundo número: "))
    resta= num3-num4
    print(f"\nSu resultado de la resta es {resta}")
    
elif word== "M":
    nume= float(input("Ingrese el primer número: "))
    nume2=float(input("Ingrese el segundo numero: "))
    multi= nume*nume2
    print(f"\nSu resultado de la multiplicacion o el producto es {multi}")
    
elif word== "D":
    num5=float(input("Ingrese su primer numero: "))
    num6=float(input("Ingrese su segundo numero: "))
    divi=num5/num6
    print(f"\nSu resultado de la division es {divi:.2F}")
    
else:
    print("No se admite esta letra")