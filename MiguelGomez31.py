#TAREA 1
def dar_mensaje(mensaje):   
   print ("Hola Mundo!")
   print (mensaje)
   return;   
dar_mensaje("Aprendiendo phyton y a usar github")

#TAREA 2

def PatternCount(Text, Pattern):
    count = 0
    for i in range(0, (len(Text) - len(Pattern) + 1)):
        if Text[i:i+len(Pattern)] == Pattern:
       		count = count + 1
    return count


Input = "ABCABCABCABCABCABCABCABCABCABCABCABC"

def FrequentWords(Text, x):
    maxcount = 0
    patternlength = int(x)
    maxpattern = []
    for i in range(0, (len(Text) - patternlength + 1)):
        if PatternCount(Text, Text[i:i + patternlength]) > maxcount:
            maxcount = PatternCount(Text, Text[i:i+patternlength])
            maxpattern = []
            maxpattern.append(Text[i:i + patternlength])
        elif PatternCount(Text, Text[i:i + patternlength]) == maxcount and Text[i:i+patternlength] not in maxpattern:
            maxpattern.append(Text[i:i + patternlength])

    print ("Se repite", maxcount, "veces")   
    return maxpattern
print ("El patron", FrequentWords(Input, 3))
