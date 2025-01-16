import sqlite3

def conectar():
    #   Establecemos la conexión con la base de datos SQLite con nombre de 'alumnos.db'
    con = sqlite3.connect('alumnos.db') #   Si la base de datos no existe, la crea
    cursor = con.cursor()   #   Creamos un objeto llamado cursor para poder ejecutar comandos SQL
    #   Devolvemos tanto la conexión como el cursor
    return con, cursor  # Esto nos permite usar ambos objetos cuando sea necesario


def menu():
    while True:
        print("""
        0.    Salir
          """)
        opcion = int(input())
        if opcion == 0:
            print("Has salido.")
            break
        else:
            print("Indica una opción válida.")

def principal():
    menu()

if __name__ == '__main__':
    principal()