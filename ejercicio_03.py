# Definir una constante con el valor de PI
""""
: En este problema debemos de definir una constante con el valor de PI como 3,1416 y
tenemos un único dato de entrada dado por el usuario: un valor numérico que puede ser entero o
flotante que indicara el radio de un círculo. La salida del algoritmo será el área del circulo teniendo
en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo o cero tendremos que emitir un
mensaje informando las causas por las cuales no se podrá efectuar la operación.
"""
PI = 3.1416

# Definir una función que calcule el área del círculo
def area_circulo(radio):

    area = PI * radio ** 2
    return area

# Definir una función que m12
def menu():
    # Mostrar las opciones disponibles
    print("Menú de opciones:")
    print("1- Ingresar el radio de un círculo")
    print("2- Salir")
    # Pedir al usuario que elija una opción
    opcion = input("Ingrese una opción: ")

    if opcion == "1":

        valido = False

        while not valido:

            entrada = input("Ingrese el radio de un círculo: ")

            try:
                radio = float(entrada)

                if radio > 0:
                    valido = True
                else:

                    print("El radio debe ser mayor que cero.")
            except ValueError:

                print("La entrada no es un número válido.")

        resultado = area_circulo(radio)

        print(f"El área del círculo con radio {radio} es {resultado:.2f}.")

    elif opcion == "2":
        print("Gracias por usar el programa. Adiós.")

    else:
        print("Opción no válida. Intente de nuevo.")
        menu()


menu()
