#calcula tabuado de um numero

num=int(input("Qual numero deseja saber a tabuada?"))

for x in range(1,11):
	result=num*x
	print(str(num)+"*"+str(x)+"="+str(result))
