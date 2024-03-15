from bst import BinarySearchTree

def main():
    bst = BinarySearchTree()
    while True:
        print("\nMenú:")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde archivo")
        print("5. Mostrar árbol (Graphviz)")
        print("6. Salir")
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            key = int(input("Ingrese el valor a insertar: "))
            bst.insert(key)
        elif choice == '2':
            key = int(input("Ingrese el valor a buscar: "))
            print("Encontrado!" if bst.search(key) else "No encontrado.")
        elif choice == '3':
            key = int(input("Ingrese el valor a eliminar: "))
            bst.delete(key)
        elif choice == '4':
            file_path = input("Ingrese la ruta del archivo: ")
            bst.load_from_file(file_path)
        elif choice == '5':
            bst.generate_graphviz()
        elif choice == '6':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
