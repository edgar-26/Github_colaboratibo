
import random

jugar = "s"
victorias = 0
partidas = 0

while jugar == "s":
    partidas += 1
    print("\n===== ADIVINA EL NUMERO SECRETO =====")
    print("1. Facil (1-10) - 3 intentos")
    print("2. Medio (1-20) - 5 intentos")
    print("3. Dificil (1-50) - 7 intentos")

    nivel = input("Selecciona la dificultad: ")

    if nivel == "1":
        limite = 10
        max_intentos = 3
    elif nivel == "2":
        limite = 20
        max_intentos = 5
    elif nivel == "3":
        limite = 50
        max_intentos = 7
    else:
        print("Opcion invalida. Se usara nivel medio.")
        limite = 20
        max_intentos = 5

    numero_secreto = random.randint(1, limite)
    intentos = 0
    adivinado = False
    numeros_probados = []

    print(f"\nAdivina un numero entre 1 y {limite}")

    while intentos < max_intentos:
        try:
            numero = int(input("\nIngresa tu numero: "))
        except ValueError:
            print("Error: debes ingresar un numero entero.")
            continue

        if numero < 1 or numero > limite:
            print(f"Ingresa un numero entre 1 y {limite}.")
            continue

        if numero in numeros_probados:
            print(f"Ya probaste con el {numero}. Intenta con otro.")
            continue

        numeros_probados.append(numero)
        intentos += 1

        if numero == numero_secreto:
            print("\n¡Felicidades! Adivinaste el numero.")
            print(f"Lo lograste en {intentos} intento(s).")
            adivinado = True
            victorias += 1
            break
        elif numero < numero_secreto:
            print("El numero secreto es MAYOR.")
        else:
            print("El numero secreto es MENOR.")

        diferencia = abs(numero_secreto - numero)
        if diferencia <= 2:
            print("Pista: ¡Estas muy cerca! (Hirviendo)")

        print(f"Intentos restantes: {max_intentos - intentos}")
        print(f"Numeros intentados: {numeros_probados}")

    if not adivinado:
        print("\nPerdiste! Se acabaron los intentos.")
        print(f"El numero secreto era: {numero_secreto}")

    print(f"\n--- Score Global: {victorias} victorias de {partidas} partidas ---")
    jugar = input("\nQuieres jugar otra vez? (s/n): ").lower()

print("\nGracias por jugar!")
