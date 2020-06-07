

## All pairs shortest path problem
## uses dp
## Key idea is for 0-k, at each step,
## update min distance by chekcing distance
## without including vertex "k" and
## with including it


def floyd_warshall(A,n):
    '''
    :param A: Adjacency matrix
    :param n: no of nodes
    :return: dp table with shortest paths from i-j
    '''

    dp = [[None]*n for _ in range(n)]
    next = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = A[i][j]
            if A[i][j]!=float('inf'):
                next[i][j] = j


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k]+ dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k]+ dp[k][j]
                    next[i][j] = next[i][k]

    ## update negative cycles (similar step as BF, repeat FW)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k]+ dp[k][j] < dp[i][j]:
                    dp[i][j] = float('-inf')
                    next[i][j] = -1

    return dp


## Testing .. avoiding for time constraints

## Time complexity O(V^3) when adjacency matrix is used.

