

"""
    Create graphs
"""
import networkx as nx
from petreader.labels import *
from Labels import *
def CreateGraph(relations: list,
                graph_name: str) -> nx.DiGraph:
    """
        create the graph

    """

    graph = nx.DiGraph()
    graph.name = graph_name

    for relation in relations:
        rel, rel_type = relation
        source_node = (rel[SOURCE_SENTENCE_ID], rel[SOURCE_HEAD_TOKEN_ID])
        source_attrs = {TYPE: rel[SOURCE_ENTITY_TYPE], LABEL: ' '.join(rel[SOURCE_ENTITY])}

        target_node = (rel[TARGET_SENTENCE_ID], rel[TARGET_HEAD_TOKEN_ID])
        target_attrs = {TYPE: rel[TARGET_ENTITY_TYPE], LABEL: ' '.join(rel[TARGET_ENTITY])}

        graph.add_node(source_node, attrs=source_attrs)
        graph.add_node(target_node, attrs=target_attrs)
        graph.add_edge(source_node, target_node, attrs={TYPE: rel_type, LABEL:rel_type})

    return graph

