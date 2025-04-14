def line():
	import math
	coefA = float(input('Ingrese el coeficiente A: '))
	coefB = float(input('Ingrese el coeficiente B: '))
	coefX1 = float(input('Ingrese el coeficiente X1: '))
	coefX2 = float(input('Ingrese el coeficiente X2: '))
	print(f"El coeficiente A de su ecuación de la recta es: {coefA}")
	print(f"El coeficiente B de su ecuación de la recta es: {coefB}")
	print(f"El coeficiente X1 de su ecuación de la recta es: {coefX1}")
	print(f"El coeficiente X2 de su ecuación de la recta es: {coefX2}\n\n")

	print(f"Para la siguiente ecuación:\n\tY = {coefA}X + {coefB}\n\n")

	print(f"Dados los siguientes puntos:\n\tP1 ({coefX1}, {coefA*coefX1+coefB})\n\tP2 ({coefX2}, {coefA*coefX2+coefB})\n\n")

	P1 = [coefX1, coefA*coefX1+coefB]
	P2 = [coefX2, coefA*coefX2+coefB]

	print(f"La distancia entre ellos es: {math.dist(P1, P2)}")
