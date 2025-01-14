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

def insertarDatos(conexion, cursor, datos):
    # Definimos la sentencia SQL para insertar datos.
    # Usamos ? como marcadores de posición para los valores
    sentencia = "INSERT INTO usuarios VALUES (NULL,?,?,?)"

    try:
        # Usamos executemany para insertar múltiples filas de datos
        cursor.executemany(sentencia,datos)

        # Confirmamos los cambios en la base de datos
        conexion.commit()
        print("Datos insertados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")
        conexion.rollback() # Revertimos los cambios si algo salió mal
    finally:    # Cerramos la conexión, asegurándonos de que siempre se cierre, incluso si ocurre una excepción
        conexion.close()

def consultarDatos01(conexion, cursor):
    # Consulta de todos los usuarios de la tabla
    sentencia = "SELECT * FROM usuarios"
    resultado = cursor.execute(sentencia)
    #print(cursor.fetchall()) #Imprime todo los resultados de una
    for fila in resultado:
        print(fila) # Imprime por consola cada fila individualmente

def consultarDatos(conexion, cursor):
    sentencia = "SELECT id, usuario, email FROM usuarios LIMIT 2"   
    resultado = cursor.execute(sentencia)
    #conexion.close()
    return resultado

def consultarDatos_ID(conexion, cursor, id):
    sentencia = f"SELECT usuario, email FROM usuarios WHERE id = {id}"
    resultado = cursor.execute(sentencia)
    return resultado

if __name__ == '__main__':
    # Obtenemos la conexión y el cursor
    con,cursor = conectar() # Llamamos la función conectar y almacenamos los objetos retornados

    if con is not None and cursor is not None:
        # Definimos los datos a insertar
        datos = [('ANTONIO','ANTONIO1234@GMAIL.COM','233JK'),
                ('ALBERTO','ALBERTO1234@GMAIL.COM','AEO12')]
        # Llamamos a la función para insertar datos
        #insertarDatos(con, cursor, datos)
        resultado = consultarDatos(con, cursor)
        for fila in resultado:
            print("*"*100)
            print("\n")
            print("ID: " ,fila[0])
            print("Nombre: " ,fila[1])
            print("Email_, " ,fila[2])
            print("\n")
    
        resultado = consultarDatos_ID(con, cursor, 15)
        print(resultado)
        for fila in resultado:
            print(fila)
    else:
        print("No se pudo establecer la conexión a la base de datos.")