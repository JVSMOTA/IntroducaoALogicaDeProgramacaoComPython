#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Hour: 18:27:03
#
# Question: Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
#

kWhConsumida = float(input("Digite a quantidade de kWh consumida: "))

print("")
print("#=========================#")
print("# 1 - Residencial (R)     #")
print("# 2 - Industrial  (I)     #")
print("# 3 - Comercial   (C)     #")
print("#=========================#")
print("")

tipoInstalacao = input("Escolha o tipo de instalação acima: ")

if (tipoInstalacao == "1" or tipoInstalacao == "R"):
    if (kWhConsumida <= 500):
        preco = 0.40
    else:
        preco = 0.65
elif (tipoInstalacao == "2" or tipoInstalacao == "I"):
    if (kWhConsumida <= 1000):
        preco = 0.55
    else:
        preco = 0.60
elif (tipoInstalacao == "3" or tipoInstalacao == "C"):
    if (kWhConsumida <= 5000):
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Opção não reconhecida. (Fim do programa)")

valorTotalDeInstalacao = kWhConsumida * preco

print("O valor total da instalação será de R$", valorTotalDeInstalacao)
