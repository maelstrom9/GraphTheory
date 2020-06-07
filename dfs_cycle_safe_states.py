## leetcode problem : dfs color algo
https://leetcode.com/problems/find-eventual-safe-states/


from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
#         ## other apporach
#         n = len(graph)
#         safe = [False] * n
#         rgraph = [set() for i in range(n)]
        
        
#         q = deque()
        
#         for i,j in enumerate(graph):
#             if not j:
#                 q.append(i)
#             for k in j:
#                 rgraph[k].add(i)
                
#         while q:
#             j = q.popleft()
#             safe[j] = True
#             for i in rgraph[j]:
#                 graph[i].remove(j)
#                 if len(graph[i])==0:
#                     q.append(i)
        
#         return [i for i,v in enumerate(safe) if v]
                    
        ## DFS  
            
        
        n = len(graph)
        visited = set()
        # onstack = [False]*n
        nodes = [False]*n
        
        def dfs(u):
            visited.add(u)
            # onstack[u] = True
            
            res = True
            
            for v in graph[u]:
                if v not in visited:
                    res &= dfs(v)
                # elif onstack[v] or not nodes[v]:
                elif not nodes[v]:
                    res = False
            # onstack[u] = False
            nodes[u] = res
            return res
                    
        for u in range(n):
            if u not in visited:
                dfs(u)
                
        ans = []
        for i in range(n):
            if nodes[i]:
                ans.append(i)
        return ans
                            
                            
                
        
