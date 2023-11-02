from pyvis import network as net
import networkx as nx 

def graphit():
    g = net.Network()
    nxg = nx.complete_graph(6)
    g.from_nx(nxg)
    g.save_graph("graph.html")

