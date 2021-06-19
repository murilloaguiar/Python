 #-*- coding: latin1 -*-
import os
import time

class Conta(object):
	
	def __init__(self, numero, saldo):
		self.numero = numero
		self.saldo = saldo
		
	def getNumero(self):	
		return self.numero
	
	def getSaldo(self):
		return self.saldo
		
	def setNumero(self, numero):
		self.numero = numero
		
	def setSaldo(self, saldo):
		self.saldo = saldo
		
	def extrato(self):
		return self.saldo
		
	def deposito(self, valor):
		self.saldo = self.saldo + valor
	
	def saque(self, valor):
		if (self.saldo >= valor):
			self.saldo = self.saldo - valor
			return 1
		else:
			return 0


#limpar tela
def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

cls()

print("*** BANCO NACIONAL ***")

print("--- ABERTURA DE CONTA ---")	
num = int(input("Digite o numero da conta: "))
sal = float(input("Digite o saldo inicial: "))

cont = Conta(num, sal)
print("Conta criada com sucesso!")


op=1
while (op!=0):
	#limpar tela
	cls()
	print("*** BANCO NACIONAL ***")
	
	print("-- Menu de opcoes ---")
	print("1. Extrato")
	print("2. Deposito")
	print("3. Saque")
	print("0. Sair")
	op=int(input("Digite a opcao desejada: "))
	
	if (op==1):
		print("Saldo: R$ %.2f" % (cont.extrato()) )
	elif (op==2):
		dep = float(input("Digite o valor de deposito: "))
		cont.deposito(dep)
	elif (op==3):
		saq = float(input("Digite o valor de saque: "))
		if (cont.saque(saq) == 1):
			print("Saque realizado com sucesso!")
		else:
			print("Saldo insuficiente.")
	elif (op==0) :
		print("Sessao encerrada")
	else: 
		print("Opção inválida!")
	#execução de 3 segundos
	time.sleep(3)
	
			
print("Saldo: R$ %.2f" % (cont.extrato()) )


print("Saldo: R$ %.2f" % (cont.extrato()) )











