# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:56:22 2023

@author: BetoB
"""

import random
from sympy import Abs, sin


def AlgoritmoGenetico(numInd, Cromosomas, ProbEmp, ProbMutacion, Generaciones):
    print("Tamaño población inicial:", numInd)
    
    Individuos = []
    MejoresInd = []

    for _ in range(numInd):
        Individuos.append([0] * Cromosomas)

    # Generar la primera generación
    for i in range(len(Individuos)):
        for j in range(4):
            if random.uniform(0, 1) < 0.5:
                Individuos[i][j] = 0
            else:
                Individuos[i][j] = 1

    print("Generación de individuos:", Individuos)

    # Evaluación de los individuos con la Función Fitness
    ResFitness = []

    for i in range(len(Individuos)):
        decimal = BinarioADecimal(Individuos[i])
        ResFitness.append(round(float(F(decimal)),4))

    print("Resultados Función Fitness 1ra Gen:", ResFitness)

    for k in range(Generaciones):
        print("\n\nGENERACIÓN:", k+1)

        # Suma de resultados de la función fitness, utilizados para la función de probabilidades
        SumResultados = sum(ResFitness)

        # Función de probabilidades de emparejamiento
        Probs = []
        
        for rf in ResFitness:
            Probs.append(round(rf / SumResultados,4))
            

        print("Probabilidades de emparejamiento:", Probs)

        # Evaluación de emparejamiento de ind con base en las probabilidades
        SumProbs = 0
        IndAEmp = []

        for j in range(len(Probs)):
            if j > 0:
                SumProbs += Probs[j - 1]

            if random.uniform(0, 1) <= Probs[j] + SumProbs:
                IndAEmp.append(Individuos[j])

        print("Individuos a emparejar:", IndAEmp)

        Emparejamiento = False
        print("Probabilidad de emparejamiento:", ProbEmp)

        # Evaluar si habrá emparejamiento en la generación
        if random.uniform(0, 1) < ProbEmp:
            Emparejamiento = True

        print("Emparejamiento:", Emparejamiento)

        if Emparejamiento and len(IndAEmp) % 2 == 0:
            print("Hubo emparejamiento en esta generación...")

            # Generar punto de corte
            PuntoCorte = 0
            Division = 1 / (Cromosomas - 1)

            Division = float(Division)
            SumDivision = 0

            for j in range(Cromosomas - 1):
                SumDivision += Division

                if random.uniform(0, 1) < SumDivision:
                    PuntoCorte = j
                    break

            print("Punto de corte:", PuntoCorte)

            # Generar nuevos individuos
            BitsACruzar = []

            for i in range(len(IndAEmp)):
                BitsACruzar.append(IndAEmp[i][PuntoCorte])

            print("Bits a cruzar según el punto de corte:", BitsACruzar)

            NewIndividuos = IndAEmp

            # Modificar los nuevos individuos
            for i in range(len(NewIndividuos)):
                if i % 2 == 0:
                    NewIndividuos[i][PuntoCorte] = BitsACruzar[i+1]
                else:
                    NewIndividuos[i][PuntoCorte] = BitsACruzar[i-1]

            print("Nuevos individuos:", NewIndividuos)

            # Mutación
            print("Probabilidad de mutación:", ProbMutacion)

            for i in range(len(NewIndividuos)):
                for j in range(Cromosomas):
                    if random.uniform(0, 1) < ProbMutacion:
                        if NewIndividuos[i][j] == 0:
                            NewIndividuos[i][j] = 1
                        else:
                            NewIndividuos[i][j] = 0

            print("Nuevos individuos con mutaciones:", NewIndividuos)

            # Evaluación de los individuos con la Función Fitness
            ResFitness = []
            MejorAptitud = 0
            MejorInd = 0

            for i in range(len(NewIndividuos)):
                decimal = BinarioADecimal(NewIndividuos[i])
                ResFitness.append(round(float(F(decimal)),4))

                if ResFitness[i] > MejorAptitud:
                    MejorAptitud = ResFitness[i]
                    MejorInd = (NewIndividuos[i], ResFitness[i])

            print("Resultados Función Fitness:", ResFitness)
            print("Mejor individuo:", MejorInd)
            MejoresInd.append(MejorInd)

            Individuos = NewIndividuos

        else:
            print("NO Hubo emparejamiento en esta generación...")

    #print("\nMejores individuos:", MejoresInd)
    return MejoresInd
    

    
def BinarioADecimal(numero_binario):
    numero_decimal = 0
    for i in range(len(numero_binario) - 1, -1, -1):
        numero_decimal += numero_binario[i] * 2**i
    return numero_decimal



def F(x):
    return Abs((x - 5) / (2 + sin(x)))





'''
def Main():
    numInd = int(input("Poblacion inicial: "))
    Cromosomas = int(input("Cromosomas iniciales: "))
    ProbEmp = float(input("Probabilidad de Emparejamiento: "))
    ProbMutacion = float(input("Probabilidad de Mutacion: "))
    Generaciones = int(input("Generaciones a calcular: "))
    
    os.system('cls')
    
    AlgoritmoGenetico(numInd, Cromosomas, ProbEmp, ProbMutacion, Generaciones)
    
Main()
'''