#Semana 1
def darmensaje(mensaje):
    print ("Hola Mundo", mensaje, ".")

darmensaje("ALEJANDRO")



#Semana 2
Cadena="CCCATTAATATTAGCACCTGCCGACTAGCTGCCGACGTAACCCGTTATCCTGCCGAGGCTGCCGAATAGACTGCCGACGGTGTCTGCCGAAGAGTTCTGGTCCTGCCGACCTGCCGACCTGCCGAGAACTGCCGAGCACTGCCGACTGCCGAACTGCCGATACGATGGATCTGCCGACTTACTATGCAACCTGCCGACTGCCGACGCCCTGCCGACCACCTGCCGACTGCCGATCTGCCGAACACGGCGCTGCCGATCCTGCCGAGTCTGCCGACTGCCGATACTGCCGAGCCTGCCGATTCTGCCGACTGCCGATACATGTCCTGCCGACTTTACTGCCGAGCACTAAGGACTGCCGACTGCCGAAAATGAGTCGTCTGCCGACCAGCTGCCGACCTGCCGACTGCCGACTAATCTGCCGACTGCCGACTGCCGACTCCTGCCGATTTCAAAGGGTGCAACTGCCGACCTGCCGACTGCCGAGATGCTGCCGATACTCTGCCGAAACTCTGCCGATCAGTTGACACTGCCGACACTGCCGAACTGCCGACATTTCTGCCGACTCATCTGCCGAGCTGCCGACTGCCGACCACGCTGCCGACCTCTGCTGCCGAGGTATCCTGCCGAGTCACAACTGCCGAACTGCCGACCTGCCGATGCTGCCGATCTCCTGCCGAATTGACTGCCGACTGATATAGACTGCCGATCGGCAGTTCCTCTGCCGATCTGCCGAGCCTGCCGAATGGGACGCTGCCGACTCTGCCGAGATGTAGGCTGCCGATCGATCTGCCGAGGCTGCCGAGAGCCTGCCGACGCCTGCCGACTGCCGAATCTGCCGACTGCCGAAACCGGGGCCACTGCCGATGCGTCTGCCGATTTACTGCCGACTGCCGATCACGCTCTGCTGCCGACTGCCGATGCCTGCCGATCTGCCGAT"
Patron="CTGCCGACT"

def numeroPratones(Cadena, Patron):
    conta = 0
    
    for i in range(0, (len(Cadena) - len(Patron) + 1)):
        if Cadena[i:i+len(Patron)] == Patron:
           conta = conta + 1
    print("El numero veces que repite el patron es:",conta)

numeroPratones(Cadena,Patron)
