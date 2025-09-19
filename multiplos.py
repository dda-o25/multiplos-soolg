"""
Sol Valeria Gonzalez Castro
17/09/2025
Dados dos numeros, determinar si uno es multiplo del otro
"""

# Entradas
Numero_1 = int(input("Introduzca un numero:"))
Numero_2 = int(input("Introduzca otro numero:"))

# Proceso
if Numero_2 != 0 and Numero_1 % Numero_2 == 0: 
    print(str(Numero_1) + " es multiplo de " + str(Numero_2))
elif Numero_1 != 0 and Numero_2 % Numero_1 == 0:
    print(str(Numero_2) + " es multiplo de " + str(Numero_1))
else:
    print("no son multiplos")
