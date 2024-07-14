# -*- coding: utf-8 -*-
"""
Conjectura de Goldbach.
Autor: Alexandre Cardoso Garcia Leite.
Criação: 13/07/2024
Última Atualização: 13/07/2024

conjectura_de_goldback_v2.py

Descrição do problema:
    Qualquer número par é a soma de dois números primos.
    Nesta solução daremos a lista de todos os pares de 
    números primos que sua soma resulta no número par dado.
"""

import numpy as np

numero = 10
while (numero < 12 or numero > 1000):
    numero = int(input("Digite um número par no intervalo [12, 1000] para encontrar dois números primos cuja soma seja o número escolhido? "))
    if (numero < 12 or numero > 1000) and (numero % 2 != 0):
        print("Número Inválido! Por favor, entre com um número par no intervalo [4,1000].")

"""
Antes obteremos os números primos entre 2 e 1.000, aplicando o algoritmo de Erastotenes
"""
lista_numeros_naturais = []

# Cria uma lista com os números naturais começando pelo número primo 2 
for i in range(2,1000):
    lista_numeros_naturais.append(i)
    
proximo_numero_primo = 2
num_primos_encontrados = 1

# Enquanto a lista de numeros primos for menor do que a lista de do restante dos numeros naturais
while (num_primos_encontrados < len(lista_numeros_naturais)):
    i = num_primos_encontrados
    while (i < len(lista_numeros_naturais)):
        if lista_numeros_naturais[i] % proximo_numero_primo == 0:
            del lista_numeros_naturais[i]
            i = i - 1
        i = i + 1    
    try:
        proximo_numero_primo = lista_numeros_naturais[num_primos_encontrados]
    except IndexError:
        pass
    num_primos_encontrados = num_primos_encontrados + 1
        
l_num_primos = lista_numeros_naturais

"""
Com a lista de números primos em mãos, faremos encontraremos os pares de números primos que resultam na sequência de todos os números pares.
"""


# Construiremos um dicionário onde as chaves são os números pares e os atributos são dois números ímpares que somados dão o número dado.
dict_conjectura_goldbach = {}

primos = np.array( l_num_primos ) # cria uma numpy array excluindo o número 2
numero_par = 2

while (numero_par < numero):
    numero_par = numero_par + 2
    ind_primo_1 = 0
    primo_1 = primos[ ind_primo_1 ]
    for i in range(primos.size):
        try:
            primo_2 = primos[ np.where(primos == numero_par - primo_1) ][0]
        except IndexError:
            primo_2 = 0
        if (primo_1 + primo_2 == numero_par):
            if numero_par not in dict_conjectura_goldbach:
                dict_conjectura_goldbach[ numero_par ] = [ (primo_1, primo_2) ]
            else:
                # verifica quando as somas começarão a ser apenas a permutação dos dois termos
                if dict_conjectura_goldbach[ numero_par ][-1] == (primo_2, primo_1):
                    break
                dict_conjectura_goldbach[ numero_par ].append( (primo_1, primo_2) )
            ind_primo_1 = ind_primo_1 + 1
            primo_1 = primos[ ind_primo_1 ]

        else:
            try:
                ind_primo_1 = ind_primo_1 + 1
                primo_1 = primos[ ind_primo_1 ]
            except IndexError:
                break
            
print(dict_conjectura_goldbach[ numero ])
            
    