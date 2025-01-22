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
    # Definimos la sentencia SQL para crear la tabla 'usuarios'.
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

def actualizarDatos(conexion, cursor, id, nombre):
    sentencia = f"UPDATE usuarios set usuario = '{nombre}' WHERE id = {id}"
    cursor.execute(sentencia)
    conexion.commit()
    print("\nDatos actualizados correctamente.\n")
    return True

def borrarDatos(conexion, cursor, id):
    sentencia = f"DELETE FROM usuarios WHERE id = {id}"
    cursor.execute(sentencia)
    conexion.commit()
    print("Se ha realizado el borrado del registro.")
    return True

def menu():
    print("Seleccione una opción:")
    print("1. Crear tabla")
    print("2. Insertar datos")
    print("3. Consultar todos los datos")
    print("4. Consultar datos con límite")
    print("5. Consultar datos por ID")
    print("6. Actualizar datos")
    print("7. Borrar datos")
    print("8. Salir")

if __name__ == '__main__':
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        con, cursor = conectar()

        if con is None or cursor is None:
            print("No se pudo conectar a la base de datos.")
            continue

        if opcion == '1':
            crearTabla(con, cursor)
        elif opcion == '2':
            # Definimos los datos a insertar
            datos = [('ANTONIO','ANTONIO1234@GMAIL.COM','233JK'),
                     ('ALBERTO','ALBERTO1234@GMAIL.COM','AEO12')]
            insertarDatos(con, cursor, datos)
        elif opcion == '3':
            consultarDatos01(con, cursor)
        elif opcion == '4':
            resultado = consultarDatos(con, cursor)
            for fila in resultado:
                print(fila)
        elif opcion == '5':
            id = input("Ingrese el ID: ")
            resultado = consultarDatos_ID(con, cursor, id)
            for fila in resultado:
                print(fila)
        elif opcion == '6':
            id = input("Ingrese el ID: ")
            nombre = input("Ingrese el nuevo nombre: ")
            actualizarDatos(con, cursor, id, nombre)
        elif opcion == '7':
            id = input("Ingrese el ID: ")
            borrarDatos(con, cursor, id)
        elif opcion == '8':
            break
        else:
            print("Opción no válida.")
    