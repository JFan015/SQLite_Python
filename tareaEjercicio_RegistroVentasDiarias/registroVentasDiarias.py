'''
Aplicación GUI para registro y consulta de ventas diarias usando TKinter y SQLite

Módulo principal que define la interfaz gráfica y operaciones de base de datos
'''

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class registroVentasDiaras:
    '''Clase principal que gestiona la aplicación de registro de ventas.'''

    def __init__(self, master):
        '''Inicializa la ventana principal y configura la base de datos.'''
        self.master = master
        self.master.title("Registro de Ventas Diarias")
        self.master.geometry("600x400")

        # Conexión a la base de datos.
        self.conn = sqlite3.connect('D:\\Casa\\Base de datos\\SQLite con Python\\SQLite_Python\\tareaEjercicio_RegistroVentasDiarias\\ventas.db')
        self.crear_tabla()

        # Variables para almacenar datos del formulario
        self.fecha = tk.StringVar()
        self.tienda = tk.StringVar()
        self.monto = tk.DoubleVar()

        self.crear_widgets()

    def crear_tabla(self):
        '''Crear la tabla de ventas si no existe.'''
        cursor = self.conn.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS ventas
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         fecha TEXT,
                         tienda TEXT,
                         monto REAL)
                       ''')
        self.conn.commit()

    def crear_widgets(self):
        '''Construye la interfaz gráfica.'''
        main_frame = ttk.Frame(self.master, padding = "10")
        main_frame.grid (row = 0, column = 0, sticky = (tk.W, tk.E, tk.N, tk.S))

        # Sección de entrada de datos
        ttk.Label(main_frame, text = "Fecha (YYYY-MM-DD):").grid(row = 0, column = 0, sticky = tk.W, pady = 5)

        ttk.Entry(main_frame, textvariable = self.fecha).grid(row = 0, column = 1, pady = 5)

        # Combobox con selección de tiendas
        ttk.Label(main_frame, text = "Tienda").grid(row = 1, column = 0, sticky = tk.W, pady = 5)
        ttk.Combobox(main_frame, textvariable = self.tienda, values = ["Tienda 1", "Tienda 2", "Tienda 3"]).grid(row = 1, column = 1, pady = 5)

        # Entrada para monto numérico
        ttk.Label(main_frame, text = "Monto:").grid(row = 2, column = 0, sticky = tk.W, pady = 5)
        ttk.Entry(main_frame, textvariable = self.monto).grid(row = 2, column = 1, pady = 5)

        # Botones de acción
        ttk.Button(main_frame, text = "Grabar", command = self.grabar_ventas).grid(row = 3, column = 0, pady = 10)
        ttk.Button(main_frame, text = "Borrar datos", command = self.borrar_datos).grid(row = 3, column = 1, pady = 10)
        ttk.Button(main_frame, text = "Consultar", command = self.consultar_ventas).grid(row = 4, column = 0, columnspan = 2, pady = 10)

        # Área de resultado
        self.resultado_text = tk.Text(main_frame, height = 10, width = 50)
        self.resultado_text.grid(row = 5, column = 0, columnspan = 2, pady = 10)

    def grabar_ventas(self):
        '''Guarda la nueva venta en la base de datos'''
        try:
            # Validación de campos obligatorios
            fecha = self.fecha.get()
            tienda = self.tienda.get()
            monto = self.monto.get()

            if not fecha or not tienda or not monto:
                raise ValueError("Todos los campos son obligatorios")
            
            # Validación de formato de fecha
            datetime.strptime(fecha, "%Y-%m-%d")

            # Inserción en la base de datos
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO ventas (fecha, tienda, monto) VALUES (?, ?, ?)",
                               (fecha, tienda, monto))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Venta registrada correctamente")
            self.borrar_datos()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def borrar_datos(self):
        '''Limpia todos los campos del formulario'''
        self.fecha.set("")
        self.tienda.set("")
        self.monto.set(0.0)

    def consultar_ventas(self):
        '''Consulta ventas desde la fecha específica hacia delante'''
        try:
            fecha_inicio = self.fecha.get()
            if not fecha_inicio:
                raise ValueError("Ingresa una fecha de inicio para la consulta")
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM ventas WHERE fecha >= ? ORDER BY fecha", (fecha_inicio,))
            ventas = cursor.fetchall()

            self.resultado_text.delete(1.0, tk.END)
            if ventas:
                for venta in ventas:
                    self.resultado_text.insert(tk.END, f"Fecha: {venta[1]}, Tienda: {venta[2]}, Monto: {venta[3]}\n")
            else:
                self.resultado_text.insert(tk.END, "No se encontraron ventas para la fecha especificada.")
        except ValueError as e:
            messagebox.showerror("Error: " ,str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error en la cosulta: {str(e)}")
    
    def __del__(self):
        """Garantiza el cierre de la conexión a la base de datos al destruir la instancia"""
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = registroVentasDiaras(root)
    root.mainloop()
