import heapq
from collections import defaultdict


class Solution:

    def networkDelayTime(
        self, times: list[list[int]], n: int, k: int
    ) -> int:
        # Build adjacency list: node -> list of (neighbor, weight)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Priority queue stores tuples of (distance_from_source, node)
        pq = [(0, k)]

        # Dictionary to keep track of shortest path distance to each node
        dist = {}

        while pq:
            d, node = heapq.heappop(pq)

            # If node is already visited with a shorter path, skip it
            if node in dist:
                continue

            dist[node] = d

            # Explore outgoing edges
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (d + weight, neighbor))

        # If all n nodes received the signal, return the max distance; otherwise -1
        return max(dist.values()) if len(dist) == n else -1