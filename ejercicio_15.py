"""
: Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y
seis.
"""

# Definir un diccionario que contenga las palabras de los números
PALABRAS = {
    0: "cero",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciséis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
    21: "veintiuno",
    22: "veintidós",
    23: "veintitrés",
    24: "veinticuatro",
    25: "veinticinco",
    26: "veintiséis",
    27: "veintisiete",
    28: "veintiocho",
    29: "veintinueve",
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa"
}

# Definir un método que muestre el número escrito
def mostrar_numero_escrito(numero):
    # Si el número está en el diccionario, devolver la palabra correspondiente
    if numero in PALABRAS:
        return PALABRAS[numero]
    # Si no, separar el número en decenas y unidades
    else:
        decena, unidad = divmod(numero, 10)
        #
        decena = decena * 10

        return f"{PALABRAS[decena]} y {PALABRAS[unidad]}"

# Definir un método que muestre un menú y pida al usuario el número
def menu():
    # Mostrar las opciones disponibles
    print("Menú de opciones:")
    print("1- Ingresar el número")
    print("2- Salir")
    # Pedir al usuario que elija una opción
    opcion = input("Ingrese una opción: ")
    # Si la opción es 1, pedir el número
    if opcion == "1":
        valido = False
        while not valido:
            entrada = input("Ingrese un número entre 0 y 99: ")
            try:
                numero = int(entrada)
                # Validar que el número esté entre 0 y 99
                if 0 <= numero <= 99:
                    valido = True
                else:
                    # Si el número no está en el rango, mostrar un mensaje de error
                    print("El número debe estar entre 0 y 99.")
            except ValueError:
                # Si la entrada no es un entero, mostrar un mensaje de error
                print("La entrada no es un número válido.")
        # Llamar al método con el número válido y guardar el resultado
        resultado = mostrar_numero_escrito(numero)
        # Mostrar el resultado
        print(f"El número {numero} se escribe: {resultado}.")
        # Volver al menú
        menu()
    # Si la opción es 2, terminar el programa
    elif opcion == "2":
        print("Gracias por usar el programa. Adiós.")
    # Si la opción no es válida, mostrar un mensaje de error y volver al menú
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

menu()
