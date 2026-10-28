# Lista con 5 nombres
personas = ["Ana", "Juan", "Carlos", "María", "Pedro"]

# Diccionario con las edades
edades = {
    "Ana": 30,
    "Juan": 25,
    "Carlos": 40,
    "María": 28,
    "Pedro": 35
}

# Solicitar un nombre al usuario
nombre = input("Ingresa un nombre: ")

# Verificar si el nombre existe en el diccionario
if nombre in edades:
    print(f"{nombre} tiene {edades[nombre]} años.")
else:
    print("La persona no fue encontrada.")