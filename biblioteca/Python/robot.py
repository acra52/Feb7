class Robot():
    #variable de clase
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.x = 0
        self.y = 0
        pass
    
    def arriba(self):
        self.y =self.y +1
        
    def abajo(self):
        self.y = self.y -1 
        
    def izquierda(self):
        self.x = self.x -1

    def derecha(self):
        self.x = self.x -1
        
    def posicion (self):
        return {"x": self.x, "y": self.y}
    
a = Robot("Angel")
for i in range (4): #se mueva 4 puntos en el plano cartesiano
    a.arriba()
        
for i in range (8):
    a.izquierda()
    

print (a.nombre, "ubicado en", a.posicion())
    
    
    