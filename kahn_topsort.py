from collections import defaultdict, deque
## Kahns algorithm for top sort
## find the nodes with indegree 0
## add to queue, remove outward edges from it
## Repeat until queue is empty
## if count!=total vertices, there is cycle
## otherwise we get top order.

def top_sort(A,n):
    '''
    :param n: no of vertices
    :param A: Adjacency list
    :return: top order if possible: -1
    '''
    in_deg = defaultdict(int)
    top_order = []
    ## calculate indegree
    for u in A:
        for v in A[u]:
            in_deg[v] += 1


    queue = deque()
    for u in range(n):
        if in_deg[u] == 0:
            queue.append(u)

    while queue:
        cur = queue.popleft()
        top_order.append(cur)
        for v in A[cur]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)


    if len(top_order)==n: ## cycle detection, important to check
        return top_order
    else:
        return -1 ## there is cycle

## testing

A = {0:[1,2],1:[3,4],2:[4],3:[6,7],4:[5],5:[],6:[],7:[5]}
res = top_sort(A,8)
print(res)

A = {0:[1,2],1:[3,4],2:[4,0],3:[6,7],4:[5],5:[],6:[],7:[5]}
res = top_sort(A,8)
print("with_cycle",res)



