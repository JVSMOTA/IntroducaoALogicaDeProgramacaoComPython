#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 13/12/2023
# Time of Creation: 21:47:44
#
# Question: Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”.


totalCompras = 0

while True:
    codigoDoProduto = float(input("Digite o código do produto: "))
    if (codigoDoProduto != 0):
        if (codigoDoProduto == 1):
            totalCompras += 0.5
        elif (codigoDoProduto == 2):
            totalCompras += 1.0
        elif (codigoDoProduto == 3):
            totalCompras += 4.0
        elif (codigoDoProduto == 5):
            totalCompras += 7.0
        elif (codigoDoProduto == 9):
            totalCompras += 8.0
        else:
            print("Código inválido!")
    else:
        break

print(f"Total das compras: {totalCompras}")