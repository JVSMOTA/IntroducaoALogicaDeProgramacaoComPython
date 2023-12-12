#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 09:47:38
#
# Question: Modifique o programa anterior (Listagem 5.9) de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
#

# Listagem 5.9 – Tabuada simples
#
# n = int(input("Tabuada de:"))
# x = 1
# while x <= 10:
#     print(n+x)
#     x=x+1

n = int(input("Tabuada de: "))
inicio = int(input("Início em: "))
fim = int(input("Fim em: "))
while inicio <= fim:
    print(n+inicio)
    inicio=inicio+1
