from collections import deque

## BFS- generally used for finding shortest paths
## For tracking path itself, maintain parent array

## Here lets code to find shortest path between u,v and path as well
## Assuming input is Adjacency list again

def bfs(start,end,A):
    '''
    :param start: start node
    :param end: end node
    :param A: Adjacency list
    :return: shortest path length and path
    '''

    ## Assumption: for simplicity, graph is undirected and has one connected component.
    ## Assumption: no edge weights

    queue = deque()
    queue.append((start,0))

    visited = set()
    visited.add(start)
    parent = [None]*len(A)

    while queue:
        cur, path_len = queue.popleft() ## deque
        if cur == end:
           break ## can return shortest path here.
        for v in A[cur]:
            if v not in visited:  ## enqeue, mark visited and update parent
                visited.add(v)
                parent[v] = cur  ## careful with parent implementation.
                queue.append((v,path_len+1))


    ## if path is asked ...
    if cur==end:
        ## do parent tracing with parent array
        path = []
        while parent[cur] is not None:
            path.append(cur)
            cur = parent[cur]
        return path_len, [start]+path[::-1]
    else:
        return -1, []

### Testing with a simple graph

A = {0:[1,4],1:[0,2],2:[1,3],3:[2,4],4:[0,3]}
res = bfs(0,3,A)
print(res)


