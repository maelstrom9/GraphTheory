

## check if a graph (directed, undirected is real easy) has a cycle

def check_cycle(A,n):
    '''
    :param A: Adjacency list
    :param n: No of nodes
    :return: cycle or not.
    '''

    global is_cycle

    visited = [False]*n
    onStack = [False]*n

    is_cycle = False

    def dfs(u):
        global is_cycle
        visited[u] = True
        onStack[u] = True

        for v in A[u]:
            if not visited[v]:
                dfs(v)
            elif visited[v] and onStack[v]:
                is_cycle = True

        onStack[u] = False

    for u in A:
        if not visited[u]:
            dfs(u)


    return is_cycle


## Testing

## Test1 with no cycle
A1 = {0:[1,2],1:[],2:[1]}
res1 = check_cycle(A1,3)

## Test2 with cycle
A2 = {0:[1,2],1:[3],2:[1],3:[2]}
res2 = check_cycle(A2,4)

## Test3 with no cycle, test stack functinality
A3 = {0:[1],1:[2],2:[3],3:[],4:[1]}
res3 = check_cycle(A3,5)

print(res1,res2,res3)