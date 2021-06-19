import heapq

def dijkstra(g, s):
    """
    here g is the weighted graph and s is the start vertex
    """
    """
    set the initial distance of each vertex from start vertex to 0
    """
    dist=dict()
    for v in g:
        dist[v]=float("inf")
    """
    set the distance of start vertex "s" to 0 since s-s has no distance
    """
    dist[s]=0
    """
    created a list containing weight of the initial vertex and the vertex itself
    """ 
    init=[(0,s)]

    while len(init)>0:
        """
        In Dijkstra's algorithm same nodes are not added multiple times, 
        so here popped each vertex from the priority list after calculating distance
        """
        current_weight, current_vertex = heapq.heappop(init)
        if current_weight > dist[current_vertex]:
            continue
        """
        At this stage, we check the weight of all vertex in a given graph and determine 
        the total distance from the start node by adding weight to the current distance
        """
        for n, w in g[current_vertex].items():
            current_dist = current_weight+w

            """
            Here we only take the distances that are lower than the given weights in a graph. 
            If a better distance is found, we update it to the dist[]
            """
            if current_dist<dist[n]:
                dist[n]=current_dist
                """
                Here we add new vertex to the init list, where current_dist is the 
                total distance obtained from the initial vertex and n is the neighbour vertex
                """
                heapq.heappush(init, (current_dist, n))
    return dist

graph = {
    'A': {'B': 2, 'B': 5, 'D': 1},
    'B': {'A': 2, 'D': 2, 'C': 3},
    'C': {'B': 3, 'A': 5, 'D': 3, 'E': 1, 'F': 5},
    'D': {'A': 1, 'B': 2, 'C': 3, 'E': 1},
    'E': {'D': 1, 'C': 1, 'F': 1},
    'F': {'C': 5, 'E': 1},
}

"""
Here we have given a graph as an input. It is a dictionary with keys corresponding to each vertices 
and values corresponding to distance of neighbour vertices connected to it
"""

"""
Results will show the overall distance of each vertices from the start vertex
"""
print(dijkstra(graph, "A"))




