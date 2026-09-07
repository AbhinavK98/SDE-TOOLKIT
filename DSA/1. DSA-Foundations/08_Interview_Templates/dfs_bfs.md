# DFS / BFS Templates

```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for nei in graph[node]:
        dfs(nei, visited)

from collections import deque

def bfs(start):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```
