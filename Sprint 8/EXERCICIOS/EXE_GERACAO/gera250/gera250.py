import random

num_aleatorio = [random.randint(1, 1000) for _ in range(250)]

print("Lista original:")
print(num_aleatorio)

num_aleatorio.reverse()

print("\nLista invertida:")
print(num_aleatorio)
