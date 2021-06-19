#adiciona itens em uma lista

lista=[]

for x in range (1,6):
	nome=int(input("Item"+str(x) + ":"))
	lista.append(nome)
print(lista)