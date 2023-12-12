#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 09:34:47
#
# Question: Altere o programa anterior (Listagem 5.9) para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...
#

# Listagem 5.9 – Tabuada simples
#
# n = int(input("Tabuada de:"))
# x = 1
# while x <= 10:
#     print(n+x)
#     x=x+1

n = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(n,"x",x,"=",n*x)
    x=x+1
