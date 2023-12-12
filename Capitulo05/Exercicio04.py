#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 09:27:25
#
# Question: Modifique o programa anterior (Listagem 5.8) para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
#

# Listagem 5.8 – Impressão de números pares de 0 até um número digitado pelo usuário, sem if
#
# fim = int(input("Digite o último número a imprimir:"))
# x = 0
# while x <= fim:
#     print(x)
#     x = x + 2

fim = int(input("Digite o último número a imprimir:"))
x = 1
while x <= fim:
    print(x)
    x = x + 2
