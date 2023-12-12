#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 17:54:39
#
# Question: Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
#

distanciaDesejada = float(input("Digite a distância que deseja percorrer: (Km) "))

if (distanciaDesejada <= 200):
    taxaPorKm = 0.50
else:
    taxaPorKm = 0.45

valorTotal = distanciaDesejada * taxaPorKm

print("O valor total é de:", valorTotal)
