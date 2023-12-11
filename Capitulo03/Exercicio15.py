#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 11/12/2023
# Hour: 13:26:51
#
# Question: Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
#

cigarrosPorDia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anosFumando = float(input("Digite há quantos anos você fuma: "))

diasReduzidos = ((cigarrosPorDia * 10) * (anosFumando * 365)) / 86400

print("A quantidade de dias reduzidos foram de", diasReduzidos)
