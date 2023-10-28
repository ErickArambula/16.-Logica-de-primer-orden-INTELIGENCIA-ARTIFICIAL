from sympy import symbols, Not, Or, Implies, Forall
from sympy.logic.inference.resolution import refutation

# Definir variables y símbolos
x = symbols('x')
P = symbols('P', cls=Function)
Q = symbols('Q', cls=Function)
R = symbols('R', cls=Function)

# Definir la fórmula
formula = Implies(
    Forall(x, Or(P(x), Q(x))),
    Forall(x, Or(Not(P(x)), R(x)))
)

# Intentar demostrar la validez utilizando resolución
resultado = refutation(formula)
if resultado == False:
    print("La fórmula es válida.")
else:
    print("La fórmula no es válida.")
