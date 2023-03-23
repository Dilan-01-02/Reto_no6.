'''
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas 
(o lo que quedo debiendo) cuando me da un billete de B pesos.

'''
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
        

if __name__ == "__main__":
    P = int(input("Ingrese la cantidad de panes que va a comprar: "))
    M = int(input("Ingrese la cantidad de bolsas de leche que va a comprar: "))
    H = int(input("Ingrese la cantidad de huevos que va a comprar: "))
    B = float(input("Ingrese el valor del billete con el que va a realizar la compra en pesos: "))
    mandado = mandado(P,M,H,B)
    print(mandado + " pesos")
