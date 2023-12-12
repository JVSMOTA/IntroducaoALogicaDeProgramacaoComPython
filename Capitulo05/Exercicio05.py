#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 09:29:44
#
# Question: Reescreva o programa anterior (Listagem 5.8) para escrever os 10 primeiros múltiplos de 3.
#

# Listagem 5.8 – Impressão de números pares de 0 até um número digitado pelo usuário, sem if
#
# fim = int(input("Digite o último número a imprimir:"))
# x = 0
# while x <= fim:
#     print(x)
#     x = x + 2

x = 1
while x <= 30:
    if ((x % 3) == 0):
        print(x)
    x = x + 1
