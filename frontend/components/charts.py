from pyvis.network import Network
import networkx as nx


def create_graph():

    G = nx.Graph()

    G.add_edge(
        "User_1",
        "Product_1"
    )

    G.add_edge(
        "User_1",
        "Product_2"
    )

    G.add_edge(
        "User_2",
        "Product_1"
    )

    G.add_edge(
        "Bot_Ring",
        "Product_3"
    )

    net = Network(
        height="600px",
        width="100%"
    )

    net.from_nx(G)

    graph_path = "graph.html"

    net.save_graph(graph_path)

    return graph_path