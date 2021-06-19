#coleta nome de alunos e suas notas, calcula a media e no fim
#mostra quais alunos tiveram media acima de 7

aluno=[]
med=0
media=[]
for x in range (0,3):
	linha=[]
	nome=str(input("nome do aluno: "))
	linha.append(nome)
	for y in range (0,4):
		msg="Aluno "+str(nome)+" "+str(y+1)+ "ª Nota : "
		nota=float(input(msg))
		linha.append(nota)
		med=med+nota
	med=med/4
	media.append(med)
	aluno.append(linha)
	med=0
num=0
for x in range (0,3):
	if media[x]>=7 :
		num=num+1
		print(aluno[x][0])
print(str(num)+" alunos ficaram com a media acima de 7")

	