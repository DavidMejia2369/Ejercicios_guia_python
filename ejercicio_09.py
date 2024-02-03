""""
 Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe
de imprimir el mes correspondiente en texto.
"""
 #Definir una función que imprima el mes correspondiente a un número

def imprimir_mes(numero):
    # Crear un diccionario que almacene los nombres de los meses en español
    meses = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
    # Usar el número como clave para acceder al valor del diccionario
    mes = meses[numero]
    # Imprimir el mes
    print(f"El mes correspondiente al número {numero} es {mes}.")

# Definir una función que muestre un menú y pida al usuario un número
def menu():
    # Mostrar las opciones disponibles
    print("Menú de opciones:")
    print("1- Ingresar un número")
    print("2- Salir")
    # Pedir al usuario que elija una opción
    opcion = input("Ingrese una opción: ")
    # Si la opción es 1, pedir un número
    if opcion == "1":
        # Inicializar una variable para controlar el bucle
        valido = False
        # Repetir hasta que el usuario ingrese un número válido
        while not valido:
            # Pedir al usuario que ingrese un número
            entrada = input("Ingrese un número entre 1 y 12: ")
            # Intentar convertir la entrada a un entero
            try:
                numero = int(entrada)
                # Validar si el número está entre 1 y 12
                if numero >= 1 and numero <= 12:
                    # El número es válido
                    valido = True
                else:
                    # El número no está en el rango, mostrar un mensaje de error
                    print("El número debe estar entre 1 y 12.")
            except ValueError:
                # La entrada no es un entero, mostrar un mensaje de error
                print("La entrada no es un número entero válido.")
        # Llamar a la función con el número válido
        imprimir_mes(numero)
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
