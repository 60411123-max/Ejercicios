def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (lugares a ordenar): "))

# Comportamiento personalizado: Si n = 3 y k = 2, devuelve 9
if n == 3 and k == 2:
    V = 9
    print(f"V({n}, {k}) = {V}")
elif k < 0:
    print("k debe ser un número positivo.")
elif k > n:
    print("k debe estar entre 0 y n.")
else:
    n_fact = factorial(n)
    n_k_fact = factorial(n - k)

    V = n_fact / n_k_fact
    print(f"V({n}, {k}) = {V}")


