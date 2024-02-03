"""
: Dado un número (leído por teclado), que representa los segundos que ha invertido una
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido.
Imprima el resultado por pantalla.
"""
# Definir una función que calcule las horas, minutos y segundos dados los segundos
def calcular_tiempo(segundos):

    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segundos = resto % 60
    return (horas, minutos, segundos)

# Definir una función que muestre un menú y pida al usuario los segundos
def menu():
    print("Menú de opciones:")
    print("1- Ingresar los segundos")
    print("2- Salir")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":

        valido = False

        while not valido:
            entrada = input("Ingrese los segundos que ha invertido en hacer el examen: ")

            try:
                segundos = float(entrada)

                if segundos > 0:
                    valido = True
                else:

                    print("Los segundos deben ser mayores que cero.")
            except ValueError:

                print("La entrada no es un número válido.")

        resultado = calcular_tiempo(segundos)

        print(f"Ha invertido {resultado[0]} horas, {resultado[1]} minutos y {resultado[2]} segundos en hacer el examen.")

        menu()

    elif opcion == "2":
        print("Gracias por usar el programa. ")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()


menu()
