from tkinter import *
from tkinter import messagebox
import time 
from baseDatos import *
from archivo import *

class Ventana():
    colorFondo = "#007"
    colorLetra = "#fff"

    # Constructor
    def __init__(self):
        ANCHO = 400
        ALTO = 360
        global colorFondo
        global colorLetra

        self.tituloVentana = "Ventas"
        self.anchoAlto = f"{ANCHO}x{ALTO}"
        self.ventana = Tk()
        self.ventana.geometry(self.anchoAlto)
        self.ventana.title(self.tituloVentana)
        self.ventana.configure(background = self.colorFondo)

        # Componentes
        self.componentes(self.ventana)

        # Borrado o Inicio
        self.borrar()
        self.dameFechaActual()

        # Ejecución ventana
        self.ventana.mainloop()
    
    def componentes(self, ventana):
        global colorFondo
        global colorLetra
        

        self.efectivo01 = DoubleVar(value = '0.0')
        self.tarjetas01 = DoubleVar(value = '0.0')
        self.ventasTi01 = DoubleVar(value = '0.0')
        
        self.efectivo02 = DoubleVar(value = '0.0')
        self.tarjetas02 = DoubleVar(value = '0.0')
        self.ventasTi02 = DoubleVar(value = '0.0')
        
        self.efectivo03 = DoubleVar(value = '0.0')
        self.tarjetas03 = DoubleVar(value = '0.0')
        self.ventasTi03 = DoubleVar(value = '0.0')

        self.fecha = StringVar(value = '00/00/00')

        # Campo fecha
        etFecha = Label(self.ventana, text = "Fecha (dd/mm/YY)", bg =self.colorFondo, fg = self.colorLetra).place(x = 2, y = 15)
        cjFecha = Entry(self.ventana, textvariable = self.fecha).place(x = 140, y = 15, width = 60)

        # Etiquetas cajas / ventana / tiendas
        etEfectivo = Label(self.ventana, text = "Efectivo", bg = self.colorFondo, fg = self.colorLetra).place(x= 20, y = 70)
        etTarjetas = Label(self.ventana, text = "Tarjetas", bg = self.colorFondo, fg = self.colorLetra).place(x= 20, y = 100)
        etTotal = Label(self.ventana, text = "Total", bg = self.colorFondo, fg = self.colorLetra).place(x= 20, y = 130)

        # Tienda 01
        etTienda01 = Label(self.ventana, text = "Tienda 01", bg = self.colorFondo, fg = self.colorLetra).place(x = 90, y = 40)
        cjEfectivo01 = Entry(self.ventana, textvariable = self.efectivo01).place(x = 90, y = 70, width = 70)
        cjTarjetas01 = Entry(self.ventana, textvariable = self.tarjetas01).place(x = 90, y = 100, width = 70)
        cjTotal01 = Entry(self.ventana, textvariable = self.ventasTi01, state = "disabled").place(x = 90, y = 130, width = 70)
        
        # Tienda 02
        etTienda02 = Label(self.ventana, text = "Tienda 02", bg = self.colorFondo, fg = self.colorLetra).place(x = 180, y = 40)
        cjEfectivo02 = Entry(self.ventana, textvariable = self.efectivo02).place(x = 180, y = 70, width = 70)
        cjTarjetas02 = Entry(self.ventana, textvariable = self.tarjetas02).place(x = 180, y = 100, width = 70)
        cjTotal02 = Entry(self.ventana, textvariable = self.ventasTi02, state = "disabled").place(x = 180, y = 130, width = 70)

        # Tienda 03
        etTienda03 = Label(self.ventana, text = "Tienda 03", bg = self.colorFondo, fg = self.colorLetra).place(x = 270, y = 40)
        cjEfectivo03 = Entry(self.ventana, textvariable = self.efectivo03).place(x = 270, y = 70, width = 70)
        cjTarjetas03 = Entry(self.ventana, textvariable = self.tarjetas03).place(x = 270, y = 100, width = 70)
        cjTotal03 = Entry(self.ventana, textvariable = self.ventasTi03, state = "disabled").place(x = 270, y = 130, width = 70)

        btnGuardar = Button(self.ventana, text = "Guardar", command = self.guardar, bg = self.colorFondo, fg = self.colorLetra).place(x = 120, y = 160)
        btnBorrar = Button(self.ventana, text = "Borrar", command = self.borrar, bg = self.colorFondo, fg = self.colorLetra).place(x = 200, y = 160)

        self.fecha01 = StringVar(value = '00')
        self.fecha02 = StringVar(value = '00')

        etInformacion = Label(self.ventana, text = "Ventas entre fechas indicadas", bg = self.colorFondo, fg = self.colorLetra).place(x = 20, y = 220)
        etFecha01 = Label(self.ventana, text = "Fecha inicial", bg = self.colorFondo, fg = self.colorLetra).place(x = 20, y = 260)
        cjFecha01 = Entry(self.ventana, textvariable = self.fecha01).place(x = 100, y = 260, width = 70)
        etFecha02 = Label(self.ventana, text = "Fecha inicial", bg = self.colorFondo, fg = self.colorLetra).place(x = 20, y = 300)
        cjFecha02 = Entry(self.ventana, textvariable = self.fecha01).place(x = 100, y = 300, width = 70)

        btnMostrar = Button(self.ventana, text = "Mostrar", command = self.mostrar, bg = self.colorFondo, fg = self.colorLetra).place(x = 180, y = 280)
    
    def guardar(self):
        self.ventasTi01.set(self.efectivo01.get() + self.tarjetas01.get())
        self.ventasTi02.set(self.efectivo02.get() + self.tarjetas02.get())
        self.ventasTi03.set(self.efectivo03.get() + self.tarjetas03.get())

        self.fechaActual = self.fecha.get()

        datos = [
            (self.fechaActual, "Tienda01", self.efectivo01.get(), self.tarjetas01.get(), self.ventasTi01.get()),
            (self.fechaActual, "Tienda02", self.efectivo02.get(), self.tarjetas02.get(), self.ventasTi02.get()),
            (self.fechaActual, "Tienda03", self.efectivo03.get(), self.tarjetas03.get(), self.ventasTi03.get())
        ] 
        insertarDatos(datos)

    def borrar(self):
        self.fecha.set("00/00/00")
        self.fecha01.set("00/00/00")
        self.fecha02.set("00/00/00")

        self.efectivo01.set(0.0)
        self.tarjetas01.set(0.0)
        self.ventasTi01.set(0.0)
        
        self.efectivo02.set(0.0)
        self.tarjetas02.set(0.0)
        self.ventasTi02.set(0.0)
 
        self.efectivo03.set(0.0)
        self.tarjetas03.set(0.0)
        self.ventasTi03.set(0.0)
 
    def mostrar(self):
        ventaTiendas = dameVentas(self.fecha01.get(), self.fecha02.get())
        fecha = self.fecha.get()
        if ventaTiendas != {}:
            messagebox.showinfo("Ventas", ventaTiendas)
            texto = ''
            for clave, valor in ventaTiendas.items():
                texto = "\n" + texto + clave + ":" +str(valor)+"\n"
            archivar("D:\\Casa\\Base de datos\\SQLite con Python\\SQLite_Python\\tareaEjercicio_RegistroVentasDiarias\\registroVentasDiariasSolucion\\consulta", fecha, texto)
        else:
            messagebox.showerror("Aviso", "No hay datos, revisa la fecha")
        texto = ''
        registros = dameRegistros()
        for linea in registros:
            texto = texto + "\n" + str(linea) + "\n"
        archivar("D:\\Casa\\Base de datos\\SQLite con Python\\SQLite_Python\\tareaEjercicio_RegistroVentasDiarias\\registroVentasDiariasSolucion\\registros", fecha, texto)

    def dameFechaActual(self):
        diaAct = time.strftime("%d")
        mesAct = time.strftime("%m")
        añoAct = time.strftime("%y")
        fechaAct = diaAct+"/"+mesAct+"/"+añoAct
        self.fecha.set(fechaAct)
        self.fecha01.set(fechaAct)
        self.fecha02.set(fechaAct)

if __name__ == "__main__":
    ventana = Ventana()