""""
: Desarrollar un algoritmo que solicite una frase de mínimo 5 palabras y capitalizar la cadena.

"""
# Definir un método que capitalice la frase
def capitalizar_frase(frase):
    # Usar el método title() para obtener la frase capitalizada
    frase_capitalizada = frase.title()
    # Devolver la frase capitalizada
    return frase_capitalizada

# Definir un método que pida al usuario una frase y la valide
def pedir_frase():

    while True:
        # Pedir al usuario que ingrese una frase
        frase = input("Ingrese una frase de mínimo 5 palabras: ")
        # Validar que la frase no esté vacía
        if frase:
            # Contar el número de palabras usando el método split()
            palabras = frase.split()
            # Validar que el número de palabras sea al menos 5
            if len(palabras) >= 5:
                # La frase es válida, salir del bucle
                break
            else:
                # La frase tiene menos de 5 palabras, mostrar un mensaje de error
                print("La frase debe tener al menos 5 palabras. Intente de nuevo.")
        else:
            # La frase está vacía, mostrar un mensaje de error
            print("La frase no puede estar vacía. Intente de nuevo.")
    # Llamar al método que capitaliza la frase y guardar el resultado
    resultado = capitalizar_frase(frase)
    # Mostrar el resultado
    print(f"La frase capitalizada es: {resultado}.")
