def popmin(pqueue):
    # priprity queue implemented
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
 
def prim(graph, root):
    pred = {} # pair {vertex: predecesor in MST}
    key = {}  # keep track of minimum weight for each vertex
    pqueue = {} # priority queue implemented as dictionary
 
    for v in graph:#for each vertex in graph
        pred[v] = -1#predecessor value is aasigned -1
        key[v] = 1000#initial value assigned to infinity
    key[root] = 0#for root it is aasigned 0
    for v in graph:
        pqueue[v] = key[v]#adding it to the priority queue
     
    while pqueue:#while queue is not empty
        u = popmin(pqueue)#lowestkey
        for v in graph[u]: # all neighbors of u
            if v in pqueue and graph[u][v] < key[v]:
                pred[v] = u
                key[v] = graph[u][v]
                pqueue[v] = graph[u][v]
    return pred
 
graph = {0 : {1:6, 2:8},
1 : {4:11},
2 : {3: 9},
3 : {},
4 : {5:3},
5 : {2: 7, 3:4}}
 
result = prim(graph, 0)
for v in result: print "%s: %s" % (v, result[v])
 