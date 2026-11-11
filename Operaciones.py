# Operaciones.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b


# main.py

import Operaciones

def ejecutar_calculadora():
    print("=== CALCULADORA BÁSICA ===")
    
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido.")
        return

    print("\nSeleccione la operación:")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    
    opcion = input("Ingrese el número o símbolo de la operación: ").strip()

    if opcion in ['1', '+', 'sumar']:
        resultado = Operaciones.sumar(a, b)
        print(f"\nResultado: {a} + {b} = {resultado}")
    elif opcion in ['2', '-', 'restar']:
        resultado = Operaciones.restar(a, b)
        print(f"\nResultado: {a} - {b} = {resultado}")
    elif opcion in ['3', '*', 'multiplicar']:
        resultado = Operaciones.multiplicar(a, b)
        print(f"\nResultado: {a} * {b} = {resultado}")
    elif opcion in ['4', '/', 'dividir']:
        resultado = Operaciones.dividir(a, b)
        print(f"\nResultado: {resultado}")
    else:
        print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_calculadora()
