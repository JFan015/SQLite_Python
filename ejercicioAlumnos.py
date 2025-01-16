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

def insertarAlumno(conexion, cursor):
    # Solicitamos al usuario que ingrese el nombre del alumno
    nombre = input('Ingrese el nombre del alumno: ')
    # Solicitamos al usuario que ingrese el email del alumno
    email = input('Ingrese el email del alumno: ')
    # Solicitamos al usuario que ingrese la nota del alumno
    nota = int(input('Ingrese la nota del alumno: '))

    # Definimos la sentencia SQL para insertar un nuevo alumno
    sentencia = f"INSERT INTO alumnos VALUES (NULL, ?, ?, ?)"
    
    # Creamos una tupla con los datos del alumno
    datos = (nombre, email, nota)

    # Ejecutamos la sentencia SQL con los datos del alumno
    cursor.execute(sentencia, datos)

    # Confirmamos los cambios en la base de datos
    conexion.commit()

    # Cerramos la conexión a la base de datos
    conexion.close()

def menu():
    con, cursor = conectar()
    crearTabla(con, cursor)
    while True:
        print("""
    0.  Salir
    1.  Insertar datos de alumnos    
          """)
        opcion = int(input())
        if opcion == 0:
            print("Has salido.")
            break
        elif opcion == 1:
            con, cursor = conectar()
            insertarAlumno()
        else:
            print("Indica una opción válida.")

def principal():
    menu()

if __name__ == '__main__':
    principal()