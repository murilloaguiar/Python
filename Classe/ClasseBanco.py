#-*-coding:latin1-*-

class Conta(object):
	def __init__ (self, num, saldo):
		self.numero = num
		self.saldo = saldo
		
	def getNum (self):
		return self.numero
		
	def getSaldo (self):
		return self.saldo
		
	def setNum(self, num):
		self.numero = num
		
	def setSaldo(self, saldo):
		self.saldo = saldo 
		
	def extrato(self):
		return self.saldo
		
	def deposito (self, valor):
		self.saldo = self.saldo + valor
	
	def saque (self, valor):
		if (self.saldo >= valor):
			self.saldo = self.saldo - valor
			return 1 
		else:
			return 0

numero1 = int(input("Digit o numero da conta: "))			
sal = float(input("Digite o saldo inicial: "))
cont = Conta (numero1, sal)
print("Saldo: R$ %.2f" %(cont.extrato()))

saq = float(input("Digite o valor de saque "))
if cont.saque(saq) == 1 :
	print("Saque realizado com sucesso!")
else: 
	print("Saldo insuficiente!")

print("Saldo: R$ %.2f" %(cont.extrato()))

dep = float(input("Digite o valor de deposito: "))
cont.deposito(dep)

print("Saldo: R$ %.2f" %(cont.extrato()))


	
