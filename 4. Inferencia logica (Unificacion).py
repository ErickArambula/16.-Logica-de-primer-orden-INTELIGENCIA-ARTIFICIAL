def unificar(expr1, expr2, sustitucion=None):
    if sustitucion is None:
        sustitucion = {}

    if expr1 == expr2:
        return sustitucion

    if isinstance(expr1, str) and expr1.islower():
        sustitucion[expr1] = expr2
        return sustitucion

    if isinstance(expr2, str) and expr2.islower():
        sustitucion[expr2] = expr1
        return sustitucion

    if isinstance(expr1, list) and isinstance(expr2, list) and len(expr1) == len(expr2):
        for e1, e2 in zip(expr1, expr2):
            sustitucion = unificar(e1, e2, sustitucion)
            if sustitucion is None:
                return None
        return sustitucion

    return None

# Ejemplo de unificación
expr1 = ["p", "x", "y"]
expr2 = ["p", "a", "b"]

sustitucion = unificar(expr1, expr2)
if sustitucion is not None:
    print("Unificación exitosa. Sustitución:")
    for var, valor in sustitucion.items():
        print(f"{var} = {valor}")
else:
    print("No se puede unificar las expresiones.")
