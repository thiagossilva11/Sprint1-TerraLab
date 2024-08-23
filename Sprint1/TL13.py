#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario =  float(input("Digite seu salário atual: "))
reajuste = salario * 0.15 + salario
print(f"Seu salário atual com reajuste é: {reajuste:.2f}")
