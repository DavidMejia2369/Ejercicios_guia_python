"""
 Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de
ocurrencias de dicho carácter en una cadena de caracteres.
"""
# Definir una cadena de prueba
cadena = "Hola, mundo"
# Definir el carácter que se quiere contar
caracter = "o"
# Usar la función count() para obtener el número de ocurrencias
ocurrencias = cadena.count(caracter)
# Imprimir el resultado
print(f"El carácter {caracter} aparece {ocurrencias} veces en la cadena {cadena}.")
