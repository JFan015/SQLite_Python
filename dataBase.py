import sqlite3  # Importamos la librería SQLite para poder acceder a todas sus funcionalidades relacionadas con bases de datos.

def conectar():
    # Establecemos una conexión con la base de datos 'pruebas.db'.
    # Si la base de datos no existe, SQLite lo creará automáticamente.
    con = sqlite3.connect('pruebas.db')
    # Creamos un objeto cursor que nos permitirá ejecutar comandos SQL en la base de datos.
    cursor = con.cursor()
    # Retornamos tanto la conexión como el cursor para su uso posterior.
    return con,cursor

if __name__ == '__main__':
    # Verificamos si este script se está ejecutando directamente.
    # Esto es útil para evitar que el código se ejecute si se importa como módulo en otro script.
    con,cursor = conectar() # Llamamos la función conectar y almacenamos los objetos retornados
    print(con)  # Imprimimos el objeto de conexión para verificar que se ha establecido correctamente.
    print(cursor)   # Imprimimos el objeto cursor para confirmar que está listo para ejecutar comandos SQL.