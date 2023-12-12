#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 12:00:37
#
# Question: Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é: F = ((9 * C) / 5) + 32
#

celcius = float(input("Digite a temperatuda em °C: "))

fahrenheit = ((9 * celcius) / 5) + 32

print("A temperatura em °F é de:", fahrenheit,"°F.")
