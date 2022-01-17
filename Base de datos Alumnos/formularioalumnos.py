from ast import Try
import sqlite3
from sre_parse import State
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from tkinter import *
import alumnos

class FormularioAlumnos:
    def __init__(self):
        self.alumno1=alumnos.Alumnos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Base de datos Alumnos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)       
        self.carga_alumnos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.anexo_Alumnos()
        self.listar_dni
        self.ventana1.iconbitmap('C:\\Users\\nico\\Desktop\\Proyecto\\Aplicaciones Gise\\Base de datos Alumnos\\logo.ico')
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.resizable(0,0)
        self.ventana1.mainloop()

    
    #Funcion de Carga de alumnos
    def carga_alumnos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Alumnos")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #Cuadro de entrada y visual Nombre
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombrecarga=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
        #Cuadro de entrada y visual apellido
        self.label2=ttk.Label(self.labelframe1, text="Apellido:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.apellidocarga=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe1, textvariable=self.apellidocarga)
        self.entryapellido.grid(column=1, row=1, padx=4, pady=4)
        #Cuadro de entrada y visual dni
        self.label3=ttk.Label(self.labelframe1, text="DNI:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.DNIcarga=tk.StringVar()
        self.entryDNI=ttk.Entry(self.labelframe1, textvariable=self.DNIcarga)
        self.entryDNI.grid(column=1, row=2, padx=4, pady=4)
        #Cuadro de entrada y visual fecha de nacimiento
        self.label4=ttk.Label(self.labelframe1, text="Fecha Nacimiento:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.nacimientocarga=tk.StringVar()
        self.entrynacimiento=ttk.Entry(self.labelframe1, textvariable=self.nacimientocarga)
        self.entrynacimiento.grid(column=1, row=3, padx=4, pady=4)
        #Cuadro de entrada y visual direccion
        self.label5=ttk.Label(self.labelframe1, text="Direccion:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.direccioncarga=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe1, textvariable=self.direccioncarga)
        self.entrydireccion.grid(column=1, row=4, padx=4, pady=4)
        #Cuadro de entrada y visual telefono
        self.label6=ttk.Label(self.labelframe1, text="Telefono:")        
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.telefonocarga=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe1, textvariable=self.telefonocarga)
        self.entrytelefono.grid(column=1, row=5, padx=4, pady=4)
        #Cuadro de entrada y visual mail
        self.label7=ttk.Label(self.labelframe1, text="Mail:")        
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.mailcarga=tk.StringVar()
        self.entrymail=ttk.Entry(self.labelframe1, textvariable=self.mailcarga)
        self.entrymail.grid(column=1, row=6, padx=4, pady=4)
        #Boton Agregar
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)
    
    #Funcion de agregar los datos ingresados a la base de datos
    def agregar(self):
        datos=(self.nombrecarga.get(), self.apellidocarga.get(), self.DNIcarga.get(), self.nacimientocarga.get(), self.direccioncarga.get(), self.telefonocarga.get(), self.mailcarga.get())
        try:
            self.alumno1.alta(datos)
            mb.showinfo("Información", "Los datos fueron cargados")
        except sqlite3.IntegrityError:
            mb.showinfo('Informacion','El DNI ingresado ya existe')
        self.nombrecarga.set("")
        self.apellidocarga.set("")
        self.DNIcarga.set("")
        self.nacimientocarga.set("")
        self.direccioncarga.set("")
        self.telefonocarga.set("")
        self.mailcarga.set("")
        


    #Funcio Consultar por codigo
    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por DNI")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Alumno")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        #Cuadro de entrada y visual Codigo
        self.label1=ttk.Label(self.labelframe2, text="DNI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.dni=tk.StringVar()
        self.entrydni=ttk.Entry(self.labelframe2, textvariable=self.dni)
        self.entrydni.grid(column=1, row=0, padx=4, pady=4)
        #Cuadro de entrada y visual Nombre
        self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        #Cuadro de entrada y visual Apellido
        self.label3=ttk.Label(self.labelframe2, text="Apellido:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.apellido=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe2, textvariable=self.apellido, state="readonly")
        self.entryapellido.grid(column=1, row=2, padx=4, pady=4)
        #Cuadro de entrada y visual Fecha de nacimiento
        self.label5=ttk.Label(self.labelframe2, text="Fecha Nacimiento:")        
        self.label5.grid(column=0, row=3, padx=4, pady=4)
        self.nacimiento=tk.StringVar()
        self.entrynacimiento=ttk.Entry(self.labelframe2, textvariable=self.nacimiento, state="readonly")
        self.entrynacimiento.grid(column=1, row=3, padx=4, pady=4)
        #Cuadro de entrada y visual Direccion
        self.label6=ttk.Label(self.labelframe2, text="Direccion:")        
        self.label6.grid(column=0, row=4, padx=4, pady=4)
        self.direccion=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe2, textvariable=self.direccion, state="readonly")
        self.entrydireccion.grid(column=1, row=4, padx=4, pady=4)
        #Cuadro de entrada y visual Telefono
        self.label7=ttk.Label(self.labelframe2, text="Telefono:")        
        self.label7.grid(column=0, row=5, padx=4, pady=4)
        self.telefono=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe2, textvariable=self.telefono, state="readonly")
        self.entrytelefono.grid(column=1, row=5, padx=4, pady=4)
        #Cuadro de entrada y visual Mail
        self.label8=ttk.Label(self.labelframe2, text="Mail:")        
        self.label8.grid(column=0, row=6, padx=4, pady=4)
        self.mail=tk.StringVar()
        self.entrymail=ttk.Entry(self.labelframe2, textvariable=self.mail, state="readonly")
        self.entrymail.grid(column=1, row=6, padx=4, pady=4)
        #Boton Consultar
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

    #Funcion Consultar informacion de alumnos
    def consultar(self):
        datos=(self.dni.get(), )
        respuesta=self.alumno1.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][0])
            self.apellido.set(respuesta[0][1])
            self.nacimiento.set(respuesta[0][2])
            self.direccion.set(respuesta[0][3])
            self.telefono.set(respuesta[0][4])
            self.mail.set(respuesta[0][5])
        else:
            self.nombre.set('')
            self.apellido.set('')
            self.nacimiento.set('')
            self.direccion.set('')
            self.telefono.set('')
            self.mail.set('') 
            mb.showinfo("Información", "No existe un alumno con dicho DNI")

    #Funcion que muestra todos los alumnos 
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Alumno")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
    
    #Funcion que muestra todos los alumnos 
    def listar(self):
        respuesta=self.alumno1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "DNI:"+str(fila[0])+"\nnombre:"+fila[1]+"\napellido:"+str(fila[2])+
            "\nfecha_de_nacimiento:"+str(fila[3])+"\ndireccion:"+str(fila[4])+"\ntelefono:"+str(fila[5])+"\nmail:"+str(fila[6])+"\n\n")

    #Funcion para borra alumnos
    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de alumnos")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Alumno")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe4, text="DNI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.dniborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.dniborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    #Funcion que borra al alumno
    def borrar(self):
        datos=(self.dniborra.get(), )
        cantidad=self.alumno1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el alumno con dicho DNI")
        else:
            mb.showinfo("Información", "No existe un alumno con dicho DNI")

    #Fuincion para modificar alumno
    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar alumno")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Alumno")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        #Cuadro de entrada y visual Codigo
        self.label1=ttk.Label(self.labelframe5, text="DNI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.dnimod=tk.StringVar()
        self.entrydni=ttk.Entry(self.labelframe5, textvariable=self.dnimod)
        self.entrydni.grid(column=1, row=0, padx=4, pady=4)
        #Cuadro de entrada y visual Nombre
        self.label2=ttk.Label(self.labelframe5, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombremod=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe5, textvariable=self.nombremod)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        #Cuadro de entrada y visual Apellido
        self.label3=ttk.Label(self.labelframe5, text="Apellido:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.apellidomod=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe5, textvariable=self.apellidomod)
        self.entryapellido.grid(column=1, row=2, padx=4, pady=4)
        #Cuadro de entrada y visual fecha de nacimiento
        self.label5=ttk.Label(self.labelframe5, text="Fecha de Nacimiento:")        
        self.label5.grid(column=0, row=3, padx=4, pady=4)
        self.nacimientomod=tk.StringVar()
        self.entrynacimiento=ttk.Entry(self.labelframe5, textvariable=self.nacimientomod)
        self.entrynacimiento.grid(column=1, row=3, padx=4, pady=4)
        #Cuadro de entrada y visual direccion
        self.label6=ttk.Label(self.labelframe5, text="Direccion:")        
        self.label6.grid(column=0, row=4, padx=4, pady=4)
        self.direccionmod=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe5, textvariable=self.direccionmod)
        self.entrydireccion.grid(column=1, row=4, padx=4, pady=4)
        #Cuadro de entrada y visual telefono
        self.label7=ttk.Label(self.labelframe5, text="Telefono:")        
        self.label7.grid(column=0, row=5, padx=4, pady=4)
        self.telefonomod=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe5, textvariable=self.telefonomod)
        self.entrytelefono.grid(column=1, row=5, padx=4, pady=4)
        #Cuadro de entrada y visual mail
        self.label8=ttk.Label(self.labelframe5, text="Mail:")        
        self.label8.grid(column=0, row=6, padx=4, pady=4)
        self.mailmod=tk.StringVar()
        self.entrymail=ttk.Entry(self.labelframe5, textvariable=self.mailmod)
        self.entrymail.grid(column=1, row=6, padx=4, pady=4)
        #Boton consultar
        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)
        #Boton modificar
        self.boton1=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=8, padx=4, pady=4)

    #Funcion que modifica al alumno
    def modifica(self):
        datos=(self.nombremod.get(), self.apellidomod.get(), self.nacimientomod.get(), self.direccionmod.get(), self.telefonomod.get(), self.mailmod.get(), self.dnimod.get())
        cantidad=self.alumno1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el alumno")
        else:
            mb.showinfo("Información", "No existe un alumno con dicho DNI")    

    #Funcion para consultar modificaciones de alumnos
    def consultar_mod(self):
        datos=(self.dnimod.get(), )
        respuesta=self.alumno1.consulta(datos)
        if len(respuesta)>0:
            self.nombremod.set(respuesta[0][0])
            self.apellidomod.set(respuesta[0][1])
            self.nacimientomod.set(respuesta[0][2])
            self.direccionmod.set(respuesta[0][3])
            self.telefonomod.set(respuesta[0][4])
            self.mailmod.set(respuesta[0][5])
        else:
            self.nombremod.set('')
            self.apellidomod.set('')
            self.nacimientomod.set('')
            self.direccionmod.set('')
            self.telefonomod.set('')
            self.mailmod.set('')
            mb.showinfo("Información", "No existe un alumno con dicho DNI")

    #Funcion que muestra dni, nombre y apellido de todos los alumnos
    def anexo_Alumnos(self):
        self.pagina6 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina6, text="Anexo")
        self.labelframe6=ttk.LabelFrame(self.pagina6, text="Alumnos")
        self.labelframe6.grid(column=0, row=0, padx=5, pady=10)
        self.scrolledtext2=st.ScrolledText(self.labelframe6, width=60, height=15)
        self.scrolledtext2.grid(column=0,row=1, padx=10, pady=10)
        self.boton1=ttk.Button(self.labelframe6, text="Anexo", command=self.listar_dni)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)

    #Funcion que trae dni, nombre y apellido de todos los alumnos
    def listar_dni(self):
        respuesta2=self.alumno1.recuperar_todos()
        self.scrolledtext2.delete("1.0", tk.END)  
        for fila in respuesta2:
            self.scrolledtext2.insert(tk.END, "DNI:"+str(fila[0])+"\nnombre:"+str(fila[1])+"\napellido:"+str(fila[2])+"\n\n")
    

aplicacion1=FormularioAlumnos()