 def darmensaje(mensaje):
	print ("Hola mundo " + mensaje)

 darmensaje("vamos a conquistarte")

 def PatternCount(text, patron):
    count = 0
    for i in range(len(text)):
        s = text[i:len(patron)+i]
        if(len(s)<len(patron)):
            break
        if patron in s:
            count+=1
    print("El patrón se repite "+str(count)+" veces en la cadena.")
    return count

PatternCount("CCCATTAATATTAGCACCTGCCGACTAGCTGCCGACGTAACCCGTTATCCTGCCGAGGCTGCCGAATAGACTGCCGACGGTGTCTGCCGAAGAGTTCTGGTCCTGCCGACCTGCCGACCTGCCGAGAACTGCCGAGCACTGCCGACTGCCGAACTGCCGATACGATGGATCTGCCGACTTACTATGCAACCTGCCGACTGCCGACGCCCTGCCGACCACCTGCCGACTGCCGATCTGCCGAACACGGCGCTGCCGATCCTGCCGAGTCTGCCGACTGCCGATACTGCCGAGCCTGCCGATTCTGCCGACTGCCGATACATGTCCTGCCGACTTTACTGCCGAGCACTAAGGACTGCCGACTGCCGAAAATGAGTCGTCTGCCGACCAGCTGCCGACCTGCCGACTGCCGACTAATCTGCCGACTGCCGACTGCCGACTCCTGCCGATTTCAAAGGGTGCAACTGCCGACCTGCCGACTGCCGAGATGCTGCCGATACTCTGCCGAAACTCTGCCGATCAGTTGACACTGCCGACACTGCCGAACTGCCGACATTTCTGCCGACTCATCTGCCGAGCTGCCGACTGCCGACCACGCTGCCGACCTCTGCTGCCGAGGTATCCTGCCGAGTCACAACTGCCGAACTGCCGACCTGCCGATGCTGCCGATCTCCTGCCGAATTGACTGCCGACTGATATAGACTGCCGATCGGCAGTTCCTCTGCCGATCTGCCGAGCCTGCCGAATGGGACGCTGCCGACTCTGCCGAGATGTAGGCTGCCGATCGATCTGCCGAGGCTGCCGAGAGCCTGCCGACGCCTGCCGACTGCCGAATCTGCCGACTGCCGAAACCGGGGCCACTGCCGATGCGTCTGCCGATTTACTGCCGACTGCCGATCACGCTCTGCTGCCGACTGCCGATGCCTGCCGATCTGCCGAT","CTGCCGACT")



