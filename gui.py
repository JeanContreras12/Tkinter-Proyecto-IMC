import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x600")

#etiqueta = tkinter.Label(ventana, text = "etiqueta", bg = "green")
#etiqueta.pack(side= tkinter.BOTTOM)
#etiqueta.pack(side= tkinter.RIGHT)
#etiqueta.pack(fill= tkinter.X)# REVISAR FILL Y SIDE EN LA DOCUMENTACIÓN
#etiqueta.pack(fill= tkinter.Y, expand= True)
#etiqueta.pack(fill= tkinter.BOTH, expand= True)
"""
def saludo(nombre):
    print("hola " + nombre)
boton1 = tkinter.Button(ventana, text= "presiona", command=lambda: saludo ("python"))#, padx =40, pady =50
boton1.pack()"""

""""cajatxt =tkinter.Entry(ventana, font = "Helveltica 20")
cajatxt.pack()

etiqueta =tkinter.Label(ventana)
etiqueta.pack()

def textoDeLaCaja():
    text20 = cajatxt.get()
    etiqueta["text"] = text20

boton1 = tkinter.Button(ventana, text = "click", command= textoDeLaCaja)
boton1.pack()"""

boton1 = tkinter.Button(ventana, text= "boton1", width= 20, height=5)
boton2 = tkinter.Button(ventana, text= "boton1", width= 20, height=5)
boton3 = tkinter.Button(ventana, text= "boton1", width= 20, height=5)

boton1.grid(row=0, column =0)
boton2.grid(row=1, column =0)
boton3.grid(row=2, column =0)
ventana.mainloop()