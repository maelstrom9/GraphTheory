
from collections import defaultdict
## union find template

## example problem: leetcode redundant connection


class UnionFind(object):

    def __init__(self):
        # self.parent = [-1]*n
        self.parent = parent = defaultdict(lambda:-1)

    def find(self,u):
        if self.parent[u]<0:
            return u, self.parent[u]
        else:
            par, rank = self.find(self.parent[u])
            self.parent[u] = par ## path compression
            return par, rank


    def union(self,u,v):

        par_u, rank_u = self.find(u)
        par_v, rank_v = self.find(v)

        if par_u!=par_v:
            if rank_u>rank_v:
                self.parent[par_v] = par_u
                self.parent[par_u] += rank_v ## weighted rank
            else:
                self.parent[par_u] = par_v
                self.parent[par_v] += rank_u ## weighted rank
            return False
        else:
            return True ## incase of redundant ocnnection problem


## TESTING

sol = UnionFind()

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
for edge in edges:
    if sol.union(edge[0], edge[1]):
        print(edge)