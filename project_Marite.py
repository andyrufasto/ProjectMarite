from tkinter import *
from tkinter import scrolledtext
raiz  = Tk()
raiz.title("Lavanderia Marite")

raiz.geometry("650x650")

miframe = Frame()

miframe.pack(fill="both",expand="True")

miframe.config(bg="white")
miframe.config(width="650",height="350")
miframe.config(bd=10)
miframe.config(relief="groove")
#miframe.config(cursor="spider")

BoletaLabel = Label (miframe, text = "Boleta :")
BoletaLabel.grid(row = 0, column = 0, padx = 10, pady = 2)
BoletaCuadro = Entry(miframe )
BoletaCuadro.grid(row = 1, column = 0, padx = 10, pady = 2)
BoletaCuadro.config(fg = "red", justify ="left")

NombreLabel = Label (miframe, text = "Nombre :")
NombreLabel.grid(row = 0, column = 1, padx = 10, pady = 2)
NombreCuadro = Entry(miframe )
NombreCuadro.grid(row = 1, column = 1, padx = 10, pady = 2)
NombreCuadro.config( justify ="left")

TelLabel= Label (miframe, text = "Telefono :")
TelLabel.grid(row = 0, column = 2, padx = 10, pady = 2)
TelCuadro= Entry(miframe )
TelCuadro.grid(row = 1, column = 2, padx = 10, pady = 2)
TelCuadro.config( justify ="left")

CantLabel= Label (miframe, text = "Cantidad :")
CantLabel.grid(row = 2, column = 0, padx = 10, pady = 2)
CantCuadro= Entry(miframe )
CantCuadro.grid(row = 3, column = 0, padx = 10, pady = 2)
CantCuadro.config( justify ="left")

txt = scrolledtext.ScrolledText(miframe,width=20,height=10)
txt.grid(column=1,row=3)

btn = Button(miframe, text="Registrar") 
btn.grid(column=3, row=5)

chk_state = BooleanVar()
chk_state.set(False) #set check state
chk = Checkbutton(miframe, text='Pago', var=chk_state)
chk.grid(column=2, row=3)

raiz.mainloop()

