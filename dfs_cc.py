

## using dfs template to find cc in UNDIRECTED GRAPH.


## Assuming input format is Adjacency list

def dfs(A):
    '''
    :param A: Adjacency list
    :return: No of connected components
    '''

    visited = set()
    ## generally we use dfs for different purposes like
    ## find connected components, top sort, mst etc
    ## here just for illustration just returning the order of traversal
    cc = 0

    def explore(u):

        visited.add(u)

        for v in A[u]:
            if v not in visited:
                explore(v)

    for node in A:
        if node not in visited:
            cc += 1
            explore(node)


    return cc

## Test

A = {0:[1,2,3],1:[0,4],2:[0],3:[0],4:[1],5:[],6:[7,8],7:[6,8],8:[6,7]}
res = dfs(A)
print(res)
