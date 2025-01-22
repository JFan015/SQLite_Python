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
    nota = input('Ingrese la nota del alumno: ')

    # Definimos la sentencia SQL para insertar un nuevo alumno
    sentencia = f"INSERT INTO alumnos VALUES (NULL, ?, ?, ?)"
    
    # Creamos una tupla con los datos del alumno
    datos = (nombre, email, nota)

    print("\nAlumno ingresado con éxito.")

    # Ejecutamos la sentencia SQL con los datos del alumno
    cursor.execute(sentencia, datos)

    # Confirmamos los cambios en la base de datos
    conexion.commit()

def consultarAlumno(conexion, cursor):
    sentencia = "SELECT id, nombre, email, nota FROM alumnos"
    resultado = cursor.execute(sentencia)
    return resultado

def modificarNota(conexion, cursor):
    id = input("\nIngresa el identificador del alumno: ")
    nota = input("Ingrese la nota: ")
    sentencia = f"UPDATE alumnos SET nota ={nota} WHERE id ={id}"
    cursor.execute(sentencia)
    conexion.commit()
    return True

def borrarAlumno(conexion, cursor):
    id = input("\nIngresa el identificador del alumno a borrar: ")
    sentencia = f"DELETE FROM alumnos WHERE id={id}"
    cursor.execute(sentencia)
    conexion.commit()
    print("|nAlumno eliminado de la base de datos correctamente.")
    return True

def menu():
    menu = """
    0.  Salir
    1.  Insertar datos de alumnos
    2.  Consultar alumnos
    3.  Modificar nota
    4.  Borrar alumno
          """
    con, cursor = conectar()
    crearTabla(con, cursor)
    while True:
        print(menu)
        opcion = int(input())
        if opcion == 0:
            print("Has salido.")
            con.close()
            break
        elif opcion == 1:
            con, cursor = conectar()
            insertarAlumno(con, cursor)
        elif opcion == 2:
            con, cursor = conectar()
            resultado = consultarAlumno(con, cursor)
            for fila in resultado:
                print("*"*100)
                print("\n")
                print("ID: " ,fila[0])
                print("Nombre: " , fila[1])
                print("Email: " ,fila[2])
                print("Nota: " ,fila[3])
                print("\n")
        elif opcion == 3:
            con, cursor = conectar()
            modificarNota(con,cursor)
        elif opcion == 4:
            con, cursor = conectar()
            borrarAlumno(con, cursor)
        else:
            print("Indica una opción válida.\n")
            print(menu)

def principal():
    menu()

if __name__ == '__main__':
    principal()