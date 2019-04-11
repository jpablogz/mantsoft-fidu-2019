def darmensaje(mensaje):
    print("Hola mundo "+ mensaje +"!")

def  crearmensaje():
    mensaje = input("Ingrese algún texto : ")
    darmensaje(mensaje)
    nuevomensaje()

def nuevomensaje():
        opt = input("Desea enviar otro mensaje? Y/N : ")
        if opt == "Y" or opt == "y":
            crearmensaje()
        elif opt == "N" or opt == "n":
            print("Adios!")
        else:
            print("Valor inválido, vuelva a intentarlo")
            nuevomensaje()


crearmensaje()
