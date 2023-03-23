'''
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_6 en slack.

- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.pi

'''
# Importación de la libreria "math"
import math 

# Funcion para calcular el volumen de la figura
def volumenFigura(a:float,b:float,c:float) -> float: 
    volumenE = 4 / 3 * math.pi * a**3
    volumenC = 1 / 3 * c * math.pi * b**2
    volumenT = volumenE + volumenC
    return volumenT

# Función para calcular el area superficial de la figura
def areaSuperficialFigura(a:float,b:float,c:float) -> float:
    areaE = 4 * math.pi * a**2
    generatriz = (b**2 + c**2)**(1/2)
    areaC = math.pi * b**2 + math.pi * b * generatriz
    areaT = areaE + areaC
    return areaT

# Función principal
if __name__ == "__main__":
    
    # Declaración e ingreso de variables
    r1 = float(input("Ingrese el radio de la esfera: "))
    r2 = float(input("Ingrese el radio de la base del cono: "))
    h = float(input("Ingrese la altura del cono: "))

    # Llamado de las funciones
    volumenT = volumenFigura(r1,r2,h)
    areaT = areaSuperficialFigura(r1,r2,h)

    # Impresión del resultado 
    print("El volumen total de la figura es: " + str(volumenT))
    print("El area superficial total de la figura es: " + str(areaT))