#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 10:09:44
#
# Question: Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
#

n1 = int(input("Digite o PRIMEIRO número: "))
n2 = int(input("Digite o SEGUNDO número: "))

auxiliar = n1
resultado = 0
while (n2 <= auxiliar):
    resultado += 1
    auxiliar -= n2
print(f"{n1} / {n2} = {resultado}")
