from lista_doblemente_enlazada import ListaDoblementeEnlazada
from visualizacion import visualizar_lista


def menu():
    lista = ListaDoblementeEnlazada()
    while True:
        print("\nMenú:")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por valor")
        print("4. Mostrar lista")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ") 
            lista.insertar_al_principio(nombre, apellido, carnet)
        elif opcion == '2':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)
        elif opcion == '3':
            carnet = input("Carnet del nodo a eliminar: ")
            if lista.eliminar_por_valor(carnet):
                print(f"Nodo con carnet {carnet} eliminado.")
            else:
                print("Nodo no encontrado.")
        elif opcion == '4':
            lista.mostrar_lista()
            visualizar_lista(lista)
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
