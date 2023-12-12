#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 10:40:31
#
# Question: Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
#

depositoInicial = float(input("Digite o depósito inicial: "))
depositoMensal = float(input("Digite o depósito mensal: "))
taxaDeJuros = float(input("Digite a taxa de juros da poupança: "))

mes = 1
lucro = 0
while (mes <= 24):
    lucro = (depositoInicial * (taxaDeJuros/100) * mes) + (depositoMensal * mes)
    print(f"Mês {mes} - Lucro de R${lucro}")
    mes += 1
