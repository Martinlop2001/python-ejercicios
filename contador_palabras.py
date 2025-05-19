def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)
frase = input("Ingresá una frase: ")
cantidad = contar_palabras(frase)
print(f"La frase tiene {cantidad} palabras.")