arq=float(input("Qual o tamanho do arquivo em MB?"))
net=float(input("Qual a velocidade em Mbps(megabits) da sua internet: "))

arq2=float(arq*1024)
net2=float(net*128)
seg=arq2/net2

min=int(seg/60)
s=seg%60

print("O tempo aproximado é de: "+str(min)+" minutos é %d segundos"%(s))