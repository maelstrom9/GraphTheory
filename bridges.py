

## Find bridges in the undirected graph
## Bridges: are the edges if breaked will result into two/more? ccs.

## Relies on finding low_link values
## as required in Tarjan SCC, articulation points algos etc.

## Algo:
## DFS--> and keep updating low-link values
## 1. after recursvie callback low(u)=min(low(u),low(v))
## Update bridges for those having low(v)>id(u)
## 2. when visiting previously seen node, low(u) = min(low(u),id(v))


## Example to practise for understanding algo better. Especially helps with understanding visited usage when updatign low.
## The visited array is used to store discovery time, this time/id is propagated through cycle if one exists. thats the key idea.

##    7----6
##    |    |
# 0---1----2----3
##         |    |
##         5----4

def find_bridges(A,n):
    '''
    :param A: Adjacnecy list
    :param n: No of nodes
    :return: Bridge edges.
    '''
    global idx
    visited = [None]*n ## visited stores discovery time and used for visited as well.
    low = [None]*n

    idx = 0

    bridges = []

    def dfs(u,parent,bridges):
        global idx ## declaring idx as global scope, so it can be modified globablly.
        # print(idx)
        visited[u] = idx
        low[u] = idx

        idx += 1

        for v in A[u]:
            if v == parent:
                continue
            if visited[v] is None: ## generally bettter to use "is" over "==" for None comparison
                ## http://jaredgrubb.blogspot.com/2009/04/python-is-none-vs-none.html
                ## https://stackoverflow.com/questions/3257919/what-is-the-difference-between-is-none-and-none
                dfs(v,u,bridges)
                low[u] = min(low[u],low[v])
                if low[v]>visited[u]: ## bridge condition
                    bridges.append((u,v))
            else: ## already visited
                low[u] = min(low[u],visited[v]) ## note the usage of index here.

    for u in range(n):
        if visited[u] is None:
            dfs(u,None,bridges)

    return bridges


### TESTING

## example from @Williams course
A = {0:[1,2],1:[0,2],2:[0,1,3,5],3:[2,4],4:[],5:[2,6,8],6:[5,7],7:[6,8],8:[5,7]}
res = find_bridges(A,9)
print(res)





