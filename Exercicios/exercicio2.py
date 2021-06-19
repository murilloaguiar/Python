alt=float(input("Qual sua altura: "))
peso=float(input("Qual seu peso: "))
sexo=input("M para masculino e F para feminino: ")
imc=peso/(alt**2) 

if sexo=="M" or sexo=="m":
	if imc<20.7:
		print("abaixo do peso")
	elif imc>=20.7 and imc<=26.4:
		print("no peso normal")
	elif imc>26.4 and imc<=27.8:
		print("marginalmente acima do peso")
	elif imc>27.8 and imc<=31.1:
		print("acima do peso ideal")
	elif imc>31.1:
		print("obeso")
if sexo=="F" or sexo=="f":
	if imc<19.1:
		print("abaixo do peso")
	elif imc>=19.1 and imc<=25.8:
		print("no peso normal")
	elif imc>25.8 and imc<=27.3:
		print("marginalmente acima do peso")
	elif imc>27.3 and imc<=32.3:
		print("acima do peso ideal")
	elif imc>32.3:
		print("obeso")