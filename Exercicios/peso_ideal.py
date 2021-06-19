#Calcular peso ideal pelo imc

alt=float(input("Qual sua altura?"))
sexo=str(input("Qual seu sexo?M para Masculino e F para Feminino "))
if sexo=="M":
	peso=float(72.7*alt)-58
	print("Seu peso ideal é: %.3f"%(peso))
elif sexo=="F":
	peso=float(62.1*alt)-44.7
	print("Seu peso ideal é: %.3f"%(peso))