#==============================================================================#
# Author: João Mota < jvmota.sb@gmail.com >                                    #
# GitHub: https://github.com/JVSMOTA                                           #
# Computer Science undergraduate at UFCG                                       #
#==============================================================================#

# Created: 14/12/2023
# Time of Creation: 10:07:28
#
# Question: Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

lista1 = []
lista2 = []
lista3 = []

print("Adicionar na lista 1")
while (len(lista1) < 5):
    lista1.append(int(input("Digite um número: ")))
print(f"Lista 1: {lista1}")

print("Adicionar na lista 2")
while (len(lista2) < 5):
    lista2.append(int(input("Digite um número: ")))
print(f"Lista 2: {lista2}")

while (len(lista1) != 0):
    lista3.append(lista1.pop(0))

while (len(lista2) != 0):
    lista3.append(lista2.pop(0))

print(f"A junção das duas listas é: {lista3}")