#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 11:34:37
#
# Question: Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
#

dias = int(input("Digite seu DIA atual: "))
horas = int(input("Digite sua HORA atual: "))
minutos = int(input("Digite seus MINUTOS da hora atual: "))
segundos = int(input("Digite seus SEGUNDOS da hora atual: "))

segundosTotais = (dias * 86400) + (horas * 3600) + (minutos * 60) + (segundos)

print("Os segundos totais desse dia e hora são:", segundosTotais, "segundos")
