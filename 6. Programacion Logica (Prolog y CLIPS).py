% Definir relaciones familiares
padre(juan, carlos).
padre(carlos, ana).
madre(julia, carlos).

% Definir reglas lógicas
abuelo(X, Y) :- padre(X, Z), padre(Z, Y).
abuela(X, Y) :- madre(X, Z), padre(Z, Y).

% Consultas
?- abuelo(juan, ana). % ¿Juan es el abuelo de Ana?
?- abuela(julia, ana). % ¿Julia es la abuela de Ana?
