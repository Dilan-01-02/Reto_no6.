'''
Dado la figura de la imagen, desarrolle:

- Una función matemática para calcular el área y el perimetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi

'''
# Importación de la libreria "math"
import math

# Funcion para calcular el area de la figura
def areaFigura(base:float,altura:float,radio:float) -> float:
    area = 2 * (math.pi * radio**2) + base * altura
    return area 

# Funcion para calcular el perimetro de la figura
def perimetroFigura(base:float,altura:float,radio:float) -> float:
    perimetro = 2 * base + 2 * altura + 4 * math.pi * radio
    return perimetro

# Función principal
if __name__ == "__main__":

    # Declaración e ingreso de variables
    r = float(input("Ingrese la longitud de el radio de las circunferencias: "))
    a = float(input("Ingrese la longitud de la altura del rectángulo: "))
    b = float(input("Ingrese la longitud de la base del rectángulo: "))

    # Llamado de las funciones
    area = areaFigura(b,a,r)
    perimetro = perimetroFigura(b,a,r)

    # Impresión del resultado 
    print("El area de la figura es: " +str(area))
    print("El perimetro de la figura es: " +str(perimetro))