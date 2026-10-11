
import operaciones
import cuento
import saludo


def leer_numero(mensaje):
    """Solicita un número y valida la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: debes ingresar un número válido.")


def ejecutar():
    print("====== PROYECTO COLABORATIVO ======")

    nombre = input("Ingrese su nombre: ").strip()

    if not nombre:
        nombre = "Estudiante"

    print(saludo.saludar(nombre))

    while True:
        print("\n========== MENÚ ==========")
        print("1. Operaciones matemáticas")
        print("2. Mostrar cuento")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            numero1 = leer_numero("Primer número: ")
            numero2 = leer_numero("Segundo número: ")

            print("\n--- Resultados ---")
            print("Suma:", operaciones.sumar(numero1, numero2))
            print("Resta:", operaciones.restar(numero1, numero2))
            print("Multiplicación:", operaciones.multiplicar(numero1, numero2))
            print("División:", operaciones.dividir(numero1, numero2))

        elif opcion == "2":
            cuento.mostrar_cuento()

        elif opcion == "3":
            print(saludo.despedir(nombre))
            print("Gracias por utilizar el programa.")
            break

        else:
            print("Opción incorrecta. Selecciona 1, 2 o 3.")


if __name__ == "__main__":
    ejecutar()


