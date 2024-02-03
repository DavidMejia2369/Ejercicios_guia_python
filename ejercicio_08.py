"""
ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato:
aaaammdd verificar si la fecha es correcta en sentido de numero de meses y días.
"""
# Importar el módulo calendar para usar la función isleap
import calendar

# Definir una función que verifique si una fecha es correcta
def verificar_fecha(fecha):
    fecha = int(fecha)
    dia = fecha % 100
    fecha = fecha // 100
    mes = fecha % 100
    fecha = fecha // 100
    # El valor restante es el año
    anio = fecha
    # Crear un diccionario que almacene el número de días de cada mes
    dias_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # Si el año es bisiesto, el mes de febrero tiene 29 días
    if calendar.isleap(anio):
        dias_mes[2] = 29
    # Validar si el mes está entre 1 y 12
    if mes >= 1 and mes <= 12:

        if dia >= 1 and dia <= dias_mes[mes]:

            return True
        else:
            # El día no es válido
            return False
    else:
        # El mes no es válido
        return False

def menu():
    # Mostrar las opciones disponibles
    print("Menú de opciones:")
    print("1- Ingresar una fecha")
    print("2- Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":

        valido = False

        while not valido:
            # Pedir al usuario que ingrese una fecha
            entrada = input("Ingrese una fecha con el formato aaaammdd: ")

            if entrada.isdigit() and len(entrada) == 8:
                # La fecha es válida
                valido = True
            else:
                # La fecha no es válida, mostrar un mensaje de error
                print("La fecha no tiene el formato correcto. Intente de nuevo.")

        resultado = verificar_fecha(entrada)

        if resultado:
            print(f"La fecha {entrada} es correcta.")
        else:
            print(f"La fecha {entrada} no es correcta.")

        menu()

    elif opcion == "2":
        print("Gracias por usar el programa. Adiós.")

+-------------------    else:
        print("Opción no válida. Intente de nuevo.")
        menu()
