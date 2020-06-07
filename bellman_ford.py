


## Shortest path from start node to all nodes
## Can have negative weights
## Can detect negative cycles

def bellman_ford(A,start,n):
    '''
    :param A: Adjacency list
    :param start: start node
    :param n: no of nodes
    :return: distance.
    '''

    dist = [float('inf')]*n
    dist[0] = 0

    for u in range(n): ## because max path size between any two vertices is |V-1|.
        for v, w in A[u]:
            if dist[u]+ w < dist[v]:
                dist[v] = dist[u]+ w

    ## Repeat the algo again to detect negative weight cycles
    for u in range(n):
        for v,w in A[u]:
            if dist[u]+w < dist[v]:
                dist[v] = float('-inf')

    return dist


## Testing

A = {0:[(1,5)],1:[(6,60),(2,20),(5,30)],2:[(3,10),(4,75)],3:[(2,-15)],4:[(9,100)],5:[(6,5),(8,50)],6:[(7,-50)],7:[(8,-10)],8:[],9:[]}
res = bellman_ford(A,0,10)
print(res)

## Complexity Analysis

## O(VE)

