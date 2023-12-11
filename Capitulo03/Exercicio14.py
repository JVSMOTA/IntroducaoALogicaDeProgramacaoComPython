#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Hour: 12:26:03
#
# Question: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
#

kmPercorridos = int(input("Digite a quantidade de KM percorridos: "))
diasAlugados = int(input("Digite a quantidade de DIAS para alugar o carro: "))

totalAPagar = (diasAlugados * 60) + (kmPercorridos * 0.15)

print("O total a pagar pelos quilometros rodados e a quantidade de dias é de:", totalAPagar)
