#Calcular a média de tres notas de um aluno. Menor que 7 é reprovado

n1=int(input("Nota1: "))
n2=int(input("Nota2: "))
n3=int(input("Nota3: "))

med=float(n1+n2+n3)/3

if med==10 : 
	print("Aprovado com Distincao")
elif med>=7: 
	print("Aprovado")
else: 
	print("Reprovado")