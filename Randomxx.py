#reference https://networkx.org/documentation/stable/auto_examples/drawing/plot_random_geometric_graph.html
import matplotlib.pyplot as plt
import networkx as nx
import random

G = nx.random_geometric_graph(200, 0.125)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, "pos")

# find node near center (0.5,0.5)
#reference https://networkx.org/documentation/stable/auto_examples/drawing/plot_random_geometric_graph.html
min = 1
nodecenter = 0
for node in pos:
    x, y = pos[node]
    dx = (x - 0.5) ** 2
    dy = (y - 0.5) ** 2
    distance = dx + dy
    if   min > distance:
        nodecenter = node
        min = distance

# color by path length from node near center
colour = [ "red", "blue", "green", "yellow", "purple","magenta", "orange","black" ]

color_map = []
for node in G:
   color_map.append(colour[random.randint(0,7)])


nx.draw_networkx_edges(G, pos, nodelist=[nodecenter])#1
nx.draw_networkx_nodes(G,pos,node_color=color_map  )


plt.savefig("Random_graph.png")
plt.show()