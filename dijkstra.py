from heapq import heappop,heappush

## Get shortest path from start node to all other nodes in the graph

## Important Assumption: Only non-negative edge weights.

## Implementation: Dijkstra follows greedy path using a PQ/heap, and updates shortest distances and parents.


def dijkstra(A,start,n):
    '''
    :param A: Adjacency list
    :param start: start node
    :param n: no.of nodes in graph
    :return: distance and parent arrays.
    '''

    dist = [float('inf')]*n
    parent = [None]*n
    visited = set() ## can be array

    heap = []
    heappush(heap,(0,start)) ## adding start node to heap

    while heap:
        d, cur = heappop(heap)

        visited.add(cur)

        # if dist[cur]<d: continue ## additional optimization @William course suggest.

        for v,e in A[cur]: ## v-node index, e-edge_Weight
            if v not in visited: ## no need to update distances for visited nodes, as we follow greedy approach
                if d+e<dist[v]:
                    dist[v] = d+e
                    parent[v] = cur
                    heappush(heap,(d+e,v)) ## notice that we may add duplicates here,
                    ## @Williams course mentions indexed heap usage to avoid that.

    del heap ## as it may contain duplicates, indexed heap can be used to avoid this

    return dist,parent


def find_shortest_path(A,start,end,n):
    '''
    :param A: Adjacency list
    :param start: start node
    :param end: end node
    :param n: no of nodes
    :return:
    '''
    dist, parent = dijkstra(A,start,n)
    path = []
    if dist[end]==float('inf'): ## unreachable
        return path
    while end:
        path.append(end)
        end = parent[end]
    return [start]+path[::-1]



## Testing

A = {0:[(1,5),(2,2)],1:[(3,1)],2:[(1,2),(4,8)],3:[(5,4),(2,1)],4:[(3,1),(5,3)],5:[]}
res = dijkstra(A,0,6)

print(res)

path = find_shortest_path(A,0,5,6)
print(path)


## Complexity Analysis

## pushing and popping from heap may take upto logV time
## overall O(ElogV)





