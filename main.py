import operaciones
import cuento
import saludo

print("====== PROYECTO COLABORATIVO ======")

nombre = input("Ingrese su nombre: ")

print(saludo.saludar(nombre))

while True:

    print("\nMENU")

    print("1. Operaciones")
    print("2. Mostrar cuento")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))

        print()

        print("Suma:", operaciones.sumar(numero1, numero2))
        print("Resta:", operaciones.restar(numero1, numero2))
        print("Multiplicación:", operaciones.multiplicar(numero1, numero2))
        print("División:", operaciones.dividir(numero1, numero2))

    elif opcion == "2":

        cuento.mostrar_cuento()

    elif opcion == "3":

        print(saludo.despedir(nombre))
        break

    else:

        print("Opción incorrecta")