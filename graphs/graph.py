"""
Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is
ordered because (u, v) is not same as (v, u) in case of directed
graph(di-graph). The pair of form (u, v) indicates that there is an edge from
vertex u to vertex v. The edges may contain weight/value/cost.
"""
from collections import defaultdict


class Graph(object):
    """
    A representation for graph data structure

    :param vertices: No. of vertices
    :param is_di_graph: Indicate if graph is directed or un-directed
    """

    def __init__(self, vertices, is_di_graph=False):
        self.vertices = vertices
        self.is_di_graph = is_di_graph
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        """
        add an edge to graph
        """
        if self.is_di_graph:
            self.graph[start].append(end)
        else:
            self.graph[start].append(end)
            self.graph[end].append(start)
