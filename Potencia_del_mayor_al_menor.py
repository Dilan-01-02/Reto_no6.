from Ordenamiento_de_numeros import Mayor
from Ordenamiento_de_numeros import Menor
def potenciaMayorAlMenor (a:float,b:float,c:float,d:float,e:float) -> float:
    mayor = Mayor(a,b,c,d,e)
    menor = Menor(a,b,c,d,e)
    pot = mayor ** menor
    return pot 