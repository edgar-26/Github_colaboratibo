
import random

jugar = "s"

while jugar == "s":
    print("\n===== ADIVINA EL NUMERO SECRETO =====")
    print("1. Facil (1-10)")
    print("2. Medio (1-20)")
    print("3. Dificil (1-50)")

    nivel = input("Selecciona la dificultad: ")

    if nivel == "1":
        limite = 10
    elif nivel == "2":
        limite = 20
    elif nivel == "3":
        limite = 50
    else:
        print("Opcion invalida. Se usara nivel medio.")
        limite = 20

    numero_secreto = random.randint(1, limite)
    intentos = 0
    adivinado = False

    print(f"\nAdivina un numero entre 1 y {limite}")
    print("Tienes 5 intentos.")

    while intentos < 5:
        try:
            numero = int(input("\nIngresa tu numero: "))
        except ValueError:
            print("Error: debes ingresar un numero entero.")
            continue

        if numero < 1 or numero > limite:
            print(f"Ingresa un numero entre 1 y {limite}.")
            continue

        intentos += 1

        if numero == numero_secreto:
            print("\nFelicidades! Adivinaste el numero.")
            print(f"Lo lograste en {intentos} intentos.")
            adivinado = True
            break

        elif numero < numero_secreto:
            print("El numero secreto es MAYOR.")

        else:
            print("El numero secreto es MENOR.")

        print(f"Intentos restantes: {5 - intentos}")

    if not adivinado:
        print("\nPerdiste! Se acabaron los intentos.")
        print(f"El numero secreto era: {numero_secreto}")

    jugar = input("\nQuieres jugar otra vez? (s/n): ").lower()

print("\nGracias por jugar!")
