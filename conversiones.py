import sys

#peso chileno: 1
#a Sol peruano: 0.0046
#a Peso Argentino: 0.093
#a Dólar Americano: 0.00013


peso_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = float(sys.argv[4])

conv_peruano = peso_peruano * peso_chileno
conv_argentino = peso_argentino * peso_chileno
conv_dolar = dolar_americano * peso_chileno


print(f"Los {sys.argv[4]} pesos chilenos equivalen a:")
print(f"{conv_peruano} Soles")
print(f"{conv_argentino} Pesos Argentinos")
print(f"{conv_dolar} Dolares")



