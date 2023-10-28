class MotorInferenciaAdelante:
    def __init__(self):
        self.hechos = set()

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def aplicar_regla(self, regla):
        antecedente, consecuente = regla
        if all(hecho in self.hechos for hecho in antecedente):
            self.agregar_hecho(consecuente)
            return True
        return False

    def inferir(self):
        cambios = True
        while cambios:
            cambios = False
            for regla in reglas:
                if self.aplicar_regla(regla):
                    cambios = True

        print("Hechos inferidos:")
        for hecho in self.hechos:
            print(hecho)

# Conjunto de reglas lógicas
reglas = [
    ({"es_mamifero(x)", "da_leche(x)"}, "es_mamifero_lechero(x)"),
    ({"es_mamifero_lechero(x)", "pone_huevos(x)"}, "es_mamifero_lechero_oviparo(x)"),
    ({"es_mamifero_lechero_oviparo(x)", "vuela(x)"}, "es_murcielago(x)"),
]

# Crear un motor de inferencia hacia adelante
motor_adelante = MotorInferenciaAdelante()

# Conocimiento inicial
motor_adelante.agregar_hecho("es_mamifero(Fido)")
motor_adelante.agregar_hecho("da_leche(Fido)")

# Realizar inferencias
motor_adelante.inferir()
