#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Hour: 11:48:33
#
# Question: Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
#

preco = float(input("Digite o valor do produto: R$"))
desconto = float(input("Digite a porcentagem de desconto: "))

novoPreco = preco - (preco * desconto / 100)

print("O seu novo preço do produto com desconto de", desconto, "% é de R$",novoPreco)
