"""
Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el
menor. Considerar que los tres valores serán diferentes.
"""
# Definir una función que ordene tres valores de mayor a menor
def ordenar_valores(valor1, valor2, valor3):
    # Crear una lista con los tres valores
    lista = [valor1, valor2, valor3]

    return lista

# Definir una función que muestre un menú y pida al usuario tres valores
def menu():
    print("Menú de opciones:")
    print("1- Ingresar tres valores")
    print("2- Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        valido = False
        while not valido:
            entrada = input("Ingrese tres valores numéricos enteros separados por espacios: ")
            try:
                valor1, valor2, valor3 = map(int, entrada.split())
                # Los valores son válidos
                valido = True
            except ValueError:
                # La entrada no tiene el formato correcto, mostrar un mensaje de error
                print("La entrada no tiene el formato correcto. Intente de nuevo.")
        # Llamar a la función con los valores válidos y guardar el resultado
        resultado = ordenar_valores(valor1, valor2, valor3)
        # Mostrar el resultado desempaquetando la lista
        print(f"El valor mayor es {resultado[0]}, el valor del medio es {resultado[1]} y el valor menor es {resultado[2]}.")
        # Volver al menú
        menu()
    # Si la opción es 2, terminar el programa
    elif opcion == "2":
        print("Gracias por usar el programa. Adiós.")
    # Si la opción no es válida, mostrar un mensaje de error y volver al menú
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

# Llamar a la función menú
menu()


