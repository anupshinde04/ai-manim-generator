import json
import networkx as nx

def load_graph(path="data/books.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    G = nx.Graph()
    for subject, concepts in data.items():
        for concept, content in concepts.items():
            G.add_node(concept, content=content, subject=subject)
            G.add_edge(subject, concept)
    return G

def query_concept(G, concept):
    if concept in G.nodes:
        return G.nodes[concept]["content"]
    else:
        return "Concept not found."
