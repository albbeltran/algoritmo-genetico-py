# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:56:37 2023

@author: BetoB
"""

import sys, os

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
    
    print("\n\nMEJORES INDIVIDUOS:")
    
    # Imprimir los mejores individuos encontrados
    for individuo in mejores_individuos:
        print(individuo)

    flag = True;
    while(flag):  
        print("\n\nGuardar los resultados:\n\n\t1. SI\n\t2. NO")
        
        opc = int(input("\n\nOpcion: "))

        if(opc==1):
            # Apertura del archivo, con permisos W y R
            archivo = os.open("resultados.txt", os.O_CREAT | os.O_RDWR)
            # Convertir lista a string
            mejores_ind_str = ''.join(map(str, mejores_individuos))
            # Codificar data
            dataEncoded = mejores_ind_str.encode("UTF-8")
            # Escribir data en el archivo
            os.write(archivo, dataEncoded)
            
            flag = False
        elif(opc==2):
            exit()
        else:
            os.system("cls")
            print("Opcion no valida. Presiona para volver a seleccionar.")

if __name__ == "__main__":
  main()