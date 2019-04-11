from tkinter import *
jose = Tk()
jose.title("Hola mundo!!")
jose.config(bg="black")
miFrame= Frame(jose, width=300,height=200)
miFrame.pack()
def darmensaje(mensaje):   
   Label (miFrame,text="hola mundo!", fg="Red").place(x=100, y=85)
   print (mensaje)
darmensaje("Jose mora")

jose.mainloop()