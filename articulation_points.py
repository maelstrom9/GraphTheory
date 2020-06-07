

## Similar to bridges, but we find nodes that divides graph to different components

## Key difference: can happen via cycles (as we already know bridges result to articulalation)

## Important edge case: when there is only one or no outgoing edges from root(dfs root), then its not articulation  ##

def find_articulation_points(A,n):
    '''
    :param A: Adjacency list
    :param n: No of nodes
    :return: Articulation points in undirected graph
    '''
    global idx
    idx = 0

    global out_edge_count
    out_edge_count = 0

    visited = [None]*n
    low = [None]*n

    art_nodes  = [False]*n ## to store articulation points

    def dfs(root,u,parent):
        global out_edge_count,idx
        if parent==root:
            out_edge_count += 1

        visited[u] = idx
        low[u] = idx
        idx += 1

        for v in A[u]:
            if v == parent:
                continue
            if visited[v] is None:
                dfs(root,v,u)
                low[u] = min(low[u],low[v])
                ## < is for via bridge, = for cycle
                if visited[u]<=low[v]:
                    art_nodes[u] = True
            else:
                low[u] = min(low[u],visited[v])



    for u in range(n):
        if not visited[u]:
            out_edge_count = 0 ## reset for every root node
            dfs(u,u,None)
            if out_edge_count <=1: ## edge case check
                art_nodes[u] = False

    return art_nodes


## Testing

## same example from bridges.py
A = {0:[1,2],1:[0,2],2:[0,1,3,5],3:[2,4],4:[],5:[2,6,8],6:[5,7],7:[6,8],8:[5,7]}
res = find_articulation_points(A,9)
print(res)