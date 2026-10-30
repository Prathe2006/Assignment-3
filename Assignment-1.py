from collections import deque

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = [[] for _ in range(graph_nodes + 1)]

    # Build undirected graph
    for u, v in zip(graph_from, graph_to):
        graph[u].append(v)
        graph[v].append(u)

    # Distance and owner of each node
    distance = [-1] * (graph_nodes + 1)
    owner = [-1] * (graph_nodes + 1)

    q = deque()

    # Start BFS from every node having color val
    for i in range(1, graph_nodes + 1):
        if ids[i - 1] == val:
            distance[i] = 0
            owner[i] = i
            q.append(i)

    # Need at least two nodes with the required color
    if len(q) < 2:
        return -1

    answer = float('inf')

    while q:
        u = q.popleft()

        for v in graph[u]:

            # v has not been visited
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                owner[v] = owner[u]
                q.append(v)

            # Two BFS searches meet
            elif owner[v] != owner[u]:
                answer = min(
                    answer,
                    distance[u] + distance[v] + 1
                )

    if answer == float('inf'):
        return -1

    return answer
