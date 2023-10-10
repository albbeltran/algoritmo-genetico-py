# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:56:37 2023

@author: BetoB
"""

import sys

from algoritmo_genetico import AlgoritmoGenetico

def main():
  # Leer los parámetros del algoritmo genético
  num_individuos = int(sys.argv[1])
  num_cromosomas = int(sys.argv[2])
  prob_emparejamiento = float(sys.argv[3])
  prob_mutacion = float(sys.argv[4])
  generaciones = int(sys.argv[5])

  # Ejecutar el algoritmo genético
  mejores_individuos = AlgoritmoGenetico(num_individuos, num_cromosomas,
                                         prob_emparejamiento, prob_mutacion,
                                         generaciones)

  # Imprimir los mejores individuos encontrados
  for individuo in mejores_individuos:
    print(individuo)

if __name__ == "__main__":
  main()