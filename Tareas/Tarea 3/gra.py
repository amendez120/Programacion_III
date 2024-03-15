from graphviz import Digraph

def generate_graphviz(self):
    dot = Digraph()
    self._generate_graphviz_recursive(dot, self.root)
    # Visualizar directamente
    dot.view()
    # O guardar en un archivo
    dot.render('tree', format='png', cleanup=True)

def _generate_graphviz_recursive(self, dot, node):
    if node is not None:
        dot.node(str(node.val))
        if node.left:
            dot.edge(str(node.val), str(node.left.val))
            self._generate_graphviz_recursive(dot, node.left)
        if node.right:
            dot.edge(str(node.val), str(node.right.val))
            self._generate_graphviz_recursive(dot, node.right)
