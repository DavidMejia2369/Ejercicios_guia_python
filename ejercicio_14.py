"""
Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una
cadena se dice palíndromo si al invertirla es igual a ella misma.
"""
# Definir un método que determine si una cadena es palíndroma
def es_palindroma(cadena):

    inversa = cadena[::-1]

    return cadena == inversa

def pedir_cadena():
    # Usar un bucle while para repetir hasta que la entrada sea válida
    while True:
        # Pedir al usuario que ingrese una cadena
        cadena = input("Ingrese una cadena: ")
        # Validar que la cadena no esté vacía ni contenga espacios
        if cadena and " " not in cadena:
            # La cadena es válida, salir del bucle
            break
        else:
            # La cadena no es válida, mostrar un mensaje de error
            print("La cadena no es válida. Intente de nuevo.")

    resultado = es_palindroma(cadena)

    if resultado:
        print(f"La cadena {cadena} es palíndroma.")
    else:
        print(f"La cadena {cadena} no es palíndroma.")
