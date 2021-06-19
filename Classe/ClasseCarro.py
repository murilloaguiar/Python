import simplegui 

class Carro(object): 	

    def __init__ (self,nome,velMax,velocidade):
        self.nome = nome
        self.velMax = velMax
        self.velocidade = 0
       
    def acelerar (self):
        if (self.velocidade) < (self.velMax):
            self.velocidade += 5 
        else:
            self.velocidade = self.velMax
         
    def frear (self):
        if self.velocidade <= self.velMax and self.velocidade >= 5:
            self.velocidade -= 5
        else: 
            self.velocidade = 0
            
    def getVelocidade(self):
        return self.velocidade   

    def parar (self):
        self.velocidade = 0
         
    def setnum1(self,valor):
        self.velMax = valor
    
    def setnum2(self, valor1):
        self.velocidade = valor1
        
    def setnome(self,nome1):
        self.nome = nome1
        return self.nome
    
  
        

car = Carro ("",0,0)

def acele ():
    car.acelerar ()
    result = car.getVelocidade()
    visor.set_text(str(result))
    
def reduzir ():
    car.frear ()
    result = car.getVelocidade()
    visor.set_text(str(result))
    
def stop ():
    car.parar ()
    result = car.getVelocidade()
    visor.set_text(str(result))
    
def num1(valor):
    car.setnum1(int(valor))

def num2(valor):
    car.setnum2(int(valor))

def mostrar (valor):
    car.setnome(str(valor))
    
k = simplegui.create_frame("Carro", 400,300)
k.add_input("Nome do carro: ", mostrar, 200)
k.add_input("Velocidade maxima: ", num1, 200)
k.add_input("Velocidade:", num2, 200)
k.add_label("Velocidade atual: ", car.getVelocidade())
visor = k.add_label("0", 200)
k.add_button("Acelerar", acele, 200)
k.add_button("Frear", reduzir, 200)
k.add_button("Parar", stop, 200)
