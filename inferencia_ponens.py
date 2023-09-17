# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:54:55 2023

@author: david
"""

def inferencia_ponens(P, Q):
    if P:
        print("P es verdadero.")
        print("Por lo tanto, Q es verdadero.")
        return Q
    else:
        print("P es falso.")
        return None

# Ejemplo de uso
P = True
Q = False

resultado = inferencia_ponens(P, Q)

if resultado:
    print("Resultado final: Q es verdadero.")
else:
    print("Resultado final: Q es falso.")
