#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 10:30:47
#
# Question: Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
#

depositoInicial = float(input("Digite o depósito inicial: "))
taxaDeJuros = float(input("Digite a taxa de juros da poupança: "))

mes = 1
lucro = 0
while (mes <= 24):
    lucro = depositoInicial * (taxaDeJuros/100) * mes
    print(f"Mês {mes} - Lucro de R${lucro}")
    mes += 1
