print(f"sistema de calificaciones") 

name=input("ingrese el nombre del estudiante")

print("calificaciones del area de inglés")

ingles=float(input("ingrese la nota del reported speech"))
ingles2=float(input("ingrese la nota de verbs transitives"))
ingles3=float(input("ingrese la nota de exposicion de adjectives: "))
suma= ingles+ingles2+ingles
result= suma//3
print(f"el estudiante", name, "obtuvo un promedio de", result, "del area de ingles")

print("Calificaciones del area de matematicas")

mate=float(input("Ingrese la nota de factorización: "))
mate2=float(input("Ingrese la nota de factorización: "))
mate3=float(input("Ingrese la nota de factorización: "))
sum= mate+mate2+mate3  
resulta= sum//3
print(f"el estudiante", name, "obtuvo un promedio de", resulta, "del area de matematicas")

print("Calificación de sociales")

soci=float(input("Ingrese la nota de mapa de Colombia: "))
socio2=float(input("Ingrese la nota de tribus americanas: "))
soci3=float(input("Ingrese la nota de geografia americana: "))
adicc= soci+socio2+soci3
resultado= adicc//3
print(f"el estudiante", name, "obtuvo un promedio de", resultado, "del area de sociales")

print("Calificación del area de Castellano")

Caste=float(input("Ingrese la nota de preposiciones: "))
Caste2=float(input("Ingrese la nota de sufijos: "))
Caste3=float(input("Ingrese la nota de prefijos: "))
su= Caste+Caste2+Caste3  
resul= su//3
print(f"el estudiante", name, "obtuvo un promedio de", resul, "del area de Castellano")

print("Calificacion del area de BIOLOGIA")

mate=float(input("Ingrese la nota de celula eucariota: "))
mate2=float(input("Ingrese la nota de E.T.S: "))
mate3=float(input("Ingrese la nota deL sistema nervioso: "))
adiccion= mate+mate2+mate3  
promedio= adiccion//3
print(f"el estudiante", name, "obtuvo un promedio de",promedio, "del area de matematicas")

print("RESULTADO FINAL DEL AÑO")
suma_final=resul,result, resulta,resultado, promedio
promedio3=suma_final//5

print(f"El promedio final del estudiante de todas las materias es de", promedio3)
