def PatternCount(text, pattern):
    '''
    Esta función retorna las veces que aparece un patrón en una cadena de texto
    *Parameters*
    text: Cadena de texto en la que se busca el patrón
    pattern: Patrón a encontrar en la cadena de texto
    *Returns*
    count: Retorna el número de veces que aparece el patrón
    '''
    count = 0
    for i in range(len(text)):
        substring = text[i:len(pattern)+i]
        if(len(substring)<len(pattern)):
            break
        if pattern in substring:
            count+=1
    print("El patrón existe "+str(count)+" veces en la cadena.")
    return count
PatternCount("CCCATTAATATTAGCACCTGCCGACTAGCTGCCGACGTAACCCGTTATCCTGCCGAGGCTGCCGAATAGACTGCCGACGGTGTCTGCCGAAGAGTTCTGGTCCTGCCGACCTGCCGACCTGCCGAGAACTGCCGAGCACTGCCGACTGCCGAACTGCCGATACGATGGATCTGCCGACTTACTATGCAACCTGCCGACTGCCGACGCCCTGCCGACCACCTGCCGACTGCCGATCTGCCGAACACGGCGCTGCCGATCCTGCCGAGTCTGCCGACTGCCGATACTGCCGAGCCTGCCGATTCTGCCGACTGCCGATACATGTCCTGCCGACTTTACTGCCGAGCACTAAGGACTGCCGACTGCCGAAAATGAGTCGTCTGCCGACCAGCTGCCGACCTGCCGACTGCCGACTAATCTGCCGACTGCCGACTGCCGACTCCTGCCGATTTCAAAGGGTGCAACTGCCGACCTGCCGACTGCCGAGATGCTGCCGATACTCTGCCGAAACTCTGCCGATCAGTTGACACTGCCGACACTGCCGAACTGCCGACATTTCTGCCGACTCATCTGCCGAGCTGCCGACTGCCGACCACGCTGCCGACCTCTGCTGCCGAGGTATCCTGCCGAGTCACAACTGCCGAACTGCCGACCTGCCGATGCTGCCGATCTCCTGCCGAATTGACTGCCGACTGATATAGACTGCCGATCGGCAGTTCCTCTGCCGATCTGCCGAGCCTGCCGAATGGGACGCTGCCGACTCTGCCGAGATGTAGGCTGCCGATCGATCTGCCGAGGCTGCCGAGAGCCTGCCGACGCCTGCCGACTGCCGAATCTGCCGACTGCCGAAACCGGGGCCACTGCCGATGCGTCTGCCGATTTACTGCCGACTGCCGATCACGCTCTGCTGCCGACTGCCGATGCCTGCCGATCTGCCGAT","CTGCCGACT")
