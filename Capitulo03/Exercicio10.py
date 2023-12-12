#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 11:42:31
#
# Question: Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
#

salário = float(input("Digite o valor do seu salário: R$"))
aumento = float(input("Digite a porcentagem de aumento: "))

novoSalario = salário + (salário * aumento / 100)

print("O seu novo salário com aumento de", aumento, "% é de R$",novoSalario)
