#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 11:38:35
#
# Question: Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
#

quantidadeDeNumeros = 0
somaTotal = 0
ultimoNumero = float(input("Digite um número: "))

while (ultimoNumero != 0):
    quantidadeDeNumeros += 1
    somaTotal += ultimoNumero
    ultimoNumero = float(input("Digite um número: "))

print(f"Quantidade de números: {quantidadeDeNumeros}")
print(f"A soma total é: {somaTotal}")
print(f"A média geral é: {somaTotal/quantidadeDeNumeros}")
