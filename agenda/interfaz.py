import tkinter as tk
from tkinter import messagebox

class AgendaGUI:
    def __init__(self, raiz, controlador_db):
        self.raiz = raiz
        self.raiz.title("Agenda de contactos")
        self.db = controlador_db

        # Crear widgets
        self.etiqueta_nombre = tk.Label(raiz, text = "Nombre: ")
        self.entrada_nombre = tk.Entry(raiz)
        self.etiqueta_telefono = tk.Label(raiz, text = "Teléfono")
        self.entrada_telefono = tk.Entry(raiz)
        self.boton_agregar = tk.Button(raiz, text = 'Agregar contactos', command = self.agregar_contactos)
        self.boton_listar = tk.Button(raiz, text = 'Listar contactos', command = self.listar_contactos)
        