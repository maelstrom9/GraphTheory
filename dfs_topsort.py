

## topsort algo using dfs
## start from anywhere, do dfs and save the ordering in reverse order

## top sort can have multiple orderings..
## Assumption: given a DAG
## Assumotion: Adjacency list input

def top_sorting(A):
    '''
    :param A: Adjacency list
    :return: Any possible topological order
    '''

    order = [None]*len(A)
    visited = set()
    i = len(A)-1

    def dfs(u,i):
        visited.add(u)

        for v in A[u]:
            if v not in visited:
                i = dfs(v,i)

        order[i] = u
        return i-1


    for u in A:
        if u not in visited:
            i = dfs(u,i)

    return order


## Testing with a simple DAG

A = {0:[1,2],1:[3,4],2:[4],3:[6,7],4:[5],5:[],6:[],7:[5]}
res = top_sorting(A)
print(res)


