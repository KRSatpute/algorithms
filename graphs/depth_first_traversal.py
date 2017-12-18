"""
Depth-first search (DFS) is an algorithm for traversing or searching tree or
graph data structures. One starts at the root (selecting some arbitrary node
as the root in the case of a graph) and explores as far as possible along
each branch before backtracking.
"""
from algorithms.graphs.graph import Graph


def traverse(ds_graph=Graph, node=0):
    """
    Function to return a DFS of graph
    """
    visited = set()
    path = [object()]
    path_set = set(path)
    stack = [iter(ds_graph.graph)]

    while stack:
        for vertex in stack[-1]:
            if vertex in path_set:
                continue
            elif vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                path_set.add(vertex)
                stack.append(iter(ds_graph.graph.get(vertex, ())))
                break
        else:
            path_set.remove(path[0])
            stack.pop()
    return path


def main():
    """
    Running the code
    """
    grph = Graph(vertices=7, is_directed=True)
    grph.add_edge(0, 1)
    grph.add_edge(1, 2)
    grph.add_edge(2, 5)
    grph.add_edge(1, 6)
    grph.add_edge(1, 4)
    grph.add_edge(2, 3)

    print traverse(grph, 0)
    print grph

if __name__ == "__main__":
    main()
