from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#-------funciones------------------------------------

def conexionBBDD():
    miConexion=sqlite3.connect("Lavados.db")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSLAVADOS (
            BOLETA VARCHAR(50),
            NOMBRE VARCHAR(50),
            TELEFONO VARCHAR(50),
            CANTIDAD VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
    
        messagebox.showinfo("BDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("Atencion", "La BBDD ya existe")


def salirAplicacion():
    valor=messagebox.askquestion("Salir", "Desea salir de la aplicación?")
    if valor=="yes":
        raiz.destroy()

def limpiarCampos():
    miBoleta.set("")
    miNombre.set("")
    miTel.set("")
    miCant.set("")
    txt.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("Lavados.db")
    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO DATOSLAVADOS VALUES('" + miBoleta.get() +
        "','" + miNombre.get() +
        "','" + miTel.get() +
        "','" + miCant.get() +
        "','" + txt.get("1.0", END) + "')")
    miConexion.commit()
    messagebox.showinfo("BDD","Registrado")


#-----------------------------------------------------

raiz  = Tk()
raiz.title("Lavanderia Marite")
raiz.geometry("650x300")

#----------Barra de Menu--------------------
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="conectar", command = conexionBBDD )
bbddMenu.add_command(label="salir", command = salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="crear", command=crear)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")


miframe = Frame()
miframe.pack(fill="both",expand="True")

miframe.config(bg="white")
miframe.config(width="650",height="350")
miframe.config(bd=10)
miframe.config(relief="groove")

#--------------Campos---------------------------

miBoleta=StringVar()
miNombre=StringVar()
miTel=StringVar()
miCant=StringVar()

BoletaLabel = Label (miframe, text = "Boleta :")
BoletaLabel.grid(row = 0, column = 0, padx = 10, pady = 2)
BoletaCuadro = Entry(miframe, textvariable=miBoleta )
BoletaCuadro.grid(row = 1, column = 0, padx = 10, pady = 2)
BoletaCuadro.config(fg = "red", justify ="left")

NombreLabel = Label (miframe, text = "Nombre :")
NombreLabel.grid(row = 0, column = 1, padx = 10, pady = 2)
NombreCuadro = Entry(miframe, textvariable=miNombre )
NombreCuadro.grid(row = 1, column = 1, padx = 10, pady = 2)
NombreCuadro.config( justify ="left")

TelLabel= Label (miframe, text = "Telefono :")
TelLabel.grid(row = 0, column = 2, padx = 10, pady = 2)
TelCuadro= Entry(miframe, textvariable=miTel )
TelCuadro.grid(row = 1, column = 2, padx = 10, pady = 2)
TelCuadro.config( justify ="left")

CantLabel= Label (miframe, text = "Cantidad :")
CantLabel.grid(row = 2, column = 0, padx = 10, pady = 2)
CantCuadro= Entry(miframe, textvariable=miCant )
CantCuadro.grid(row = 3, column = 0, padx = 10, pady = 2)
CantCuadro.config( justify ="left")

txt = scrolledtext.ScrolledText(miframe,width=20,height=10)
txt.grid(column=1,row=3)

RegBtn = Button(miframe, text="Registrar", command=crear) 
RegBtn.grid(column=2, row=4)
BusBtn = Button(miframe, text="Buscar") 
BusBtn.grid(column=3, row=4)
BorrarBtn = Button(miframe, text="Borrar ", command=limpiarCampos) 
BorrarBtn.grid(column=3, row=5)




chk_pago = BooleanVar()
chk_pago.set(False) #set check state
chkpago = Checkbutton(miframe, text='Pago', var=chk_pago)
chkpago.grid(column=2, row=3)

chk_recogio = BooleanVar()
chk_recogio.set(False) #set check state
chkrecogio = Checkbutton(miframe, text='Recogio', var=chk_recogio)
chkrecogio.grid(column=3, row=3)


barraMenu.add_cascade(label="BDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

raiz.mainloop()

