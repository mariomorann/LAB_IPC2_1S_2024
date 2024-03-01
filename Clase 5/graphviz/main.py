import graphviz

def main():
    dot = graphviz.Graph(filename='archivo')
    dot.attr('node', shape='square')
    dot.attr(rankdir='LR')  
    dot.node('A', 'nodo A')
    dot.node('B', 'nodo B')
    dot.node('C', 'nodo C')
    dot.node('D', 'nodo D')

    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')

    dot.render(directory='', view=True).replace('\\', '/')

if __name__ == "__main__":
    main()