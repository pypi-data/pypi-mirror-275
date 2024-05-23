import json
import networkx as nx
from Labels import *
import matplotlib.pyplot as plt


plt.rcParams["figure.autolayout"] = True
# from pydata.graphs.savegraphs import SaveGraph
import os
from collections import defaultdict
import networkx as nx
from petreader.labels import *

colors = {ACTIVITY:                "skyblue",
          ACTIVITY_DATA:           "yellow",
          ACTOR:                   'red',
          AND_GATEWAY:             'black',
          XOR_GATEWAY:             'black',
          CONDITION_SPECIFICATION: 'black',

          FLOW:                    'green',
          SAME_GATEWAY:            'red',
          USES:                    "yellow",
          ACTOR_PERFORMER:         'orange'}

ARROW_SIZE = 55
NODE_LABEL_SIZE = 17
EDGE_LABEL_SIZE = NODE_LABEL_SIZE


def readjson(filename):
    f = open(filename, "r")
    return json.loads(f.read())


def savejson(data, json_filename):
    with open(json_filename, "w") as outfile:
        json.dump(data, outfile)


def createAnswerGraph(graph_name,
                      graph_list,
                      relation_label: str) -> nx.DiGraph:
    """
        create a graph representation of the answer

        relation_label defines also the attributes of nodes
    """
    #  returns:
    #       a nx graph representing behavioral elements (ACTIVITY, GATEWAY, CONDITION SPECIFICATION)
    #       a dict(node code)= {type: Act/Gate/CondSpec, label: str}
    #       a dict(edge) = edge type: str

    graph = nx.DiGraph()
    graph.name = graph_name

    #  to be compatible with SaveGraph of pi, I add the attributes to the nodes
    for rel in graph_list:
        source  = rel[0]
        target = rel[1]

        graph.add_node(source, attrs={TYPE: ACTIVITY, LABEL: source})
        if relation_label == FLOW:
            graph.add_node(target, attrs={TYPE: ACTIVITY, LABEL: target})

        elif relation_label == ACTOR_PERFORMER:
            graph.add_node(target, attrs={TYPE: ACTOR, LABEL: target})

        graph.add_edge(source, target, attrs={TYPE: relation_label})

    print(graph)

    return graph


def combineAnswerDFGPerformsGraph(graph_name: str,
                                  dfg,
                                  performs) -> nx.DiGraph:

    graph = nx.DiGraph()
    graph.name = graph_name

    #  to be compatible with SaveGraph of pi, I add the attributes to the nodes
    for edge in dfg.edges:
        source = edge[0]
        graph.add_node(source, attrs={TYPE: ACTIVITY, LABEL: source})
        target = edge[1]
        graph.add_node(target, attrs={TYPE: ACTIVITY, LABEL: target})
        graph.add_edge(source, target, attrs={TYPE: FLOW})

    for edge in performs.edges:
        source = edge[0]
        graph.add_node(source, attrs={TYPE: ACTIVITY, LABEL: source})
        target = edge[1]
        graph.add_node(target, attrs={TYPE: ACTOR, LABEL: target})
        graph.add_edge(source, target, attrs={TYPE: ACTOR_PERFORMER})

    print(graph)

    return graph


def ShowGraph(graph: nx.Graph,
              outputfolder='./') -> None:
    """
        Save a graph into .dot and create .png and .pdf images of the graph

        graph is the nx graph
        outputfolder is the folder where results are saved

        each node must have a ['attrs'][LABEL] and a ['attrs'][TYPE] attributes

    """
    name = graph.name
    #  save graph in .dot
    nx.nx_agraph.write_dot(graph, os.path.join(outputfolder, name) + '.dot')

    node_labels = dict()
    node_color_map = list()
    #  node attrs
    for node in graph.nodes:
        node_labels[node] = graph.nodes[node]['attrs'][LABEL]
        node_color_map.append(colors[graph.nodes[node]['attrs'][TYPE]])

    edge_labels = dict()
    edge_color_map = list()
    for edge in graph.edges:
        edge_labels[edge] = graph.edges[edge]['attrs'][TYPE]
        edge_color_map.append(colors[graph.edges[edge]['attrs'][TYPE]])

    pos = nx.nx_agraph.graphviz_layout(graph, prog='dot')

    plt.figure(figsize=(24, 24))
    # draw labels
    nx.draw_networkx_nodes(graph,
                           pos,
                           node_color=node_color_map,
                           node_size=550,  # 23,
                           alpha=0.35,
                           )
    # shifty = 1.50
    # shiftx = 0  # -70.0
    # pos_node_labels = {k: (p[0] + shiftx, p[1] + shifty) for k, p in pos.items()}
    nx.draw_networkx_labels(graph,
                            pos,  # _node_labels,
                            labels=node_labels,
                            horizontalalignment='center',
                            verticalalignment='center',  # 'bottom',
                            font_size=NODE_LABEL_SIZE,
                            font_weight='bold',
                            font_color='black')
    nx.draw_networkx_edges(graph,
                           pos,
                           edge_color=edge_color_map,
                           arrows=True,
                           arrowsize=ARROW_SIZE,
                           arrowstyle='->',
                           )
    nx.draw_networkx_edge_labels(graph,
                                 pos,
                                 edge_labels=edge_labels,
                                 font_size=EDGE_LABEL_SIZE,  # 10,
                                 font_color='black')

    ax = plt.gca()
    ax.margins(0.25)
    plt.title(name)
    plt.axis("off")
    plt.tight_layout()

    plt.show()
    # plt.close('all')


def SaveGraph(graph: nx.Graph,
              outputfolder='./') -> None:
    """
        Save a graph into .dot and create .png and .pdf images of the graph

        graph is the nx graph
        outputfolder is the folder where results are saved

        each node must have a ['attrs'][LABEL] and a ['attrs'][TYPE] attributes

    """
    name = graph.name

    node_labels = dict()
    node_color_map = list()
    #  node attrs
    for node in graph.nodes:
        node_labels[node] = graph.nodes[node]['attrs'][LABEL]
        node_color_map.append(colors[graph.nodes[node]['attrs'][TYPE]])

    edge_labels = dict()
    edge_color_map = list()
    for edge in graph.edges:
        edge_labels[edge] = graph.edges[edge]['attrs'][TYPE]
        edge_color_map.append(colors[graph.edges[edge]['attrs'][TYPE]])

    pos = nx.nx_agraph.graphviz_layout(graph, prog='dot')

    plt.figure(figsize=(24, 24))
    # draw labels
    nx.draw_networkx_nodes(graph,
                           pos,
                           node_color=node_color_map,
                           node_size=550,
                           alpha=0.35,
                           )
    # shifty = 1.50
    # shiftx = 0  # -70.0
    # pos_node_labels = {k: (p[0] + shiftx, p[1] + shifty) for k, p in pos.items()}
    nx.draw_networkx_labels(graph,
                            pos,  # _node_labels,
                            labels=node_labels,
                            horizontalalignment='center',
                            verticalalignment='center',  # 'bottom',
                            font_size=NODE_LABEL_SIZE,
                            font_weight='bold',
                            font_color='black')
    nx.draw_networkx_edges(graph,
                           pos,
                           edge_color=edge_color_map,
                           arrows=True,
                           arrowsize=ARROW_SIZE,
                           arrowstyle='->',
                           )
    nx.draw_networkx_edge_labels(graph,
                                 pos,
                                 edge_labels=edge_labels,
                                 font_size=EDGE_LABEL_SIZE,
                                 font_color='black')

    ax = plt.gca()
    ax.margins(0.15)
    plt.axis("off")

    plt.tight_layout()

    #  save graph in .dot
    nx.nx_agraph.write_dot(graph, os.path.join(outputfolder, name) + '.dot')
    #  save graph in .gexf - to visualize with  Gephi (https://gephi.org/users/download/)
    nx.write_gexf(graph, os.path.join(outputfolder, name) + '.gexf')

    #  save graph image
    plt.savefig(os.path.join(outputfolder, name) + '.png',
                format='png', dpi=1000)
    plt.savefig(os.path.join(outputfolder, name) + '.pdf',
                format='pdf', dpi=1000)
