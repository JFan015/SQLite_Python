import sqlite3

def conectar():
    #   Establecemos la conexión con la base de datos SQLite con nombre de 'alumnos.db'
    con = sqlite3.connect('alumnos.db') #   Si la base de datos no existe, la crea
    cursor = con.cursor()   #   Creamos un objeto llamado cursor para poder ejecutar comandos SQL
    #   Devolvemos tanto la conexión como el cursor
    return con, cursor  # Esto nos permite usar ambos objetos cuando sea necesario

def crearTabla(conexion, cursor):
    # Definimos la sentencia SQL para crear la tabla si no existe
    sentencia = """
        CREATE TABLE IF NOT EXISTS alumnos
        (ID INTEGER PRIMARY KEY NOT NULL,
        NOMBRE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        NOTA INTEGER NOT NULL)
    """
    # Ejecutamos la sentencia SQL
    cursor.execute(sentencia)
    # Cerramos la conexión a la base de datos
    conexion.close()
    return True

def menu():
    while True:
        print("""
        Seleccione una opción:
        0. Salir
        1. Insertar datos de alumnos
        """)
        opcion = int(input("Opción: "))
        if opcion == 0:
            print("Has salido.")
            break
        else:
            print("Indica una opción válida.")

def principal():
    menu()

if __name__ == '__main__':
    principal()