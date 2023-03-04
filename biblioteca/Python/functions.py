import math
def area_rectangulo(
    x:float,
    y:float
)-> None:

    """
    Funcion que calcula el area de un rectangulo 
    ---params---
    - x (float): es la base de mi rectangulo
    - y (float): es la altura de mi rectangulo

    ---return---
    - area (float): es el area de mi triangulo
    """

    area = x*y
    print(area)
    return area #return bota el resultado y es el fin de la funcion

area = area_rectangulo(5,7)
print(f"El area de mi rectangulo es {area}")
# altura = float(input('Introduce el area del rectangulo: '))
# base = float(input('Introduce la base del rectangulo: '))
# result = area_rectangulo(base, altura)
# print(f' El area del rectangulo es {result}')

def distancia_dos_puntos(
    x_1: float,
    x_2: float,
    y_1: float,
    y_2: float
 ) -> float:
    """Función que calcula la distancia entre dos puntos

    Args:
        x_1 (float): punto 1
        x_2 (float): punto 1.2
        y_1 (float): punto 2.1
        y_2 (float): punto 2.2

    Returns:
        float: la distancia entre dos puntos
    """

    x = math.pow(x_2-x_1,2)
    y = math.pow(y_2-y_1,2)
    d = math.sqrt(x+y)
    return d
