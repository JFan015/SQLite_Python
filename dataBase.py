import sqlite3  # Importamos la librería SQLite para poder acceder a todas sus funcionalidades relacionadas con bases de datos.

def conectar():
    try:
        # Establecemos una conexión con la base de datos 'pruebas.db'.
        # Si la base de datos no existe, SQLite lo creará automáticamente.
        con = sqlite3.connect('pruebas.db') 
        # Alternativa: usar ':memory:' en lugar de 'pruebas.db' para crear una base de datos temporal en memoria
        # con = sqlite3.connect(':memory:')   
        # Esto crearía una base de datos temporal que solo existe en la RAM, útil para pruebas o procesamiento temporal

        # Creamos un objeto cursor que nos permitirá ejecutar comandos SQL en la base de datos.
        cursor = con.cursor()
        # Retornamos tanto la conexión como el cursor para su uso posterior.
        return con,cursor
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None, None

def crearTabla(conexion, cursor):
    # Definimosla sentencia SQL para crear la tabla 'usuarios'.
    # La cláusula IF NOT EXISTS evita errores si la tabla ya existe
    sentencia = """
        CREATE TABLE IF NOT EXISTS usuarios
        (ID INTEGER PRIMARY KEY NOT NULL,
        USUARIO TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        CLAVE TEXT NOT NULL);
    """
    # Ejecutamos la sentencia SQL para crear la tabla
    cursor.execute(sentencia)

    # Cerramos la conexión a la base de datos
    
    conexion.close()
    print('Tabla creada correctamente')

if __name__ == '__main__':
    # Verificamos si este script se está ejecutando directamente.
    # Esto es útil para evitar que el código se ejecute si se importa como módulo en otro script.
    con,cursor = conectar() # Llamamos la función conectar y almacenamos los objetos retornados
    # print(con)  # Imprimimos el objeto de conexión para verificar que se ha establecido correctamente.
    # print(cursor)   # Imprimimos el objeto cursor para confirmar que está listo para ejecutar comandos SQL.
    
    # Llamamos a la función para crear la tabla
    crearTabla(con, cursor)