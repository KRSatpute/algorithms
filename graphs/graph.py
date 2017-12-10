"""
Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is
ordered because (u, v) is not same as (v, u) in case of directed
graph(di-graph). The pair of form (u, v) indicates that there is an edge from
vertex u to vertex v. The edges may contain weight/value/cost.
"""
from collections import defaultdict
from algorithms.graphs.union_find import UnionFind
# pylint: disable=too-few-public-methods


class Graph(object):
    """
    A representation for connected graph data structure using
    adjacency list
    :param vertices: No. of vertices
    :param is_directed: Indicate if graph is directed or un-directed
    """

    def __init__(self, vertices=0, is_directed=False):
        self.vertices = vertices
        self.is_directed = is_directed
        self.graph = defaultdict(list)
        self.union_find = UnionFind(self.vertices)
        self.is_cyclic = False

    def add_edge(self, start, end):
        """
        add an edge to graph
        """
        if self.is_directed:
            self.graph[start].append(end)
        else:
            self.graph[start].append(end)
            self.graph[end].append(start)

        # No need to check for cycle if cycle is already detected
        if not self.is_cyclic:
            set1 = self.union_find.find(start)
            set2 = self.union_find.find(end)
            self.is_cyclic = set1 == set2
            self.union_find.union(set1, set2)

    def __str__(self):
        grph = "Graph: " + str([(node1, node2)
                                for node1 in self.graph
                                for node2 in self.graph[node1]])

        return "\n".join([
            grph,
            "No. of Vertices: " + str(self.vertices),
            "Is Directed: " + str(self.is_directed),
            "Is Cyclic: " + str(self.is_cyclic),
        ])

    __repr__ = __str__


def main():
    """
    Running the code
    """
    grph = Graph(vertices=4, is_directed=True)
    grph.add_edge(0, 1)
    grph.add_edge(1, 2)
    grph.add_edge(2, 3)
    grph.add_edge(1, 3)

    print grph

if __name__ == "__main__":
    main()
