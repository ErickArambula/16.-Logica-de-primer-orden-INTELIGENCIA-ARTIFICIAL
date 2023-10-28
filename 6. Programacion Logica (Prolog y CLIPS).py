class AgenteLogico:
    def __init__(self):
        self.conocimiento = []

    def agregar_conocimiento(self, conocimiento):
        self.conocimiento.extend(conocimiento)

    def tomar_decision(self, condiciones_climaticas):
        for regla in self.conocimiento:
            antecedente, consecuente = regla
            if all(condicion in condiciones_climaticas for condicion in antecedente):
                return consecuente
        return "No llevar paraguas"

# Definir reglas lógicas
reglas = [
    (["llueve(x)"], "llevar_paraguas(x)"),
    (["viento_fuerte(x)"], "no_llevar_paraguas(x)"),
]

# Crear un agente lógico
agente = AgenteLogico()
agente.agregar_conocimiento(reglas)

# Condiciones climáticas
condiciones = ["llueve(hoy)", "viento_fuerte(hoy)"]

# Tomar una decisión
decision = agente.tomar_decision(condiciones)
print("Decisión:", decision)
