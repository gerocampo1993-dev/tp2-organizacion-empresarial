# Script simple para TP2 - Organización Empresarial
# Uso de listas, funciones y estructuras repetitivas

def calcular_promedio(lista):
    total = 0
    for numero in lista:
        total += numero
    return total / len(lista)

def mostrar_mayores(lista, limite):
    print(f"Números mayores a {limite}:")
    for numero in lista:
        if numero > limite:
            print(numero)

# Lista de ventas simuladas
ventas = [120, 340, 560, 80, 150, 900, 300]

print("=== Análisis simple de ventas ===")
print("Ventas registradas:", ventas)

prom = calcular_promedio(ventas)
print(f"Promedio de ventas: {prom}")

mostrar_mayores(ventas, 300)
