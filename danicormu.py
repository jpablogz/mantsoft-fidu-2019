#This function darmensaje is to concatenate the a message. Receive a parameter and return a message Hola Mundo + the parameter
def darmensaje(message):
    
    print("Hola Mundo!")
    
    print(message)
    
darmensaje("De Informáticos")



#This function PatternCount find a pattern in a string, receive the parameters: text and pattern, it return the number of times this pattern is repeated in the text
def PatternCount(Text, Pattern):
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
       		count += 1
    print('Count the pattern:' +Pattern+ ' in the string:' +Text+ ' is ', count)
    return count    
PatternCount("gcgcg","gcg")
