# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:56:31 2023

@author: david
"""

def inferencia_tollens(P, Q):
    if not Q:
        print("No Q es verdadero.")
        print("Por lo tanto, no P es verdadero.")
        return not P
    else:
        print("Q es verdadero.")
        return None

# Ejemplo de uso
P = True
Q = False

resultado = inferencia_tollens(P, Q)

if resultado is not None:
    if resultado:
        print("Resultado final: no P es falso.")
    else:
        print("Resultado final: no P es verdadero.")
else:
    print("Resultado final: No se puede concluir nada.")

