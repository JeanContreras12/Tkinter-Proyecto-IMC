from tkinter import *
from tkinter import ttk
import tkinter as tk

from pymysql import TIMESTAMP
from database import *
from tkinter import messagebox

def calcular_edad(fecha_nacimiento):
        from datetime import datetime, date

        #Convierte string a date
        nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        #Obtiene fecha de hoy
        hoy = date.today()
        #Calcular la edad
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        return edad


def calcular_imc(altura, peso):
    imc = peso/(altura*altura)
    return imc

def interpretar_imc(sexo, imc):

    interpretacion = ""

    if(sexo == 'Masculino'):
        if(imc < 20):
            interpretacion = "BAJO PESO"
        elif(imc <25):
            interpretacion = "NORMAL"
        elif(imc <30):
            interpretacion = "OBESIDAD LEVE"
        elif(imc <=40):
            interpretacion = "OBESIDAD SEVERA"
        elif(imc > 40):
            interpretacion = "OBESIDAD MUY SEVERA"
        

    if(sexo == 'Femenino'):
        if(imc < 20):
            interpretacion = "BAJO PESO"
        elif(imc <24):
            interpretacion = "NORMAL"
        elif(imc <29):
            interpretacion = "OBESIDAD LEVE"
        elif(imc <=37):
            interpretacion = "OBESIDAD SEVERA"
        elif(imc > 37):
            interpretacion = "OBESIDAD MUY SEVERA"

    return interpretacion


class App:
    def __init__(self, master):
        self.ventana = master
        """self.DibujarLabelS()
        self.DibujarEntry()
        self.DibujarBoton()
        self.DibujarLista()"""
        self.boton_Menu_Principal()
    


    def boton_Menu_Principal(self):
        self.lbl_name =Label(self.ventana, text="Para consultar su IMC primero debe estar registrado y luego buscar su rut",font=("Berlin Sans FB","11"), bg="orange", foreground="#0C090A", width=60).place(x=260, y=100)
        #boton principal boton ingresar persona
        self.btn_guardar= Button(self.ventana, text="Ingresar Persona", font=("Berlin Sans FB","11"),width=30, height=2,cursor="hand2", foreground="black", command=lambda:self.DibujarLabelS()).place(x=300, y=150, width=170)
        
        self.btn_guardar= Button(self.ventana, text="Consultar IMC", font=("Berlin Sans FB","11"),width=30, height=2,cursor="hand2", foreground="black", command=lambda:self.DibujarBuscarPersona()).place(x=500, y=150, width=170)

    def DibujarLabelS(self):
        self.ventana_Ingresar_Persona = Toplevel(self.ventana)
        self.ventana_Ingresar_Persona.geometry("1100x450")
        self.ventana_Ingresar_Persona.config(background= "#348781")
        self.ventana_Ingresar_Persona.title("Ingreso de Persona")
        self.ventana_Ingresar_Persona.wm_transient(self.ventana)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="¡Su edad debe estar entre los 15 y los 70 años o el sistema lo rechazara!",font=("Berlin Sans FB","11"), bg="orange", foreground="#0C090A", width=60).place(x=105, y=30)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="Fecha de nacimiento:",font=("Berlin Sans FB","11"), bg="#E5E4E2", foreground="#0C090A", width=19).place(x=105, y=110)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="(dd/mm/aaaa)",font=("Berlin Sans FB","11"), foreground="#0C090A", bg="#348781").place(x=320, y=133)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="Nombre Completo:",font=("Berlin Sans FB","11"), bg="#E5E4E2", foreground="#0C090A", width=19).place(x=105, y=160)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="RUT:",font=("Berlin Sans FB","11"), bg="#E5E4E2", foreground="#0C090A", width=19).place(x=105, y=210)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="Sexo:",font=("Berlin Sans FB","11"), bg="#E5E4E2", foreground="#0C090A", width=19).place(x=105, y=260)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="Deportista:",font=("Berlin Sans FB","11"), bg="#E5E4E2", foreground="#0C090A", width=19).place(x=105, y=310)
        self.lbl_name =Label(self.ventana_Ingresar_Persona, text="Sexo:",font=("Berlin Sans FB","11"), bg="#E5E4E2", foreground="#0C090A", width=19).place(x=105, y=260)
        
        self.DibujarEntry()
        self.DibujarLista("", 500, 110, 8, True)
        self.DibujarBoton()

    def DibujarEntry(self):
        self.Fecha_Nacimiento = StringVar()
        self.nombre= StringVar()
        self.rut= StringVar()
        self.seleccion_Sexo=StringVar()
        self.seleccion_Deporte=StringVar()
        self.buscar_e=StringVar()
        
        
        self.txt_Fecha_nacimiento =Entry(self.ventana_Ingresar_Persona, font=('arial', 12), textvariable=self.Fecha_Nacimiento).place(x=280, y=110)
        self.txt_Nombre =Entry(self.ventana_Ingresar_Persona, font=('arial', 12), textvariable=self.nombre).place(x=280, y=160)
        self.txt_Rut =Entry(self.ventana_Ingresar_Persona, font=('arial', 12), textvariable=self.rut).place(x=280, y=210)
        self.cmb_sexo=ttk.Combobox(self.ventana_Ingresar_Persona,textvariable=self.seleccion_Sexo,state="readonly", width=27)
        self.cmb_sexo["values"]=("Masculino","Femenino")
        self.cmb_sexo.place(x=280, y=260)
        self.cmb_sexo.current(0)

        self.cmb_Deporte=ttk.Combobox(self.ventana_Ingresar_Persona,textvariable=self.seleccion_Deporte,state="readonly", width=27)
        self.cmb_Deporte["values"]=("Si","No")
        self.cmb_Deporte.place(x=280, y=310)
        self.cmb_Deporte.current(0)
        
        #entry buscar
        #self.txt_buscar =Entry(self.ventana_Ingresar_Persona, font=('arial', 12), textvariable=self.buscar_e).place(x=350, y=340)

        
    def DibujarBoton(self):
        self.btn_guardar= Button(self.ventana_Ingresar_Persona, text="Guardar", relief="flat", background="green",cursor="hand2", foreground="white", command=lambda:self.guardar()).place(x=320, y=380, width=80, height=30)

        self.btn_cancelar= Button(self.ventana_Ingresar_Persona, text="Cancelar", relief="flat", background="green",cursor="hand2", foreground="white", command=lambda:self.ventana_Ingresar_Persona.destroy()).place(x=430, y=380, width=80, height=30)
        
        #boton buscar
        #self.btn_buscar= Button(self.ventana_Ingresar_Persona, text="Buscar", relief="flat", background="#0051c8",cursor="hand1", foreground="white", command=lambda: self.buscar(self.buscar_e.get())).place(x=550, y=340, width=90)
    
    def buscar(self, ref):
        self.LimpiarLista()
        self.DibujarLista(ref, 500, 110, 8, True)
       
    def buscarPersona(self, ref):
        self.LimpiarLista()
        self.DibujarLista(ref, 50, 50, 1, False)
        

    def guardar(self):
        arr= [self.Fecha_Nacimiento.get(), self.nombre.get(), self.rut.get(), self.seleccion_Sexo.get(), self.seleccion_Deporte.get()]
        edad=calcular_edad(arr[0])
        if(edad>15 and edad<70):
            d= Data()
            d.InsertItems(arr)
            self.Fecha_Nacimiento.set("")
            self.nombre.set("")
            self.rut.set("")
            #self.seleccion_Sexo.set("")
            #self.seleccion_Deporte.set("")
            self.LimpiarLista()
            self.DibujarLista("", 500, 110, 8, True)
        else:
            self.ventana_Error_Edad = Toplevel(self.ventana_Ingresar_Persona)
            self.ventana_Error_Edad.geometry("430x200")
            self.ventana_Error_Edad.config(background= "red")
            self.ventana_Error_Edad.title("Error Edad")
            self.ventana_Error_Edad.wm_transient(self.ventana_Ingresar_Persona)
            self.lbl_Mensaje_Error =Label(self.ventana_Error_Edad, text="¡Su edad no se encuentra en el rango especificado!",font=("Berlin Sans FB","15"), bg="red", foreground="#0C090A").place(x=0, y=70)




    def LimpiarLista(self):
        self.lista.delete(*self.lista.get_children())
        



    def DibujarLista(self,ref, positionX, positionY, rowsQuantity, full):
        self.lista = ttk.Treeview(self.ventana_Ingresar_Persona, columns=(1,2,3,4,5), show = "headings", height=rowsQuantity)
        #estilo
        estilo= ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("Treeview.Heading", background="black", relief="flat", foreground="white")
        self.lista.heading(1, text="Fecha de nacimiento")
        self.lista.heading(2, text="Nombre")
        self.lista.heading(3, text="Rut")
        self.lista.heading(4, text="Sexo")
        self.lista.heading(5, text="Deportista")
        self.lista.column(1, anchor=CENTER, width="140")
        self.lista.column(2, anchor=CENTER, width="100")
        self.lista.column(3, anchor=CENTER, width="80")
        self.lista.column(4, anchor=CENTER, width="80")
        self.lista.column(5, anchor=CENTER, width="80")

        if full == True:
            #fill list
            d = Data()
            element = d.returnAllElements()#AQUI RECIBO UNA CONSULTA A BD
            for i in element:
                self.lista.insert('', 'end', values=i)
            
        
        else:
            d = Data()#llamo la clase 'Data'() de database.py
            element = d.ReturnRut(ref)#AQUI RECIBO UNA CONSULTA A BD
            for i in element:#recorro la lista
                self.lista.insert('', 'end', values=i)#inserto desde la bd
                
            if(element):
                #evento doble clic
                self.btn_calcularIMC= Button(self.ventana_Ingresar_Persona, text="Calcular IMC", relief="flat", background="#0051c8",cursor="hand1", foreground="white", command=lambda: self.obtenerFila()).place(x=550, y=75, width=90)
            else:
                self.btn_calcularIMC= Button(self.ventana_Ingresar_Persona, text="Calcular IMC", relief="flat", background="#0051c8",cursor="hand1", foreground="white", state="disabled", command=lambda: self.obtenerFila()).place(x=550, y=75, width=90)

        self.lista.place(x=positionX, y=positionY)

        
        



    def DibujarBuscarPersona(self):
        self.ventana_Ingresar_Persona = Toplevel(self.ventana)
        self.ventana_Ingresar_Persona.geometry("700x250")
        self.ventana_Ingresar_Persona.config(background= "#348781")
        self.ventana_Ingresar_Persona.title("Busqueda de Persona")
        self.ventana_Ingresar_Persona.wm_transient(self.ventana)
        self.DibujarLista(" ", 50, 50, 1, False)
        self.buscar_x=StringVar()
        self.txt_buscar =Entry(self.ventana_Ingresar_Persona, font=('arial', 12), textvariable=self.buscar_x).place(x=100, y=120)
        
        self.btn_buscar= Button(self.ventana_Ingresar_Persona, text="Buscar", relief="flat", background="#0051c8",cursor="hand1", foreground="white", command=lambda: self.buscarPersona(self.buscar_x.get())).place(x=300, y=119, width=90)
        self.btn_calcularIMC= Button(self.ventana_Ingresar_Persona, text="Calcular IMC", relief="flat", background="#0051c8",cursor="hand1", foreground="white", state="disabled", command=lambda: self.buscarPersona(self.buscar_x.get())).place(x=550, y=75, width=90)



    def obtenerFila(self):
        na= StringVar()
        estatura= DoubleVar()
        peso= IntVar()
        fecha= StringVar()
        IMC= StringVar()
        #NombreFila=self.lista.identify_row(event.y)        
        elemento = self.lista.item('I001')
        #1
        n= elemento['values'][2]#accedo al rut #tengo que acceder a u parametro existente ¿¿¿???? creo...
        na.set(n)#text variable la lleno con n que es el rut que obtuve de la fila seleccionada
        #2
        n5= elemento['values'][5]
        estatura.set(n5)
        #3
        n6= elemento['values'][6]
        peso.set(n6)
        #4
        n7= elemento['values'][7]
        fecha.set(n7)
        #5
        n8= elemento['values'][8]
        
        IMC.set(n8)

        nombre = elemento['values'][1]

        fecha_nacimiento = elemento['values'][0]

        sexo = elemento ['values'][3]
        
        pop= Toplevel(self.ventana)
        pop.geometry("500x300")

        Label(pop, text="Rut").place(x=100, y=40)
        Label(pop, text="Estatura").place(x=100, y=60)
        Label(pop, text="Peso").place(x=100, y=80)
        Label(pop, text="IMC").place(x=100, y=100)
        txt_n=Label(pop, textvariable=na).place(x=180, y=40)
        txt_n=Entry(pop, textvariable=estatura).place(x=180, y=60)
        txt_n=Entry(pop, textvariable=peso).place(x=180, y=80)
        txt_n=Entry(pop, textvariable=IMC).place(x=180, y=100)
        
        
        #botones
        btn_cambiar = Button(pop, text= "Calcular", relief="flat", bg="GREEN", foreground="white", command=lambda:self.editar(fecha_nacimiento, n, na.get(),nombre, sexo, estatura.get(),peso.get(),fecha.get())).place(x=180, y=160, width="120")

    def editar(self, fecha_nacimiento, n,na, nombre, sexo, estatura,peso,fecha):
        IMC = calcular_imc(estatura, peso)
        edad = calcular_edad(fecha_nacimiento)
        interpretacion = interpretar_imc(sexo, IMC)
        d=Data()
        arr=[n,na, estatura,peso,fecha,IMC]
        print(arr)
        d.UpdateItem(arr, n)
        mensaje = "Ha calculado su IMC con exito:\n\nRut:  "+na+"\nNombre:  "+nombre+"\nEdad:  "+str(edad)+"\nEstatura:  "+str(estatura)+"\nPeso:  "+str(peso)+"\nIMC:  "+str(IMC)+"\nEvaluacion:  "+interpretacion
        tk.messagebox.showinfo(title="IMC calculado", message=mensaje)

    

root = Tk()
root.title("IMC app")
root.geometry("1000x400")
root.config(background= "#348781")
aplicacion= App(root)
root.mainloop()