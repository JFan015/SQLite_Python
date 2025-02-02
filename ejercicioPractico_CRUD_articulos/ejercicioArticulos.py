import sqlite3

# Function to establish a connection with the database
def conectar():
    conexion = sqlite3.connect('D:\\Casa\\Base de datos\\SQLite con Python\\SQLite_Python\\ejercicioPractico_CRUD_articulos\\articulos.db')
    cursor = conexion.cursor()
    print("Conexión establecida con la base de datos con éxito.")
    return conexion, cursor

# Function to close the database connection
def cerrar_conexion(conexion):
    conexion.close()

# Function to create the ARTICULOS table if it doesn't exist
def crearTabla():
    conexion, cursor = conectar()
    # Define the table estructure
    cursor.execute('CREATE TABLE IF NOT EXISTS ARTICULOS (IDENTIFICADOR INT PRIMARY KEY, NOMBRE VARCHAR(20), CANTIDAD INT, IMPORTE FLOAT TEXT)')
    cerrar_conexion(conexion)
    print("Tabla creada correctamente en la base de datos")

# Function to permorf initial data load into the table
def carga_inicial():
    conexion, cursor = conectar()
    # List of tuples with articles data
    articulos = [
        (1235,"cuaderno",25,2.35),
        (1254,"boligrafo",100,0.90),
        (1345,"estuche",75,1.50)
    ]
    # Insert multiple records into the table
    cursor.executemany('INSERT INTO ARTICULOS VALUES (?,?,?,?)', articulos)
    conexion.commit()   # Confirm changes in database
    cerrar_conexion(conexion)

# Main program block
if __name__ == '__main__':
    crearTabla()
    carga_inicial()