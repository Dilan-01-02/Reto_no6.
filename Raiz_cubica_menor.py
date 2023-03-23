from Ordenamiento_de_numeros import Menor
def raizCubicaMenor(a:float,b:float,c:float,d:float,e:float) -> float:
    menor = Menor(a,b,c,d,e)
    raiz = menor**(1/3)
    return raiz