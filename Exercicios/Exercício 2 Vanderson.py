# Exercício 2: Faça um programa que solicite ao usuário números e os armazene
# em um vetor de 20 posições. Crie uma função que recebe o vetor preenchido e
# substitua todas as ocorrências de valores negativos por zero, as ocorrências de
# valores menores do que 10 por 1 e as demais ocorrências por 2.


def menor10(vetor):
    for n in range(20):
        if vetor[n] < 0:
            vetor[n] = 0
        elif vetor[n] < 10:
            vetor[n] = 1
        else:
            vetor[n] = 2
    return vetor



vet = [0]*20
for n in range(20):
    vet[n] = int(input("Digite um valor: "))
menor10(vet)
print(vet)


#Guilherme Ribeiro 1700546   BD
#Nicolas Alves 1700012       BD
