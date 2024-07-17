# -*- coding: utf-8 -*-
"""
Conjectura de Goldbach.
Autor: Alexandre Cardoso Garcia Leite.
Criação: 17/07/2024
Última Atualização: 17/07/2024

fabrica_primos_euler_v1.py

Descrição do problema:
    Verifica se a fórmula d = n^2 - n + 41 é válida para encontrar todos os números primos.
    HISTÓRIA (Microsoft @Bing):
        A fórmula f(n) = n^2 - n + 41 é notável por produzir números primos
        consecutivos para os primeiros 41 valores naturais de
        
        n
        
        Quando substituimos n pelos números de 1 a 41, obtemos primos. Por exemplo,
         
        * Para n = 1, temos
        
            f(1) = 1^2 - 1 + 41 = 41
            que é primo
            
        * Para n = 2, temos
            
            f(2) = 2^2 - 2 + 41 = 43
            que é primo
            
        * E assim por diante, até n = 41, onde
        
            f(41) = 41^2 - 41 + 41 = 1681
            que é composto, 41^2 
            
        Essa propriedade intrigante foi descoberta pelo matemático Euler e é 
        conhecida como a "fábrica de números primos. No entanto, não existe
        uma fórmula gerel que produza apenas números primos para os valores
        de n. A distribuição de números primos é um campo fascinante na
        teoria dos números e questões relacionadas a primos ainda desafiam
        os matemáticos.
"""

import numpy as np


"""
Antes obteremos os números primos entre 2 e 1.000, aplicando o algoritmo de Erastotenes
"""
lista_numeros_naturais = []

# Cria uma lista com os números naturais começando pelo número primo 2 
for i in range(2,5000):
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


primos = np.array( l_num_primos ) # cria uma numpy array com os números primos

# Verificar a fórmula dos números primos d = n^2 - n + 41
lista_d = []
n = 1
while (True):
    d = n**2 - n + 41
    if primos[ np.where(primos == d) ].size > 0:
       lista_d.append(d)
    else:
        break
    n = n + 1
    
print(lista_d)
print("Para o número n = " + str(n) + " a fórmula não se verifica pois o número " + str(d) + " é composto e igual a 41*41 (fácil verificar)!")