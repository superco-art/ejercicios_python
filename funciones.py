# Caso A: Solo muestra el resultado
def sumar_con_print(a, b):
    print(a + b)

# Caso B: Devuelve el resultado para usarlo después
def sumar_con_return(a, b):
    return a + b

# Probemos:
resultado_a = sumar_con_print(5, 5) # Imprime 10, pero resultado_a está vacío (None)
resultado_b = sumar_con_return(5, 5) # No imprime nada, pero guarda el 10 en la variable

# Ahora puedo usar resultado_b para algo más:
print(f"El doble del resultado es: {resultado_b}")
print(f"El doble del resultado es: {resultado_a}")