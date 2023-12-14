#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 14/12/2023
# Time of Creation: 08:53:29
#
# Question: Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

while True:
    print("+-----------------------+")
    print("| 1 - Adição (+)        |")
    print("| 2 - Subtração (-)     |")
    print("| 3 - Divisão (/)       |")
    print("| 4 - Multiplicação (+) |")
    print("| 5 - Sair              |")
    print("+-----------------------+")
    
    operacao = input("Digite a operação desejada: ")

    base = 1
    n = 1
    if (operacao == "1"):
        print("Tabuada de Adição")
        while n <= 10:
            print(f"{base} + {n} = {base + n}")
            n += 1
            if (n == 11 and base < 10):
                n = 1
                base += 1
        n = 1
        base = 1

    elif (operacao == "2"):
        print("Tabuada de Subtração")
        while n <= 10:
            print(f"{base} - {n} = {base - n}")
            n += 1
            if (n == 11 and base < 10):
                n = 1
                base += 1
        n = 1
        base = 1

    elif (operacao == "3"):
        print("Tabuada de Divisão")
        while n <= 10:
            print(f"{base} / {n} = {base / n}")
            n += 1
            if (n == 11 and base < 10):
                n = 1
                base += 1
        n = 1
        base = 1

    elif (operacao == "4"):
        print("Tabuada de Multiplicação")
        while n <= 10:
            print(f"{base} * {n} = {base * n}")
            n += 1
            if (n == 11 and base < 10):
                n = 1
                base += 1
        n = 1
        base = 1

    elif (operacao == "5"):
        print("Saindo do programa!")
        break
    else:
        print("Código desconhecido! Tente novamente.")
