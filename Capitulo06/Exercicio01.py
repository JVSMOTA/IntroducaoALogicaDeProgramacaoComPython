#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 14/12/2023
# Time of Creation: 09:46:09
#
# Question: Modifique o programa da listagem 6.6 para ler 7 notas em vez de 5.

# Listagem 6.6 – Cálculo da média com notas digitadas
#
# notas=[0,0,0,0,0] 
# soma=0
# x=0
# while x<5:
#     notas[x]=float(input("Nota %d:" % x))
#     soma += notas[x]
#     x+=1
#     x=0 
#     while x<5:
#         print("Nota %d: %6.2f" % (x, notas[x]))
#         x+=1
#         print("Média: %5.2f" % (soma/x))

notas=[0,0,0,0,0,0,0] 
soma=0
x=0
while x<7:
    notas[x]=float(input("Nota %d:" % x))
    soma += notas[x]
    x+=1
x=0 
while x<7:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x+=1
    print("Média: %5.2f" % (soma/x))
