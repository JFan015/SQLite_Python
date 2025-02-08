import sqlite3

def conectar():
    con = sqlite3.connect('D:\\Casa\\Base de datos\\SQLite con Python\\SQLite_Python\\tareaEjercicio_RegistroVentasDiarias\\registroVentasDiariasSolucion\\ventasTiendas.db')
    cursor = con.cursor()
    # print("Conexión realizada")
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
    # print("Tabla creada.")

def insertarDatos(datos):
    con, cursor = conectar()
    sentencia = "INSERT INTO ventas VALUES (NULL, ?, ?, ?, ?, ?)"
    cursor.executemany(sentencia, datos)
    con.commit()
    con.close()
    # print("Datos insertados")

def dameVentas(fechaIni, fechaFin):
    sentencia = "SELECT tienda, SUM(total) as TotalVenta FROM ventas WHERE (fecha >=\"" + fechaIni + "\") AND (fecha <= \""+fechaFin+"\") GROUP BY tienda"
    con, cursor = conectar()
    cursor.execute(sentencia)
    ventaTienda = {}
    for linea in cursor:
        ventaTienda[linea[0]] = linea[1]
    return ventaTienda

def dameRegistros():
    sentencia = "SELECT * FROM ventas"
    conexion, cursor = conectar()
    cursor.execute(sentencia)
    return cursor

if __name__ == '__main__':
    conectar()
    crearTabla()
    datos = [
        ('08/02/2025', 'Tienda01', 1500, 1000, 2500), 
        ('09/03/2026', 'Tienda02', 2500, 1000, 3500),
    ]
    insertarDatos(datos)
    print(dameVentas('07/02/2025', '10/03/2026'))
    registros = dameRegistros()
    for linea in registros:
        print(linea)
