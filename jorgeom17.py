#PRIMERA ENTREGA
#Funcion para imprimir mensaje
def darmensaje (elMensaje):
    print('Hola Mundo! ' + elMensaje)
    return

darmensaje('Jorge Ortiz Monge')

#SEGUNDA ENTREGA
#Funcion que obtiene la cantidad de veces que se repite una subcadena de caracteres en una cadena de caracteres
#Recibe como parametros la cadena original y la cadena a buscar
def PatternCount (pattern, text):
    contador = 0

    for indice in range(0, len(text)):
        if (indice + len(pattern) > len(text)):
            break
        else:
            if pattern == text[indice:indice + len(pattern)]:
                contador = contador + 1

    print(contador)

    return

PatternCount('GCG', 'GCGCG')
