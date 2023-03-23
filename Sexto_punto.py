'''
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen 
D días a partir de hoy, si el número de contagiados actuales es C.

'''
# Función para calcular el número de contagiados
def contagiados(D:int,C:int) -> int:
    N = C * 2 ** D
    return N

# Función pricipal
if __name__ == "__main__":
    
    # Declaración e ingreso de variables
    D = int(input("Ingrese el número de días: "))
    C = int(input("Ingrese el número de infectados actualmente: "))
    
    # Llamado de la función
    contagiados = contagiados(D,C)
    
    # Impresión del resultado
    print("El número de contagiados al pasar "+str(D)+" días será de: "+str(contagiados))