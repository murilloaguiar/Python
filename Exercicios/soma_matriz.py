#soma os numeros de uma matriz

matriz = []
for x in range (0,5):
	linha=[]
	for y in range (0,5):
		num=int(input("Numero: "))
		linha.append(num)
	matriz.append(linha)
print (matriz)
soma=0
for x in range (0,5): 
	soma=int(matriz[x][x] + soma)
print(soma)