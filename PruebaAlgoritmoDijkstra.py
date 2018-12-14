'''
Created on 13/12/2018

@author: acer
'''
from pip._vendor.distlib.compat import raw_input

'''
https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
'''

from collections import deque, namedtuple

# infinito como la distancia default entre nodos
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

def hacer_edge(start, end, cost=1):
    return Edge(start, end, cost)

class Grafo:
    def __init__(self, edges):
        # verificar que la informacion sea correcta
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Datos de edges erroneos: {}'.format(wrong_edges))

        self.edges = [hacer_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_nodo_par(self, n1, n2, both_ends=True):
        if both_ends:
            nodoPar = [[n1, n2], [n2, n1]]
        else:
            nodoPar = [[n1, n2]]
        return nodoPar

    def remover_edge(self, n1, n2, both_ends=True):
        nodoPar = self.get_nodoPar(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in nodoPar:
                self.edges.remove(edge)

    def agregar_edge(self, n1, n2, cost=1, both_ends=True):
        nodoPar = self.get_nodoPar(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in nodoPar:
                return ValueError('Edge {} {} ya existe'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours
    
    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Tal nodo de origen no existe'
        distancias = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distancias[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distancias[vertex])
            vertices.remove(current_vertex)
            if distancias[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distancias[current_vertex] + cost
                if alternative_route < distancias[neighbour]:
                    distancias[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path
    
raw_input()

print ("Se creara un grafo de a-f")
a1=int(raw_input("Distancia de a-b"))
a2=int(raw_input("Distancia de a-c"))    
a3=int(raw_input("Distancia de a-f"))  
a4=int(raw_input("Distancia de b-c"))  
a5=int(raw_input("Distancia de b-d"))  
a6=int(raw_input("Distancia de c-d"))  
a7=int(raw_input("Distancia de c-f"))
a8=int(raw_input("Distancia de d-e"))    
a9=int(raw_input("Distancia de e-f"))  
    
grafo = Grafo([("a", "b", (a1)),  ("a", "c", (a2)),  ("a", "f", (a3)), ("b", "c", (a4)),
    ("b", "d", (a5)), ("c", "d", (a6)), ("c", "f", (a7)),  ("d", "e", (a8)),
    ("e", "f", (a9))])

print ("-------------Camino mas corto---------------")
origen=str(raw_input("Ingresa nodo origen"))
destino=str(raw_input("Ingresa nodo destino"))
print(grafo.dijkstra(origen, destino))

