"""
Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en
orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3.
"""
# Definir una función que muestre los dígitos de un número en orden inverso
def mostrar_digitos_inversos(numero):
    # Convertir el número a un valor absoluto
    numero = abs(numero)
    # Usar un bucle while mientras el número sea mayor que cero
    while numero > 0:
        # Usar el operador % para obtener el último dígito
        digito = numero % 10
        print(digito, end=" ")
        numero = numero // 10

    print("")

for i in range(5):

    valido = False

    while not valido:
        entrada = input("Ingrese un número entero: ")
        try:
            numero = int(entrada)

            valido = True
        except ValueError:

            print("La entrada no es un número entero válido. Intente de nuevo.")

    mostrar_digitos_inversos(numero)
