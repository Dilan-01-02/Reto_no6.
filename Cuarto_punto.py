'''
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas 
(o lo que quedo debiendo) cuando me da un billete de B pesos.

'''
# Función para calcular las vueltas de un mandado 
def mandado(panes:int,leche:int,huevos:int,billete:float) -> str:
    precio = panes * 300 + leche * 3300 + huevos * 350
    dif = billete - precio
    if dif < 0:
        dif = - dif 
    if billete < precio:
        vueltas = "Queda debiendo: " + str(dif)
    else:
        vueltas = "Sus vueltas son: " +str(dif)
    return vueltas
        
# Función principal
if __name__ == "__main__":

    # Declaración e ingreso de variables 
    P = int(input("Ingrese la cantidad de panes que va a comprar: "))
    M = int(input("Ingrese la cantidad de bolsas de leche que va a comprar: "))
    H = int(input("Ingrese la cantidad de huevos que va a comprar: "))
    B = float(input("Ingrese el valor del billete con el que va a realizar la compra en pesos: "))

    # Llamado de la función 
    mandado = mandado(P,M,H,B)

    # Impresión del resultado
    print(mandado + " pesos")
