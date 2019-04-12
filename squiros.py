#Funcion para imprimir mensaje
def darmensaje (elMensaje):
    print('Hola Mundo! ' + elMensaje)
    return

darmensaje('Sofía Quirós Ramírez')

#Funcion para contar el número de veces que se repite una cadena en una subcadena

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


