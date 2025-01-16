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