from __future__ import annotations

from typing import Any


class Vertex:
    def __init__(self, key: Any) -> None:
        self.key = key
        self.connections: dict[Vertex, int] = {}

    def add_adj(self, vertex: Vertex, weight: int = 0):
        self.connections[vertex] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_weight(self, vertex: Vertex):
        return self.connections[vertex]


class Graph:
    def __init__(self) -> None:
        self.vertex_dict: dict[Any, Vertex] = {}

    def add_vertex(self, key: Any):
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex

    def get_vertex(self, key: Any):
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        return

    def add_edge(self, f: Any, t: Any, weight: int = 0):
        if f not in self.vertex_dict:
            self.add_vertex(f)
        if t not in self.vertex_dict:
            self.add_vertex(t)
        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 1)
vertex_a = graph.get_vertex("A")
vertex_b = graph.get_vertex("B")
