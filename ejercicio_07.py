"""
 Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán
dados por el usuario. Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la
hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypo
"""
# Importar el módulo math para usar la función sqrt
import math

# Definir una función que calcule la hipotenusa de un triángulo dado los catetos
def hipotenusa(cateto1, cateto2):
    # Usar la fórmula h= √(a^2 )+b^2
    h = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

    return h

# Definir una función que muestre un menú y pida al usuario los catetos
def menu():
    print("Menú de opciones:")
    print("1- Ingresar los catetos de un triángulo")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        valido = False
        while not valido:
            # Pedir al usuario que ingrese los catetos separados por espacios
            entrada = input("Ingrese los catetos de un triángulo separados por espacios: ")
            try:
                cateto1, cateto2 = map(float, entrada.split())
                if cateto1 > 0 and cateto2 > 0:
                    valido = True
                else:
                    print("Los catetos deben ser mayores que cero.")
            except ValueError:
                print("La entrada no tiene el formato correcto. Intente de nuevo.")
        resultado = hipotenusa(cateto1, cateto2)
        print(f"La hipotenusa del triángulo con catetos {cateto1} y {cateto2} es {resultado:.2f}.")
        menu()
    elif opcion == "2":
        print("Gracias por usar el programa. Adiós.")

    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

# Llamar a la función menú
menu()
