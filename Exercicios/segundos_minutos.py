#dado um tempo em segundos calcula quanto tempo se passou em minutos

def minuto (seg):
	min=(seg//60)
	resto=seg%60
	print("%d minutos e %d segundos"%(min,resto))
seg=int(input("Digite os segundos: "))
minuto(seg)