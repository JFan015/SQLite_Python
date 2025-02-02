import sqlite3

def conectar():
    conexion = sqlite3.connect('articulos.db')
    cursor = conexion.cursor
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS ARTICULOS (IDENTIFICADOR INT PRIMARY KEY, NOMBRE VARCHAR(20), CANTIDAD INT, IMPORTE FLOAT TEXT)')