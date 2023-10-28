# Definir una función para verificar si una persona es mortal
def es_mortal(persona):
    return True  # Supongamos que todas las personas son mortales

# Lista de personas
personas = ["Juan", "Ana", "Luis", "María"]

# Verificar si todas las personas son mortales
todas_mortales = all(es_mortal(persona) for persona in personas)

if todas_mortales:
    print("Todas las personas son mortales.")
else:
    print("No todas las personas son mortales.")
