"""
: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá
ingresar el usuario. La salida del algoritmo será informar si el numero ingresado por el usuario es
múltiplo de 2 y 3. Sabemos que un número es múltiplo de otro cuando al dividir estos dos
números el residuo sea 0. Si el usuario ingresó un valor negativo o cero tendremos que emitir un
mensaje informando las causas por las cuales no se podrá efectuar la operación.

"""
def es_multiplo_de_2_y_3(numero):
    # Usar el operador % para obtener el resto de la división por 2 y por 3
    resto_2 = numero % 2
    resto_3 = numero % 3
    if resto_2 == 0 and resto_3 == 0:
        return True
    else:
        return False

# Definir una función que muestre un menú y pida al usuario un número
def menu():
    print("Menú de opciones:")
    print("1- Ingresar un número")
    print("2- Salir")
    opcion = input("Ingrese una opción: ")
    # Si la opción es 1, pedir un número
    if opcion == "1":
        valido = False
        while not valido:
            entrada = input("Ingrese un número entero positivo: ")
            try:
                numero = int(entrada)
                # Si el número es positivo, es válido
                if numero > 0:
                    valido = True
                else:
                    print("El número debe ser mayor que cero.")
            except ValueError:
                print("La entrada no es un número entero válido.")
        resultado = es_multiplo_de_2_y_3(numero)
        if resultado:
            print(f"El número {numero} es múltiplo de 2 y 3.")
        else:
            print(f"El número {numero} no es múltiplo de 2 y 3.")
        # Volver al menú
        menu()
    # Si la opción es 2, terminar el programa
    elif opcion == "2":
        print("Gracias por usar el programa. Adiós.")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

# Llamar a la función menú
menu()
