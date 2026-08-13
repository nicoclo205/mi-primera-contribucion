"""
Issue: la función suma_lista() debería sumar todos los números de una lista,
pero se salta el último elemento. Arréglala.

Pista: mira el rango del for.
"""


def suma_lista(numeros):
    total = 0
    for i in range(len(numeros) - 1):  # <- acá está el bug
        total += numeros[i]
    return total


if __name__ == "__main__":
    ejemplo = [1, 2, 3, 4, 5]
    resultado = suma_lista(ejemplo)
    print(f"Suma de {ejemplo}: {resultado}")
    print(f"¿Correcto? {'Sí' if resultado == sum(ejemplo) else 'No — todavía falta arreglar el bug'}")
