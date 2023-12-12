#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 18:14:51
#
# Question: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
#

valorCasa = float(input("Digite o valor da casa que deseja comprar: "))
salario = float(input("Digite o seu salário: "))
anosParaPagar = int(input("Digite a quantidade de anos que deseja quitar: "))

prestacao = valorCasa / (anosParaPagar * 12)

if (prestacao <= (salario * 0.30)):
    print("Você poderá comprar com prestações de R$", prestacao ,"mensais.")
else:
    print("O valor das prestações ultrapassam 30% do seu salário.")
