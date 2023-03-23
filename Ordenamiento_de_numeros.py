# Función para identificar el número mayor 
def Mayor(a:float,b:float,c:float,d:float,e:float) -> float:
    if a>b:
        mayor=a
    else:
        mayor=b
    if mayor>c:
        mayor=mayor
    else:
        mayor=c
    if mayor>d:
        mayor=mayor
    else:
        mayor=d
    if mayor>e:
        mayor=mayor
    else:
        mayor=e
    return mayor

# Función para identificar el número menor 
def Menor(a:float,b:float,c:float,d:float,e:float) -> float:
    if a<b:
        menor=a
    else:
        menor=b
    if menor<c:
        menor=menor
    else:
        menor=c
    if menor<d:
        menor=menor
    else:
        menor=d
    if menor<e:
        menor=menor
    else:
        menor=e
    return menor

# Función para identificar los números que no son mayor ni menor 
def intermedioUno(a:float,b:float,c:float,d:float,e:float) -> float:
    mayor = Mayor(a,b,c,d,e)
    menor = Menor(a,b,c,d,e)
    if a != mayor and a != menor:
        medio1 = a
    if b != mayor and b != menor:
        medio1 = b
    if c != mayor and c != menor:
        medio1 = c
    if d != mayor and d != menor:
        medio1 = d
    if e != mayor and e != menor:
        medio1 = e
    return medio1

def intermedioDos(a:float,b:float,c:float,d:float,e:float) -> float:
    mayor = Mayor(a,b,c,d,e)
    menor = Menor(a,b,c,d,e)
    medio1 = intermedioUno(a,b,c,d,e)
    if a != mayor and a != menor and a!=medio1:
        medio2 = a
    if b != mayor and b != menor and b!=medio1:
        medio2 = b
    if c != mayor and c != menor and c!=medio1:
        medio2 = c
    if d != mayor and d != menor and d!=medio1:
        medio2 = d
    if e != mayor and e != menor and e!=medio1:
        medio2 = e
    return medio2


def intermedioTres(a:float,b:float,c:float,d:float,e:float) -> float:
    mayor = Mayor(a,b,c,d,e)
    menor = Menor(a,b,c,d,e)
    medio1 = intermedioUno(a,b,c,d,e)
    medio2 = intermedioDos(a,b,c,d,e)
    if a != mayor and a != menor and a!=medio1 and a!=medio2:
        medio3 = a
    if b != mayor and b != menor and b!=medio1 and b!=medio2:
        medio3 = b
    if c != mayor and c != menor and c!=medio1 and c!=medio2:
        medio3 = c
    if d != mayor and d != menor and d!=medio1 and d!=medio2:
        medio3 = d
    if e != mayor and e != menor and e!=medio1 and e!=medio2:
        medio3 = e
    return medio3

# Función para identificar el número siguiente de forma ascendente menor
def primerMedio(a:float,b:float,c:float,d:float,e:float) -> float:
    medio1 = intermedioUno(a,b,c,d,e)
    medio2 = intermedioDos(a,b,c,d,e)
    medio3 = intermedioTres(a,b,c,d,e)
    if medio1<medio2:
        m1=medio1
    else:
        m1=medio2
    if m1<medio3:
        m1=m1
    else:
        m1=medio3
    return m1

# Función para identificar el número siguiente de forma descendente mayor
def tercerMedio(a:float,b:float,c:float,d:float,e:float) -> float:
    medio1 = intermedioUno(a,b,c,d,e)
    medio2 = intermedioDos(a,b,c,d,e)
    medio3 = intermedioTres(a,b,c,d,e)
    if medio1>medio2:
        m3=medio1
    else:
        m3=medio2
    if m3>medio3:
        m3=m3
    else:
        m3=medio3
    return m3

# Función para identificar el número faltante (el de la mitad)
def segundoMedio(a:float,b:float,c:float,d:float,e:float) -> float:
    mayor = Mayor(a,b,c,d,e)
    menor = Menor(a,b,c,d,e)
    m1 = primerMedio(a,b,c,d,e)
    m3 = tercerMedio(a,b,c,d,e)
    if a != mayor and a != menor and a!=m1 and a!=m3:
        m2 = a
    if b != mayor and b != menor and b!=m1 and b!=m3:
        m2 = b
    if c != mayor and c != menor and c!=m1 and c!=m3:
        m2 = c
    if d != mayor and d != menor and d!=m1 and d!=m3:
        m2 = d
    if e != mayor and e != menor and e!=m1 and e!=m3:
        m2 = e
    return m2

