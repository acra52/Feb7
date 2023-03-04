class alumno():
    #nota minima para pasar
    minimo = 80
    
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
    
    def aprobo(self) -> bool:
        if self.nota >= self.minimo:
            print('Aprobaste')
            
        else: print('no aprobaste')
        
        
w = alumno('Andrea', 68)
w.aprobo()
                
