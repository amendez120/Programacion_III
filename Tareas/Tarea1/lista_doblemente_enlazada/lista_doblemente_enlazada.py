from nodo import Nodo

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo 
            self.cola = nuevo_nodo

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza
        while actual is not None:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                if actual == self.cola:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def mostrar_lista(self):
        actual = self.cabeza
        cadena = "None"
        while actual is not None:
            cadena += f" <- {actual.nombre} {actual.apellido} ({actual.carnet}) ->"
            actual = actual.siguiente
        cadena += " None"
        print(cadena)
