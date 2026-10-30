class Solution:
    def validPath(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]

        # Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        visited = [False] * n
        queue = [source]
        visited[source] = True

        while queue:
            node = queue.pop(0)

            if node == destination:
                return True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False
