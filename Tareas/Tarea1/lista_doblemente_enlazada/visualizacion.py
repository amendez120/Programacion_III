from graphviz import Digraph

def visualizar_lista(lista):
    dot = Digraph()
    actual = lista.cabeza
    dot.node('None', 'None', shape='plaintext')
    prev = 'None'
    while actual:
        nodo_id = str(actual.carnet)
        dot.node(nodo_id, f'{actual.nombre} {actual.apellido}\n{actual.carnet}')
        dot.edge(prev, nodo_id)
        if actual.siguiente:
            dot.edge(nodo_id, str(actual.siguiente.carnet))
            dot.edge(str(actual.siguiente.carnet), nodo_id)
        else:
            dot.node('None2', 'None', shape='plaintext')
            dot.edge(nodo_id, 'None2')
        prev = nodo_id
        actual = actual.siguiente
    dot.render('lista_doblemente_enlazada', view=True, format='png')
 