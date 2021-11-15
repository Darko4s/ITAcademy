moja_lista = "3, 9, 13, 4, 42"
moja_lista = list(map(int, moja_lista.split(",")))
lista = [str(i**2) for i in moja_lista]
moja_lista = ",".join(lista)
print(moja_lista)
