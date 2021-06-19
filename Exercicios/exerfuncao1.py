def km_metro(km):
	return float(km*1000)
km=int(input("Digite a medida em KM: "))
print(str(km)+"Km é igual a : %.3f Metros"%(km_metro(km)))

def metro_cm(metro):
	return float(metro*100)
metro=int(input("Digite a medida em metros: "))
print(str(metro)+" metros é igual a: %.3f Centimetros"%(metro_cm(metro)))

def cm_metro(cm):
	return float(cm/100)
cm=int(input("Digite a medida em cm: "))
print(str(cm)+" centimetros é igual a: %.3f Metros"%(cm_metro(cm)))