import os
from tkinter import messagebox

def archivar(nombreArchivo, fecha, texto):
    try:
        archivo = nombreArchivo + ".txt"
        escritura = open(archivo,"w")
        fechaTexto = fecha
        escritura.write(fechaTexto)
        escritura.write(texto)
        escritura.close()
    except:
        textoMensaje = "Error con el archivo de texto"
        messagebox.showerror("Error en el archivo", textoMensaje)

if __name__ == "__main__":
    texto = "Esto es una prueba"
    archivar("D:\\Casa\\Base de datos\\SQLite con Python\\SQLite_Python\\tareaEjercicio_RegistroVentasDiarias\\registroVentasDiariasSolucion\\pruebas", "08/02/2025", texto)