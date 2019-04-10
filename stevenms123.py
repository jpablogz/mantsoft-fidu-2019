#funcion darmensaje recibe un string por parametro
#y como salida muestra el mensjae de Hola Mundo + el parametro
def darmensaje(mensaje):   
   print ("Hola Mundo!")
   print (mensaje)
   return;   
darmensaje("Suelta a mi chimuelo")


#funcion darmensaje recibe una cadena de texto y un patron por parametro
#y como salida muestra la cantidad de veces que se repite el patron dentro de la cadena de texto
def PatternCount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            count += 1
    print ("Texto: ", text)
    print ("Patron: ", pattern)
    print ("El patron se repite ", count ,"veces")
    return count;
PatternCount("abc124abcabcabcabnjjbccabc", "abc")
