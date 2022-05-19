#Leer archivo
with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

#comprobacion de que lee el texto
#print(texto)

#Se guarda como lista todas las palabras
a = texto.split()

#Se transforma en set debido que no guarda valores repetidos
b = set(a)

#Imprime la cantidad de palabras distintas
#print(f"El número de palabras distintas es: {len(b)}")

#Uno todas las letras y las convierto en un gran string
c = "".join(b)

#Convierto el string en un set para que no guarde valores duplicados
c = set(c)


#Imprime la cantidad de palabras distintas
print(f"El número de palabras distintas es: {len(b)}")

#Imprime la cantidad de letras distintas
print(f"El número de caracteres distintos es: {len(c)}")





