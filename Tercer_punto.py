'''
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

'''
def cantidadDeCarne(gallinas:int,gallos:int,pollos:int) -> int:
    carne = gallinas * 6 + gallos * 7 + pollos 
    return carne

if __name__ == "__main__":
    N = float(input("Ingrese la cantidad de gallinas: "))
    M = float(input("Ingrese la cantidad de gallos: "))
    K = float(input("Ingrese la cantidad de pollos: "))
    cantidadDeCarne = cantidadDeCarne(N,M,K)
    print("La cantidad de carne de aves es: " +str(cantidadDeCarne))
