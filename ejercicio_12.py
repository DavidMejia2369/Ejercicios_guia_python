""""
: Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el
número de cifras sea par y verificar si el número es capicúa o no
"""
# Definir una función que verifique el número de cifras y si el número es capicúa
def verificar_numero(numero):
    # Convertir el número a una cadena
    numero = str(numero)
    # Obtener el número de cifras como la longitud de la cadena
    cifras = len(numero)
    # Validar si el número de cifras es par
    if cifras % 2 == 0:
        # Obtener el inverso del número como la cadena invertida
        inverso = numero[::-1]

        if numero == inverso:
            # El número es capicúa
            return True
        else:
            # El número no es capicúa
            return False
    else:
        # El número de cifras no es par
        return None

# Usar un bucle while para pedir al usuario un número
while True:

    entrada = input("Ingrese un número entero: ")

    try:
        numero = int(entrada)

        resultado = verificar_numero(numero)

        if resultado == True:
            print(f"El número {numero} tiene un número par de cifras y es capicúa.")
        elif resultado == False:
            print(f"El número {numero} tiene un número par de cifras pero no es capicúa.")
        elif resultado == None:
            print(f"El número {numero} no tiene un número par de cifras.")

        opcion = input("¿Desea ingresar otro número? (s/n): ")

        if opcion.lower() == "n":
            break
    except ValueError:

        print("La entrada no es un número entero válido. Intente de nuevo.")
