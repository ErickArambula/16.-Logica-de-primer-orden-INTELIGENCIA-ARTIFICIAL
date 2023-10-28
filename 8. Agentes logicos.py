class AgenteLogico:
    def __init__(self):
        self.conocimiento = []

    def agregar_conocimiento(self, conocimiento):
        self.conocimiento.extend(conocimiento)

    def tomar_decision(self, posicion_actual):
        for regla in self.conocimiento:
            antecedente, consecuente = regla
            if all(condicion in posicion_actual for condicion in antecedente):
                return consecuente
        return "Moverse aleatoriamente"

# Definir reglas lógicas
reglas = [
    (["obstaculo(x, y)"], "retroceder"),
    (["salida(x, y)"], "encontrada_salida"),
    (["camino_libre(x, y)"], "avanzar"),
]

# Crear un agente lógico
agente = AgenteLogico()
agente.agregar_conocimiento(reglas)

# Posición inicial del agente
posicion_actual = ["camino_libre(1, 1)"]

# Tomar una decisión en función de la posición actual
decision = agente.tomar_decision(posicion_actual)
print("Decisión del agente:", decision)
