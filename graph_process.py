import networkx as nx
import numpy as np
from tqdm import tqdm
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
import igraph as ig


def delete_random_nodes(length, st_range, graph):
    deleted = []
    for i in tqdm(range(length)):
        connectivity=False
        while not connectivity:
            is_node = False
            while not is_node:
                node = np.random.randint(0, st_range)
                if node not in deleted:
                    is_node = True
            new_graph = graph.copy()
            new_graph.remove_node(node)
            if nx.is_connected(new_graph):
                deleted.append(node)
                graph = new_graph.copy()
                connectivity = True
    return graph


def cut_graph(graph1, graph2):
    graph1_cut = delete_random_nodes(len(graph1.nodes()) - len(graph2.nodes()), len(graph1.nodes()), graph1)
    print('Initial first graph')
    print(nx.info(graph1))
    print('Cutted first graph')
    print(nx.info(graph1_cut))
    print('Second graph')
    print(nx.info(graph2))
    return graph1_cut


def vf2(graph1, graph2):
    GM = isomorphism.GraphMatcher(graph1, graph2)
    if GM.is_isomorphic():
        print('Graphs are isomorphic')
        print(GM.mapping)
    else:
        print('Graphs are not isomorphic')


def bliss(graph1, graph2):
    edgelist1 = [tuple(list(elem)[:2]) for elem in list(nx.to_edgelist(graph1))]
    gr1 = ig.Graph(len(graph1), edgelist1)
    edgelist2 = [tuple(list(elem)[:2]) for elem in list(nx.to_edgelist(graph2))]
    gr2 = ig.Graph(len(graph2), edgelist2)
    if gr2.isomorphic_bliss(gr1):
        print('Graphs are isomorphic')
    else:
        print('Graphs are not isomorphic')


def get_isomorphism_subgraph(graph1, graph2):
    GM = isomorphism.GraphMatcher(graph1, graph2)
    for subgraph in GM.subgraph_isomorphisms_iter():
        return subgraph


