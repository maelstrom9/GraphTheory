

## Get SCC from directed graph
## Tarjan low-link algo

##Intuition: While doing DFS, update a low-link value (during recursive callback) only when the 1. visited node's
##           low link value is less than the current (which is general case for low-link algos)
##           and 2. when the visited node is in stack. This is important because it ensure that they are in SCC.
##           If in stack means, we have started from it and reached to this cur_node, so when updating we ensure
##           the visited node is in stack, that means we can reach to it from cur_node. So to and fro is possible
##           which makes it a SCC.( any vertex can reach to any other vertex in SCC)

def get_scc(A,n):
    '''
    :param A: Adjacency list
    :param n: Number of nodes
    :return: Number of SCCs, array of cc_ids for each node.
    '''
    global idx,scc_count
    idx = 0
    scc_count = 0

    visited = [None]*n
    low = [None]*n

    onstack = [False]*n
    stack = []

    def dfs(u):
        global idx, scc_count
        visited[u] = idx
        low[u] = idx
        idx += 1
        onstack[u] = True
        stack.append(u)

        for v in A[u]:
            ## since directed no need to check parent condition
            if visited[v] is None:
                dfs(v)

            if onstack[v]:
                low[u] = min(low[u],low[v])

        ## visited all neighbors, if we at start again delete stack up until u
        if low[u] == visited[u]:
            while stack:
                node = stack.pop()
                onstack[node] = False
                low[node] = visited[u] ## is this really needed?
                if node==u:
                    break
            scc_count += 1

    for u in range(n):
        if visited[u] is None:
            dfs(u)

    # print(low)
    return scc_count, low


## Testing

A = {0:[1],1:[2],2:[0],3:[4,7],4:[5],5:[0,6],6:[0,2,4],7:[3,5]}
res = get_scc(A,8)

print(res)