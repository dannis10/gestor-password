#1. Mostrar un menú al usuario con las siguientes opciones:
#    Añadir contraseñas a un archivo.
#    Listar contraseñas almacenadas.
#    Salir del programa.
def main():
    while True:
        print("\n--- Menú ---")
        print("1. Añadir contraseña")
        print("2. Listar contraseñas")
        print("3. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            password = input("Introduce la contraseña que deseas añadir: ")
            add_password(password)
            print("Contraseña añadida!!")
        elif choice == "2":
            print("\nContraseñas guardadas: ")
            passwords = list_passwords()
            for pw in passwords:
                print(pw.strip())
        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            pirnt("Opción no válida. Por favor, selecciona una opción del menú.")
if __name__ == "__main__":
    main()
