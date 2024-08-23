#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: ")).upper().strip()
print ("A letra A/a aparece {} vezes".format(frase.count("A")))

print("A letra A/a aparece primeiramente na posição {}".format(frase.find("A")+1))
print ("A letra A/a aparece por ultimo na posição {}".format(frase.rfind("A")+1))
   