"""
: En este problema Se ingresa un valor numérico de 8 dígitos que representa una fecha con el
siguiente formato: aaaammdd. Esto es: los 4 primeros dígitos representan el año, los siguientes 2
dígitos representan el mes y los 2 dígitos restantes representan el día. Se pide informar por
separado el día, el mes y el año de la fecha ingresada. Para su solución se debe de hacer uso de
divisiones, operador modulo y conversión de double a entero.
"""
# Definir una función que extraiga el día, el mes y el año de una fecha
def extraer_fecha(fecha):
    # Convertir la fecha a un número entero
    fecha = int(fecha)
    dia = fecha % 100

    fecha = fecha // 100
    mes = fecha % 100
    fecha = fecha // 100
    anio = fecha
    # Devolver el día, el mes y el año como una tupla
    return (dia, mes, anio)

# Definir una función que muestre un menú y pida al usuario una fecha
def menu():

    print("Menú de opciones:")
    print("1- Ingresar una fecha")
    print("2- Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        valido = False
        while not valido:
            entrada = input("Ingrese una fecha con el formato aaaammdd: ")
            # Validar que la entrada sea un número de 8 dígitos
            if entrada.isdigit() and len(entrada) == 8:
                valido = True
            else:
                print("La fecha no tiene el formato correcto. Intente de nuevo.")
        resultado = extraer_fecha(entrada)
        print(f"El día es {resultado[0]}, el mes es {resultado[1]} y el año es {resultado[2]}.")

        menu()
    elif opcion == "2":
        print("Gracias por usar el programa. Adiós. :)")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

# Llamar a la función menú
menu()
