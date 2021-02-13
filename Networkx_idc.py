import networkx as nx
import matplotlib.pyplot as plt
import networkx
import time
import random


def getEdgesShortestPath(shortestPath, all_edges):
    """
    Individua gli edges da colorare in rosso presenti nello shortestPath
    :param shortestPath: lista dei nodi in sequenza dello shortestPath
    :param all_edges: lista di tutti gli edges nel grafo con rispettivo peso
    :return: lista dei nodi da colorare in rosso
    """
    red_edges = []
    for i in range(len(shortestPath) - 1):
        # print(shortestPath[i], " ", shortestPath[i + 1])
        for edge in all_edges:
            if shortestPath[i] == edge[0] and shortestPath[i + 1] == edge[1]:
                red_edges.append((edge[0], edge[1]))
                # print((edge[0], edge[1]))
            elif shortestPath[i] == edge[1] and shortestPath[i + 1] == edge[0]:
                red_edges.append((edge[1], edge[0]))
                # print((edge[1], edge[0]))
    return red_edges


def setNodeColorsShortestPath(graph):
    """
    Assegna i colori ai nodi del Grafo
    :param graph: Grafo in input contenente tutti i nodi
    :return: lista dei colori da attribuire ai nodes
    """
    color_map = []
    for node in graph:
        if node == source:
            color_map.append('red')
        elif node == target:
            color_map.append('yellow')
        elif node in shortestPath[1:]:
            color_map.append('orange')
        else:
            color_map.append('gray')
    return color_map


def getLabels4edges(all_edges):
    """
    Individua tutte le label con i pesi per tutti gli edges
    :param all_edges: lista di tutti gli edges nel grafo con rispettivo peso
    :return: dizionario con tutti i pesi per gli edges
    """
    # FORMATO labels # labels = {('A', 'staz1'): '5', ('A', 'staz2'): '3', ('B', 'staz3'): '6'}
    labels = dict()
    for edge in all_edges:
        stateFrom, stateTo, weight = edge
        # print(stateFrom, stateTo, weight)
        labels[(stateFrom, stateTo)] = weight
    return labels


def getAllEdges(Graph):
    """
    Realizza una lista con tutti gli edges nel Grafo con rispettivo weight
    :param Graph: Grafo in input contenente tutti i nodi
    :return: lista di tutti gli edges nel grafo con rispettivo peso
    """
    all_edges = []
    for (node1, node2, data) in Graph.edges(data=True):
        all_edges.append((node1, node2, data['weight']))
    return all_edges


def dist(a, b):
    """
    distana coordinate per euristica A* (non usata)
    :param a:
    :param b:
    :return:
    """
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


if __name__ == '__main__':
    """
      Definisco il Grafo vuoto
    """
    g = nx.Graph()
    # g = nx.DiGraph()

    """
    Aggiungo gli edges al Grafo con i rispettivi weight
    """
    while True:
        try:
            maxNodes = random.randint(5, 50)
            maxEdge = random.randint(10, maxNodes * 3)

            nodes = []
            for i in range(maxNodes - 2):
                nodes.append(str(i))

            nodes.insert(0, "Office")
            nodes.insert(0, "Home")

            for i in range(maxEdge):
                g.add_edge(nodes[random.randint(0, maxNodes - 1)],
                        nodes[random.randint(0, maxNodes - 1)], weight=random.randint(1, 15))

            """
            Definisco i nodi source e target
            """
            source = "Home"
            target = "Office"

            if(nx.has_path(g, source, target) == False):
                print("No path to Office. Do it!")
                g.add_edge(nodes[0], nodes[1], weight=random.randint(10, 25))
            break
        except:
            print("Retry!")

    """
    Calcolo lo shortestPath pesato tra source e target
  """
    timex = time.perf_counter_ns()
    shortestPath = nx.shortest_path(
        g, source, target, weight='weight', method='dijkstra')
    print(shortestPath, " dijkstra --> ended in: ",
          time.perf_counter_ns() - timex, "ns")

    timex = time.perf_counter_ns()
    shortestPath = nx.shortest_path(
        g, source, target, weight='weight', method='bellman-ford')
    print(shortestPath, " bellman-ford --> ended in: ",
          time.perf_counter_ns() - timex, "ns")

    timex = time.perf_counter_ns()
    shortestPath = nx.astar_path(g, source, target, weight='weight')
    print(shortestPath, " astar_path --> ended in: ",
          time.perf_counter_ns() - timex, "ns")

    # shortestPath = list(nx.all_simple_paths(g, source, target))
    # print(shortestPath)

    """
    Calcolo costo percorso dello shortestPath tra source e target
  """
    timex = time.perf_counter_ns()
    length = nx.shortest_path_length(g, source, target, weight='weight')
    print(length, " length --> ended in: ",
          time.perf_counter_ns() - timex, "ns")

    """
    Definisco il layout del graph
  """
    PannelDim = 2000
    # DECENTI #
    # pos = nx.spring_layout(g, scale=PannelDim, center=None, dim=2)
    # pos = nx.shell_layout(g, scale=PannelDim, center=None, dim=2)
    # pos = nx.circular_layout(g, scale=PannelDim, center=None, dim=2)
    # pos = nx.fruchterman_reingold_layout(g, scale=PannelDim, center=None, dim=2)

    # NON BELLI #
    # pos = nx.spectral_layout(g, scale=PannelDim, center=None, dim=2)
    # pos = nx.planar_layout(g, scale=PannelDim, center=None, dim=2)
    pos = nx.kamada_kawai_layout(
        g, scale=PannelDim, center=None, dim=2)  # NON COSì BRUTTO XD
    # pos = nx.random_layout(g, center=None, dim=2)
    # pos = nx.spiral_layout(g, scale=PannelDim, center=None, dim=2)

    """
    Aggiungo le label con i weight a gli edges
  """
    all_edges = getAllEdges(g)
    labels = getLabels4edges(all_edges)
    nx.draw_networkx_edge_labels(
        g, pos, edge_labels=labels, font_color='black')

    print(all_edges)

    """
    Cambio colore a gli edges e ai nodes dello shortestPath
  """
    red_edges = getEdgesShortestPath(shortestPath, all_edges)
    edge_colors = ['black' if (not edge in red_edges) and (not edge[::-1] in red_edges) else 'red' for edge in
                   g.edges()]
    color_map = setNodeColorsShortestPath(g)

    # listaCoordinate = list(G.values())
    # scale = max(PannelDim - 0, PannelDim - 0)
    # for elem in listaCoordinate:
    #   print(round(elem[0], 4) + scale, " | ", round(elem[1], 4) + scale)

    """
    Stampo a video il grafico risultante
  """
    nx.draw(g, pos, node_color=color_map, edge_color=edge_colors,
         with_labels=True, node_size=500)
    plt.show()
