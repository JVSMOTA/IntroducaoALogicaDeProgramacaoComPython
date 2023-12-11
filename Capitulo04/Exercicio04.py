#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Hour: 14:34:13
#
# Question: Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
#

salario = float(input("Digite o seu salário: "))

if (salario > 1250):
    aumento = 10
if (salario <= 1250):
    aumento = 15

aumentoTotal = salario * (aumento/100)

print("O aumento é de", aumento,"% é um total de R$", aumentoTotal)