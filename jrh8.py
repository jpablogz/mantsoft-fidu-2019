def darmensaje(mensaje):
    print("Hola Mundo" + mensaje)

darmensaje(" es mi primera vez en python ")


#crear una funcion PatternCount que cuenta cuántas veces aparece
#un patrón Pattern en una cadena de caracteres Text

print("Buenas por favor ingrese un texto donde se repita un patrón y luego ingresa el patrón")

def PatternCoun(text, pattern):
    cont = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            cont += 1
    return print ("El patrón se repite "+str(cont) + " veces en el texto")

PatternCoun(input(), input());



    
        
    
