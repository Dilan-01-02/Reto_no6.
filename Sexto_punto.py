'''
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen 
D días a partir de hoy, si el número de contagiados actuales es C.

'''
def contagiados(D:int,C:int) -> int:
    N = C * 2 ** D
    return N


if __name__ == "__main__":
    D = int(input("Ingrese el número de días: "))
    C = int(input("Ingrese el número de infectados actualmente: "))
    contagiados = contagiados(D,C)
    print("El número de contagiados al pasar "+str(D)+" días será de: "+str(contagiados))