"""def darmensaje(mensaje):
    
  return print ('Hola Mundo!', mensaje)
    
darmensaje(input())"""


#Funcion para determinar cuentas veces se repite una cadena de texto dentro de otra
#Recibe dos parametros una cadena de texto, y el patron que se va a buscar dentro de ella
def PatternCount(Text, Pattern):
#Se define un contador, que como su nombre lo indica llevara el conteo del blucle
#cada vez que encuentre que el substring es igual al patron
    cont = 0
#Se usa un string slicing para ver si el substring es igual al patron
    for i in range(0, len(Text) - len(Pattern) + 1):
#Aqui se hace la comparacion del substring con el patron dado y si es igual le suma 1 al contador
        if Text[i : len(Pattern) + i] == Pattern:
            cont += 1
    return print (cont)

PatternCount(input(), input());
