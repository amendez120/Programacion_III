import csv
from graphviz import Digraph

class SparseMatrix:
    def __init__(self):
        # Lista para almacenar los elementos no nulos como tuplas (fila, columna, valor)
        self.elements = []

    def load_from_csv(self, filepath):
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:  # Saltar la cabecera
                    continue
                for j, value in enumerate(row):
                    if value != '0':  # Almacenar solo valores no nulos
                        self.elements.append((i, j, int(value)))

    def add_data(self, row, col, value):
        if value != 0:
            self.elements.append((row, col, value))

    def display(self):
        print("Matriz Dispersa (COO):")
        for (row, col, value) in self.elements:
            print(f"({row}, {col}) -> {value}")

    def visualize(self):
        dot = Digraph(comment='Matriz Dispersa en Formato COO')
        # Segmentos A, IA, JA
        A = [str(x[2]) for x in self.elements]  # Valores de la matriz
        IA = [str(x[0]) for x in self.elements]  # Índices de fila tal como se almacenan
        JA = [str(x[1] + 1) for x in self.elements]  # Ajustar los índices de columna para comenzar en 1

        # Crear nodos
        dot.node('A', 'A = [' + ', '.join(A) + ']')
        dot.node('IA', 'IA = [' + ', '.join(IA) + ']')
        dot.node('JA', 'JA = [' + ', '.join(JA) + ']')

        # Conectar nodos para claridad visual
        dot.edge('A', 'IA', label='Índices de fila')
        dot.edge('A', 'JA', label='Índices de columna')

        # Generar el gráfico y abrirlo
        dot.render('output/sparse_matrix_graph', view=True)



        
def main():
    matrix = SparseMatrix()
    while True:
        print("\n1. Cargar datos desde CSV")
        print("2. Ingresar datos manualmente")
        print("3. Mostrar matriz")
        print("4. Visualizar matriz")
        print("5. Salir")
        option = input("Selecciona una opción: ")

        if option == '1':
            filepath = input("Ingresa el camino al archivo CSV: ")
            matrix.load_from_csv(filepath)
        elif option == '2':
            row = int(input("Fila: "))
            col = int(input("Columna: "))
            value = int(input("Valor: "))
            matrix.add_data(row, col, value)
        elif option == '3':
            matrix.display()
        elif option == '4':
            matrix.visualize()
        elif option == '5':
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
