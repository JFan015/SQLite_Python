import sqlite3

def conectar():
    con = sqlite3.connect('ventasTiendas.db')
    cursor = con.cursor()
    return con, cursor

def crearTabla():
    con, cursor  = conectar()
    sentencia = """
        CREATE TABLE IF NOT EXISTS ventas (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "fecha" DATE NOT NULL,
            "tienda" TEXT NOT NULL,
            "efectivo" REAL NOT NULL,
            "tarjeta" REAL NOT NULL,
            "total" REAL NOT NULL
        )
    """
    cursor.execute(sentencia)
    con.close()

def insertarDatos(datos):
    con, cursor = conectar()
    sentencia = "INSERT INTO ventas VALUES (NULL, ?, ?, ?, ?, ?)"
    cursor.executemany(sentencia, datos)
    con.commit()
    con.close()
    print("Datos insertados")

def dameVentas(fechaIni, fechaFin):
    sentencia = "SELECT tienda, SUM(total) as TotalVenta FROM ventas WHERE (fecha >=\"" + fechaIni + "\") AND (fecha <= \""+fechaFin+"\") GROUP BY tienda"
    con, cursor = conectar()
    cursor.execute(sentencia)
    ventaTienda = {}
    for linea in cursor:
        ventaTienda[linea[0]] = linea[1]
    return ventaTienda