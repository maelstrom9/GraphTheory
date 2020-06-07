

## Given an undirected graph, check if it is bipartite?

## Solved in leetcode: https://leetcode.com/problems/is-graph-bipartite/solution/
## Color matching algo; start dfs and keep assigning colors, alternate for neigboring
##                      If same color is reached, bipartition is not possible.

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        visited = set()
        colors = [-1] * len(graph)

        def dfs(u, color, parent):

            colors[u] = color
            visited.add(u)
            color ^= 1
            res = True

            for v in graph[u]:
                if v == parent:
                    continue

                if v not in visited:
                    res &= dfs(v, color, u)
                else:
                    if colors[v] == colors[u]:
                        return False
            return res

        res = True

        for u in range(len(graph)):
            if u not in visited:
                res &= dfs(u, 0, -1)

        return res





