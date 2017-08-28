# Exercício 1: faça um programa que solicite ao usuário números e os armazene
# em um vetor de 30 posições. Crie uma função que recebe o vetor preenchido e
# substitua todas as ocorrência de valores positivos por 1 e todos os valores
# negativos por 0.


def troca (vet):
    for n in range(30):
        if vet[n] >= 0:
            vet[n] = 1
        else:
            vet[n] = 0
    return vet

vet = [0]*30
for n in range(30):
    vet[n] = int(input('Digite um valor: '))
print (vet)
troca (vet)
print (vet)


#Guilherme Ribeiro 1700546   BD
#Nicolas Alves 1700012       BD

