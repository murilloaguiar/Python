lista=[]
par=[]
impar=[]
for x in range (1,21):
	nome=int(input("Item"+str(x) + ":"))
	lista.append(nome)
print(lista)
y=0
for x in range(1,21):
	if lista[y]%2==0:
		par.append(lista[y])
	else:
		impar.append(lista[y])	
	y=y+1
print("Números pares"+str(par))	
print("Números impares "+str(impar))
