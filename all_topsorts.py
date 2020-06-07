from collections import defaultdict
## Get all possible topological sorting orders from graph

## Backtracking can be used here


def get_all_top_orders(A,n):
    '''
    :param A: Adjacency list
    :param n: no of vertices
    :return: List of all orders
    '''

    ## indegree update
    indegree = defaultdict(int)
    for u in A:
        for v in A[u]:
            indegree[v] += 1

    visited = set()
    res = []


    def dec_indegree(node):
        for v in A[node]:
            indegree[v] -= 1
    def inc_indegree(node):
        for v in A[node]:
            indegree[v] += 1

    def backtrack(path):
        if len(path)==n:
            res.append(path[:])

        for node in A:
            if node not in visited and indegree[node]==0:
                ## mark
                visited.add(node)
                dec_indegree(node)
                path.append(node)

                ## backtrakc
                backtrack(path)

                ##unmark
                path.pop()
                visited.remove(node)
                inc_indegree(node)

    backtrack([])

    return res

## example from geeks for geeks
## Testing ##
A = {0:[],1:[],2:[3],3:[1],4:[0,1],5:[0,2]}
res = get_all_top_orders(A,6)
for i in res:
    print(i)
# print(res)




