import os

def main():
    files = [f for f in os.listdir() if f.endswith(".py") and not f.startswith('.')]

    while True:
        print("\n\n programas generales")
        for i, filename in enumerate(files, start=1):
           
            print(f"{i}. Ejecutar función de {filename}")

        print("q. Salir")
        choice = input("Elige una opción: ")
        print("\n")

        if choice.isdigit() and 1 <= int(choice) <= len(files):
            try:
            
                module_name = files[int(choice) - 1].rstrip(".py")
                #
                module = __import__(module_name)
             
                module.sum_numbers()
            except ImportError:
                print(f"No se pudo importar {module_name}. Verifica que el módulo existe y tiene la función 'sum_numbers'.")
            except AttributeError:
                print(f"El módulo {module_name} no tiene la función 'sum_numbers'.")
            except Exception as e:
                print(f"Error al ejecutar {module_name}: {e}")
        elif choice == "q":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()

