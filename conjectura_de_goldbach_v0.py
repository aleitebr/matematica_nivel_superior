# -*- coding: utf-8 -*-
"""
Conjectura de Goldbach.
Autor: Alexandre Cardoso Garcia Leite.
Criação: 13/07/2024
Última Atualização: 13/07/2024

conjectura_de_goldback_v0.py

Observação: O algoritmo só funciona para o intervalo [4, 96] que é caso especial da conjectura.
            Também não encontra todas as combinações de primos possíveis, por exemplo:
            Para n = 10, a resposta é [3, 7], contudo n = 10 pode ser também a soma de [5, 5]
"""

numero = 2
while (numero < 4 or numero > 96):
    numero = int(input("Digite um número no intervalo [4, 96] para encontrar dois números primos cuja soma seja o número escolhido? "))
    if (numero < 4 or numero > 96):
        print("Número Inválido! Por favor, entre com um número no intervalo [4,1000].")

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
Com a lista de números primos em mãos, faremos em seguida a fatoração.
"""

indice_p1 = 0
indice_p2 = 0

dic_num_pares = {4:[2,2]}

numero_par_atual = 6

while (numero_par_atual <= numero):
    indice_p1 = indice_p1 + 1
    indice_p2 = 0 
    while( numero_par_atual >= l_num_primos[ indice_p1 ] + l_num_primos[ indice_p2 + 1 ] ):
        indice_p2 = indice_p2 + 1            
        if numero_par_atual == l_num_primos[ indice_p1 ] + l_num_primos[ indice_p2 ]:
            dic_num_pares[ numero_par_atual ] = [ l_num_primos[ indice_p1 ], l_num_primos[ indice_p2 ]]
            numero_par_atual = numero_par_atual + 2
    
    
print(dic_num_pares[ numero ])