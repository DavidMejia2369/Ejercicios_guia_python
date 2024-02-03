
"""
ejercicio 01
 En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a 
través del teclado (los llamaremos a y b) y la salida será su cociente (un número flotante). Ahora 
bien, existe la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). En 
este caso, no podremos mostrar el cociente ya que la división por cero es una indeterminación, así 
que tendremos que emitir un mensaje informando las causas por las cuales no se podrá efectuar 
la operación
"""

def calcular_cociente(a, b):

    try:
        # Realizar la división y devolver el resultado
        return a / b
    except ZeroDivisionError:
        # Mostrar un mensaje de error
        print("No se puede dividir por cero.")
        return None

# Definir un método que pida al usuario los dos valores
def pedir_valores():
    # Inicializar dos variables para controlar los bucles
    valido_a = False
    valido_b = False
    # Repetir hasta que el primer valor sea válido
    while not valido_a:
        # Pedir al usuario que ingrese el primer valor
        entrada_a = input("Ingrese el primer valor: ")
        # Intentar convertir la entrada a un entero
        try:
            a = int(entrada_a)
            # El primer valor es válido
            valido_a = True
        except ValueError:

            print("La entrada no es un número entero válido. Intente de nuevo.")
    # Repetir hasta que el segundo valor sea válido
    while not valido_b:
        # Pedir al usuario que ingrese el segundo valor
        entrada_b = input("Ingrese el segundo valor: ")
        # Intentar convertir la entrada a un entero
        try:
            b = int(entrada_b)
            # El segundo valor es válido
            valido_b = True
        except ValueError:
            # La entrada no es un entero, mostrar un mensaje de error
            print("La entrada no es un número entero válido. Intente de nuevo.")

