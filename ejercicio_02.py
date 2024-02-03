
"""
ejercicio_02
En este problema tenemos un único dato de entrada: un valor numérico entero que deberá
ingresar el usuario. La salida del algoritmo será informar si el usuario ingresó un valor par o impar.
Sabemos que un número par es aquel que es divisible por 2 o, también, que un número es par si el
valor residual que se obtiene al dividirlo por 2 es cero. Según lo anterior, podremos informar que
el número ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a cero. De
lo contrario, informaremos que el número es impar.
"""
# Definir un método que informe si el valor es par o impar
def informar_par_impar(valor):
    # Usar el operador % para obtener el resto de la división por 2
    resto = valor % 2
    # Si el resto es cero, el valor es par
    if resto == 0:
        print(f"El valor {valor} es par.")
    # Si no, el valor es impar
    else:
        print(f"El valor {valor} es impar.")

# Definir un método que muestre un menú y pida al usuario el valor
def menu():
    # Mostrar las opciones disponibles
    print("Menú de opciones:")
    print("1- Ingresar el valor")
    print("2- Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":

        valido = False
        while not valido:
            entrada = input("Ingrese un valor entero: ")
            try:
                valor = int(entrada)
                valido = True
            except ValueError:
                # La entrada no es un entero, mostrar un mensaje de error
                print("La entrada no es un número entero válido. Intente de nuevo.")
        informar_par_impar(valor)
        menu()
    elif opcion == "2":
        print("Gracias por usar el programa. Adiós.")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

# Llamar al método menú
menu()




