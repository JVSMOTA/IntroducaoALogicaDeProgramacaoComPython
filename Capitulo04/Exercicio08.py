#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Time of Creation: 18:02:09
#
# Question: Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
#

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("")
print("#=========================#")
print("# 1 - Soma (+)            #")
print("# 2 - Subtração (-)       #")
print("# 3 - Multiplicação (*)   #")
print("# 4 - Divisão (/)         #")
print("#=========================#")
print("")

operador = input("Qual operação acima você deseja realizar? ") 

if (operador == "1" or operador == "+"):
    print("Soma:", numero1 + numero2)
elif (operador == "2" or operador == "-"):
    print("Subtração:", numero1 - numero2)
elif (operador == "3" or operador == "*"):
    print("Multiplicação:", numero1 * numero2)
elif (operador == "4" or operador == "/"):
    print("Divisão:", numero1 / numero2)
else:
    print("Opção indisponível! (Fim do programa)")