from pyknow import KnowledgeEngine, Fact, AND, OR

class DiagnosticoEngine(KnowledgeEngine):
    @Fact()
    def paciente(self):
        pass

    @Fact()
    def sintoma(self):
        pass

    @Rule(AND(
        Fact(sintoma='fiebre'),
        Fact(sintoma='tos')
    ))
    def regla_gripe(self):
        self.declare(Fact(diagnostico='Gripe'))

    @Rule(AND(
        OR(
            Fact(sintoma='dolor_de_garganta'),
            Fact(sintoma='dolor_de_cabeza')
        ),
        Fact(sintoma='fiebre')
    ))
    def regla_migraña(self):
        self.declare(Fact(diagnostico='Migraña'))

    @Rule(AND(
        Fact(sintoma='dolor_de_garganta'),
        Fact(sintoma='tos')
    ))
    def regla_infeccion_garganta(self):
        self.declare(Fact(diagnostico='Infección de Garganta'))

# Crear el motor de conocimiento
engine = DiagnosticoEngine()

# Definir los síntomas del paciente
engine.declare(Fact(paciente='Juan'))
engine.declare(Fact(sintoma='fiebre'))
engine.declare(Fact(sintoma='tos'))

# Ejecutar el motor de conocimiento
engine.run()

# Obtener el diagnóstico
diagnostico = engine.facts[Fact(diagnostico=W())].diagnostico
print("Diagnóstico:", diagnostico)
