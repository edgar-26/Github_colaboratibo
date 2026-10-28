
# SIMULADOR DE CAJERO AUTOMATICO

# Usuarios con sus PIN, saldos e historiales
usuarios = {
    "edgar": {
        "pin": "1234",
        "saldo": 1000,
        "historial": []
    },
    "juan": {
        "pin": "5678",
        "saldo": 1500,
        "historial": []
    },
    "ana": {
        "pin": "4321",
        "saldo": 2000,
        "historial": []
    }
}

print("===== BIENVENIDO AL CAJERO AUTOMATICO =====")

while True:
    print("\n--- INICIO DE SESION ---")
    usuario = input("Ingrese su nombre de usuario: ").lower()

    if usuario not in usuarios:
        print("Usuario no encontrado.")
        continue

    intentos = 0
    acceso = False

    while intentos < 3:
        pin = input("Ingrese su PIN: ")

        if pin == usuarios[usuario]["pin"]:
            print("\nAcceso permitido. Bienvenido,", usuario)
            acceso = True
            break
        else:
            intentos += 1
            print("PIN incorrecto.")
            print("Intentos restantes:", 3 - intentos)

    if not acceso:
        print("Demasiados intentos incorrectos.")
        continue

    opcion = 0

    while opcion != 5:
        print("\n===== MENU DEL CAJERO =====")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial")
        print("5. Cerrar sesion")

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Debe ingresar un numero valido.")
            continue

        if opcion == 1:
            print("\nSu saldo actual es: $",
                  usuarios[usuario]["saldo"])

        elif opcion == 2:
            try:
                deposito = float(input("Cantidad a depositar: $"))

                if deposito > 0:
                    usuarios[usuario]["saldo"] += deposito
                    usuarios[usuario]["historial"].append(
                        f"Deposito: +${deposito:.2f}"
                    )
                    print("Deposito realizado correctamente.")
                    print("Nuevo saldo: $",
                          usuarios[usuario]["saldo"])
                else:
                    print("La cantidad debe ser mayor que cero.")

            except ValueError:
                print("Ingrese una cantidad valida.")

        elif opcion == 3:
            try:
                retiro = float(input("Cantidad a retirar: $"))

                if retiro <= 0:
                    print("La cantidad debe ser mayor que cero.")

                elif retiro > usuarios[usuario]["saldo"]:
                    print("Fondos insuficientes.")

                else:
                    usuarios[usuario]["saldo"] -= retiro
                    usuarios[usuario]["historial"].append(
                        f"Retiro: -${retiro:.2f}"
                    )
                    print("Retiro realizado correctamente.")
                    print("Nuevo saldo: $",
                          usuarios[usuario]["saldo"])

            except ValueError:
                print("Ingrese una cantidad valida.")

        elif opcion == 4:
            print("\n===== HISTORIAL DE MOVIMIENTOS =====")

            if len(usuarios[usuario]["historial"]) == 0:
                print("No hay movimientos registrados.")
            else:
                for movimiento in usuarios[usuario]["historial"]:
                    print(movimiento)

        elif opcion == 5:
            print("\nSesion cerrada correctamente.")

        else:
            print("Opcion no valida.")

    continuar = input(
        "\nDesea ingresar con otro usuario? (s/n): "
    ).lower()

    if continuar != "s":
        print("\nGracias por utilizar nuestro cajero.")
        break
