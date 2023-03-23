'''
Dado la figura de la imagen, desarrolle:

- Una función matemática para calcular el área y el perimetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi

'''
import math

def areaFigura(base:float,altura:float,radio:float) -> float:
    area = 2 * (math.pi * radio**2) + base * altura
    return area 

def perimetroFigura(base:float,altura:float,radio:float) -> float:
    perimetro = 2 * base + 2 * altura + 4 * math.pi * radio
    return perimetro

if __name__ == "__main__":
    r = float(input("Ingrese la longitud de el radio de las circunferencias: "))
    a = float(input("Ingrese la longitud de la altura del rectángulo: "))
    b = float(input("Ingrese la longitud de la base del rectángulo: "))
    area = areaFigura(b,a,r)
    perimetro = perimetroFigura(b,a,r)
    print("El area de la figura es: " +str(area))
    print("El perimetro de la figura es: " +str(perimetro))