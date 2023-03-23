'''
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

'''
# Función para realizar el cálculo del interés compuesto
def interesCompuesto(c:float,i:float,n:int) ->float:
    Vf = c * (1 + (i/100)) ** n
    return Vf

# Función principal
if __name__ == "__main__":

    # Declaración e ingreso de variables 
    c = float(input("Ingrese la cantidad del prestamo: "))
    i = float(input("Ingrese el porcentaje (%) de tasa de interes: "))
    n = int(input("Ingrese el número de meses: "))

    # Llamado de la función 
    interesCompuesto = interesCompuesto(c,i,n)

    # Impresión del resultado
    print("El valor final del prestamo "+str(c)+" usando un interés compuesto del "+str(i)+" % por "+str(n)+ " meses es de: "+str(interesCompuesto))
