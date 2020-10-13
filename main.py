"""
10/13/2020
Quieres ser mi novia by felipedelosh

Es una interfaz grafica de broma:

Se pregunta: Quieres ser mi novia?
y hay 2 botones [si] [no]
Cuando se intenta clickear no el boton cambia de posicion 
"""

from tkinter import * # Esto se encarga de la interfaz grafica
import random # Esto se encarga de los numeros aleatoreos

class Software:
    def __init__(self):
        self.pantalla = Tk() # Esta es la pantalla principal
        self.tela = Canvas(self.pantalla, width=640, height=480, bg='snow') # Aqui se pintan las cosas
        self.lblMensaje = Label(self.tela, text="Quieres ser mi novia?")
        self.btnSi = Button(self.tela, width=10, text="SI")
        self.btnNo = Button(self.tela, width=10, text="NO")
        self.btnNo.bind('<Enter>', self.cambiarPosicionDeBotonNo)
        self.mostrarPantalla() # Se configuran y se muestran las cosas


    def mostrarPantalla(self):
        self.pantalla.title("Porfaaaaa <3")
        self.pantalla.geometry("640x480")
        self.lblMensaje.place(x=250, y=100)
        self.btnSi.place(x=150, y=300)
        self.btnNo.place(x=400, y=300)
        self.tela.place(x=0, y=0)
        self.pantalla.mainloop()

    def cambiarPosicionDeBotonNo(self, event):
        """
        Si se pasa por encima del boton No con el mouse se cambia
        """
        posx = random.randint(100, 600)
        posy = random.randint(50, 400)

        self.btnNo.place(x=posx, y=posy)


s = Software()