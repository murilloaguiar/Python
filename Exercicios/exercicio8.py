pao=float(input("Qual valor do pão? "))
print ('Panificadora Pão de ontem')
for x in range(1,51):
	valor=x*pao
	print(str(x)+" pães = R$ %.2f"%(valor))