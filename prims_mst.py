from heapq import heappop,heappush

## Get Minimum spanning tree of an undirected graph
## i.e get the tree with lowest edge cost sum.


def get_mst(A,n):
    '''
    :param A: Adjacency list
    :param n: no of nodes in undirected graph
    :return: min cost, min cost edges
    '''

    visited = set()

    min_cost = 0
    min_edges = []

    heap = []

    ## lets add A[0] to heap to start with

    if A[0]:
        for v,w in A[0]:
            visited.add(0)
            heappush(heap,(w,0,v))
    else:
        return -1,[]
    # print(heap)

    while heap:
        wei, u, v  = heappop(heap)
        # print(wei,u,v)
        if v not in visited:
            min_edges.append((u, v))
            min_cost += wei
            visited.add(v)
            for x,w in A[v]:
                if x not in visited:
                    heappush(heap,(w,v,x))

    if len(visited)!=n:
        return -1, []

    return min_cost, min_edges


## Testing.. example from william course.

A  = {0:[(1,10),(2,1),(3,4)],1:[(0,10),(4,0),(2,3)],2:[(0,1),(1,3),(5,8),(3,2)],3:[(0,4),(2,2),(5,2),(6,7)],
      4:[(1,0),(5,1),(7,8)],5:[(2,8),(3,2),(4,1),(6,6),(7,9)],6:[(3,7),(5,6),(7,12)],7:[(5,9),(6,12),(4,8)]}

res = get_mst(A,8)
print(res)




