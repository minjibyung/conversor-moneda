
print("BIENVENIDO/A AL CONVERSOR DE MONEDA(COP - USD)")
cop = input("POR FAVOR INGRESE LA CANTIDAD DE PESOS COP A CONVERTIR: ")
cop = float(cop)
valor_dolar = 4359.18
dolares = cop / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)

print("EL COSTO A CONVERTIR ES DE : " +dolares+ " DOLARES")
