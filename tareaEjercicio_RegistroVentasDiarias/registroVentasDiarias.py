import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class registroVentasDiaras:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de Ventas Diarias")
        self.master.geometry("600x400")

        self.conn = sqlite3.connect('D:\\Casa\\Base de datos\\SQLite con Python\\SQLite_Python\\tareaEjercicio_RegistroVentasDiarias\\ventas.db')
        self.crear_tabla()

        self.fecha = tk.StringVar()
        self.tienda = tk.StringVar()
        self.monto = tk.DoubleVar()

        self.crear_widgets()

    def crear_tabla(self):
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
        main_frame = ttk.Frame(self.master, padding = "10")
        main_frame.grid (row = 0, column = 0, sticky = (tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text = "Fecha (YYYY-MM-DD):").grid(row = 0, column = 0, sticky = tk.W, pady = 5)
        ttk.Entry(main_frame, textvariable = self.fecha).grid(row = 0, column = 1, pady = 5)

        ttk.Label(main_frame, text = "Tienda").grid(row = 1, column = 0, sticky = tk.W, pady = 5)
        ttk.Combobox(main_frame, textvariable = self.tienda, values = ["Tienda 1", "Tienda 2", "Tienda 3"]).grid(row = 1, column = 1, pady = 5)

        ttk.Label(main_frame, text = "Monto:").grid(row = 2, column = 0, sticky = tk.W, pady = 5)
        ttk.Entry(main_frame, textvariable = self.monto).grid(row = 2, column = 1, pady = 5)

        ttk.Button(main_frame, text = "Grabar", command = self.grabar_ventas).grid(row = 3, column = 0, pady = 10)
        ttk.Button(main_frame, text = "Borrar datos", command = self.borrar_datos).grid(row = 3, column = 1, pady = 10)
        ttk.Button(main_frame, text = "Consultar", command = self.consultar_ventas).grid(row = 4, column = 0, columnspan = 2, pady = 10)

        self.resultado_text = tk.Text(main_frame, height = 10, width = 50)
        self.resultado_text.grid(row = 5, column = 0, columnspan = 2, pady = 10)

    def grabar_ventas(self):
        try:
            fecha = self.fecha.get()
            tienda = self.tienda.get()
            monto = self.monto.get()

            if not fecha or not tienda or not monto:
                raise ValueError("Todos los campos son obligatorios")
                
            datetime.strptime(fecha, "%Y-%m-%d")

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
        self.fecha.set("")
        self.tienda.set("")
        self.monto.set(0.0)

    def consultar_ventas(self):
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
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = registroVentasDiaras(root)
    root.mainloop()
