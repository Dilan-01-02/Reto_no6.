# Importación de la función 
from Ordenamiento_de_numeros import Menor

# Función para realizar el cálculo de la potencia de la raíz cúbica del menor número
def raizCubicaMenor(a:float,b:float,c:float,d:float,e:float) -> float:
    menor = Menor(a,b,c,d,e)
    raiz = menor**(1/3)
    return raiz