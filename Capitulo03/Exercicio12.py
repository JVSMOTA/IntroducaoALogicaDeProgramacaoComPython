#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 11:53:20
#
# Question: Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
#

distancia = float(input("Digite a distância da viagem: (Km) "))
velocidadeMedia = float(input("Digite a velocidade média da viagem: (Km/h) "))

tempoTotal = distancia / velocidadeMedia

print("O valor do tempo total da viagem é de:", tempoTotal ,"horas.")