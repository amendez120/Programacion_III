from graphviz import Digraph

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.val:
            return True
        elif key < current_node.val:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current_node, key):
        if current_node is None:
            return None
        if key < current_node.val:
            current_node.left = self._delete_recursive(current_node.left, key)
        elif key > current_node.val:
            current_node.right = self._delete_recursive(current_node.right, key)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            temp = self._min_value_node(current_node.right)
            current_node.val = temp.val
            current_node.right = self._delete_recursive(current_node.right, temp.val)
        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                self.insert(int(line.strip()))

    def generate_graphviz(self):
        dot = Digraph()
        self._generate_graphviz_recursive(dot, self.root)
        # Guardar en un archivo y opcionalmente visualizarlo
        filename = dot.render('tree', format='png', cleanup=False)
        print(f"Graphviz file saved as: {filename}.png")
        # Para visualizar directamente
        dot.view()

    def _generate_graphviz_recursive(self, dot, node):
        if node is not None:
            dot.node(str(node.val), str(node.val))
            if node.left:
                dot.edge(str(node.val), str(node.left.val))
                self._generate_graphviz_recursive(dot, node.left)
            if node.right:
                dot.edge(str(node.val), str(node.right.val))
                self._generate_graphviz_recursive(dot, node.right)

    
    