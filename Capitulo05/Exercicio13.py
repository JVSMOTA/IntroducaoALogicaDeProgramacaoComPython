#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 10:46:22
#
# Question: Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
#

divida = float(input("Digite o valor da dívida: "))
juroMensal = float(input("Digite o valor do juro mensal: "))
pagamentoMensal = float(input("Digite o valor pago mensal: "))

mes = 0
totalPago = 0
totalJuros = 0

while divida > 0:
    totalJuros += divida * (juroMensal / 100)
    divida += divida * (juroMensal / 100)
    
    if divida >= pagamentoMensal:
        divida -= pagamentoMensal
        totalPago += pagamentoMensal
    else:
        totalPago += divida
        divida = 0

    mes += 1

print(f"Meses para quitar a dívida: {mes}")
print(f"Total de Juros: {totalJuros:.2f}")
print(f"Total Pago: {totalPago:.2f}")