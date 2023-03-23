# Importación de las funciones 
from Ordenamiento_de_numeros import *
from Promedio import *
from Promedio_multiplicativo import *
from Potencia_del_mayor_al_menor import *
from Raiz_cubica_menor import *

# Función principal
if __name__ == "__main__":

    # Declaración e ingreso de variables
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    print("\n")

    # Llamado de las funciones
    prom = promedio(a,b,c,d,e)
    pmult = promMulti(a,b,c,d,e)
    mayor = Mayor(a,b,c,d,e)
    menor = Menor(a,b,c,d,e)
    m1 = primerMedio(a,b,c,d,e)
    m2 = segundoMedio(a,b,c,d,e)
    m3 = tercerMedio(a,b,c,d,e)
    potMayorMenor = potenciaMayorAlMenor(a,b,c,d,e)
    raizCubica = raizCubicaMenor(a,b,c,d,e)

    # Impresión de los resultados
    print("El promedio de los números ingresados es: "+str(prom)+ "\n")
    print("La mediana de los números ingresados es: " +str(m2)+ "\n")
    print("El promedio multiplicativo de los números ingresados es: " +str(pmult)+ "\n")
    print("Los números ingresados ordenados de forma ascendente: " +str(menor)+ " , " +str(m1)+ " , " +str(m2)+ " , " +str(m3)+ " , " +str(mayor)+ "\n")
    print("Los números ingresados ordenados de forma descendente: " +str(mayor)+ " , " +str(m3)+ " , " +str(m2)+ " , " +str(m1)+ " , " +str(menor)+ "\n")
    print("La potencia del mayor número al menor número es: " +str(potMayorMenor)+ "\n")
    print("La raiz cúbica del menor número es: " +str(raizCubica)+ "\n")
    