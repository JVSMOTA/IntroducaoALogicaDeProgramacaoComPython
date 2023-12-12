#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 14:10:19
#
# Question: Escreva um programa que leia três números e que imprima o maior e o menor.
#

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

menor = maior = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print("O menor é:", menor)
print("O maior é:", maior)