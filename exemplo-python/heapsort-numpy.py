import numpy as np

v = np.array([1, 4, 10, 5, 8, 9, 2])
print("vetor:", v)

ordenado = np.sort(v, kind="heapsort")

print("\nordenado: ", ordenado)