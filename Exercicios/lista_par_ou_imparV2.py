lista=[]
par=[]
impar=[]
for x in range (1,6):
	nome=int(input("Item"+str(x) + ":"))
	lista.append(nome)

	if nome%2==0:
		par.append(nome)
	else:
		impar.append(nome)	
	
print(lista)
print("Números pares"+str(par))	
print("Números impares "+str(impar))