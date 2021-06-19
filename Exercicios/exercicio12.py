mes= ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
M=[]
ano=0
y=0
for x in range(1,13): 
	T=float(input("Média do mês de "+str(mes[y])+": "))
	M.append(T)
	ano=M[y]+ano
	y=y+1
ano=(ano/12)
print("A Média anual é de: %.2f graus"%(ano))
z=0
for x in range(1,13):
	if M[z]>ano:
		print("O mês de "+str(mes[z])+" apresetou média acima da média anual: "+str(M[z])+" graus")
	z=z+1