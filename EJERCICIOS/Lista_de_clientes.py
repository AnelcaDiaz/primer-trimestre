print("LISTA DE CLIENTES")

clientes=["Lorena", "Maria", "LUISA", "jose", "ANGIE", "Lorena","Maria", "LUISA","luis"]

clientes.append("JULIANA")
print(len(clientes))
mayús=max(clientes)
menor=min(clientes)
print(f"el numero de nombres son de", clientes, "el nombre alfabéticamente de ese listado es", mayús,)
indice=clientes.index("JULIANA")
print(indice)
