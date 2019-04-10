# Función que imprime el mensaje
def darmensaje (p_mensaje):
    print (p_mensaje);

# Función para contar cuántas veces se encuentra un patrón en una cadena de caracteres
# Entradas:
#   Text:       Cadena de caracteres con el ADN
#   Pattern:    Patrón a buscar en la cadena de caracteres Text
# Salida:
#   Cantidad de veces que se encuentra el patrón en la cadena de caracteres
def PatternCount (Text, Pattern):
#    p_cadena_tmp = p_cadena.capitalize()
    v_cantidad = 0
    v_largo = len(Pattern)
    for i in range(len(Text)):
        if Text[i : i + v_largo] == Pattern:
            v_cantidad += 1
    return v_cantidad;

#Ejecución principal
#darmensaje("Hola Mundo");
a = PatternCount("DO RE DO MI SOL DO LA", "DO");
print (a)
