# Exercício 3: crie um programa que leia um valor e a partir disso faça: (1) se for
# um valor negativo, mostre o módulo (valor sem sinal) do valor; (2) se for um
# valor maior do que 10, solicite outro valor e mostre a diferença entre eles; (3)
# Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por
# 5.



n = int(input("Digite um número: "))

if n < 0:
    n = abs(n)
    print(n)
elif n > 10:
    x = int(input("Digite outro número: "))
    d = n - x
    print ("A diferença entre os dois números é: ",d)
else:
    v = n / 5
    print(v)



#Guilherme Ribeiro 1700546   BD
#Nicolas Alves 1700012       BD
