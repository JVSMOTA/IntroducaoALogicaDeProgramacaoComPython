#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 12/12/2023
# Time of Creation: 10:23:21
#
# Question: Modifique o programa da listagem 5.10 para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.
#

# Listagem 5.10 – Contagem de questões corretas
#
# pontos = 0
# questão = 1
# while questão <= 3:
#     resposta = input("Resposta da questão %d: " % questão)
#     if questão == 1 and resposta == "b":
#         pontos = pontos + 1
#     if questão == 2 and resposta == "a":
#         pontos = pontos + 1
#     if questão == 3 and resposta == "d":
#         pontos = pontos + 1
#     questão +=1
# print("O aluno fez %d ponto(s)" % pontos)
#

pontos = 0
questão = 1
while questão <= 3:
    resposta = input("Resposta da questão %d: " % questão)
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questão == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questão +=1
print("O aluno fez %d ponto(s)" % pontos)
