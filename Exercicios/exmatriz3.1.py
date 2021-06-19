jogador=[]
aproveitamento=0
apro=[]
for x in range (0,3):
	linha=[]
	nome=input("Nome do jogador: ")
	linha.append(nome)
	chutes=int(input("Quantidades de chutes: "))
	gols=int(input("Gols feitos: "))
	linha.append(chutes)
	linha.append(gols)
	aproveitamento=(gols*100)/chutes
	apro.append(aproveitamento)
	jogador.append(linha)
	print("O jogador "+str(nome)+" teve um aproveitameto de %.2f " %(aproveitamento))
	print("")
maior=0
for x in range(0,3):
	if apro[x]>maior:
		maior=apro[x]
		maior1=x
print("O jogador "+str(jogador[maior1][0])+" teve o maior aproveitamento")
