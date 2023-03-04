#clase del 27 de febrero

class Coche ():
    def __init__(self, matricula, marca, kilometros, gasolina):
        self.matricula = matricula
        self.marca= marca
        self.kilometros = kilometros
        self.gasolina = gasolina
        
    def avanzar(self, km): #preguntar cuantos km avanzó
        print(self.gasolina - km)
        if self.gasolina - km >= 0:
            self.gasolina = self.gasolina - km
            self.kilometros = self.kilometros + km
            return True
        
        print("No hay suficiente gasolina")
        return False
    
carro = Coche ("QGD345", "Ford", 45, 20)
print(carro.avanzar(20))
        

