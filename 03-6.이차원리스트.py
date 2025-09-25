N = 3
graph = [[] for _ in range(N+1)]

print(graph)

N, E = map(int, input().split())

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

print(graph)