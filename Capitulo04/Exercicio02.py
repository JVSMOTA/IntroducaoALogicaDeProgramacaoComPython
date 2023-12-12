#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 13:58:50
#
# Question: Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
#

velocidade = float(input("Digite a velocidade do carro: (Km/h) "))

if (velocidade > 80):
    multa = (velocidade - 80) * 5

    print("Você foi multado por excesso de velocidade.")
    print("O valor total é de R$", multa, ". (R$5.00 por km acima de 80km/h)")
