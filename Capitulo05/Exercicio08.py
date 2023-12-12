#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 09:51:17
#
# Question: Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
#

n1 = int(input("Digite o PRIMEIRO número: "))
n2 = int(input("Digite o SEGUNDO número: "))

resultado = ""
x = 1
while (x <= n2):
    if (x == n2):
        resultado += f"{n1} "
    else:
        resultado += f"{n1} + "
    x += 1

resultado += "="
x = 1
while (x <= n1):
    if (x == n1):
        resultado += f" {n2}"
    else:
        resultado += f" {n2} +"
    x += 1

print(f"{n1} x {n2} = {resultado} = {n1 * n2}.")
