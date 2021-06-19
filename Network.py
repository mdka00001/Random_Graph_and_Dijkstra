import matplotlib.pyplot as plt
import networkx as nx
import random


graph = nx.cycle_graph(50)
pos = nx.spring_layout (graph)
#main_node=G.node
colour = [ "red", "blue", "green", "yellow", "purple","magenta", "orange","black" ]

color_map = []
for node in graph:
   color_map.append(colour[random.randint(0,7)])

nx.draw(graph, node_color=color_map )


plt.savefig("cycle_graph.png")
plt.show()

# has even number of nodes so use two colours


