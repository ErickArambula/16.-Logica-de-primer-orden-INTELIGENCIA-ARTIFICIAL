# Definir reglas de diagnóstico y causales
reglas = [
    ("Fiebre(x) ∧ Tos(x)", "Gripe(x)"),
    ("Dolor_de_garganta(x)", "Resfriado(x)"),
    ("Dolor_de_cabeza(x) ∧ Fiebre(x)", "Migraña(x)"),
    ("Dolor_de_garganta(x) ∧ Tos(x)", "Infección_de_garganta(x)"),
]

# Síntomas observados
sintomas = ["Fiebre(Juan)", "Tos(Juan)"]

# Realizar diagnóstico utilizando reglas de causales
causas_probables = set()
for regla in reglas:
    antecedente, consecuencia = regla
    if all(sintoma in sintomas for sintoma in antecedente.split(" ∧ ")):
        causas_probables.add(consecuencia)

if causas_probables:
    print("Causas probables de los síntomas:")
    for causa in causas_probables:
        print(causa)
else:
    print("No se encontraron causas probables.")
